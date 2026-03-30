// Variabel för att hålla alla produkter
let allaProdukter = [];
let visadeProdukter = [];

// Ladda produkter när sidan laddas
window.addEventListener('load', function() {
    laddaProdukter();
});

// Funktion för att ladda produktdata från JSON
function laddaProdukter() {
    fetch('../testdata/products.json')
        .then(response => response.json())
        .then(data => {
            allaProdukter = data;
            visadeProdukter = data;
            
            // Fyll kategoridropdown
            fyllKategorier();
            
            // Visa produkter
            visaProdukter(visadeProdukter);
            
            // Uppdatera antal
            uppdateraAntal();
        })
        .catch(error => {
            console.log('Fel vid laddning av produkter:', error);
        });
}

// Funktion för att fylla kategori-dropdown
function fyllKategorier() {
    const kategorier = ['Elektronik', 'Kläder', 'Hem & Trädgård', 'Sport', 'Leksaker'];
    const select = document.getElementById('categoryFilter');
    
    kategorier.forEach(kategori => {
        const option = document.createElement('option');
        option.value = kategori;
        option.textContent = kategori;
        select.appendChild(option);
    });
}

// Funktion för att visa produkter i rutnät
function visaProdukter(produkter) {
    const grid = document.getElementById('productGrid');
    grid.innerHTML = '';
    
    // Loopa genom alla produkter
    for (let i = 0; i < produkter.length; i++) {
        const produkt = produkter[i];
        
        // Skapa produktkort
        const card = document.createElement('div');
        card.className = 'product-card';
        
        // Lägg till innehåll
        card.innerHTML = 
            '<span class="category">' + produkt.kategori + '</span>' +
            '<h3>' + produkt.namn + '</h3>' +
            '<div class="price">' + produkt.pris + ' kr</div>' +
            '<p class="description">' + produkt.beskrivning + '</p>';
        
        // Lägg till i grid
        grid.appendChild(card);
    }
}

// Funktion för att uppdatera antal produkter
function uppdateraAntal() {
    const countDiv = document.getElementById('productCount');
    countDiv.textContent = 'Visar ' + visadeProdukter.length + ' av ' + allaProdukter.length + ' produkter';
}