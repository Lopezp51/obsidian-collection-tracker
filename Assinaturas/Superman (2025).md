---
Título: "Assinatura Superman (2025) - 12 Meses + 20% Desc. + Livro Superman: Kryptonita"
Editora:
  - Panini
Status: Ativa
Envio: Mensal
Parcelas: 12
Valor Original: 233.80
Desconto: 28%
Valor Total: 168.34
Valor Mensal: 14.02
Início: 2025-12-24
Início Pagamento: 2026-01
Fim Pagamento: 2026-12
Status Pagamento: Em Pagamento
Volume Inicial: 3
Volume Final Contratado: 14
Volume Atual Recebido: 12
imagem: Banco de Imagens/HQ's/Superman (2025) Vol. 3.png
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
| **Valor por Volume** | **R$ 14,02** *(com 20% de desc. + cupom extra)* |
| **Valor Original Estimado** | **R$ 233,80** *(~R$ 19,48 / volume)* |
| **Valor Total Pago** | **R$ 168,34** *(Preço base do pacote: R$ 187,04)* |
| **Frequência de Envio** | Mensal (Contrato de 12 Meses) |
| **Data do Pedido** | 24/12/2025 |
| **Início dos Envios** | 25/12/2025 |
| **Volumes Contratados** | Vol. 03 ao 14 (12 volumes no total) |
| **Brinde Incluso** | Livro *Superman: Kryptonita (DC Vintage)* |

---

### 📝 Observações
- Pedido Panini de 24/12/2025.
- Contratados 12 volumes começando na edição 03 até a 14. 
- Volumes 03 ao 12 já entregues/faturados. Volume 13 recentemente processado e Volume 14 pendente para conclusão do plano.
