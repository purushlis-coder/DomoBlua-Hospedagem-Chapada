# 📸 Fotos reais para os posts do Instagram

Esta pasta é a "fila de fotos reais" da automação. **Fotos reais rendem mais alcance
que cards**, então alimente esta pasta sempre que puder (cachoeiras, trilhas, a
hospedagem, o pôr do sol do cerrado...).

## Como funciona
1. Jogue aqui arquivos `.jpg` ou `.png` (qualquer nome, sem espaços de preferência).
2. A cada post agendado, a automação **prioriza uma foto desta pasta** que ainda não
   foi usada (em ordem alfabética) e ajusta o corte para o formato do Instagram.
3. Se não houver foto nova, ela gera um **card de conteúdo** automaticamente.
4. As fotos já usadas ficam registradas em `instagram/state.json` (não são apagadas).

## Legenda personalizada (opcional)
Quer uma legenda específica para uma foto? Crie um `.txt` com o mesmo nome:

```
por-do-sol-mirante.jpg      ← a foto
por-do-sol-mirante.txt      ← a legenda (as hashtags você inclui no txt mesmo)
```

Sem o `.txt`, a automação usa a próxima legenda do banco de conteúdo
(`instagram/content.json`), que combina com o tema da página.

⚠️ Use apenas fotos suas ou com autorização — nada de fotos baixadas do Google.
