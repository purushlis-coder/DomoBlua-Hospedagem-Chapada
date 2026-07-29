# 🧹💰 Estratégia de limpeza e o preço que a sustenta

Resolve o problema levantado pelo anfitrião: **a diarista cobra R$400, a taxa cobrada é
R$257, e a casa suja sozinha quando fica muito tempo vazia** — teias, poeira e insetos
mortos se acumulam durante a ociosidade.

Complementa o [`RELATORIO-DIAGNOSTICO-AIRBNB.md`](RELATORIO-DIAGNOSTICO-AIRBNB.md),
aprofundando a economia da limpeza.

---

## 1. O erro que está invertido hoje

| Taxa cadastrada | Valor | Estadia típica | Custo de limpeza por noite |
|---|---:|---:|---:|
| Estadia **curta** | R$233 | 2 noites | **R$200/noite** |
| Estadia regular | R$257 | 3-4 noites | R$100-133/noite |

**A taxa de estadia curta é menor que a regular.** Isso está ao contrário da economia:
a limpeza custa o mesmo R$400 independentemente de o hóspede ficar 2 ou 7 noites, então
é justamente a estadia curta que menos consegue diluir esse custo — e é ela que recebe
desconto hoje.

Resultado por reserva de 2 noites: R$400 de custo contra R$233 arrecadados =
**R$167 de prejuízo direto**, antes de qualquer outro gasto.

---

## 2. A raiz do problema: uma limpeza no momento errado

Limpar **depois do checkout** não garante casa limpa **na chegada seguinte**. Entre uma
coisa e outra pode haver semanas de cerrado entrando pela fresta.

Isso empurra o anfitrião para uma armadilha: ou aceita entregar a casa empoeirada, ou
paga **duas** limpezas (R$800) para uma única reserva.

### A saída: separar em dois trabalhos distintos

| Trabalho | Quando | O que inclui | Quem faz | Custo alvo |
|---|---|---|---|---:|
| **Fechamento** | até 24h após o checkout | lixo, alimentos, roupa de cama recolhida e lavada, água/gás fechados, checagem de danos, fotos | anfitrião, coanfitrião ou ajudante | **R$0-120** |
| **Preparação** | 24-48h **antes** da chegada | limpeza completa, poeira, teias, insetos, roçagem do acesso, camas montadas, testes, 12 fotos | diarista | **R$400** |

**Por que resolve:** a limpeza completa acontece imediatamente antes da chegada. O tempo
ocioso passa com a casa *fechada*, não *pronta*. O hóspede sempre encontra casa recém-limpa,
não importa se a reserva anterior foi há três dias ou há dois meses.

**E o custo não dobra:** continua sendo **uma** limpeza completa por reserva. O fechamento
é tarefa de 45-60 minutos — não exige a diarista.

> ⚠️ O fechamento é inegociável mesmo assim: roupa suja e lixo parados por semanas geram
> mofo e cheiro que nenhuma limpeza posterior remove.

---

## 3. Custo real por reserva

| Item | Valor |
|---|---:|
| Preparação (diarista) | R$400 |
| Fechamento | R$100 |
| Consumíveis (produtos, papel, gás, sabonete) | R$50 |
| **Custo operacional por reserva** | **R$550** |

Como esse custo é **fixo por reserva**, o número de noites muda tudo:

| Noites | Custo de limpeza diluído |
|---:|---:|
| 2 | R$275/noite |
| 3 | R$183/noite |
| 4 | R$138/noite |
| 5 | R$110/noite |
| 7 | R$79/noite |

**Os similares da região são reservados por 3,25 noites em média** (relatório, §2.3).
A estadia curta de 2 noites é a pior faixa possível para esta operação.

---

## 4. Proposta de estrutura de preço

O relatório já identificou a distorção central: **R$117 por hóspede adicional acima de 3
pessoas** pune exatamente o público que a casa deveria atrair. A correção move dinheiro
da taxa por pessoa para a base, e leva a limpeza para perto do custo.

| Parâmetro | Hoje | Proposto |
|---|---:|---:|
| Preço Inteligente | ativo, R$408-1.634 | **desligar** ou estreitar para R$460-900 |
| Base (inclui) | 3 hóspedes | **4 hóspedes** |
| Diária base (dom-qui) | — | **R$480-520** |
| Diária base (sex-sáb) | — | **R$580-650** |
| Hóspede adicional | R$117/noite | **R$65/noite** (a partir do 5º) |
| Taxa de limpeza | R$257 | **R$390** |
| Taxa de estadia curta | R$233 *(menor!)* | **eliminar** — mesma taxa para todos |
| Mínimo de noites | 2 | **2 na baixa · 3 em fins de semana e feriados** |
| Desconto mensal | 25% | **15%** |
| Desconto semanal | 10% | **8%** |

### O que o hóspede paga — antes e depois (3 noites)

