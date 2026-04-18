module.exports = async (params) => {
    const {quickAddApi} = params;
    
    const titulo = await quickAddApi.inputPrompt("Título do Quadrinho:");
    
    const valorEntrada = await quickAddApi.inputPrompt("Valor (ex: 57,90):", "0,00");
    const valorTratado = valorEntrada.replace(",", ".");

    const situacao = await quickAddApi.suggester(
        ["Desejado", "Faturado", "Pendente", "Pré Venda", "Finalizado"],
        ["Desejado", "Faturado", "Pendente", "Pré Venda", "Finalizado"]
    );
    
    let folderPath = `Gestão de Compras/${situacao}`;
    let dataFormatada = new Date().toISOString().split('T')[0];
    let chegouStatus = "false"; // Padrão para os outros
    let imagemSelecionada = "";

    // Lógica específica para FINALIZADO
    if (situacao === "Finalizado") {
        chegouStatus = "true"; // Define como true automaticamente
        
        // 1. Pergunta a Data
        const ano = await quickAddApi.inputPrompt("ANO:", new Date().getFullYear().toString());
        const meses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"];
        const mes = await quickAddApi.suggester(meses, meses);
        const dia = await quickAddApi.inputPrompt("DIA:", "01");
        
        folderPath += `/${ano}/${mes}`;
        dataFormatada = `${ano}-${mes}-${dia.padStart(2, '0')}`;

        // 2. Seletor de Imagem (Busca na sua pasta de capas)
        const pastaImagens = "Banco de Imagens/HQ's"; // Caminho da sua pasta
        const pastaAbstract = app.vault.getAbstractFileByPath(pastaImagens);
        
        if (pastaAbstract && pastaAbstract.children) {
            // Filtra apenas arquivos de imagem comuns
            const imagens = pastaAbstract.children
                .filter(f => ["jpg", "jpeg", "png", "webp"].includes(f.extension))
                .map(f => f.path);
            
            if (imagens.length > 0) {
                // Abre o seletor com os nomes dos arquivos, mas retorna o caminho completo
                imagemSelecionada = await quickAddApi.suggester(
                    imagens.map(p => p.split('/').pop()), 
                    imagens
                );
            }
        }
    }

    // Exporta tudo para o QuickAdd
    params.variables["titulo"] = titulo;
    params.variables["valorFinal"] = valorTratado;
    params.variables["dynamicPath"] = folderPath;
    params.variables["situacao"] = situacao;
    params.variables["dataFinal"] = dataFormatada;
    params.variables["chegouFinal"] = chegouStatus;
    params.variables["imagemFinal"] = imagemSelecionada || ""; // Se não escolher, fica vazio
};