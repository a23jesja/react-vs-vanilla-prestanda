const fs = require('fs');

// Produktkategorier
const kategorier = ['Elektronik', 'Kläder', 'Hem & Trädgård', 'Sport', 'Leksaker'];

// Märken
const märken = ['Samsung', 'Apple', 'Nike', 'Adidas', 'Sony', 'LG', 'IKEA', 'H&M'];

// Funktion för att skapa produkter
function skapaProduktLista(antal) {
    const produkter = [];
    
    console.log('Skapar ' + antal + ' produkter...');
    
    for (let i = 1; i <= antal; i++) {
        // Slumpa kategori
        const kategori = kategorier[Math.floor(Math.random() * kategorier.length)];
        
        // Slumpa märke
        const märke = märken[Math.floor(Math.random() * märken.length)];
        
        // Slumpa pris mellan 100-9999 kr
        const pris = Math.floor(Math.random() * 9000) + 100;
        
        // Slumpa om produkten finns i lager (80% chans)
        const iLager = Math.random() > 0.2;

        // Skapa produkt
        const produkt = {
            id: i,
            namn: märke + ' Produkt ' + i,
            kategori: kategori,
            pris: pris,
            beskrivning: 'Beskrivning för produkt ' + i + ' i kategorin ' + kategori,
            iLager: iLager
        };
        
        produkter.push(produkt);
        
        // Visa progress var 100:e produkt
        if (i % 100 === 0) {
            console.log('  ' + i + ' produkter färdiga...');
        }
    }
    
    console.log('Alla produkter genererade!');
    return produkter;
}

// Generera produkterna
const allaProduktData = skapaProduktLista(1000);

// Spara till JSON-fil
const filnamn = 'products-1000.json';
console.log('Sparar produktdata till fil: ' + filnamn);
fs.writeFileSync(filnamn, JSON.stringify(allaProduktData, null, 2));

console.log('\n=== STATISTIK ===');
console.log('Totalt antal produkter: ' + allaProduktData.length);
console.log('Filstorlek: ' + (JSON.stringify(allaProduktData).length / 1024).toFixed(2) + ' KB');

// Räkna fördelning per kategori
console.log('\n=== FÖRDELNING PER KATEGORI ===');
const antalPerKategori = {};

for (let i = 0; i < allaProduktData.length; i++) {
    const kat = allaProduktData[i].kategori;
    
    if (antalPerKategori[kat]) {
        antalPerKategori[kat] = antalPerKategori[kat] + 1;
    } else {
        antalPerKategori[kat] = 1;
    }
}

// Skriv ut fördelningen
for (const kategori in antalPerKategori) {
    const antal = antalPerKategori[kategori];
    const procent = ((antal / allaProduktData.length) * 100).toFixed(1);
    console.log('  ' + kategori + ': ' + antal + ' st (' + procent + '%)');
}

console.log('\nKLART! Filen products-1000.json är skapad.');
