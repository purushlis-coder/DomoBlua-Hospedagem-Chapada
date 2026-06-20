# Fase 5 · Modelo Financeiro Completo e Cenários

> Versão consolidada e calibrada pelo **histórico real (2021–2025)** e custos reais. Mecânica e
> estrutura de contas detalhadas em [Fase 1 · doc 07](../fase-1-diagnostico/07-modelo-financeiro-inicial.md);
> análise da decisão (Airbnb × aluguel) em [Fase 1 · doc 09](../fase-1-diagnostico/09-analise-financeira-real-e-decisao.md).
> Planilha: [`../templates/modelo-financeiro.csv`](../templates/modelo-financeiro.csv).

## 1. Estrutura do P&L mensal
```
Receita de hospedagem (ADR × noites)        [varia por mix de preço — Fase 5 doc 01]
+ Taxa de limpeza recebida                   [≈ repassada à diarista]
− Taxa do Airbnb (~3% host-only)
= Receita líquida de plataforma
− Custos fixos (~R$ 660: condomínio 380 + luz 80 + internet 110 + IPTU 90)
− Custos variáveis (diarista + consumíveis + lavanderia)
− Fundo de manutenção (5% da receita)
− Imposto de renda (carnê-leão — ver doc 03)
= LÍQUIDO ao dono
     ├─ 50% → Fundo de Aquisição (2º imóvel)
     └─ 50% → Você + reserva de vacância/manutenção
```

## 2. Os 3 cenários (já com o reposicionamento)

| Linha (R$/mês) | Conservador | Realista | Otimista |
|---|---:|---:|---:|
| Diária média efetiva (ADR) | 130 | 165 | 200 |
| Ocupação | 60% | 70% | 80% |
| Noites/mês | 18 | 21 | 24 |
| **Receita de hospedagem** | 2.340 | 3.465 | 4.800 |
| (−) Taxa Airbnb ~3% | −70 | −104 | −144 |
| (−) Custos fixos | −660 | −660 | −660 |
| (−) Diarista + consumíveis | −150 | −200 | −250 |
| (−) Fundo de manutenção (5%) | −117 | −173 | −240 |
| (−) IR estimado (carnê-leão) | ~0 | ~−50 | ~−190 |
| **= LÍQUIDO ao dono** | **≈ 1.343** | **≈ 2.278** | **≈ 3.316** |
| → 50% Fundo de Aquisição | 672 | 1.139 | 1.658 |
| → 50% Você + reservas | 672 | 1.139 | 1.658 |

> O IR é uma estimativa (ver [doc 03](03-tributacao-e-estrutura.md)); no conservador tende a **zero**
> (abaixo da faixa de isenção mensal após deduções). Limpeza tratada como pass-through.

## 3. Detalhamento por cenário

### 🔴 Conservador (ADR 130 · ocup. 60%)
- **Receita líquida:** ~R$ 1.343/mês · **Ao fundo:** R$ 672/mês.
- **Riscos:** reposicionamento fraco, nota não sobe, muitos buracos de calendário, sazonalidade.
- **Alavancas:** subir taxa de resposta (50%→100%), fotos, AC/TV, desconto mensal para preencher buraco.
- *Leitura honesta:* ainda **empata** com inquilino fixo. É o piso a superar.

### 🟡 Realista (ADR 165 · ocup. 70%) — meta operacional
- **Receita líquida:** ~R$ 2.278/mês · **Ao fundo:** R$ 1.139/mês.
- **Riscos:** execução da operação remota, consistência de limpeza, manter resposta rápida.
- **Alavancas:** precificação dinâmica, mix curta+longa, eventos de Brasília, avaliações 5★.
- *Leitura:* **supera o inquilino fixo** e gera caixa real para a expansão.

### 🟢 Otimista (ADR 200 · ocup. 80%)
- **Receita líquida:** ~R$ 3.316/mês · **Ao fundo:** R$ 1.658/mês.
- **Riscos:** depende de alta temporada/eventos sustentados e operação afiada.
- **Alavancas:** PriceLabs captando picos, mínimo de noites em datas quentes, Superhost.
- *Leitura:* patamar que **acelera de verdade** a entrada do 2º imóvel.

## 4. Reservas e reinvestimento (disciplina de caixa)
Dos **50% que ficam com você**, sugiro subdividir:
- **Reserva de vacância:** até atingir **3× custo fixo (~R$ 2.000)** — depois, redirecionar.
- **Fundo de manutenção:** já provisionado (5% da receita) — para quebras/reposição de CAPEX (split, TV, colchão).
- **Reinvestimento inicial:** nos primeiros meses, parte dos 50% paga o **CAPEX faseado** (split, TV — ver Fase 2).
- O restante é sua **renda**.

## 5. Tempo para formar a entrada do 2º imóvel (R$ 80 mil)

| Cenário | Aporte/mês (50%) | Meses | ≈ Anos |
|---------|-----------------:|------:|-------:|
| Conservador | 672 | 119 | ~10 |
| Realista | 1.139 | 70 | ~5,9 |
| Otimista | 1.658 | 48 | ~4,0 |

> ⚡ **Lembrete da Fase 6:** o imóvel está **quitado**. A alavanca de **home equity/garantia** pode
> antecipar a compra do 2º imóvel **muito antes** desses prazos — poupar os 50% é o plano B, não o principal.

## 6. Indicadores a acompanhar (dashboard — ver Fase 3 doc 06)
RevPAR · ADR · Ocupação · NOI · Margem líquida · Taxa de resposta · % 5★ · Custo por turnover ·
Aporte acumulado no Fundo de Aquisição.

## 7. O que ainda calibra o modelo (vira DADO)
1. Confirmar IR real com contador (regime, deduções) — [doc 03](03-tributacao-e-estrutura.md).
2. Custo real de energia no verão (AC sobe a conta de luz — ajustar custos fixos).
3. Mix real curta×longa nos primeiros 3 meses → recalibrar ADR/ocupação.
