---
Título: "Assinatura A Cor do Fim (Vol. 1 ao 5) - 30% Desc."
Editora:
  - Panini
Status: Ativa
Envio: Bimestral
Parcelas: 5
Valor Original: 239.50
Desconto: 30%
Valor Total: 172.45
Valor Mensal: 34.49
Início: 2026-10-16
Início Pagamento: 2026-11
Fim Pagamento: 2027-03
Status Pagamento: Em Pagamento
Término: 2027-06
Volume Inicial: 1
Volume Final Contratado: 5
Volume Atual Recebido: 0
imagem: Banco de Imagens/Mangas/A Cor Do Fim Vol. 01.webp
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
| **Parcelamento** | 5x de **R$ 34,49** |
| **Valor Total** | **R$ 172,45** *(desconto de 30% sobre R$ 239,50)* |
| **Frequência de Envio** | Bimestral |
| **Início dos Envios** | 16/10/2026 |
| **Volumes Contratados** | Vol. 1 ao 5 (5 volumes no total) |

---

### 📝 Observações
- Assinatura fechada do pacote completo da obra (5 volumes) com 30% de desconto na Panini.
- Primeiro ciclo de pagamento agendado para novembro/2026 (após o corte do cartão no dia 06).
