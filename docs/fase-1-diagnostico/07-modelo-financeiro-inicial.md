# Fase 1 · Estrutura Inicial do Modelo Financeiro

Estrutura + **3 cenários** com números **`HIPÓTESE`** (mercado BR/Brasília, jun/2026). Serve para
você ver a mecânica e a ordem de grandeza. Vira modelo calibrado na Fase 5, quando você informar
custos fixos reais e a configuração do imóvel. Planilha para preencher:
[`../templates/modelo-financeiro.csv`](../templates/modelo-financeiro.csv).

## 1. Premissas explícitas (todas `HIPÓTESE` — substituir por dados reais)

| Premissa | Conservador | Realista | Otimista | Fonte/nota |
|----------|------------|----------|----------|------------|
| Diária média (ADR) | R$ 170 | R$ 220 | R$ 280 | Calibrar com concorrentes da sua quadra |
| Ocupação | 45% | 60% | 72% | Média capitais BR ~59–62% (mercado) |
| Noites/mês (base 30) | 13,5 | 18,0 | 21,6 | = 30 × ocupação |
| Taxa da plataforma | 15% | 15% | 15% | Modelo host-paid simplificado |
| Custos fixos/mês | R$ 1.300 | R$ 1.300 | R$ 1.300 | Condomínio+IPTU+energia+água+internet (estimado) |
| Consumíveis/noite | R$ 10 | R$ 10 | R$ 10 | Papel, café, amenities, etc. |
| Fundo de manutenção | 5% da receita | 5% | 5% | CAPEX recorrente (desgaste/quebra) |
| Taxa de limpeza | repassada ao hóspede ≈ cobre a diarista | idem | idem | Tratada como pass-through (net ≈ 0) |

> **Faixa de preço apertada — atenção:** se a sua diária real hoje for muito diferente, o resultado
> muda bastante. Por isso o nº 6 da [lista de dados](03-informacoes-a-levantar.md) (diária que você
> praticava) é prioritário.

## 2. P&L mensal por cenário (R$)

| Linha | Conservador | Realista | Otimista |
|-------|------------:|---------:|---------:|
| Receita de hospedagem (ADR × noites) | 2.295 | 3.960 | 6.048 |
| (−) Taxa da plataforma (15%) | −344 | −594 | −907 |
| **= Receita líquida de plataforma** | **1.951** | **3.366** | **5.141** |
| (−) Custos fixos | −1.300 | −1.300 | −1.300 |
| (−) Consumíveis | −135 | −180 | −216 |
| (−) Fundo de manutenção (5%) | −98 | −168 | −257 |
| **= Receita líquida operacional (NOI)** | **418** | **1.718** | **3.368** |
| → 50% Fundo de aquisição (2º imóvel) | 209 | 859 | 1.684 |
| → 50% Você + reserva de vacância | 209 | 859 | 1.684 |

> Limpeza tratada como pass-through (taxa cobrada do hóspede ≈ custo da diarista). Se a taxa **não**
> cobrir, lance a diferença como custo variável — a planilha tem essa linha.

## 3. Quanto tempo para formar a entrada do 2º imóvel?

Alvo `HIPÓTESE`: imóvel de **R$ 350 mil**, entrada de **20% + custos (~R$ 80 mil)**.
Acumulando **só os 50% da renda líquida** deste imóvel:

| Cenário | Aporte/mês (50%) | Meses p/ R$ 80 mil | ≈ Anos |
|---------|-----------------:|-------------------:|-------:|
| Conservador | 209 | 383 | ~32 |
| Realista | 859 | 93 | ~7,8 |
| Otimista | 1.684 | 48 | ~4,0 |

### ⚠️ Leitura honesta (o ponto mais importante desta fase)
**Um apartamento sozinho, no cenário conservador/realista, leva muitos anos para formar a entrada
inteira.** Isso não invalida a meta — mostra onde estão as alavancas:

1. **Subir o ADR** (anúncio melhor, fotos, eventos de Brasília, estadias premium) — maior alavanca.
2. **Subir a ocupação** (precificação dinâmica, mín. de noites, avaliações 5★).
3. **Aporte pessoal mensal** somado aos 50% (acelera muito o prazo).
4. **Reduzir a entrada necessária:** consórcio, financiamento com entrada menor, ou usar a
   **valorização/garantia do 1º imóvel** como alavanca (home equity) — analisado na Fase 6.
5. **Reduzir custos fixos** (renegociar internet, eficiência de energia).

> Conclusão: trate o 1º imóvel como **motor + prova de modelo**, não como única fonte da entrada.
> A combinação "caixa do Airbnb + aporte pessoal disciplinado + estrutura de crédito inteligente"
> é o que torna o 2º imóvel viável em prazo razoável. Isso é o tema central da Fase 6.

## 4. Estrutura de contas recomendada (separação desde o dia 1)

Quatro "caixas" (podem ser contas/sub-contas distintas):
1. **Conta Operacional do Imóvel** — entra receita Airbnb, saem custos fixos/variáveis.
2. **Fundo de Manutenção** — 5% da receita; só para quebra/desgaste/reposição de CAPEX.
3. **Reserva de Vacância** — cobre custos fixos de 2–3 meses fracos (meta: 3× custo fixo ≈ R$ 3.900).
4. **Fundo de Aquisição (2º imóvel)** — os 50% da renda líquida; intocável, idealmente rendendo.

> Regra de ouro: **dinheiro do imóvel não se mistura com dinheiro pessoal.** É o que permite medir
> rentabilidade de verdade e replicar o modelo no 2º imóvel.

## 5. Indicadores para acompanhar todo mês
- **RevPAR** (ADR × ocupação) — o número-rei.
- **Ocupação %** e **ADR** isolados (para saber qual alavanca puxar).
- **NOI** e **margem líquida** (NOI ÷ receita).
- **Custo por turnover** (diarista + consumíveis + lavanderia).
- **Nota média das novas avaliações** e **% de 5★**.
- **Aporte acumulado no Fundo de Aquisição** vs. meta.

## 6. Dados que faltam para fechar o modelo (vira `DADO`)
1. Custos fixos reais (condomínio, IPTU, energia, água, internet).
2. Diária e taxa de limpeza praticadas antes.
3. Configuração (capacidade real altera ADR e ocupação).
4. Valor por faxina da diarista.
5. Existe financiamento/parcela neste imóvel hoje?
6. Pessoa física ou MEI (impacto tributário sobre a receita).
