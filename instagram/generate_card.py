#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera cards de conteúdo para o Instagram (1080x1350, formato retrato 4:5).

Visual: gradientes inspirados no cerrado (mata, terracota do pôr do sol,
águas de cachoeira e capim dourado), morros em camadas, sol difuso e
granulado sutil. O estilo é escolhido de forma determinística pelo id do
post, então o feed alterna as paletas sozinho.

Uso direto (para testar):
    python instagram/generate_card.py 0            # gera o post de índice 0
    python instagram/generate_card.py --amostras   # gera 4 amostras (1 por paleta)

Na automação, quem chama é o instagram/post_instagram.py.
"""
import hashlib
import json
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(BASE)

W, H = 1080, 1350

PALETAS = [
    {"nome": "mata",      "topo": "#16281b", "base": "#3f6b45", "acento": "#e8b54d", "sol": "#f2e2b3"},
    {"nome": "terracota", "topo": "#5f2a17", "base": "#c2603d", "acento": "#f5dfa9", "sol": "#ffd9a0"},
    {"nome": "aguas",     "topo": "#1d3a4a", "base": "#5a8ca8", "acento": "#f2c14e", "sol": "#eaf4f7"},
    {"nome": "capim",     "topo": "#3e2e12", "base": "#a08347", "acento": "#f7e6b5", "sol": "#fff3cf"},
]

CREME = (250, 246, 239)


def _hex(cor):
    cor = cor.lstrip("#")
    return tuple(int(cor[i:i + 2], 16) for i in (0, 2, 4))


def _fonte(negrito=True, tamanho=64):
    candidatas = []
    nome = "DejaVuSans-Bold.ttf" if negrito else "DejaVuSans.ttf"
    candidatas.append(os.path.join(RAIZ, "assets", "fonts", nome))
    candidatas.append("/usr/share/fonts/truetype/dejavu/" + nome)
    for c in candidatas:
        if os.path.exists(c):
            return ImageFont.truetype(c, tamanho)
    return ImageFont.load_default()


def _semente(texto):
    return int(hashlib.sha256(texto.encode("utf-8")).hexdigest(), 16)


def _gradiente(topo, base):
    im = Image.new("RGB", (W, H))
    t, b = _hex(topo), _hex(base)
    px = im.load()
    for y in range(H):
        f = y / (H - 1)
        cor = tuple(int(t[i] + (b[i] - t[i]) * f) for i in range(3))
        for x in range(0, W, 1):
            px[x, y] = cor
    return im


def _sol(im, paleta, semente):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    cx = 200 + (semente % 680)
    cy = 300 + ((semente // 7) % 260)
    r = 190 + (semente % 90)
    cor = _hex(paleta["sol"])
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=cor + (70,))
    d.ellipse([cx - r // 2, cy - r // 2, cx + r // 2, cy + r // 2], fill=cor + (60,))
    overlay = overlay.filter(ImageFilter.GaussianBlur(60))
    im.paste(overlay, (0, 0), overlay)
    return im


def _morros(im, paleta, semente):
    """Camadas de morros/chapadas na base do card."""
    base = _hex(paleta["topo"])
    camadas = 3
    for c in range(camadas):
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(overlay)
        alt = H - 320 + c * 95
        amp = 46 - c * 10
        fase = (semente // (c + 3)) % 628 / 100.0
        freq = 1.4 + c * 0.9 + ((semente // (c + 11)) % 10) / 12.0
        pontos = [(0, H)]
        for x in range(0, W + 20, 20):
            y = alt + amp * math.sin(fase + freq * x / W * math.pi * 2)
            y += (amp * 0.5) * math.sin(fase * 1.7 + freq * 2.3 * x / W * math.pi * 2)
            pontos.append((x, y))
        pontos.append((W, H))
        alpha = 60 + c * 45
        d.polygon(pontos, fill=base + (alpha,))
        im.paste(overlay, (0, 0), overlay)
    return im


def _granulado(im, intensidade=0.05):
    ruido = Image.effect_noise((W, H), 28).convert("RGB")
    return Image.blend(im, ruido, intensidade)


def _quebra_linhas(draw, texto, fonte, largura_max):
    palavras = texto.split()
    linhas, atual = [], ""
    for p in palavras:
        teste = (atual + " " + p).strip()
        if draw.textlength(teste, font=fonte) <= largura_max:
            atual = teste
        else:
            if atual:
                linhas.append(atual)
            atual = p
    if atual:
        linhas.append(atual)
    return linhas


def _texto_espacado(draw, xy, texto, fonte, cor, espaco=6):
    x, y = xy
    for ch in texto:
        draw.text((x, y), ch, font=fonte, fill=cor)
        x += draw.textlength(ch, font=fonte) + espaco


def make_card(post, config, caminho_saida):
    """Gera o card de um post e salva em caminho_saida (JPEG)."""
    semente = _semente(post["id"])
    paleta = PALETAS[semente % len(PALETAS)]

    im = _gradiente(paleta["topo"], paleta["base"])
    im = _sol(im, paleta, semente)
    im = _morros(im, paleta, semente)
    im = _granulado(im)

    d = ImageDraw.Draw(im)
    margem = 90
    largura_util = W - 2 * margem
    acento = _hex(paleta["acento"])

    # Kicker (rótulo do tema)
    kicker = post.get("kicker", "Ecoturismo").upper()
    f_kicker = _fonte(True, 34)
    d.rectangle([margem, 208, margem + 74, 214], fill=acento)
    _texto_espacado(d, (margem + 96, 190), kicker, f_kicker, acento, espaco=5)

    # Título (encolhe até caber)
    titulo = post["titulo"]
    tamanho = 92
    while tamanho >= 54:
        f_titulo = _fonte(True, tamanho)
        linhas = _quebra_linhas(d, titulo, f_titulo, largura_util)
        altura_linha = int(tamanho * 1.18)
        if len(linhas) <= 6 and len(linhas) * altura_linha <= 640:
            break
        tamanho -= 6
    y = 300
    for linha in linhas:
        d.text((margem + 3, y + 4), linha, font=f_titulo, fill=(10, 14, 10))   # sombra
        d.text((margem, y), linha, font=f_titulo, fill=CREME)
        y += altura_linha

    # Rodapé (assinatura)
    assinatura = (config.get("assinatura_card") or "").replace("«", "").replace("»", "").strip()
    if not assinatura or assinatura == "@":
        assinatura = "ecoturismo • cerrado"
    f_rodape = _fonte(False, 34)
    y_rodape = H - 150
    d.line([(margem, y_rodape - 26), (W - margem, y_rodape - 26)], fill=CREME + (90,), width=2)
    d.text((margem, y_rodape), assinatura, font=f_rodape, fill=CREME)
    dica = "salve este post ➜"
    d.text((W - margem - d.textlength(dica, font=f_rodape), y_rodape), dica, font=f_rodape, fill=acento)

    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
    im.save(caminho_saida, "JPEG", quality=90)
    return caminho_saida


def _carrega(nome):
    with open(os.path.join(BASE, nome), encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    config = _carrega("config.json")
    posts = _carrega("content.json")["posts"]
    saida_dir = os.path.join(BASE, "generated")

    if "--amostras" in sys.argv:
        vistos, feitos = set(), []
        for p in posts:
            pal = _semente(p["id"]) % len(PALETAS)
            if pal in vistos:
                continue
            vistos.add(pal)
            destino = os.path.join(saida_dir, f"amostra-{PALETAS[pal]['nome']}.jpg")
            feitos.append(make_card(p, config, destino))
            if len(vistos) == len(PALETAS):
                break
        print("\n".join(feitos))
    else:
        indice = int(sys.argv[1]) if len(sys.argv) > 1 else 0
        p = posts[indice % len(posts)]
        destino = os.path.join(saida_dir, f"preview-{p['id']}.jpg")
        print(make_card(p, config, destino))
