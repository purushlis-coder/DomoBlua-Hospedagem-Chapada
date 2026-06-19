# Fase 1 · Diagnóstico do Anúncio e do Imóvel

> ⚠️ **Limitação de partida:** o Airbnb bloqueia leitura automatizada do anúncio (erro HTTP 403),
> então **não tenho acesso ao título, descrição, fotos, preço, nota e avaliações atuais**.
> Este diagnóstico combina (a) o que é estruturalmente verdade para qualquer anúncio que ficou
> ~1 ano fora de operação no Plano Piloto e (b) hipóteses marcadas como `HIPÓTESE`, a serem
> confirmadas quando você preencher [`info-imovel-coletar.md`](../templates/info-imovel-coletar.md)
> e enviar fotos.

## A. Diagnóstico do anúncio (status e riscos estruturais)

### A.1. O problema nº 1: o anúncio "esfriou" no algoritmo
Um imóvel que passou ~1 ano alugado para inquilino fixo provavelmente esteve **com calendário
bloqueado ou sem reservas**. No Airbnb isso tem consequências concretas:

- **Perda de relevância na busca.** O algoritmo prioriza anúncios com reservas recentes, respostas
  rápidas e avaliações frescas. Um anúncio "parado" cai no ranking.
- **Status de Superhost provavelmente perdido** (`HIPÓTESE`), pois ele depende de volume de
  reservas e avaliações nos últimos 12 meses.
- **Avaliações desatualizadas.** As notas existentes continuam, mas sem reviews recentes o anúncio
  transmite menos confiança e o algoritmo "não sabe" se a operação ainda é boa.

➡️ **Implicação:** ao reabrir, você estará efetivamente **recomeçando a reputação ativa**. A
estratégia dos primeiros 30–45 dias precisa ser desenhada para **gerar avaliações 5★ rápido**
(preço de entrada competitivo + experiência impecável). Detalhamento na Fase 4.

### A.2. Riscos prováveis de conteúdo do anúncio (a confirmar com as fotos/print)
Padrões mais comuns em anúncios que precisam de repaginação:

| Item | Risco provável | Por que importa |
|------|----------------|-----------------|
| **Fotos** | Fotos antigas, escuras, desorganizadas, fora de ordem, ou do tempo do inquilino | Fotos são ~80% da decisão de clique. É a alavanca de maior ROI do anúncio. |
| **Título** | Genérico ("Apartamento em Brasília") sem gancho de localização/benefício | Título define a taxa de clique na busca. |
| **Descrição** | Texto longo, sem escaneabilidade, sem destacar diferenciais reais | Hóspede lê em diagonal; precisa bater o olho e entender o valor. |
| **Comodidades** | Lista incompleta (Wi-Fi, ar-condicionado, cozinha equipada não marcados) | Filtros de busca eliminam seu anúncio se a comodidade não está marcada. |
| **Regras/políticas** | Frouxas demais (atrai problema) ou rígidas demais (afasta reserva) | Calibram o perfil de hóspede e o risco de dano. |
| **Check-in** | Sem autoatendimento descrito | Essencial para operação remota; hóspede valoriza autonomia. |

### A.3. O que provavelmente já é um trunfo (a confirmar)
- **Localização Plano Piloto** é forte para o público certo: viagem a trabalho, concursos públicos,
  eventos do governo, saúde (hospitais/HUB), turismo cívico. `HIPÓTESE` a confirmar pela quadra exata.
- **Avaliações históricas** acumuladas valem ouro — não se perde o histórico, só a "frescura". É uma
  vantagem enorme sobre um anúncio zerado.

## B. Diagnóstico do imóvel (a partir de premissas; calibrar com fotos)

> Sem fotos atuais, avalio por **dimensões de risco**. Cada uma será pontuada de 0–5 quando eu
> receber as imagens. Por ora, aponto **o que olhar** e **o padrão-alvo**.

### B.1. Dimensões a avaliar
1. **Estado de pintura e paredes** — após inquilino fixo, é comum haver marcas, furos, desgaste.
   *Padrão-alvo:* paredes brancas/neutras, limpas, sem marcas — base de "limpeza percebida" e de boas fotos.
2. **Iluminação** — ponto subestimado. Luz amarela fraca destrói fotos e sensação de aconchego.
   *Padrão-alvo:* lâmpadas brancas/neutras potentes nas áreas de foto + pontos de luz quente para conforto.
3. **Estado do enxoval/colchão** — provavelmente comprometido após uso de inquilino.
   *Padrão-alvo:* colchão sem manchas com protetor impermeável; enxoval branco hoteleiro novo.
4. **Cozinha funcional** — itens faltando/desemparelhados afetam avaliação e praticidade.
   *Padrão-alvo:* kit completo e padronizado (detalhado na Fase 2).
5. **Banheiro** — vedação, chuveiro, espelho, organização. Área crítica de "limpeza percebida".
6. **Cheiro e umidade** — imóvel fechado por transição costuma ter odor; mata a primeira impressão.
7. **Pequenos defeitos** — tomadas, fechaduras, vazamentos, portas — geram reclamação e nota baixa.

### B.2. Hipótese de configuração (CONFIRMAR)
- `HIPÓTESE`: apartamento de **1 quarto ou quitinete/JK** no Plano Piloto, dada a faixa típica do
  anúncio. **Preciso confirmar:** nº de quartos, nº de banheiros, nº de camas e tipo, metragem,
  capacidade máxima, andar, elevador, vaga, mobília atual.

## C. Conclusão do diagnóstico (o veredito honesto)

1. **O ativo é bom; a operação está "fria".** O maior gargalo não é o imóvel — é **reativar reputação
   e modernizar a vitrine (fotos + texto + comodidades)**.
2. **Operação remota ainda não existe de fato.** Não há (ainda) diarista contratada, fechadura
   eletrônica, enxoval redundante nem checklists. Isso é o que separa "alugar um apê" de "ter um negócio".
3. **A reabertura exige um sprint curto e bem priorizado** (Jun–Jul/2026): essencial primeiro,
   estética depois, automação em paralelo.

➡️ Os próximos documentos transformam isso em ação: [gargalos](02-gargalos-reativacao.md) →
[dados a levantar](03-informacoes-a-levantar.md) → [plano de 15 dias](04-plano-de-acao-15-dias.md).
