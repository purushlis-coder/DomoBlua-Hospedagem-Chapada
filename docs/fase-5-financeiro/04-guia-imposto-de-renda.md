# Fase 5 · Guia de Imposto de Renda para Anfitrião Airbnb (do zero)

> Você disse que **nunca fez IR** e quer se **antecipar**. Este guia te ensina o essencial, explica o
> que a planilha [`controle-fiscal-airbnb.xlsx`](controle-fiscal-airbnb.xlsx) faz por você, e registra o
> que estudei da legislação vigente em **junho/2026**.
>
> ⚠️ **Sou seu analista, não um contador registrado.** Isto é educação + ferramenta, baseado na lei
> atual. Regras mudam todo ano. Para a **sua 1ª declaração anual**, vale uma conferência pontual com um
> profissional — depois você toca sozinho com a planilha.

---

## Parte 1 — O essencial do Imposto de Renda (em linguagem simples)

### O que é
O **IRPF** (Imposto de Renda da Pessoa Física) é um imposto sobre o que você **ganha** no ano. Tem duas
"frentes" que te afetam como anfitrião:

1. **Carnê-leão (mensal):** quando você recebe aluguel/temporada **de pessoas físicas** (como hóspedes
   do Airbnb), o imposto **não é descontado na fonte**. Você mesmo apura e paga **todo mês**, se devido.
2. **Declaração de Ajuste Anual (anual):** uma vez por ano você declara tudo o que ganhou e possui. O
   que pagou de carnê-leão no ano é **abatido** ali (pode gerar restituição ou imposto a pagar).

> Pense assim: **carnê-leão = adiantamento mensal**; **declaração anual = acerto de contas**.

### Como o Airbnb é tributado
A renda de **aluguel por temporada** é tratada como **rendimento de aluguel** (não como "empresa").
Recebendo de pessoas físicas via plataforma, cai no **carnê-leão** (DARF código **0190**). Na declaração
anual, entra em **"Rendimentos Tributáveis Recebidos de Pessoa Física/Exterior"**.

### As deduções que reduzem o imposto (importante!)
Do valor recebido de aluguel você pode **descontar**, antes de calcular o imposto, as despesas ligadas
ao imóvel **pagas por você**:
- **Condomínio**
- **IPTU**
- **Comissão/intermediação** → a **taxa do Airbnb** se enquadra aqui
- **Despesas de conservação/manutenção** do imóvel

> Por isso a planilha calcula a **"base tributável"** = receita − (taxa Airbnb + condomínio + IPTU +
> manutenção). É sobre essa base menor que o imposto incide.

---

## Parte 2 — A grande notícia de 2026 (o que muda no SEU caso)

Em **26/11/2025** foi sancionada a **Lei 15.270/2025**: a partir de **janeiro/2026**, quem tem
rendimentos tributáveis de **até R$ 5.000 por mês fica ISENTO** de IR (um "redutor" zera o imposto).
Entre **R$ 5.000 e R$ 7.350** há redução parcial; acima disso, tabela cheia.

**O que isso significa para você:** sua **base tributável** de aluguel (depois das deduções) tende a
ficar **bem abaixo de R$ 5.000/mês** em todos os cenários do modelo. Logo, o **imposto a pagar tende a
ser R$ 0** — **desde que você não tenha outra renda tributável grande** somada no mês.

### ⚠️ A variável decisiva: você tem OUTRA renda tributável?
A regra dos R$ 5.000 considera a **soma de tudo no mês**. Exemplos:
- Só Airbnb, base de R$ 2.800/mês → **isento** (abaixo de 5.000). IR = R$ 0.
- Salário R$ 4.000 + Airbnb R$ 2.800 → soma R$ 6.800 → **não** é isento; entra na faixa de redução parcial.

> 👉 **Me diga se você tem salário/pró-labore/outra renda tributável.** A planilha já tem a coluna
> "Outros rendimentos tributáveis" justamente para somar corretamente. Sem isso, eu assumo que o Airbnb
> é sua única renda tributável (hipótese).

---

## Parte 3 — "Pagar" é diferente de "Declarar" (a parte que te protege)

Você nunca teve problema, mas **isso não significa estar em dia** — a Receita pode revisar os últimos
**5 anos**. Há duas obrigações independentes:

| Obrigação | Quando se aplica | No seu caso |
|-----------|------------------|-------------|
| **Pagar carnê-leão (mensal)** | Quando a base tributável do mês passa da isenção (hoje R$ 5.000) | Provavelmente **não há imposto a pagar** (base baixa) |
| **Entregar a declaração anual** | Vários critérios — inclusive **ter recebido aluguel sujeito a carnê-leão** e ter rendimentos tributáveis acima do limite do ano | Você **provavelmente PRECISA declarar**, mesmo com imposto R$ 0 |

> 🔑 **Conclusão honesta:** receber aluguel de temporada + possuir imóvel costuma **te obrigar a
> declarar anualmente**, ainda que o imposto seja zero. Começar a declarar é a melhor forma de "se
> antecipar" e evitar **malha fina**. Não declarar quando se é obrigado gera **multa mínima de R$ 165,74**
> (e mais, se houver imposto). A planilha tem um indicador de obrigatoriedade na aba "Resumo Anual".

