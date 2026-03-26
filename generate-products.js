// Script för att generera 500 produkter
// Enkel kod för att skapa testdata

const fs = require('fs');

const kategorier = ['Elektronik', 'Kläder', 'Hem & Trädgård', 'Sport', 'Leksaker'];

const produktNamn = {
  'Elektronik': ['Laptop', 'Telefon', 'Hörlurar', 'Tangentbord', 'Mus', 'Skärm', 'Kamera', 'Högtalare'],
  'Kläder': ['T-shirt', 'Jeans', 'Jacka', 'Skor', 'Mössa', 'Byxor', 'Klänning', 'Tröja'],
  'Hem & Trädgård': ['Lampa', 'Stol', 'Bord', 'Kruka', 'Verktyg', 'Kudde', 'Filt', 'Vas'],
  'Sport': ['Fotboll', 'Löparskor', 'Yogamatta', 'Hantel', 'Cykel', 'Tennisracket', 'Simglasögon', 'Skidor'],
  'Leksaker': ['Docka', 'Bil', 'Pussel', 'Klossar', 'Spel', 'Teddybjörn', 'Drakar', 'Färgpennor']
};

const produkter = [];

// Skapa 500 produkter
for (let i = 1; i <= 500; i++) {
  // Välj slumpmässig kategori
  const kategori = kategorier[Math.floor(Math.random() * kategorier.length)];
  
  // Välj slumpmässigt produktnamn från kategorin
  const namnLista = produktNamn[kategori];
  const namn = namnLista[Math.floor(Math.random() * namnLista.length)];
  
  // Slumpa pris mellan 99-9999 kr
  const pris = Math.floor(Math.random() * 9900) + 99;
  
  // Skapa produkt-objekt
  produkter.push({
    id: i,
    namn: namn + ' ' + i,
    pris: pris,
    kategori: kategori,
    beskrivning: 'Bra produkt i kategorin ' + kategori + '. Produktnummer ' + i + '.'
  });
}

// Spara till fil
fs.writeFileSync('testdata/products.json', JSON.stringify(produkter, null, 2));

console.log('Skapade 500 produkter!');
console.log('Fil: testdata/products.json');