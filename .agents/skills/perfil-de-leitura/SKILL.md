---
name: perfil-de-leitura
description: Analisa o histórico de leituras do Acervo (avaliações, favoritos, anotações de leitura, coleções e assinaturas) para traçar o DNA de Leitura, arquétipo de leitor, gatilhos de interesse, dealbreakers e recomendações assertivas.
---

# Skill: Diagnóstico do Perfil de Leitura (`perfil-de-leitura`)

Esta skill deve ser usada sempre que o usuário quiser:
- Compreender seus padrões de gosto para quadrinhos, mangás e graphic novels.
- Identificar por que gosta tanto de certas obras e se decepciona com outras.
- Obter recomendações cirúrgicas de novas leituras baseadas no seu acervo real.
- Atualizar seu documento de perfil de leitor no Obsidian.

---

## 1. Passo 1: Executar a Extração de Dados
Antes de realizar a análise, execute o extrator nativo via terminal para garantir que os dados de todas as notas do Acervo e Assinaturas estejam atualizados:

```bash
python helpers/extract_reading_profile.py
```

O script irá gerar:
- `helpers/dados_perfil_leitor.json`: Dados brutos estruturados de obras, autores, notas e coleções.
- `helpers/resumo_perfil_leitor.md`: Resumo consolidado com distribuição de notas, favoritos, obras críticas e as impressões reais registradas em `[obs:: ...]`.

---

## 2. Passo 2: Ler o Resumo Atualizado
Leia o conteúdo de `helpers/resumo_perfil_leitor.md` usando a ferramenta de leitura de arquivos.

Dê atenção especial às frases literais do leitor em `[obs:: ...]`:
- O que fez o usuário dar nota máxima ou chorar/se emocionar?
- O que gerou descontentamento, notas baixas (0.5 a 2.5) ou sensação de tempo perdido?
- O que o usuário destacou sobre a arte, o ritmo e o desenvolvimento dos personagens?

---

## 3. Passo 3: Diretrizes de Análise (A Mente da IA Curadora)
Ao analisar os dados, adote o tom de um **curador editorial e crítico cultural experiente**. A análise deve ser dividida em:

1. **Arquétipo do Leitor:** Título descritivo marcante e 2-3 parágrafos sobre a relação do usuário com a nona arte.
2. **Pilares do Gosto (O que move a paixão):** 
   - Temas centrais (mitologia, fantasia sombria, humanismo, laços interpessoais).
   - Dinâmica narrativa (construção paciente de mundo, arcos que amarram todas as pontas).
   - Estética visual valorizada (arte densa, expressiva, cinética, respeito entre texto e imagem).
3. **Padrões de Criadores & Fases:** 
   - Autores e artistas recorrentes nas notas 4.5 e 5.0.
   - Fases preferidas (ex: George Pérez e Greg Rucka em Mulher-Maravilha, Kentaro Miura, Alan Moore, Kelly Thompson, Scott Snyder/Nick Dragotta).
4. **O Filtro de Dealbreakers (O que é rejeitado):**
   - Incoerências com a essência de personagens amados.
   - Exposição vazia, violência sem peso emocional ("edgy gratuito").
   - Romances repentinos sem química ou tramas aceleradas/rushadas.
   - Capas enganosas ou decepção visual.
5. **Gatilhos para Decisões de Compra:**
   - Critérios para compra às cegas (*blind buys*).
   - Sinais vermelhos de alerta antes de assinar ou comprar.
6. **Recomendações Cirúrgicas:**
   - 5 a 7 recomendações de quadrinhos ou mangás que não constam no acervo lido, justificadas cruzando obras específicas que o leitor já favoritou.

---

## 4. Passo 4: Salvar e Relatar
Salve a análise formatada em Markdown no arquivo:
`Visão Geral - Perfil do Leitor.md` (na raiz da vault).

Apresente um resumo executivo acolhedor e instigante diretamente na conversa com o usuário.
