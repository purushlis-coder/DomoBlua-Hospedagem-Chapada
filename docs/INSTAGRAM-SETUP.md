# 🔑 Setup da automação do Instagram (Meta / Graph API)

Este guia gera as duas chaves que o robô precisa: `IG_USER_ID` e `IG_ACCESS_TOKEN`.
Feito uma vez, vale para sempre (ou por 60 dias, se optar pelo token simples).

**Pré-requisitos**: Instagram como **conta profissional** vinculada a uma
**Página do Facebook**.

> ## ⚠️ Página ≠ "modo profissional" — não confunda
>
> São três coisas diferentes, e você precisa de duas delas:
>
> | O que é | Precisa? | Para quê |
> |---|---|---|
> | **Conta pessoal do Facebook** (seu perfil) | ✅ já tem | Ser o administrador da Página |
> | **Página do Facebook** (Page) | ✅ **obrigatória** | É dela que sai o vínculo com o Instagram |
> | **"Modo profissional" no perfil pessoal** | ❌ não serve | Recurso para criadores; **não gera uma Página** |
>
> Se a Meta te ofereceu "criar uma Página" ou "transformar o perfil em conta
> profissional", **escolha criar a Página**. O modo profissional não produz o
> Page ID que a API precisa, e o passo B abaixo não vai funcionar sem ele.
>
> Seu perfil pessoal continua existindo normalmente e vira o administrador da
> Página — isso é o esperado, não um problema.
>
> **Bônus:** a Página também é obrigatória para anunciar no Meta Ads depois
> (Fase 3 do protocolo de divulgação). Ou seja, você vai precisar dela de todo jeito.

### Como criar a Página (2 min)

1. No Facebook: menu **☰** → **Páginas** → **Criar nova Página**.
2. Nome: `DomoBlua` (ou o mesmo @ do Instagram). Categoria: *Aluguel por temporada*
   ou *Hospedagem*.
3. Criada a Página, vá ao **Instagram** → **Editar perfil** → **Página** →
   selecione a Página que você acabou de criar.

✅ *Como saber que deu certo:* no app do Instagram, em Editar perfil, o campo
**Página** mostra o nome da sua Página em vez de "Criar" ou "Nenhuma".

---

## Parte A — Criar o app na Meta · 10 min

1. Acesse **https://developers.facebook.com** e entre com a conta do Facebook
   que administra a sua Página.
2. **My Apps → Create App** → tipo **Business** → dê um nome (ex.: `automacao-ecoturismo`).
3. No painel do app, em *Add products*, adicione **Instagram Graph API**
   (e **Facebook Login for Business**, se oferecido).

> O app pode ficar em "Development mode" — para publicar na SUA própria conta
> não é preciso passar por revisão da Meta, basta que o usuário do token seja
> administrador do app e da Página.

## Parte B — Descobrir o IG_USER_ID · 5 min

1. Abra o **Graph API Explorer**: https://developers.facebook.com/tools/explorer
2. Em *Meta App*, selecione o app criado. Em *User or Page*, **Get User Access Token**,
   marcando as permissões:
   `instagram_basic`, `instagram_content_publish`, `pages_show_list`,
   `pages_read_engagement`, `business_management`.
3. Rode a consulta `me/accounts` → copie o `id` da sua Página (PAGE_ID).
4. Rode `PAGE_ID?fields=instagram_business_account` → o `id` retornado é o seu
   **IG_USER_ID** (um número longo). Guarde-o.

## Parte C — Gerar o token definitivo

### Opção 1 (recomendada): token de usuário do sistema — **não expira**

1. Acesse **https://business.facebook.com/settings** (Configurações do negócio).
2. Menu **Usuários → Usuários do sistema** (System users) → **Adicionar** →
   nome `robo-instagram`, função **Administrador**.
3. Clique no usuário criado → **Adicionar ativos**: selecione a sua **Página**
   (controle total) e o seu **App** (desenvolver app).
4. **Gerar token** → selecione o app → validade **Nunca expira** → marque as mesmas
   permissões da Parte B → **Gerar**.
5. Copie o token exibido (ele aparece UMA vez): é o seu **IG_ACCESS_TOKEN**.

### Opção 2 (mais rápida): token de longa duração — expira em ~60 dias

1. No Graph API Explorer (Parte B), copie o token curto gerado.
2. Troque por um de 60 dias (rode no terminal, preenchendo os 3 valores):

```bash
curl "https://graph.facebook.com/v23.0/oauth/access_token?grant_type=fb_exchange_token&client_id=SEU_APP_ID&client_secret=SEU_APP_SECRET&fb_exchange_token=TOKEN_CURTO"
```

   (`SEU_APP_ID` e `SEU_APP_SECRET` estão no painel do app → App settings → Basic.)
3. O `access_token` da resposta é o seu **IG_ACCESS_TOKEN**.
4. ⏰ Marque no calendário: repetir esta troca a cada ~50 dias, atualizando o secret.

## Parte D — Cadastrar os secrets no GitHub · 2 min

1. Repositório → **Settings → Secrets and variables → Actions → New repository secret**.
2. Crie **exatamente** estes dois:

| Name | Value |
|---|---|
| `IG_USER_ID` | o número da Parte B |
| `IG_ACCESS_TOKEN` | o token da Parte C |

> 🔒 Nunca cole esses valores em arquivos do repositório, issues ou commits.

## Parte E — Testar · 5 min

Aba **Actions → "Instagram — publicar post" → Run workflow**. Em ~2 minutos o log
deve terminar com `🎉 publicado!` e o post aparece no perfil.

---

## 🩺 Problemas comuns

| Sintoma no log | Causa provável | Solução |
|---|---|---|
| `Secrets ... não configurados` | Parte D não feita | Criar os 2 secrets com os nomes exatos |
| Erro `code: 190` | Token expirado/inválido | Gerar novo token (Parte C) e atualizar o secret |
| Erro `code: 10` ou `200` | Permissão faltando | Refazer token marcando TODAS as permissões da Parte B |
| `A imagem não ficou acessível` | Pages desativado ou repo privado | Checklist passos 1 e 2 |
| Erro de mídia/aspect ratio | Foto fora do padrão | O robô já corta para 4:5; confira se o arquivo não está corrompido |
| Nada posta no horário | Cron do GitHub pode atrasar alguns minutos | Aguardar; se persistir, rodar manualmente e conferir logs |

**Limites da API**: até 50 publicações por 24h — nosso ritmo (4/semana) está muito abaixo.

**Plano B sem API**: enquanto não configurar as chaves, você pode agendar manualmente
os mesmos conteúdos no **Meta Business Suite** (gratuito): as imagens ficam em
`instagram/generated/` e as legendas em `instagram/content.json`.
