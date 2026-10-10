---
Editora:
  - Panini
Status: Ativa
Envio: Mensal
Parcelas: 1
Valor Original: 
Desconto: 
Valor Total: 
Valor Mensal: 
Início: 
Início Pagamento: 
Fim Pagamento: 
Status Pagamento: Em Pagamento
Volume Inicial: 1
Volume Final Contratado: 
Volume Atual Recebido: 0
imagem: 
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
> const pct = Math.min(100, Math.round((atual / total) * 100));
> 
> const htmlBar = `
> <div style="width: 100%; background-color: var(--background-modifier-border); border-radius: 10px; height: 18px; margin-top: 6px; overflow: hidden; position: relative; border: 1px solid rgba(0,0,0,0.1);">
>     <div style="width: ${pct}%; background: linear-gradient(90deg, #10b981, #059669); height: 100%; transition: width 0.5s ease;"></div>
>     <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; color: white; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
>         ${pct}%
>     </div>
> </div>
> <div style="text-align: center; font-size: 0.85em; margin-top: 4px; color: var(--text-muted);">
>     Recebidos <b>${atual}</b> de <b>${total}</b> volumes contratados (Vol. ${ini} ao ${fim})
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
| **Parcelamento** | `$= dv.current()?.Parcelas ? dv.current().Parcelas + "x de R$ " + (dv.current()["Valor Mensal"] || 0) : "-"` |
| **Ciclo Pagamento** | `$= (dv.current()?.["Início Pagamento"] || "-") + " até " + (dv.current()?.["Fim Pagamento"] || "-")` |
| **Status Pagamento** | `$= dv.current()?.["Status Pagamento"] || "Em Pagamento"` |
| **Valor Total** | `$= "R$ " + (dv.current()["Valor Total"] || 0)` |
| **Frequência de Envio** | `$= dv.current()?.Envio || "-"` |
| **Início dos Envios** | `$= dv.current()?.Início || "-"` |
| **Volumes Contratados** | `$= "Vol. " + (dv.current()["Volume Inicial"] || 1) + " ao " + (dv.current()["Volume Final Contratado"] || "-")` |

---

### 📝 Observações
- 
