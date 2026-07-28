# 📤 Como enviar as fotos do rio e da cachoeira

As 5 fotos que você mandou no chat (rio ao pôr do sol, céu rosa e o banho no poço)
**não chegam ao repositório automaticamente** — imagens coladas na conversa são
visualizadas, mas não viram arquivo. Anexos de verdade (como o PDF e o `.docx`) sim.

Escolha **um** dos caminhos abaixo. Os dois levam 2 minutos.

---

## Caminho A — Direto no GitHub (recomendado, não precisa de mais nada)

1. Abra: `https://github.com/purushlis-coder/airbnb-goal/upload/main/assets/fotos`
2. Arraste as fotos e **renomeie** para os nomes exatos abaixo.
3. Escreva "fotos do rio" na caixa de commit e clique em **Commit changes**.
4. Repita em `https://github.com/purushlis-coder/airbnb-goal/upload/main/instagram/media`
   para alimentar o robô do Instagram.

## Caminho B — Aqui no chat

Reenvie as mesmas fotos usando o **anexo/clipe de arquivo** (não colar na conversa).
Aí eu mesmo processo, renomeio, comprimo e faço o commit.

---

## 📛 Nomes exatos dos arquivos

### Em `assets/fotos/` (aparecem na landing page)

| Nome do arquivo | Qual das suas fotos |
|---|---|
| `rio-1.jpg` | **O rio dourado com a faixa de areia** — vira a foto grande da seção "O rio é seu" |
| `rio-2.jpg` | O poço com o **céu rosa** refletido na água |
| `poco-do-motor.jpg` | A pessoa **boiando** de frente para a queda d'água |

> A seção "O rio é seu. Literalmente." fica **escondida** até o `rio-1.jpg` existir.
> Assim que ele aparecer, a seção surge sozinha — não precisa mexer em código.

### Em `instagram/media/` (o robô publica sozinho)

Suba as mesmas fotos com estes nomes:

| Nome do arquivo | Legenda já pronta |
|---|---|
| `rio-1.jpg` | ✅ `rio-1.txt` (fim de tarde no ribeirão) |
| `rio-2.jpg` | ✅ `rio-2.txt` (céu rosa) |
| `poco-do-motor.jpg` | ✅ `poco-do-motor.txt` (boiando no poço) |

As legendas **já estão escritas e commitadas** nesta pasta. No próximo horário
agendado, o robô pega a foto, usa a legenda correspondente e publica — fotos reais
têm prioridade sobre os cards gerados.

Se quiser mandar mais fotos além dessas três, pode usar qualquer nome (`trilha-01.jpg`,
`deck-manha.jpg`…). Sem um `.txt` de mesmo nome, o robô usa a próxima legenda do
banco de conteúdo, que também combina com o tema.

---

## 💡 Dica de formato

- O Instagram corta tudo para **4:5 (retrato)** — o robô já faz esse corte sozinho,
  centralizado. Se o assunto principal estiver muito na borda, prefira mandar já cortada.
- Para a landing page, fotos com **1200px ou mais** de largura ficam melhores.
- Suas fotos parecem ser quadros de vídeo (vertical, 9:16). Funcionam bem — só evite
  as que ficaram com desfoque de movimento.
