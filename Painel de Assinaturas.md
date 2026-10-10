# 📬 Painel de Assinaturas

```dataviewjs
function verificarPagamento(p) {
    const statusPag = String(p["Status Pagamento"] || "").toLowerCase();
    const totalParcelas = parseInt(p["Parcelas"] || 0, 10);
    
    // 1. Se explicitamente marcado como Quitado
    if (statusPag === "quitado" || statusPag === "pago") {
        return { quitado: true, label: "Quitado", parcelaAtual: totalParcelas, totalParcelas };
    }
    
    // 2. Se a assinatura em si já foi concluída
    if (p.Status === "Concluída") {
        return { quitado: true, label: "Quitado", parcelaAtual: totalParcelas, totalParcelas };
    }

    const hoje = new Date();
    const anoMesAtual = hoje.getFullYear() * 12 + (hoje.getMonth() + 1);

    // 3. Verificar por data de término do pagamento se existir
    const fimPag = p["Fim Pagamento"];
    if (fimPag) {
        const m = String(fimPag).match(/^(\d{4})-(\d{2})/);
        if (m) {
            const anoMesFim = parseInt(m[1], 10) * 12 + parseInt(m[2], 10);
            if (anoMesAtual > anoMesFim) {
                return { quitado: true, label: "Quitado", parcelaAtual: totalParcelas, totalParcelas };
            }
        }
    }

    // 4. Se tiver Início Pagamento e Parcelas
    const iniPag = p["Início Pagamento"] || p["Início"];
    if (iniPag && totalParcelas > 0) {
        const m = String(iniPag).match(/^(\d{4})-(\d{2})/);
        if (m) {
            const anoMesIni = parseInt(m[1], 10) * 12 + parseInt(m[2], 10);
            const decorridos = anoMesAtual - anoMesIni + 1;
            if (decorridos > totalParcelas) {
                return { quitado: true, label: "Quitado", parcelaAtual: totalParcelas, totalParcelas };
            } else if (decorridos >= 1) {
                return { quitado: false, label: `${decorridos}/${totalParcelas}x`, parcelaAtual: decorridos, totalParcelas };
            }
        }
    }

    return { quitado: false, label: totalParcelas ? `${totalParcelas}x` : "Em Pagamento", parcelaAtual: 1, totalParcelas };
}

const pages = dv.pages('"Assinaturas"').where(p => p.Status === "Ativa");
let totalMensal = 0;
let qtdEmPagamento = 0;
let qtdQuitadasRecebendo = 0;

for (let p of pages) {
    const pag = verificarPagamento(p);
    if (!pag.quitado) {
        totalMensal += Number(p["Valor Mensal"] || 0);
        qtdEmPagamento++;
    } else {
        qtdQuitadasRecebendo++;
    }
}
const qtdAtivas = pages.length;

const kpiHtml = `
<div style="display: flex; gap: 16px; margin-bottom: 20px; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 200px; padding: 14px 18px; background-color: var(--background-secondary); border-radius: 8px; border-left: 4px solid #10b981;">
        <div style="font-size: 0.85em; color: var(--text-muted); text-transform: uppercase; font-weight: 600;">Gasto Mensal Atual (Fatura)</div>
        <div style="font-size: 1.6em; font-weight: bold; color: var(--text-normal); margin-top: 4px;">R$ ${totalMensal.toFixed(2).replace('.', ',')} / mês</div>
        <div style="font-size: 0.8em; color: var(--text-muted); margin-top: 2px;">${qtdEmPagamento} assinatura(s) com parcelas ativas</div>
    </div>
    <div style="flex: 1; min-width: 200px; padding: 14px 18px; background-color: var(--background-secondary); border-radius: 8px; border-left: 4px solid #6366f1;">
        <div style="font-size: 0.85em; color: var(--text-muted); text-transform: uppercase; font-weight: 600;">Assinaturas Vigentes (Em Entrega)</div>
        <div style="font-size: 1.6em; font-weight: bold; color: var(--text-normal); margin-top: 4px;">${qtdAtivas} ativa(s)</div>
        <div style="font-size: 0.8em; color: var(--text-muted); margin-top: 2px;">${qtdQuitadasRecebendo > 0 ? `${qtdQuitadasRecebendo} já quitada(s) (recebendo volumes)` : 'Todas em fase de pagamento'}</div>
    </div>
</div>
`;
dv.span(kpiHtml);
```

### 📋 Assinaturas Vigentes

