# 🌿 DomoBlua — landing page + automação de Instagram

Sistema completo de captação de hóspedes para a **DomoBlua**, casa com rio privativo e
deck panorâmico em **Colinas do Sul – GO**, no portal da Chapada dos Veadeiros
([anúncio no Airbnb](https://www.airbnb.com.br/rooms/1482393056413027238)):
landing page de alta conversão publicada no GitHub Pages, posts automáticos no
Instagram sobre ecoturismo/cerrado/Chapada e um protocolo de divulgação passo a passo.

**A casa:** 10 hóspedes · 2 suítes · 5 camas · 3 banheiros · acesso privativo ao
Ribeirão dos Padres · Poço do Motor a poucos metros · pet friendly · check-in autônomo.

> ℹ️ Este repositório é dedicado **exclusivamente a esta hospedagem**. Dados, fotos,
> links e textos de outras hospedagens não devem ser misturados aqui.

## 🚀 Comece por aqui

**➡️ [`docs/CONFIGURACAO-OBRIGATORIA.md`](docs/CONFIGURACAO-OBRIGATORIA.md)** — checklist
único do que só você pode fazer (≈1h30). Depois dele, tudo roda sozinho.

Demais documentos:
- [`docs/INSTAGRAM-SETUP.md`](docs/INSTAGRAM-SETUP.md) — como gerar as chaves da Meta (Graph API)
- [`docs/PROTOCOLO-DIVULGACAO.md`](docs/PROTOCOLO-DIVULGACAO.md) — plano completo de divulgação e captura de hóspedes

## 🗺️ O que tem aqui

| Caminho | O que é |
|---|---|
| `index.html` | Landing page. Todo o conteúdo sai do bloco **CONFIG** no topo do arquivo |
| `obrigado.html` | Página de confirmação após o formulário (mede conversão) |
| `assets/fotos/` | Fotos da hospedagem (`foto-1.jpg` … `foto-6.jpg`) |
| `instagram/config.json` | Dados da conta e da hospedagem usados nos posts |
| `instagram/content.json` | Banco com 40 posts prontos (ecoturismo, cerrado, Chapada, dicas, promoções) |
| `instagram/media/` | Suas fotos reais — têm prioridade sobre os cards gerados |
| `instagram/generate_card.py` | Gera cards 1080×1350 com paleta do cerrado |
| `instagram/post_instagram.py` | Escolhe o conteúdo, monta a legenda e publica via Graph API |
| `instagram/state.json` | Memória do robô (o que já foi postado) |
| `.github/workflows/` | Deploy do site e agendamento dos posts |

## 🤖 Como a automação funciona

```
cron (seg/qua/sex 17h30 · sáb 10h BRT)
  └─ prepare  → escolhe o próximo post do content.json
              → usa foto de instagram/media/ (se houver nova) ou gera um card
              → monta legenda + rodapé + hashtags
  └─ commit   → a imagem ganha URL pública via GitHub Pages
  └─ publish  → cria o contêiner de mídia e publica no Instagram
```

Regras embutidas:
- **80% conteúdo de valor / 20% promoção** — a ordem do `content.json` já faz isso.
- Enquanto o `config.json` tiver `«placeholders»`, os posts promocionais são **pulados**.
- Sem os secrets configurados, o workflow avisa e não falha.
- Ao chegar no fim do banco de conteúdo, ele recomeça (edite/adicione posts à vontade).

## 🧪 Rodar localmente

```bash
pip install pillow requests

python instagram/generate_card.py --amostras   # 4 cards de amostra
python instagram/post_instagram.py dry-run     # simula um post (não altera o estado)
python -m http.server 8000                     # abre a landing em localhost:8000
```

## 🔒 Segurança

Tokens e IDs ficam **apenas** nos Secrets do GitHub (`IG_ACCESS_TOKEN`, `IG_USER_ID`) —
nunca em arquivos do repositório, que é público para o Pages funcionar.
