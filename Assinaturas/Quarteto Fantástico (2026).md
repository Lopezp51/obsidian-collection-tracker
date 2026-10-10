---
Título: "Assinatura Quarteto Fantástico - 12 Meses + 20% Desc."
Editora:
  - Panini
Status: Ativa
Envio: Bimestral
Parcelas: 12
Valor Original: 119.40
Desconto: 28%
Valor Total: 85.97
Valor Mensal: 7.16
Início: 2026-10-09
Início Pagamento: 2026-11
Fim Pagamento: 2027-10
Status Pagamento: Em Pagamento
Volume Inicial: 3
Volume Final Contratado: 8
Volume Atual Recebido: 0
imagem: Banco de Imagens/HQ's/Quarteto Fantástico (2026) 03.webp
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
| **Parcelamento** | 12x de **R$ 7,16** |
| **Valor Total** | **R$ 85,97** *(28% de desconto sobre R$ 119,40)* |
| **Frequência de Envio** | Bimestral |
| **Início dos Envios** | 09/10/2026 |
| **Volumes Contratados** | Vol. 03 ao 08 (6 volumes no total) |

---

### 📝 Observações
- Assinatura de 12 meses contratada em 09/10/2026 via site Panini com 20% de desconto de assinatura + cupom de checkout.
- Periodicidade bimestral compreendendo 6 edições (Vol. 03 até o 08).
- Nenhuma edição enviada até o momento. Aguardando processamento e envio do Vol. 03.