| Grupo | Estrutura atual | Proposta | Diferença |
|---|---:|---:|---:|
| 4 pessoas | R$1.832 | R$1.890 | +3% |
| 6 pessoas | R$2.534 | R$2.280 | **−10%** |
| 8 pessoas | R$3.236 | R$2.670 | **−17%** |
| 10 pessoas | R$3.938 | R$3.060 | **−22%** |

*(base R$500/noite na coluna proposta; atual calculado sobre o piso de R$408 do Preço Inteligente)*

**A proposta fica mais barata para todo grupo a partir de 5 pessoas — que é o público-alvo
— e ainda assim cobre o custo real da limpeza.** Hoje acontece o inverso: a casa subsidia
a limpeza e cobra o prejuízo dos grupos grandes.

### Contribuição por reserva (3 noites, após 15% de taxa e R$550 de custo)

| Grupo | Total do hóspede | Contribuição |
|---|---:|---:|
| 4 pessoas | R$1.890 | R$1.057 |
| 6 pessoas | R$2.280 | R$1.388 |
| 8 pessoas | R$2.670 | R$1.720 |
| 10 pessoas | R$3.060 | R$2.051 |

Com **3 reservas por mês** (9 noites, 30% de ocupação), a contribuição fica entre
**R$3.200 e R$4.200/mês**. É o patamar em que a operação começa a financiar as melhorias
da fila do relatório (§12).

Hoje são **zero reservas**, então qualquer estrutura que converta é superior à atual.

---

## 5. O custo fixo mensal ainda não existe como dado

Para saber quantas reservas por mês tornam a operação lucrativa, falta o outro lado da
conta: **quanto a casa custa por mês mesmo vazia.**

Esse número precisa ser levantado da realidade — extratos, boletos e recibos —, não estimado:

| Item | Valor/mês | Onde conferir |
|---|---|---|
| IPTU (÷12) | | carnê |
| Energia (consumo mínimo com a casa vazia) | | fatura |
| Internet | | fatura |
| Seguro | | apólice |
| Água / poço / bomba | | fatura |
| Manutenção preventiva (roçagem, dedetização, jardim) | | recibos |
| Financiamento ou custo de capital, se houver | | contrato |
| **Total fixo mensal** | | |

Com esse total, o ponto de equilíbrio sai direto:

> **reservas necessárias por mês = custo fixo ÷ contribuição por reserva**

Usando a contribuição da tabela acima (R$1.057 a R$2.051 conforme o tamanho do grupo):

| Se o custo fixo for | Reservas/mês para empatar |
|---:|---:|
| R$1.000 | ~1 |
| R$2.000 | ~1,5 a 2 |
| R$3.000 | ~2 a 3 |
| R$4.000 | ~3 a 4 |

**Nenhuma meta de ocupação ou projeção de retorno é confiável antes desse levantamento.**

---

## 6. Reserva por aprovação — mantida, e por quê

O anfitrião mantém o anúncio em **solicitação de reserva** porque a disponibilidade de
diarista é limitada na cidade. Está correto, e o relatório concorda (§7.3).

Mas isso cria uma dependência crítica: **cada hora de demora em responder é uma reserva
que pode evaporar.** Com resposta hoje em 78-80% e "até um dia", o anúncio combina o pior
dos dois mundos — exige aprovação e demora a aprovar.

Protocolo mínimo:

1. **Resposta automática imediata** ("Recebi! Confirmo a disponibilidade em até 2 horas")
2. **Confirmar com a diarista** a janela de preparação
3. **Aprovar ou recusar em até 2 horas** no horário comercial
4. **Nunca deixar mensagem sem resposta** — é o que derruba a taxa de 80%

**Cadastrar uma segunda pessoa para limpeza**, mesmo que faça só a revisão, elimina o
gargalo que justifica a aprovação manual. Com duas opções confiáveis, a Reserva Instantânea
passa a ser viável — e ela melhora ranking.

---

## 7. Sobre o Booking

A tentativa anterior não gerou resultado e o anúncio pode ter sido bloqueado.

**Recomendação: não retomar agora.** Um segundo canal multiplica o risco de reserva dupla
justamente enquanto a operação de limpeza ainda não está estabilizada — e o problema atual
não é falta de canal. São 74 visualizações com 0% de conversão: o gargalo está na página,
não no alcance.

Reavaliar quando houver **ocupação acima de 20% e nota ≥ 4,8**. Aí sim, com calendários
sincronizados via iCal.

---

## 8. Ordem de execução

**Esta semana — sem custo:**
1. Eliminar a taxa de estadia curta (é um desconto no lugar errado)
2. Subir a taxa de limpeza para R$390
3. Baixar hóspede adicional para R$65 e incluir 4 pessoas na base
4. Desligar ou estreitar o Preço Inteligente
5. Reduzir desconto mensal para 15%
6. Criar a resposta automática de solicitação de reserva

**Na próxima limpeza:**
7. Implantar a separação fechamento × preparação
8. Rodar o checklist fotográfico do relatório (§8.2)

**Nas próximas semanas:**
9. Cadastrar uma segunda pessoa para limpeza/revisão
10. Levantar o custo fixo mensal real (tabela do §5)
11. Confirmar o número exato de reservas históricas
