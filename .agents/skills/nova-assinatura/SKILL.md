---
name: nova-assinatura
description: Cadastra uma nova assinatura de mangá ou quadrinho no Acervo, calculando parcelas, descontos, volume inicial/final e vinculando capa e barra de progresso.
---

# Skill: Cadastrar Nova Assinatura (`nova-assinatura`)

Use esta skill sempre que o usuário quiser registrar uma nova assinatura de mangás ou quadrinhos (seja ativa ou já concluída).

---

## 1. Regras de Nomes e Pastas
* Todas as notas de assinatura devem ser salvas em: `Assinaturas/<Nome da Série>.md`.
* Evite caracteres proibidos no Windows (`:`, `?`, `*`, `<`, `>`, `|`, `"`). Use hífen ou travessão.

---

## 2. Coleta e Normalização de Dados

Ao receber os dados do usuário (que podem vir incompletos ou em linguagem natural):

1. **Título:** Nome da obra / série (ex: `Claymore Remix`, `Batman (2025)`).
2. **Editora:** Se não especificado, assuma `Panini`.
3. **Status:**
   * `Ativa` (se em andamento ou futura).
   * `Concluída` (se já entregue/finalizada).
4. **Volumes:**
   * `Volume Inicial`: geralmente 1, mas pode começar em outro volume (ex: 7).
   * `Volume Final Contratado`: o último volume contratado (ex: 16).
   * `Volume Atual Recebido`: quantos já chegaram (para concluídas, é igual ao final).
5. **Cálculos Financeiros:**
   * Se o usuário der o valor total e o número de parcelas, calcule `Valor Mensal = round(Valor Total / Parcelas, 2)`.
   * Se o usuário der o valor com desconto e o % de desconto, calcule o `Valor Original = round(Valor Total / (1 - %desconto), 2)`.
   * Se o usuário der o valor por volume, calcule o `Valor Total = Valor Volume * Qtd Volumes`.
6. **Datas e Ciclo Financeiro:**
   * **Data de Corte do Cartão:** Dia **06** de cada mês.
   * Se a data da compra for posterior ao dia 06 (ex: dia 07 em diante), a 1ª parcela vai para o mês seguinte (`YYYY-(MM+1)`).
   * Se for até o dia 06, a 1ª parcela é no próprio mês (`YYYY-MM`).
   * `Início Pagamento`: mês da 1ª fatura (`YYYY-MM`).
   * `Fim Pagamento`: mês da última fatura (`YYYY-MM` após somar `Parcelas - 1` meses).
   * `Status Pagamento`: `Em Pagamento` (enquanto durar o parcelamento) ou `Quitado` (quando todas as parcelas forem pagas).
   * ⚠️ **Atenção:** Uma assinatura permanece com `Status: Ativa` enquanto ainda houver volumes para receber, mesmo que `Status Pagamento` já seja `Quitado`. O Painel de Assinaturas não soma mensalidade de assinaturas quitadas.
7. **Busca de Capa:**
   * Busque em `Banco de Imagens/Mangas/` ou `Banco de Imagens/HQ's/` pelo primeiro volume do pacote para vincular à propriedade `imagem`.

---

## 3. Template Obrigatório da Nota

```markdown
---
Título: "{{titulo_completo}}"
Editora:
  - {{editora}}
Status: {{status}}
Envio: {{frequencia_envio}}
Parcelas: {{numero_parcelas}}
Valor Original: {{valor_original}}
Desconto: {{desconto_pct}}
Valor Total: {{valor_total}}
Valor Mensal: {{valor_mensal}}
Início: {{data_inicio_iso}}
Início Pagamento: {{inicio_pagamento_ano_mes}}
Fim Pagamento: {{fim_pagamento_ano_mes}}
Status Pagamento: {{status_pagamento}}
Término: {{data_termino_iso}}
Volume Inicial: {{volume_inicial}}
Volume Final Contratado: {{volume_final}}
Volume Atual Recebido: {{volume_atual}}
imagem: {{caminho_imagem}}
tags:
  - Assinatura
---

> [!bookbox]
> ```meta-bind
> INPUT[imageSuggester(optionQuery("")):imagem]
> ```
> <div class="book-metadata">
>
> **Status:** `$= dv.current()?.Status || "Ativa"` &nbsp;|&nbsp; **Editora:** `$= (Array.isArray(dv.current()?.Editora) ? dv.current()?.Editora.join(", ") : dv.current()?.Editora) || "Panini"`
>
> ```dataviewjs
> const ini = dv.current()?.["Volume Inicial"] || 1;
> const fim = dv.current()?.["Volume Final Contratado"] || 1;
> const atual = dv.current()?.["Volume Atual Recebido"] || 0;
> const total = (fim - ini + 1) || 1;
> const recebidos = atual === 0 ? 0 : Math.min(total, Math.max(0, atual - ini + 1));
> const pct = Math.min(100, Math.round((recebidos / total) * 100));
> const corGradiente = dv.current()?.Status === "Concluída" ? "linear-gradient(90deg, #3b82f6, #1d4ed8)" : "linear-gradient(90deg, #10b981, #059669)";
> 
> const htmlBar = `
> <div style="width: 100%; background-color: var(--background-modifier-border); border-radius: 10px; height: 18px; margin-top: 6px; overflow: hidden; position: relative; border: 1px solid rgba(0,0,0,0.1);">
>     <div style="width: ${pct}%; background: ${corGradiente}; height: 100%; transition: width 0.5s ease;"></div>
>     <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
>         ${pct}%
>     </div>
> </div>
> <div style="text-align: center; font-size: 0.85em; margin-top: 4px; color: var(--text-muted);">
>     Recebidos <b>${recebidos}</b> de <b>${total}</b> volumes contratados (Vol. ${ini} ao ${fim})
> </div>
> `;
> 
> dv.span(htmlBar);
> ```
> 
> </div>

### 💳 Dados Financeiros e Envio

| Informação | Detalhe |
| :--- | :--- |
| **Parcelamento** | {{numero_parcelas}}x de **R$ {{valor_mensal_formatado}}** |
| **Valor Total** | **R$ {{valor_total_formatado}}** *(desconto sobre R$ {{valor_original_formatado}})* |
| **Frequência de Envio** | {{frequencia_envio}} |
| **Início dos Envios** | {{data_inicio_formatada}} |
| **Volumes Contratados** | Vol. {{volume_inicial}} ao {{volume_final}} ({{total_volumes}} volumes no total) |

---

### 📝 Observações
- {{observacoes}}
```

---

## 4. Atualização Automática
O [Painel de Assinaturas.md](file:///d:/Obsidian/Acervo%20de%20Leitura/Painel%20de%20Assinaturas.md) e [Bases/Assinaturas.base](file:///d:/Obsidian/Acervo%20de%20Leitura/Bases/Assinaturas.base) leem a pasta `Assinaturas/` automaticamente, sem necessidade de editar manualmente os painéis.