```dataviewjs
function formatarData(val) {
    if (!val) return "";
    if (typeof val === "object" && val.toFormat) return val.toFormat("dd/MM/yyyy");
    const s = String(val);
    const isoMatch = s.match(/^(\d{4})-(\d{2})-(\d{2})/);
    if (isoMatch) return `${isoMatch[3]}/${isoMatch[2]}/${isoMatch[1]}`;
    const num = Number(val);
    if (!isNaN(num) && num > 1000000000) {
        const d = new Date(num);
        return `${String(d.getDate()).padStart(2, '0')}/${String(d.getMonth() + 1).padStart(2, '0')}/${d.getFullYear()}`;
    }
    return s;
}

function verificarPagamento(p) {
    const statusPag = String(p["Status Pagamento"] || "").toLowerCase();
    const totalParcelas = parseInt(p["Parcelas"] || 0, 10);
    
    if (statusPag === "quitado" || statusPag === "pago") {
        return { quitado: true, label: "Quitado" };
    }
    if (p.Status === "Concluída") {
        return { quitado: true, label: "Quitado" };
    }

    const hoje = new Date();
    const anoMesAtual = hoje.getFullYear() * 12 + (hoje.getMonth() + 1);

    const fimPag = p["Fim Pagamento"];
    if (fimPag) {
        const m = String(fimPag).match(/^(\d{4})-(\d{2})/);
        if (m) {
            const anoMesFim = parseInt(m[1], 10) * 12 + parseInt(m[2], 10);
            if (anoMesAtual > anoMesFim) {
                return { quitado: true, label: "Quitado" };
            }
        }
    }

    const iniPag = p["Início Pagamento"] || p["Início"];
    if (iniPag && totalParcelas > 0) {
        const m = String(iniPag).match(/^(\d{4})-(\d{2})/);
        if (m) {
            const anoMesIni = parseInt(m[1], 10) * 12 + parseInt(m[2], 10);
            const decorridos = anoMesAtual - anoMesIni + 1;
            if (decorridos > totalParcelas) {
                return { quitado: true, label: "Quitado" };
            } else if (decorridos >= 1) {
                return { quitado: false, label: `${decorridos}/${totalParcelas}x` };
            }
        }
    }

    return { quitado: false, label: totalParcelas ? `${totalParcelas}x` : "Em Pagamento" };
}

dv.table(
    ["Assinatura", "Status", "Editora", "Gasto Mensal", "Pagamento", "Volumes (Recebido / Total)", "Envio", "Início"],
    dv.pages('"Assinaturas"')
        .where(p => p.Status === "Ativa")
        .sort(p => p.file.name, 'asc')
        .map(p => {
            const ini = p["Volume Inicial"] || 1;
            const fim = p["Volume Final Contratado"] || "-";
            const atual = p["Volume Atual Recebido"] ?? 0;
            const faixa = ini > 1 ? ` (Vol. ${ini} ao ${fim})` : "";
            const pag = verificarPagamento(p);
            const gastoMensalTexto = pag.quitado 
                ? "<span style='color: var(--text-muted);'>R$ 0,00</span>" 
                : (p["Valor Mensal"] ? "<b>R$ " + Number(p["Valor Mensal"]).toFixed(2).replace(".", ",") + "</b>" : "-");
            const statusPagTexto = pag.quitado 
                ? "<span style='color: #10b981; font-weight: 600;'>✅ Quitado</span>" 
                : `<span style='color: #6366f1;'>💳 ${pag.label}</span>`;

            return [
                p.file.link,
                p.Status,
                Array.isArray(p.Editora) ? p.Editora.join(", ") : (p.Editora || "-"),
                gastoMensalTexto,
                statusPagTexto,
                `${atual} / ${fim}${faixa}`,
                p.Envio || "-",
                formatarData(p["Início"]) || "-"
            ];
        })
);
```

### 📦 Todas as Assinaturas (Histórico)

```dataviewjs
function formatarData(val) {
    if (!val) return "";
    if (typeof val === "object" && val.toFormat) return val.toFormat("dd/MM/yyyy");
    const s = String(val);
    const isoMatch = s.match(/^(\d{4})-(\d{2})-(\d{2})/);
    if (isoMatch) return `${isoMatch[3]}/${isoMatch[2]}/${isoMatch[1]}`;
    const num = Number(val);
    if (!isNaN(num) && num > 1000000000) {
        const d = new Date(num);
        return `${String(d.getDate()).padStart(2, '0')}/${String(d.getMonth() + 1).padStart(2, '0')}/${d.getFullYear()}`;
    }
    return s;
}

dv.table(
    ["Assinatura", "Status", "Total Contratado", "Parcelas / Mês", "Volumes Contratados", "Período"],
    dv.pages('"Assinaturas"')
        .sort(p => p.Status, 'asc')
        .map(p => {
            const ini = p["Volume Inicial"] || 1;
            const fim = p["Volume Final Contratado"] || "-";
            const faixa = ini > 1 ? `Vol. ${ini} ao ${fim}` : `1 ao ${fim}`;
            const dtIni = formatarData(p["Início"]);
            const dtFim = formatarData(p["Término"]);
            let periodo = "-";
            if (dtIni && dtFim) {
                periodo = `${dtIni} até ${dtFim}`;
            } else if (dtIni) {
                periodo = dtIni;
            }
            return [
                p.file.link,
                p.Status,
                p["Valor Total"] ? "R$ " + Number(p["Valor Total"]).toFixed(2).replace(".", ",") : "-",
                p.Parcelas ? `${p.Parcelas}x (R$ ${Number(p["Valor Mensal"] || 0).toFixed(2).replace('.', ',')})` : "-",
                faixa,
                periodo
            ];
        })
);
```
