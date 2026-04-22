module.exports = async (params) => {
    const {quickAddApi} = params;
    
    const titulo = await quickAddApi.inputPrompt("Título do Manga:");
    
    const valorEntrada = await quickAddApi.inputPrompt("Valor (ex: 57,90):", "0,00");
    const valorTratado = valorEntrada.replace(",", ".");

    const situacao = await quickAddApi.suggester(
        ["Desejado", "Faturado", "Pendente", "Pré Venda", "Finalizado"],
        ["Desejado", "Faturado", "Pendente", "Pré Venda", "Finalizado"]
    );
    
    let folderPath = `Acervo/${situacao}`;
    let dataFormatada = new Date().toISOString().split('T')[0];
    let chegouStatus = "false"; // Padrão para os outros
    let imagemSelecionada = "";

    // Lógica específica para FINALIZADO
    if (situacao === "Finalizado") {
        chegouStatus = "true"; // Define como true automaticamente
        
        const agora = new Date();
        const ano = agora.getFullYear().toString();
        const mes = (agora.getMonth() + 1).toString().padStart(2, '0');
        const dia = agora.getDate().toString().padStart(2, '0');
        
        folderPath += `/${ano}/${mes}`;
        dataFormatada = `${ano}-${mes}-${dia}`;

        // Imagem fica vazia ou pode ser preenchida manualmente depois
        imagemSelecionada = "";
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