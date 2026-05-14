// Generera 2000 produkter för testet
const fs = require('fs');

const kategorier = ['Elektronik', 'Kläder', 'Hem & Trädgård', 'Sport', 'Leksaker'];
const märken = ['Samsung', 'Apple', 'Nike', 'Adidas', 'Sony', 'LG', 'IKEA', 'H&M'];

function skapaProduktLista(antal) {
    const produkter = [];
    
    for (let i = 1; i <= antal; i++) {
        const kategori = kategorier[Math.floor(Math.random() * kategorier.length)];
        const märke = märken[Math.floor(Math.random() * märken.length)];
        const pris = Math.floor(Math.random() * 9000) + 100;
        const iLager = Math.random() > 0.2;
        
        const produkt = {
            id: i,
            namn: märke + ' Produkt ' + i,
            kategori: kategori,
            pris: pris,
            beskrivning: 'Beskrivning för produkt ' + i + ' i kategorin ' + kategori,
            iLager: iLager
        };
        
        produkter.push(produkt);
        
        if (i % 200 === 0) {
            console.log(i + ' produkter färdiga...');
        }
    }
    
    return produkter;
}

const produktData = skapaProduktLista(2000);

fs.writeFileSync('products-2000-svenska.json', JSON.stringify(produktData, null, 2));

console.log('Totalt: ' + produktData.length + ' produkter');
console.log('Filstorlek: ' + (JSON.stringify(produktData).length / 1024).toFixed(2) + ' KB');
console.log('Klar!');
