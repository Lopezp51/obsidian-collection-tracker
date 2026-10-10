---
description: Cadastra uma nova assinatura de mangás ou quadrinhos com cálculos de parcelas, datas, volumes e barra de progresso.
---

# Workflow: Nova Assinatura (`/nova-assinatura`)

Siga rigorosamente as instruções da skill [nova-assinatura](file:///d:/Obsidian/Acervo%20de%20Leitura/.agents/skills/nova-assinatura/SKILL.md).

## Passos:
1. Obtenha os dados do usuário (Título, volumes inicial/final, parcelas, valores, descontos, datas e periodicidade).
2. Calcule os campos numéricos (valor total, mensalidade, % de desconto) e o ciclo financeiro (corte do cartão dia 06: compras após dia 06 têm 1ª parcela no mês seguinte; defina `Início Pagamento`, `Fim Pagamento` e `Status Pagamento`).
3. Busque a imagem da capa do volume inicial em `Banco de Imagens/` para enriquecer a nota.
4. Crie a nota em `Assinaturas/<Título>.md` usando o template oficial com metadados YAML e barra de progresso DataviewJS.
5. Verifique se o [Painel de Assinaturas.md](file:///d:/Obsidian/Acervo%20de%20Leitura/Painel%20de%20Assinaturas.md) reflete os novos dados corretamente.
