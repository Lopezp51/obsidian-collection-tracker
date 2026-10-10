---
Título: Assinatura Super Trio Absolute (Superman) - 12 Meses + 40% Desc.
Editora:
  - Panini
Status: Concluída
Envio: Bimestral
Parcelas: 12
Valor Original: 147.73
Desconto: 40%
Valor Total: 88.64
Valor Mensal: 7.39
Início: 2025-11-23
Início Pagamento: 2025-12
Fim Pagamento: 2026-11
Status Pagamento: Em Pagamento
Término: 2026-08-28
Volume Inicial: 2
Volume Final Contratado: 7
Volume Atual Recebido: 7
imagem: Banco de Imagens/HQ's/Absolute Superman 02.webp
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
| **Valor por Volume** | **R$ 14,77** *(com 40% de desconto)* |
| **Valor Total** | **R$ 88,64** *(cota correspondente do Super Trio Absolute - Pedido #2815063)* |
| **Frequência de Envio** | Bimestral |
| **Início dos Envios** | 12/01/2026 |
| **Volumes Contratados** | Vol. 02 ao 07 (6 volumes no total) |

---

### 📝 Observações
- Integrante do pacote "Super Trio Absolute - 12 Meses" com 40% de desconto.
- ⚠️ **Edição 07 pendente de envio / conclusão.** As edições 2 a 6 foram recebidas com sucesso.