---

## Parte 4 — Como usar a planilha (rotina de 5 min/mês)

Arquivo: [`controle-fiscal-airbnb.xlsx`](controle-fiscal-airbnb.xlsx). Abre no **Excel** ou suba no
**Google Sheets** (Arquivo → Importar) para usar no celular.

**Toda virada de mês:**
1. Aba **"Lançamentos Mensais"** → preencha as **células amarelas** do mês:
   - Receita de hospedagem (diárias) e taxa de limpeza recebida → pegue no **app Airbnb** (payout do mês).
   - Taxa Airbnb paga, condomínio, IPTU, manutenção, outros custos (luz/internet/diarista) → boletos/extratos.
   - "Outros rendimentos tributáveis" → salário/pró-labore do mês, se houver.
2. As colunas **cinza/verde** calculam sozinhas: base tributável, **IR a pagar (DARF)**, líquido do
   imóvel e os **50% do Fundo de Aquisição**.
3. Se "IR a pagar (DARF)" for **R$ 0**, não há imposto naquele mês. Se for **> R$ 0**, veja a Parte 5.

**As abas:**
- **Instruções** — resumo de uso.
- **Tabela IR** — os valores da lei (editáveis quando a regra mudar). **Não precisa mexer no dia a dia.**
- **Lançamentos Mensais** — onde você trabalha.
- **Resumo Anual** — totais do ano e o indicador "precisa declarar?".

---

## Parte 5 — Passo a passo prático (quando houver imposto a pagar)

### Carnê-Leão (só se a base passar de R$ 5.000 num mês)
1. Acesse o **e-CAC** (gov.br) ou o app **"Carnê-Leão"** da Receita.
2. Lance o **rendimento de aluguel** recebido no mês e as **deduções** (condomínio, IPTU, comissão).
3. O sistema gera o **DARF (código 0190)**; pague até o **último dia útil do mês seguinte**.
4. Guarde o comprovante (a planilha já te diz o valor estimado).

### Declaração Anual (entre março e maio do ano seguinte)
1. Baixe o programa **"Meu Imposto de Renda"** (Receita) ou faça online no e-CAC.
2. Importe os dados do carnê-leão do ano (se usou) — ficha **"Rendimentos Tributáveis de PF/Exterior"**.
3. Informe o **imóvel** na ficha **"Bens e Direitos"** (com valor de aquisição).
4. Confira restituição/imposto a pagar e **transmita**. Guarde o recibo.

> 💡 A planilha te dá os **totais do ano** prontos para essas fichas (receita, deduções, base, imposto pago).

---

## Parte 6 — O que estudei (resumo técnico para você ficar craque também)

- **Base legal atual:** Lei 15.270/2025 (isenção até R$ 5.000/mês, redução até R$ 7.350), vigente desde
  jan/2026. A **tabela progressiva mensal** em si **não mudou** (continua de 2024): isenção até R$ 2.259,20,
  depois 7,5% / 15% / 22,5% / 27,5%, com "parcela a deduzir" em cada faixa. O **redutor** novo é o que zera
  o imposto até R$ 5.000.
- **Carnê-leão:** mecanismo mensal para renda de PF sem retenção na fonte (aluguel, autônomos). DARF 0190.
- **Deduções de aluguel:** IPTU, condomínio, comissão (taxa Airbnb), conservação/manutenção — **quando
  pagos pelo locador**. Reduzem a base antes da alíquota.
- **Temporada x serviço:** aluguel mobiliado simples = **rendimento de aluguel** (nosso caso). Se você
  oferecesse serviços de hotelaria (limpeza diária, café da manhã, recepção), poderia virar **prestação de
  serviço/PJ** — não é o seu caso hoje.
- **Reforma/CAPEX:** algumas benfeitorias podem **somar ao custo de aquisição** do imóvel na ficha de Bens
  e Direitos — isso **reduz o ganho de capital** (e o imposto) numa futura venda. Guarde todas as notas.
- **Prazo de fiscalização:** a Receita pode rever os **últimos 5 anos** → manter registros é proteção.

---

## Parte 7 — Seu plano fiscal (checklist para se antecipar)

- [ ] Me confirmar se tem **outra renda tributável** (muda a conta da isenção).
- [ ] Abrir conta/sub-conta **só do imóvel** e guardar todos os comprovantes (receita e despesas).
- [ ] Preencher a planilha **todo mês** (5 min) — receita do payout + custos.
- [ ] Verificar na aba "Resumo Anual" se está **obrigado a declarar** (provavelmente sim).
- [ ] Fazer a **declaração anual** no período (mar–mai), mesmo com imposto R$ 0.
- [ ] Guardar notas de **reforma/CAPEX** (reduzem imposto numa venda futura).
- [ ] (Opcional, recomendado uma vez) Validar a **1ª declaração** com um contador para pegar o jeito.

> Quando você me passar (a) se tem outra renda e (b) os primeiros meses reais de operação, eu **rodo a
> planilha com você**, confiro os números e ajusto o que for preciso. A partir daí, vira rotina simples.
