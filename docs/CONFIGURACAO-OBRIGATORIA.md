# 🚦 Comece aqui — do zero ao site no ar e ao robô postando

> ## ❓ "Cadê o link da landing page?"
>
> **Ele ainda não existe.** A página está pronta e testada, mas é código guardado
> numa branch do GitHub. Um site só ganha endereço depois de ser *publicado*, e a
> publicação exige 3 cliques que **só o dono da conta pode dar** (ligar o GitHub
> Pages, tornar o repositório público e juntar a branch à `main`).
>
> Faça a **PARTE 1** abaixo — leva 10 minutos — e o link passa a existir em:
>
> ### 🔗 https://purushlis-coder.github.io/airbnb-goal/
>
> Esse endereço é fixo. Depois da Parte 1 ele funciona para sempre, e cada
> alteração no conteúdo é publicada sozinha.

---

# PARTE 1 — Colocar o site no ar (10 min) → resultado: **o link funcionando**

### Passo 1.1 — Juntar o trabalho à branch principal · 3 min

Todo o código está na branch `claude/landing-page-instagram-automation-ic13ev`.
Ele precisa ir para a `main`, que é a branch que o site publica.

1. Abra: **https://github.com/purushlis-coder/airbnb-goal/pulls**
2. Clique em **New pull request**.
3. Em *base* escolha `main`; em *compare* escolha `claude/landing-page-instagram-automation-ic13ev`.
4. **Create pull request** → depois **Merge pull request** → **Confirm merge**.

✅ *Como saber que deu certo:* a aba **Code** do repositório passa a mostrar as
pastas `assets`, `docs`, `instagram` e o arquivo `index.html`.

### Passo 1.2 — Tornar o repositório público · 2 min

O GitHub Pages só é gratuito em repositório público. Sem isso, não há link.

1. **Settings** (engrenagem no topo do repositório) → role até o fim.
2. Em **Danger Zone** → **Change repository visibility** → **Change to public**.
3. Digite o nome do repositório para confirmar.

> 🔒 Isso torna o *código* visível, não seus dados. Não há nenhuma senha, token ou
> informação pessoal nos arquivos — as chaves do Instagram ficam nos **Secrets**,
> que continuam privados mesmo em repositório público (Parte 2).

### Passo 1.3 — Ligar o GitHub Pages · 2 min

1. **Settings** → menu lateral **Pages**.
2. Em *Build and deployment* → **Source**: selecione **GitHub Actions**.
3. Vá na aba **Actions** → workflow **"Site — publicar no GitHub Pages"** →
   botão **Run workflow** → **Run workflow** (verde).
4. Espere ~1 minuto até a bolinha ficar verde ✅.

### 🎉 Pronto: abra **https://purushlis-coder.github.io/airbnb-goal/**

O site está no ar. Salve esse link — ele vai na bio do Instagram, no WhatsApp e
em qualquer divulgação. **A Parte 1 acabou aqui.**

---

# PARTE 2 — Conectar o robô ao Instagram (45 min) → resultado: **posts automáticos**

> ⚠️ Faça a Parte 1 antes. O robô publica imagens hospedadas no seu próprio site —
> sem o site no ar, o Instagram não consegue baixar a foto.

### Passo 2.1 — Preparar a conta do Instagram · 10 min

1. Crie (ou use) a conta da página de ecoturismo.
   Sugestões de @: `domoblua`, `domoblua.chapada`, `ecocerrado.colinas`.
2. No app do Instagram: **Configurações → Central de contas → Tipo de conta →
   Mudar para conta profissional → Empresa**.
   ⚠️ Conta pessoal **não funciona** com a automação.
3. Crie uma **Página no Facebook** com o mesmo nome e **vincule ao Instagram**
   (Editar perfil → Página). A API da Meta exige esse vínculo.
4. Coloque na bio:
   > 🌿 Ecoturismo, cerrado e cachoeiras
   > 📍 Colinas do Sul · Chapada dos Veadeiros
   > 🏡 DomoBlua: casa com rio privativo ↓
   > `https://purushlis-coder.github.io/airbnb-goal/`

### Passo 2.2 — Gerar as duas chaves na Meta · 30 min

