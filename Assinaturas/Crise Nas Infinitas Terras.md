---
Título: Assinatura Crise Nas Infinitas Terras - 14 Volumes + 30% Desc.
Editora:
  - Panini
Status: Ativa
Envio: Mensal
Parcelas: 12
Valor Original: 1328.60
Desconto: 37%
Valor Total: 837.02
Valor Mensal: 69.75
Início: 2025-12-07
Início Pagamento: 2026-01
Fim Pagamento: 2026-12
Status Pagamento: Em Pagamento
Volume Inicial: 1
Volume Final Contratado: 14
Volume Atual Recebido: 5
imagem: Banco de Imagens/HQ's/Crise Nas Infinitas Terras Vol. 01 - Crise Nas Múltiplas Terras Parte 01.webp
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
| **Valor por Volume** | **R$ 59,78** *(com 30% de desc. + cupom adicional)* |
| **Valor Original Estimado** | **R$ 1.328,60** *(~R$ 94,90 / volume)* |
| **Valor Total Pago** | **R$ 837,02** *(Preço base do pacote: R$ 930,02)* |
| **Frequência de Envio** | Mensal |
| **Data do Pedido** | 07/12/2025 |
| **Início das Entregas** | 19/05/2026 |
| **Volumes Contratados** | Vol. 01 ao 14 (14 volumes no total) |

---

### 📝 Observações
- Pedido Panini #2851086 / #009024124 de 07/12/2025.
- Contratados 14 volumes. Volumes 01 a 05 recebidos/faturados e Volume 06 recentemente processado na Panini.
