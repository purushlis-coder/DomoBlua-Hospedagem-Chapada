# Pacote de Automação do Airbnb (passo a passo de configuração)

> Tudo o que configurar **dentro do Airbnb** para a operação rodar quase sozinha e a taxa de resposta
> ir de **50% → ~100%**. Faça com o anúncio ainda **oculto**; só publique no go-live. Cada item diz
> **onde** ir e traz o **texto pronto** para colar. Substitua {variáveis}.

## A. Mensagens programadas (Airbnb → Mensagens → Programadas)
Crie 6 mensagens com estes gatilhos. (Textos completos no fim deste documento.)

| # | Mensagem | Gatilho |
|---|----------|---------|
| M1 | Confirmação da reserva | Ao reservar |
| M2 | Pré-check-in (dados p/ portaria) | 2 dias antes |
| M3 | Instruções de acesso (endereço, senha, Wi-Fi) | Dia do check-in, 10h |
| M4 | Boas-vindas / "entrou tudo certo?" | Dia do check-in, 19h |
| M5 | Lembrete de check-out | 1 dia antes do check-out |
| M6 | Pedido de avaliação | Dia do check-out, 14h |

> Para **estadia longa (28+)**: enviar manualmente a cada ~15 dias o check intermediário (M7).

## B. Respostas salvas / atalhos (Airbnb → Mensagens → Respostas salvas)
Crie atalhos para responder dúvidas em segundos: **/garagem, /wifi, /checkincedo, /checkout, /mercado,
/ar, /estacionar_visita** (textos no [doc de mensagens da Fase 4](../fase-4-anuncio/04-mensagens-automaticas.md)).

## C. Regras da casa (Airbnb → Anúncio → Regras da casa)
- Máx. **2 hóspedes** · Sem festas/eventos · Sem animais · Proibido fumar · Silêncio 22h–8h.
- Check-in a partir das **15h** · Check-out até **11h**.

## D. Política de hóspedes e reservas
- **Reserva imediata: ATIVADA com requisitos** (perfil verificado + sem avaliações negativas).
- Exigir **documento com foto** (cadastro na portaria 24h).
- (Opcional recomendado) **idade mínima 25** para o reservante.

## E. Preço e calendário (Airbnb → Calendário → Preços)
- **Preço-base de relançamento:** ~15–20% abaixo da tabela (ver [precificação](../fase-5-financeiro/01-modelo-de-precificacao.md)).
- **Smart Pricing:** ATIVADO **com preço mínimo definido** (piso) para não cair demais.
- **Descontos por duração:** **semanal −10/15%** e **mensal −25/35%** (capta a média temporada).
- **Taxa de limpeza:** R$ {100–120}.
- **Noites mínimas:** 2 (base); 3 em feriados/eventos.
- Abrir o calendário de **julho** em diante.

## F. Comodidades (Airbnb → Anúncio → Comodidades) — marcar TODAS as reais
Wi-Fi 250 Mbps · **Ar-condicionado** (após instalar) · **TV** · Cozinha · Estacionamento gratuito ·
Elevador · Espaço de trabalho · **Detector de fumaça** · Água quente · Roupa de cama/banho ·
Ferro/secador (se houver). *Não marcar o que não existe (exatidão é nota avaliada).*

## G. Check-in instructions (Airbnb → Anúncio → Instruções de check-in)
Cadastrar o passo a passo de acesso (portaria → elevador → andar → fechadura). A senha vai **só na
mensagem M3 do dia** (nunca pública).

---

## Textos prontos das mensagens (colar no Airbnb)

**M1 — Confirmação (ao reservar)**
```
Olá, {hospede}! 😊 Sou o Purush, anfitrião do apê na Asa Norte. Que bom ter você!
Sua reserva está confirmada para {checkin} → {checkout}.
Uns dias antes eu te envio todas as instruções de acesso.
Dúvidas? É só chamar por aqui. O apê tem garagem coberta, Wi-Fi rápido e ar-condicionado. 👍
```
**M2 — Pré-check-in (2 dias antes)**
```
Oi, {hospede}! Sua chegada está chegando ({checkin}). 🎉
Para eu deixar tudo certo na portaria, me confirma:
1) Horário previsto de chegada?
2) Vai de carro? (libero a vaga e a placa na portaria 24h)
3) Nome completo + documento de quem vai se hospedar?
No dia te mando endereço, senha da fechadura e Wi-Fi. Até já!
```
**M3 — Acesso (dia do check-in, 10h)**
```
Bom dia, {hospede}! Tudo pronto para o check-in a partir das 15h. 🔑
Endereço: SGAN 912 Norte, Bloco B — Cond. Master Place
Portaria 24h: informe seu nome (você já está cadastrado)
Senha da fechadura: {CÓDIGO}
Apartamento {nº} • Andar {andar} • Vaga {nº}
Wi-Fi: {rede} / senha {senha}
Manual da casa: {link}
Qualquer coisa no acesso, me chame na hora. Boa estadia! 😊
```
**M4 — Boas-vindas (dia do check-in, 19h)**
```
{hospede}, conseguiu entrar tranquilo? Está tudo certo no apê?
Se faltar algo, me avise que resolvo rápido. Boa estadia! 🙌
```
**M5 — Check-out (1 dia antes)**
```
Oi, {hospede}! O check-out é até as 11h de amanhã ({checkout}).
Antes de sair: louça lavada, lixo no local, janelas fechadas, ar desligado, porta trancada.
Foi um prazer! Se puder, depois deixe sua avaliação. 💙
```
**M6 — Avaliação (dia do check-out, 14h)**
```
{hospede}, obrigado pela estadia! 🙏 Sua avaliação ajuda muito.
Se algo não saiu 100%, me conta antes que eu corrijo. Até a próxima! 😊
```
**M7 — Estadia longa (manual, a cada ~15 dias)**
```
Oi, {hospede}! Como está sendo a estadia? Tudo funcionando?
Se quiser, agendo uma limpeza/troca de toalhas com a secretária. É só dizer. 🙂
```
