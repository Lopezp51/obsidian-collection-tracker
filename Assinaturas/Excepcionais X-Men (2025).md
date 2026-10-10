---
Título: Assinatura Excepcionais X-Men - 12 Meses + 40% Desc.
Editora:
  - Panini
Status: Concluída
Envio: Mensal
Parcelas: 12
Valor Original: 238.80
Desconto: 40%
Valor Total: 143.28
Valor Mensal: 11.94
Início: 2025-11-24
Término: 2026-09-25
Volume Inicial: 1
Volume Final Contratado: 12
Volume Atual Recebido: 12
imagem: Banco de Imagens/HQ's/Excepcionais X-Men Vol. 01.webp
tags:
  - Assinatura
---

> [!bookbox]
> ```meta-bind
> INPUT[imageSuggester(optionQuery("")):imagem]
> ```
> <div class="book-metadata">
>
> **Status:** `$= dv.current()?.Status || "Concluída"` &nbsp;|&nbsp; **Editora:** `$= (Array.isArray(dv.current()?.Editora) ? dv.current()?.Editora.join(", ") : dv.current()?.Editora) || "Panini"`
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
>         ${pct}% (Concluída)
>     </div>
> </div>
> <div style="text-align: center; font-size: 0.85em; margin-top: 4px; color: var(--text-muted);">
>     Recebidos todos os <b>${total}</b> volumes contratados (Vol. ${ini} ao ${fim})
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
| **Parcelamento** | 12x de **R$ 11,94** |
| **Valor Total** | **R$ 143,28** *(40% de desconto sobre R$ 238,80)* |
| **Frequência de Envio** | Mensal |
| **Período de Envio** | 24/11/2025 a 25/09/2026 |
| **Volumes Contratados** | Vol. 01 ao 12 (12 volumes no total) |

---

### 📝 Observações
- Pedido Panini #2815063. Todas as 12 edições foram entregues e finalizadas.
