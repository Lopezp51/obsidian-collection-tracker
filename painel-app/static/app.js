let cart = [];
const searchInput = document.getElementById("search-input");
const searchResults = document.getElementById("search-results");
const cartList = document.getElementById("cart-list");
const emptyState = document.getElementById("empty-state");
const addBtn = document.getElementById("add-btn");

// Debounce helper
let timeoutId;

// New elements for Dashboard
const comicGrid = document.getElementById("comic-grid");
const itemCount = document.getElementById("item-count");
const pageTitle = document.getElementById("page-title");
const navItems = document.querySelectorAll(".nav-item");

// Data Store
let collectionData = [];
let currentFilter = "visao-completa";

init();

async function init() {
    setupModal();
    setupNavigation();
    setupSearch();
    await fetchCollection();
}

async function fetchCollection() {
    comicGrid.innerHTML = `<div class="empty-state">Carregando coleção...</div>`;
    try {
        const response = await fetch("/api/collection");
        const data = await response.json();
        if(data.status === "success") {
            collectionData = data.items;
            renderCollection();
        }
    } catch(err) {
        console.error("Erro ao carregar colação:", err);
        comicGrid.innerHTML = `<div class="empty-state">Erro ao carregar a coleção.</div>`;
    }
}

function renderCollection() {
    // Filter logic
    let filtered = collectionData.filter(item => {
        // Exclude specific tracking folders from normal views, except for tracking view
        const isTrackingFolder = item.folder && (item.folder.includes("Faturado") || item.folder.includes("Pré Venda") || item.folder.includes("Pendente"));
        
        switch(currentFilter) {
            case "visao-completa":
                return !isTrackingFolder; 
            case "estante":
                return item.chegou === true && item.situacao === "Finalizado";
            case "fila-leitura":
                return item.chegou === true && (item.status_leitura === "Não Iniciado" || item.status_leitura === "Lendo");
            case "wishlist":
                return item.situacao === "Lista de Desejos" || item.chegou === false;
            case "historico-compra":
                return true; 
            case "historico-leitura":
                return item.status_leitura === "Lido";
            case "rastreio":
                return item.situacao !== "Desejado" && item.chegou !== true && isTrackingFolder;
            default:
                return true;
        }
    });

    // Sorting logic
    if (currentFilter === "historico-compra") {
        filtered.sort((a, b) => new Date(b.processado_em || 0) - new Date(a.processado_em || 0));
    } else {
        // Default alpha sort
        filtered.sort((a, b) => a.title.localeCompare(b.title));
    }

    itemCount.innerText = `${filtered.length} itens`;

    if (filtered.length === 0) {
        comicGrid.innerHTML = `
            <div class="empty-state" style="grid-column: 1/-1;">
                <ion-icon name="folder-open-outline" style="font-size: 3rem; margin-bottom: 10px;"></ion-icon>
                <br>Nenhum quadrinho encontrado para esta visão.
            </div>`;
        return;
    }

    comicGrid.innerHTML = "";
    filtered.forEach(item => {
        const div = document.createElement("div");
        div.className = "comic-card";
        
        const priceStr = item.valor ? `R$ ${item.valor.toFixed(2).replace('.', ',')}` : "";
        let metaHtml = `<span>${item.paginas || '?'} págs</span>`;
        if(item.data_publi) {
            metaHtml += `<span>${item.data_publi}</span>`;
        }

        // Star rating
        let stars = "";
        let r = item.avaliacao || 0;
        for(let i=0; i<5; i++) {
            if(i < r) stars += "★"; else stars += "☆";
        }

        div.innerHTML = `
            <div class="card-cover">
                <img src="${item.imagem_url}" loading="lazy" onerror="this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' fill=\\'none\\' viewBox=\\'0 0 24 24\\' stroke=\\'%236c757d\\'><path stroke-linecap=\\'round\\' stroke-linejoin=\\'round\\' stroke-width=\\'2\\' d=\\'M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z\\'/></svg>'">
                <div class="card-badge" style="color: gold;">${stars}</div>
            </div>
            <div class="card-info">
                <div class="card-title">${item.title}</div>
                <div class="card-price">${priceStr}</div>
                <div class="card-meta">${metaHtml}</div>
            </div>
        `;
        comicGrid.appendChild(div);
    });
}

function setupNavigation() {
    navItems.forEach(item => {
        item.addEventListener("click", (e) => {
            navItems.forEach(n => n.classList.remove("active"));
            item.classList.add("active");
            
            currentFilter = item.getAttribute("data-tab");
            pageTitle.innerText = item.innerText.trim();
            renderCollection();
        });
    });
}

