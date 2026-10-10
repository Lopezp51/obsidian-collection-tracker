---
Título: "Assinatura Batman/Superman: Os Melhores Do Mundo - 12 Meses + 30% Desc."
Editora:
  - Panini
Status: Ativa
Envio: Mensal
Parcelas: 12
Valor Original: 178.80
Desconto: 37%
Valor Total: 112.65
Valor Mensal: 9.39
Início: 2026-10-09
Início Pagamento: 2026-11
Fim Pagamento: 2027-10
Status Pagamento: Em Pagamento
Volume Inicial: 11
Volume Final Contratado: 22
Volume Atual Recebido: 0
imagem: Banco de Imagens/HQ's/Batman∕Superman - Os Melhores Do Mundo (2025) 11.webp
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
| **Parcelamento** | 12x de **R$ 9,39** |
| **Valor Total** | **R$ 112,65** *(37% de desconto sobre R$ 178,80)* |
| **Frequência de Envio** | Mensal |
| **Início dos Envios** | 09/10/2026 |
| **Volumes Contratados** | Vol. 11 ao 22 (12 volumes no total) |

---

### 📝 Observações
- Assinatura de 12 meses contratada em 09/10/2026 via site Panini com 30% de desconto de assinatura + cupom de checkout.
- Periodicidade mensal compreendendo as edições 11 até a 22.
- Nenhuma edição enviada até o momento. Aguardando processamento e envio do Vol. 11.
