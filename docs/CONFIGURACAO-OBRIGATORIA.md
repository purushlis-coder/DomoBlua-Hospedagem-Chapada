# ✅ Configuração obrigatória (faça uma única vez)

Este é o checklist do que **só você pode fazer**. Depois dele, tudo roda sozinho:
site publicado, posts automáticos no Instagram e leads chegando no seu e-mail.

Tempo total estimado: **1h30 a 2h** (o passo 7 é o mais longo).

> ⚠️ **Separação das hospedagens:** este repositório é 100% dedicado a ESTA
> hospedagem (anúncio `airbnb.com.br/rooms/1482393056413027238`) e à página de
> Instagram de ecoturismo. Não use aqui fotos, links ou textos da outra hospedagem.

---

## Passo 0 — Colocar o trabalho no ar (branch → main) · 2 min

O código está na branch `claude/landing-page-instagram-automation-ic13ev`.

1. Abra o repositório no GitHub → aba **Pull requests** → **New pull request**.
2. Base: `main` ← compare: `claude/landing-page-instagram-automation-ic13ev`.
3. **Create pull request** → **Merge pull request**.

## Passo 1 — Tornar o repositório público · 1 min

Necessário para o GitHub Pages gratuito e para as imagens dos posts terem URL pública.

1. **Settings** → **General** → role até **Danger Zone** → **Change visibility** → *Public*.

> 🔒 Regra de segurança: com o repositório público, **nunca** escreva tokens ou
> senhas em arquivos. Tokens vão apenas em **Settings → Secrets** (passo 7).

## Passo 2 — Ativar o GitHub Pages (o site) · 2 min

1. **Settings** → **Pages** → em *Build and deployment*, **Source: GitHub Actions**.
2. Aba **Actions** → workflow **"Site — publicar no GitHub Pages"** → **Run workflow**.
3. Em ~1 minuto seu site estará em: **https://purushlis-coder.github.io/airbnb-goal/**

Esse endereço é a sua landing page — é ele que vai na bio do Instagram.

## Passo 3 — Preencher os dados da hospedagem · 15 min

Edite direto no GitHub (ícone de lápis) ou localmente:

| Arquivo | O que preencher |
|---|---|
| `index.html` (bloco `CONFIG` no topo) | nome, cidade, WhatsApp, Instagram, nota, nº de avaliações, preço, capacidade, diferenciais, 3 avaliações reais copiadas do Airbnb, 4 atrações da região |
| `obrigado.html` (constante `WHATSAPP`) | o mesmo número de WhatsApp |
| `instagram/config.json` | `handle`, `nome_hospedagem`, `cidade_hospedagem`, `assinatura_card` |

Tudo que está entre `«...»` precisa ser trocado. Enquanto não trocar:
- a página **esconde** nota/preço/capacidade (para nunca exibir dado fictício);
- o robô do Instagram **pula os posts promocionais** e publica só conteúdo de valor.

## Passo 4 — Subir as fotos · 15 min

1. `assets/fotos/` → `foto-1.jpg` … `foto-6.jpg` (instruções em `assets/fotos/LEIA-ME.md`).
2. `instagram/media/` → jogue fotos reais de cachoeiras/da hospedagem sempre que tiver
   (o robô prioriza fotos reais; instruções em `instagram/media/LEIA-ME.md`).

## Passo 5 — Ativar o formulário de leads · 5 min

O formulário envia os leads para **purushlis@gmail.com** via FormSubmit (gratuito).

1. Com o site no ar, abra a página, preencha o formulário com dados de teste e envie.
2. Você receberá um e-mail do FormSubmit → clique em **Activate** (só na 1ª vez).
3. Envie um segundo teste e confirme que o lead chegou na sua caixa de entrada.
4. (Recomendado) No e-mail de ativação o FormSubmit mostra um **alias aleatório**
   (ex.: `formsubmit.co/a1b2c3...`). Troque o e-mail pelo alias na linha `action=` do
   formulário em `index.html` — isso esconde seu e-mail do código público.

## Passo 6 — Preparar o Instagram · 10 min

1. Crie a conta da página de ecoturismo (sugestões de nome no protocolo de divulgação).
2. No app: **Configurações → Central de contas → Tipo de conta → Mudar para conta
   profissional → Empresa** (obrigatório para a automação).
3. Crie uma **Página no Facebook** com o mesmo nome e **vincule-a ao Instagram**
   (Editar perfil → Página). A API só funciona com esse vínculo.
4. Bio pronta para usar (edite o que quiser):
   > 🌿 Ecoturismo, cerrado e cachoeiras
   > 📍 Chapada dos Veadeiros e além
   > 🏡 Hospedagem com anfitrião local ↓
   > `https://purushlis-coder.github.io/airbnb-goal/`

## Passo 7 — Chaves da automação (Meta) · 30–45 min

Siga o passo a passo detalhado em **[`docs/INSTAGRAM-SETUP.md`](INSTAGRAM-SETUP.md)**.
Ao final você terá dois valores:

- `IG_USER_ID` — o ID da sua conta profissional do Instagram
- `IG_ACCESS_TOKEN` — o token de acesso (recomendado: token de usuário do sistema, que não expira)

Cadastre-os em: **Settings → Secrets and variables → Actions → New repository secret**
(um secret para cada, com exatamente esses nomes).

## Passo 8 — Testar o robô · 5 min

1. Aba **Actions** → **"Instagram — publicar post"** → **Run workflow**.
2. Acompanhe a execução (bolinha verde = sucesso) e confira o post no seu perfil.
3. Pronto: a partir daqui ele posta sozinho **seg/qua/sex 17h30 e sáb 10h** (Brasília).

## Passo 9 — Medição e anúncios (opcional, recomendado) · 20 min

1. **GA4**: crie uma propriedade em analytics.google.com e cole o snippet nos espaços
   marcados com `ANALYTICS` no `index.html` e no `obrigado.html`.
2. **Meta Pixel**: crie em Gerenciador de Eventos da Meta e cole nos mesmos espaços —
   no `obrigado.html`, dispare `fbq('track','Lead')` (o comentário no arquivo mostra onde).
   Sem o Pixel você não consegue fazer remarketing depois.

---

## 🚦 Depois de tudo configurado, o que roda sozinho?

| Automático (sem você) | Manual (seu papel) |
|---|---|
| Site publicado e atualizado a cada alteração | Responder leads e WhatsApp (ideal < 15 min) |
| 4 posts/semana no Instagram com conteúdo + imagem | Stories e interação (30–40 min/semana) |
| Rotação 80% conteúdo / 20% promoção | Subir fotos novas de vez em quando |
| Fotos reais priorizadas sobre cards | Renovar token (se optar pelo de 60 dias) |
| Leads do formulário direto no seu e-mail | Ajustar preços/calendário no Airbnb |

O plano completo de divulgação está em **[`docs/PROTOCOLO-DIVULGACAO.md`](PROTOCOLO-DIVULGACAO.md)**.