function setupModal() {
    const modal = document.getElementById("add-modal");
    const openBtn = document.getElementById("open-modal-btn");
    const closeBtn = document.getElementById("close-modal-btn");

    openBtn.addEventListener("click", () => modal.classList.add("active"));
    closeBtn.addEventListener("click", () => modal.classList.remove("active"));
    modal.addEventListener("click", (e) => {
        if(e.target === modal) modal.classList.remove("active");
    });
}

/* -------------------------------------------------------------
   Legacy Panini Search Features
--------------------------------------------------------------*/
function setupSearch() {
    searchInput.addEventListener("input", (e) => {
        clearTimeout(timeoutId);
        const query = e.target.value.trim();
        
        if (query.length < 3) {
            searchResults.classList.remove("active");
            return;
        }

        timeoutId = setTimeout(() => {
            performSearch(query);
        }, 500);
    });

    // Close autocomplete when clicking outside
    document.addEventListener("click", (e) => {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.classList.remove("active");
        }
    });
}

async function performSearch(query) {
    searchResults.innerHTML = `<div class="search-item" style="justify-content:center"><div class="loader"></div></div>`;
    searchResults.classList.add("active");

    try {
        const response = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        
        searchResults.innerHTML = "";
        
        if (data.length === 0) {
            searchResults.innerHTML = `<div class="search-item" style="color:var(--text-muted)">Nenhum resultado encontrado.</div>`;
            return;
        }

        data.forEach(item => {
            const div = document.createElement("div");
            div.className = "search-item";
            
            div.innerHTML = `
                <div style="flex-grow:1">
                    <div style="font-weight: 500">${item.title}</div>
                    <div style="color: var(--color-primary); font-size: 0.85em; margin-top:2px;">${item.price}</div>
                </div>
            `;
            
            div.addEventListener("click", () => {
                addToCart(item);
            });
            
            searchResults.appendChild(div);
        });

    } catch (err) {
        console.error(err);
        searchResults.innerHTML = `<div class="search-item">Erro ao buscar resultados.</div>`;
    }
}

function addToCart(item) {
    if (!cart.some(c => c.url === item.url)) {
        cart.push(item);
        renderCart();
    }
    searchResults.classList.remove("active");
}

function removeFromCart(url) {
    cart = cart.filter(c => c.url !== url);
    renderCart();
}

function renderCart() {
    if (cart.length === 0) {
        cartList.innerHTML = `<div class="empty-state" id="empty-state">
                        <ion-icon name="search-outline" style="font-size: 2rem; margin-bottom:10px"></ion-icon>
                        <br>Nenhum item adicionado ainda. Pesquise e clique neles!
                    </div>`;
        addBtn.disabled = true;
        return;
    }

    cartList.innerHTML = "";
    cart.forEach(item => {
        const div = document.createElement("div");
        div.className = "cart-item";
        div.innerHTML = `
            <div class="cart-item-title">${item.title}</div>
            <div class="cart-item-price">${item.price}</div>
            <button class="remove-btn" onclick="removeFromCart('${item.url}')">
                <ion-icon name="trash-outline"></ion-icon>
            </button>
        `;
        cartList.appendChild(div);
    });
    
    addBtn.disabled = false;
}

const progressContainer = document.getElementById("progress-container");
const progressBar = document.getElementById("progress-bar");
const progressText = document.getElementById("progress-text");

addBtn.addEventListener("click", async () => {
    if (cart.length === 0) return;
    
    addBtn.disabled = true;
    const oldText = addBtn.innerHTML;
    addBtn.innerHTML = `<div class="loader"></div> Sincronizando...`;
    
    progressContainer.classList.add("active");
    progressText.classList.add("active");
    progressBar.style.width = "0%";
    
    const selectedFolder = document.getElementById("folder-selector").value;
    
    let successCount = 0;
    const total = cart.length;
    
    for (let i = 0; i < total; i++) {
        const item = cart[i];
        progressText.innerText = `Processando: ${item.title} (${i+1}/${total})`;
        
        try {
            // Adiciona a pasta destino na estrutura de dados enviada ao backend
            const payload = { ...item, folder_flag: selectedFolder };

            const response = await fetch("/api/add_item", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });
            
            const data = await response.json();
            if(data.status === "success") {
                successCount++;
            }
        } catch (err) {
            console.error(err);
        }
        
        let pct = ((i + 1) / total) * 100;
        progressBar.style.width = `${pct}%`;
    }
    
    addBtn.innerHTML = oldText;
    progressContainer.classList.remove("active");
    progressText.classList.remove("active");
    
    alert(`Sucesso! ${successCount} notas enviadas para o seu Obsidian em Gestão de Compras/${selectedFolder}!`);
    cart = [];
    renderCart();

    // Refresh Dashboard Collection!
    await fetchCollection();
});
