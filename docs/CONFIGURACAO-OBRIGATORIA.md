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

## Passo 3 — Preencher o que ainda falta · 5 min

A maior parte já veio preenchida do seu anúncio (nome DomoBlua, Colinas do Sul,
10 hóspedes, 2 quartos, 5 camas, 3 banheiros, diferenciais, avaliação do Ronald,
atrações da região). **Só faltam 3 campos**, todos marcados com `⚠️ FALTA`:

| Arquivo | O que ainda falta |
|---|---|
| `index.html` (bloco `CONFIG`) | `whatsapp`, `instagram`, `precoAPartir` |
| `obrigado.html` (constante `WHATSAPP`) | o mesmo número de WhatsApp |
| `instagram/config.json` | `handle` e `assinatura_card` (seu @) |

Tudo que está entre `«...»` precisa ser trocado. Enquanto não trocar:
- a página **esconde** preço e nota (nunca exibe dado fictício);
- o robô do Instagram continua publicando conteúdo normalmente.

> 💡 **Sobre a nota:** ela está escondida de propósito. Com 2 avaliações, o próprio
> Airbnb ainda não mostra média ("aparece depois de 3 avaliações"). Assim que a 3ª
> chegar, preencha `avaliacao` e `numAvaliacoes` e ela aparece sozinha.

## Passo 4 — Melhorar as fotos · 15 min (opcional)

As 6 fotos do anúncio já estão em `assets/fotos/` (extraídas do PDF que você enviou).
Elas funcionam, mas 4 delas são verticais e de resolução média. Para deixar a página
ainda melhor, substitua pelos originais em alta do seu Drive, mantendo os nomes:

| Arquivo | Foto atual |
|---|---|
| `foto-1.jpg` | deck panorâmico *(é o fundo do topo da página — a mais importante)* |
| `foto-2.jpg` | fachada ao pôr do sol |
| `foto-3.jpg` | fachada com a rede |
| `foto-4.jpg` | sala de jantar / varanda |
| `foto-5.jpg` | sala de estar |
| `foto-6.jpg` | suíte 1 |

**⭐ Prioridade:** subir as fotos do **Ribeirão dos Padres** e do **Poço do Motor**.
São seus maiores diferenciais, a landing page já tem uma seção inteira reservada para
elas e as legendas do Instagram já estão escritas esperando os arquivos.
Passo a passo em **[`docs/COMO-ENVIAR-AS-FOTOS.md`](COMO-ENVIAR-AS-FOTOS.md)**.

Também jogue fotos em `instagram/media/` sempre que puder — o robô prioriza fotos
reais sobre os cards gerados (instruções em `instagram/media/LEIA-ME.md`).

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
   > 📍 Colinas do Sul · Chapada dos Veadeiros
   > 🏡 DomoBlua: casa com rio privativo ↓
   > `https://purushlis-coder.github.io/airbnb-goal/`

   Sugestões de @: `domoblua`, `domoblua.chapada`, `ecocerrado.colinas`.

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