Passo a passo com telas em **[`INSTAGRAM-SETUP.md`](INSTAGRAM-SETUP.md)**.
No fim você terá dois valores:

- `IG_USER_ID` — o número da sua conta profissional
- `IG_ACCESS_TOKEN` — o token de acesso (escolha o que **não expira**)

### Passo 2.3 — Guardar as chaves no GitHub · 2 min

1. **Settings → Secrets and variables → Actions → New repository secret**.
2. Crie os dois, com os nomes **exatamente** assim:

| Name | Value |
|---|---|
| `IG_USER_ID` | o número do passo anterior |
| `IG_ACCESS_TOKEN` | o token do passo anterior |

### Passo 2.4 — Testar · 3 min

Aba **Actions** → **"Instagram — publicar post"** → **Run workflow**.
Em ~2 minutos o log termina com `🎉 publicado!` e o post aparece no perfil.

### 🎉 Pronto: o robô está no ar

---

## 📅 Frequência de postagem (já configurada)

| Dia | Horário (Brasília) |
|---|---|
| Segunda | 17h30 |
| Quarta | 17h30 |
| Sexta | 17h30 |
| Sábado | 10h00 |

**4 posts por semana**, alternando conteúdo do cerrado, Chapada dos Veadeiros,
cachoeiras de Colinas do Sul, dicas de ecoturismo e — a cada 5 posts — uma
divulgação da DomoBlua. São 46 posts no banco (11 semanas sem repetir).

**Para mudar a frequência:** edite as duas linhas `cron` no arquivo
`.github/workflows/instagram-post.yml`. Elas usam UTC (Brasília + 3h).

| Você quer | Coloque |
|---|---|
| Seg/Qua/Sex 17h30 *(atual)* | `30 20 * * 1,3,5` |
| Sábado 10h *(atual)* | `0 13 * * 6` |
| Todo dia às 18h | `0 21 * * *` |
| Só terça e quinta às 12h | `0 15 * * 2,4` |

---

# PARTE 3 — Ajustes que aumentam a conversão (opcional)

### 3.1 — Os 3 campos que faltam · 5 min
No `index.html` (bloco `CONFIG` no topo), procure por `⚠️ FALTA`:
`whatsapp`, `instagram` e `precoAPartir`. No `obrigado.html`, a constante `WHATSAPP`.
No `instagram/config.json`, o `handle` e a `assinatura_card`.

### 3.2 — Ativar o formulário de leads · 5 min
Os leads vão para **purushlis@gmail.com** via FormSubmit (gratuito).
Com o site no ar, envie um teste pelo formulário → você recebe um e-mail do
FormSubmit → clique em **Activate**. Só é preciso uma vez.

### 3.3 — Fotos do rio e da cachoeira · 5 min
São seus maiores diferenciais e a página já tem uma seção reservada para elas.
Passo a passo em **[`COMO-ENVIAR-AS-FOTOS.md`](COMO-ENVIAR-AS-FOTOS.md)**.

### 3.4 — Medição (para poder anunciar depois) · 20 min
Cole o Google Analytics 4 e o Meta Pixel nos espaços marcados com `ANALYTICS`
no `index.html` e no `obrigado.html`. Sem o Pixel não há remarketing.

### 3.5 — Consertar o que trava o anúncio hoje
As avaliações reais apontam problemas concretos (mato alto na chegada, taxa de
resposta de 80%, só 2 avaliações). Está tudo na **Fase 0** do
**[`PROTOCOLO-DIVULGACAO.md`](PROTOCOLO-DIVULGACAO.md)** — é o que mais afeta
suas reservas hoje, mais do que qualquer divulgação.

---

## 🤖 Depois disso, o que roda sozinho?

| Automático | Seu papel |
|---|---|
| Site publicado e atualizado a cada alteração | Responder leads e WhatsApp (< 15 min) |
| 4 posts/semana no Instagram, com imagem e legenda | Stories e comentários (~30 min/semana) |
| Rotação 80% conteúdo / 20% divulgação | Subir fotos novas de vez em quando |
| Fotos reais priorizadas sobre cards gerados | Ajustar preços e calendário no Airbnb |
| Leads do formulário direto no seu e-mail | Pedir avaliação a cada saída de hóspede |
