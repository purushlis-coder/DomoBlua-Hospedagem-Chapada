#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automação de posts do Instagram (Instagram Graph API — conta profissional).

Funciona em duas fases, orquestradas pelo workflow .github/workflows/instagram-post.yml:

  python instagram/post_instagram.py prepare
      Escolhe o próximo conteúdo do banco (content.json), prioriza fotos reais
      da pasta instagram/media/, gera um card se não houver foto nova, monta a
      legenda final e grava tudo em instagram/outbox.json + atualiza state.json.
      (O workflow então commita a imagem para que ela tenha uma URL pública.)

  python instagram/post_instagram.py publish
      Espera a imagem ficar acessível publicamente (GitHub Pages ou raw) e
      publica no Instagram: cria o contêiner de mídia e o publica.
      Requer as variáveis de ambiente IG_ACCESS_TOKEN e IG_USER_ID
      (no GitHub: Settings → Secrets and variables → Actions).

  python instagram/post_instagram.py dry-run
      Igual ao prepare, mas não altera state.json (bom para testar localmente).
"""
import json
import os
import re
import sys
import time
import unicodedata
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(BASE)
GENERATED_REL = "instagram/generated"
MEDIA_DIR = os.path.join(BASE, "media")

sys.path.insert(0, BASE)
from generate_card import make_card  # noqa: E402


# ----------------------------- utilidades -----------------------------

def _json(caminho):
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def _salva_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
        f.write("\n")


def _tem_placeholder(texto):
    return isinstance(texto, str) and "«" in texto


def _slug(texto):
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", texto.lower()).strip("-")[:48] or "post"


def _log(msg):
    print(msg, flush=True)


# ----------------------------- fase: prepare -----------------------------

def _proxima_foto_real(state):
    """Retorna o caminho da próxima foto real ainda não usada (ou None)."""
    if not os.path.isdir(MEDIA_DIR):
        return None
    usadas = set(state.get("fotos_usadas", []))
    candidatas = sorted(
        f for f in os.listdir(MEDIA_DIR)
        if f.lower().endswith((".jpg", ".jpeg", ".png")) and f not in usadas
    )
    return os.path.join(MEDIA_DIR, candidatas[0]) if candidatas else None


def _ajusta_para_instagram(origem, destino):
    """Corta para 4:5 (retrato) e redimensiona para no máx. 1080px de largura."""
    from PIL import Image
    im = Image.open(origem).convert("RGB")
    alvo = 4 / 5
    w, h = im.size
    if w / h > alvo:                       # larga demais → corta laterais
        novo_w = int(h * alvo)
        x = (w - novo_w) // 2
        im = im.crop((x, 0, x + novo_w, h))
    elif w / h < alvo:                     # alta demais → corta topo/base
        novo_h = int(w / alvo)
        y = (h - novo_h) // 2
        im = im.crop((0, y, w, y + novo_h))
    if im.width > 1080:
        im = im.resize((1080, 1350), Image.LANCZOS)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    im.save(destino, "JPEG", quality=90)
    return destino


def _escolhe_post(posts, state, config):
    """Avança o ponteiro pulando promos enquanto o config tiver «placeholders»."""
    inicio = state.get("proximo_indice", 0)
    promo_ok = not (_tem_placeholder(config.get("nome_hospedagem", "«"))
                    or _tem_placeholder(config.get("cidade_hospedagem", "«")))
    for salto in range(len(posts)):
        i = (inicio + salto) % len(posts)
        post = posts[i]
        if post.get("tema") == "promo" and not promo_ok:
            _log(f"↷ pulando promo '{post['id']}' (config ainda com «placeholders»)")
            continue
        return i, post
    return inicio % len(posts), posts[inicio % len(posts)]


def _monta_legenda(post, config, legenda_customizada=None):
    nome = config.get("nome_hospedagem", "")
    cidade = config.get("cidade_hospedagem", "")
    corpo = (legenda_customizada or post["legenda"]).replace("{nome}", nome).replace("{cidade}", cidade)
    partes = [corpo.strip()]

    rodape = config.get("rodape_legenda", "").strip()
    if rodape and not _tem_placeholder(rodape):
        partes.append(rodape)

    ja_tem_hashtags = "#" in (legenda_customizada or "")
    if not ja_tem_hashtags:
        partes.append(" ".join(post.get("hashtags", [])))

    return "\n\n".join(p for p in partes if p)


def prepare(gravar_estado=True):
    config = _json(os.path.join(BASE, "config.json"))
    posts = _json(os.path.join(BASE, "content.json"))["posts"]
    state = _json(os.path.join(BASE, "state.json"))

    indice, post = _escolhe_post(posts, state, config)
    agora = datetime.now(timezone.utc)
    carimbo = agora.strftime("%Y%m%d-%H%M")

    foto_real = _proxima_foto_real(state)
    legenda_customizada = None
    foto_usada = None

    if foto_real:
        sidecar = os.path.splitext(foto_real)[0] + ".txt"
        if os.path.exists(sidecar):
            with open(sidecar, encoding="utf-8") as f:
                legenda_customizada = f.read().strip()
        nome_arq = f"{carimbo}-foto-{_slug(os.path.basename(foto_real))}.jpg"
        destino = os.path.join(RAIZ, GENERATED_REL, nome_arq)
        _ajusta_para_instagram(foto_real, destino)
        foto_usada = os.path.basename(foto_real)
        _log(f"📷 usando foto real: {foto_usada}")
    else:
        nome_arq = f"{carimbo}-card-{_slug(post['id'])}.jpg"
        destino = os.path.join(RAIZ, GENERATED_REL, nome_arq)
        make_card(post, config, destino)
        _log(f"🎨 card gerado para o post: {post['id']}")

    legenda = _monta_legenda(post, config, legenda_customizada)
    caminho_repo = f"{GENERATED_REL}/{nome_arq}"

    outbox = {
        "post_id": post["id"],
        "imagem": caminho_repo,
        "legenda": legenda,
        "gerado_em": agora.isoformat(),
    }
    _salva_json(os.path.join(BASE, "outbox.json"), outbox)

    if gravar_estado:
        state["proximo_indice"] = (indice + 1) % len(posts)
        if foto_usada:
            state.setdefault("fotos_usadas", []).append(foto_usada)
        state.setdefault("historico", []).append(
            {"data": agora.isoformat(), "post_id": post["id"], "arquivo": caminho_repo}
        )
        state["historico"] = state["historico"][-200:]
        _salva_json(os.path.join(BASE, "state.json"), state)

    saida_gh = os.environ.get("GITHUB_OUTPUT")
    if saida_gh:
        with open(saida_gh, "a", encoding="utf-8") as f:
            f.write(f"imagem={caminho_repo}\n")

    _log(f"✅ prepare concluído → {caminho_repo}")
    _log("---- legenda ----\n" + legenda + "\n-----------------")


# ----------------------------- fase: publish -----------------------------

def _espera_url_publica(config, caminho_repo, timeout=360):
    import requests
    candidatas = []
    pages = (config.get("pages_base_url") or "").rstrip("/")
    raw = (config.get("raw_base_url") or "").rstrip("/")
    if pages:
        candidatas.append(f"{pages}/{caminho_repo}")
    if raw:
        candidatas.append(f"{raw}/{caminho_repo}")

    limite = time.time() + timeout
    tentativa = 0
    while time.time() < limite:
        tentativa += 1
        for url in candidatas:
            try:
                r = requests.get(url, timeout=30)
                if r.status_code == 200 and r.content[:2] == b"\xff\xd8":  # JPEG
                    _log(f"🌐 imagem acessível ({tentativa}ª tentativa): {url}")
                    return url
            except requests.RequestException:
                pass
        _log(f"⏳ imagem ainda não acessível (tentativa {tentativa}), aguardando 20s...")
        time.sleep(20)
    raise RuntimeError(
        "A imagem não ficou acessível publicamente a tempo. Verifique se o GitHub Pages "
        "está ativado (Settings → Pages → Source: GitHub Actions) e se o repositório é público."
    )


def publish():
    import requests

    token = os.environ.get("IG_ACCESS_TOKEN", "").strip()
    ig_user = os.environ.get("IG_USER_ID", "").strip()
    if not token or not ig_user:
        _log("⚠️ IG_ACCESS_TOKEN / IG_USER_ID não configurados — publicação pulada.")
        _log("   Configure em: GitHub → Settings → Secrets and variables → Actions.")
        _log("   Passo a passo completo: docs/INSTAGRAM-SETUP.md")
        return

    config = _json(os.path.join(BASE, "config.json"))
    outbox_path = os.path.join(BASE, "outbox.json")
    if not os.path.exists(outbox_path):
        raise RuntimeError("outbox.json não encontrado — rode a fase 'prepare' antes.")
    outbox = _json(outbox_path)

    url_imagem = _espera_url_publica(config, outbox["imagem"])
    versao = config.get("graph_api_version", "v23.0")
    api = f"https://graph.facebook.com/{versao}"

    _log("📤 criando contêiner de mídia...")
    r = requests.post(
        f"{api}/{ig_user}/media",
        data={"image_url": url_imagem, "caption": outbox["legenda"], "access_token": token},
        timeout=60,
    )
    corpo = r.json()
    if "id" not in corpo:
        raise RuntimeError(f"Falha ao criar contêiner: {json.dumps(corpo, ensure_ascii=False)}")
    creation_id = corpo["id"]

    for _ in range(12):
        r = requests.get(
            f"{api}/{creation_id}",
            params={"fields": "status_code", "access_token": token},
            timeout=30,
        )
        status = r.json().get("status_code")
        if status == "FINISHED":
            break
        if status == "ERROR":
            raise RuntimeError(f"Contêiner com erro: {r.text}")
        _log(f"⏳ processando mídia ({status})...")
        time.sleep(5)

    _log("🚀 publicando...")
    r = requests.post(
        f"{api}/{ig_user}/media_publish",
        data={"creation_id": creation_id, "access_token": token},
        timeout=60,
    )
    corpo = r.json()
    if "id" not in corpo:
        raise RuntimeError(f"Falha ao publicar: {json.dumps(corpo, ensure_ascii=False)}")
    media_id = corpo["id"]

    try:
        r = requests.get(
            f"{api}/{media_id}",
            params={"fields": "permalink", "access_token": token},
            timeout=30,
        )
        _log(f"🎉 publicado! {r.json().get('permalink', '(permalink indisponível)')}")
    except requests.RequestException:
        _log(f"🎉 publicado! media_id={media_id}")


# ----------------------------- main -----------------------------

if __name__ == "__main__":
    comando = sys.argv[1] if len(sys.argv) > 1 else "dry-run"
    if comando == "prepare":
        prepare(gravar_estado=True)
    elif comando == "dry-run":
        prepare(gravar_estado=False)
    elif comando == "publish":
        publish()
    else:
        print(__doc__)
        sys.exit(2)
