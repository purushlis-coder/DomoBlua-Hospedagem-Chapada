# ✏️ Como editar a landing page

Você não precisa instalar nada nem saber programar. Tudo é feito pelo navegador,
e o site se republica sozinho em cerca de 1 minuto.

**Link direto para o editor:**

```
https://github.com/purushlis-coder/DomoBlua-Hospedagem-Chapada/edit/main/index.html
```

Salve esse endereço nos favoritos. É por ali que 90% das mudanças acontecem.

---

## O passo a passo (4 cliques)

1. **Abra o link acima.** Você verá o código da página, com uma barra de rolagem.
2. **Ache o que quer mudar** (use `Ctrl+F` para buscar a palavra).
3. **Edite o texto** entre as aspas. Só o que está entre `"aspas"`.
4. Role até o fim, escreva o que mudou na caixa **Commit changes** e clique no
   botão verde **Commit changes**.

Pronto. Em ~1 minuto o site está atualizado.

> **Para conferir:** abra a página e recarregue com `Ctrl+Shift+R` (força ignorar o
> cache do navegador). Sem isso você pode continuar vendo a versão antiga.

---

## Onde fica cada coisa

Quase tudo está no **bloco CONFIG**, nas primeiras 105 linhas do arquivo. Ele começa em
`const CONFIG = {` e termina em `};`.

| Quero mudar… | Busque por (`Ctrl+F`) | Observação |
|---|---|---|
| Título grande do topo | `fraseHero` | Frase curta, até ~10 palavras |
| Texto abaixo do título | `subFraseHero` | 2 a 3 linhas |
| Preço "a partir de" | `precoAPartir` | Ex.: `"R$ 480"` |
| Capacidade exibida | `capacidade` | Ex.: `"4 a 6 pessoas (até 8)"` |
| Nota e nº de avaliações | `avaliacao` / `numAvaliacoes` | Ver seção "A nota" abaixo |
| WhatsApp | `whatsapp` | Só números, com 55 + DDD |
| Instagram | `instagram` | Sem @ |
| Link do Airbnb | `linkAirbnb` | |
| Os 6 quadros de diferenciais | `diferenciais` | Cada um tem `icone`, `titulo`, `texto` |
| Depoimentos de hóspedes | `depoimentos` | Ver "Adicionar avaliação" abaixo |
| Lista "O que fazer por perto" | `atracoes` | Uma linha por atração |
| Selos (Rio, Cozinha, Família) | `destaques` | |
| **Perguntas frequentes** | `<details><summary>` | Fica **fora** do CONFIG, mais abaixo |
| Título da aba do navegador | `<title>` | Bem no começo do arquivo |

---

## As três regras de ouro

**1. Mexa só no que está entre aspas.**

```
fraseHero:  "Um rio no fundo do quintal"
            ↑ troque só o que está aqui dentro ↑
```

**2. Não apague vírgulas, aspas, chaves `{ }` ou colchetes `[ ]`.**
São eles que seguram a estrutura. Se apagar um por engano, a página fica em branco.
(Tem conserto — veja "Se algo quebrar" abaixo.)

**3. Não edite abaixo da linha `FIM DO CONFIG`.**
Dali para baixo é o funcionamento da página. A única exceção é o FAQ, explicado adiante.

---

## Casos comuns

### Trocar o preço

Busque `precoAPartir` e troque o valor:

```
precoAPartir:    "R$ 450",
```

### Adicionar uma avaliação nova

Busque `depoimentos`. Cada avaliação é um bloco entre `{ }`. Para acrescentar,
copie o bloco existente e cole **antes** do `]`, separando com vírgula:

```
depoimentos: [
  { nome: "Ronald, fevereiro de 2026",
    texto: "Local hiper agradável, seguro, tudo funciona..." },
  { nome: "Camila, março de 2026",
    texto: "Cole aqui o texto da avaliação." }
],
```

⚠️ Repare: o penúltimo bloco termina com **vírgula**, o último **não**.

### Fazer a nota aparecer

A nota está escondida de propósito — com 2 avaliações o próprio Airbnb ainda não
mostra média. Quando chegar a **terceira**, tire as aspas angulares `«»`:

```
avaliacao:       "«4,5»",      →      avaliacao:       "4,8",
numAvaliacoes:   "«3»",        →      numAvaliacoes:   "3",
```

Enquanto tiverem `«»`, esses dados ficam ocultos automaticamente.

### Editar uma pergunta do FAQ

Busque `details><summary`. Cada pergunta é uma linha:

```
<details><summary>A PERGUNTA</summary><div class="resp">A RESPOSTA</div></details>
```

Troque só o texto da pergunta e da resposta. Mantenha as etiquetas `<...>` como estão.

### Trocar uma foto

Vá em **Add file → Upload files** dentro da pasta `assets/fotos/` e suba a foto nova
**com o mesmo nome** da que quer substituir (`foto-1.jpg`, `rio-1.jpg`…).

Link direto: `https://github.com/purushlis-coder/DomoBlua-Hospedagem-Chapada/upload/main/assets/fotos`

| Arquivo | Onde aparece |
|---|---|
| `foto-1.jpg` | fundo do topo da página |
| `rio-1.jpg` | foto grande da seção "O rio é o fundo do seu quintal" |
| demais | galeria |

---

## Se algo quebrar

A página ficou em branco ou estranha? Nada se perde — dá para voltar em 3 cliques:

1. Abra `https://github.com/purushlis-coder/DomoBlua-Hospedagem-Chapada/commits/main`
2. Ache a sua alteração na lista e clique nela
3. Botão **Revert** → **Commit changes**

Em 1 minuto o site volta ao que era antes.

---

## Quando me chamar

Vale mais a pena me pedir quando a mudança for:

- **Estrutural** — mover seções, criar uma nova, mudar cores ou layout
- **De texto longo** — reescrever a página inteira ou vários blocos de uma vez
- **Arriscada** — mexer em várias vírgulas e chaves ao mesmo tempo
- **De medição** — instalar Google Analytics ou Meta Pixel

Para trocar um preço, uma frase ou adicionar uma avaliação, o caminho acima é mais rápido
do que me pedir.
