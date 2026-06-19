# Fase 1 · Estrutura do Modelo Financeiro (método e governança)

> ✅ Os **números reais e os 3 cenários calibrados** passaram a viver em
> [09-analise-financeira-real-e-decisao.md](09-analise-financeira-real-e-decisao.md), porque agora
> temos o histórico de pagamentos e os custos reais. **Este documento ficou com a parte que não muda:
> a mecânica do modelo, a estrutura de contas e os indicadores.** A planilha está em
> [`../templates/modelo-financeiro.csv`](../templates/modelo-financeiro.csv).

## 1. Como o modelo é construído (a mecânica)
```
Receita de hospedagem (ADR × noites ocupadas)
  − Taxa do Airbnb (~3% no modelo host-only, confirmado no seu extrato)
  = Receita após plataforma
  − Custos fixos (condomínio + luz + internet + IPTU = ~R$ 660/mês reais)
  − Custos variáveis (diarista líq. da taxa de limpeza + consumíveis)
  − Fundo de manutenção (5% da receita)
  = Líquido ao dono (NOI)
       ├─ 50% → Fundo de aquisição do 2º imóvel
       └─ 50% → Você + reserva de vacância
```

## 2. Estrutura de contas recomendada (separação desde o dia 1)
Quatro "caixas" distintas (contas ou sub-contas):
1. **Operacional do Imóvel** — entra receita, saem custos fixos/variáveis.
2. **Fundo de Manutenção** — 5% da receita; só para quebra/desgaste/reposição de CAPEX.
3. **Reserva de Vacância** — cobre ~3 meses de custo fixo (meta ≈ R$ 2.000).
4. **Fundo de Aquisição (2º imóvel)** — os 50%; intocável, idealmente rendendo (Tesouro/CDB liquidez diária).

> Regra de ouro: **dinheiro do imóvel não se mistura com dinheiro pessoal.** Sem isso, não dá para
> medir rentabilidade real nem replicar o modelo no 2º imóvel.

## 3. Indicadores para acompanhar todo mês (dashboard)
- **RevPAR** (ADR × ocupação) — o número-rei.
- **ADR** e **Ocupação %** isolados — para saber qual alavanca puxar.
- **NOI** e **margem líquida** (NOI ÷ receita).
- **Taxa de resposta do Airbnb** (hoje 50% — meta 100%) e **tempo de resposta**.
- **Nota das novas avaliações** e **% de 5★** (hoje 4,53 geral; meta ≥ 4,8).
- **Custo por turnover** (diarista + consumíveis + lavanderia).
- **Aporte acumulado no Fundo de Aquisição** vs. meta.

## 4. Premissa fiscal a validar
Receita de temporada/aluguel tem tratamento de **Imposto de Renda** (carnê-leão para pessoa física;
ou regime de pessoa jurídica). Isso **não entrou** nos cenários ainda — pode reduzir o líquido. Item a
planejar na Fase 5 com seu contador (saber se você opera como PF ou tem CNPJ).
