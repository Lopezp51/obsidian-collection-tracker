---
description: Analisa o acervo de quadrinhos e mangás lidos no Obsidian para gerar o perfil de gosto do leitor, dealbreakers e recomendações.
---

# Workflow: Análise do Perfil de Leitor (`/perfil-leitor`)

Quando o usuário invocar `/perfil-leitor` ou pedir para analisar o seu gosto literário/de quadrinhos, siga estas etapas:

## 1. Atualizar a Base de Dados
Execute o script extrator para garantir que qualquer obra recém-lida ou nota alterada esteja contemplada:
```bash
python helpers/extract_reading_profile.py
```

## 2. Ler o Resumo de Dados
Abra o arquivo gerado:
`helpers/resumo_perfil_leitor.md`

Examine as estatísticas, os favoritos, os itens com notas baixas e, fundamentalmente, as observações pessoais registradas nas notas.

## 3. Gerar a Análise Completa
Seguindo as diretrizes da skill `perfil-de-leitura`, elabore o relatório completo contendo:
- Arquétipo e Síntese de Leitura
- Os Grandes Pilares de Interesse
- Estilo Visual & Narrativa Preferida
- Mapeamento de Dealbreakers (O que gera decepção)
- Bússola de Compras Futuras
- 5 a 6 Recomendações Cirúrgicas com Justificativa Cruzada

## 4. Salvar na Nota de Visão Geral
Escreva ou atualize a nota:
[Visão Geral - Perfil do Leitor.md](file:///d:/Obsidian/Acervo%20de%20Leitura/Visão%20Geral%20-%20Perfil%20do%20Leitor.md)

## 5. Feedback no Chat
Exiba os pontos mais marcantes da análise para o usuário de forma envolvente, convidando-o a consultar a nota completa na vault.
