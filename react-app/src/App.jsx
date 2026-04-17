import { useState, useEffect } from 'react'
import './App.css'

function App() {
  // State för produkter
  const [allaProdukter, setAllaProdukter] = useState([]);
  const [visadeProdukter, setVisadeProdukter] = useState([]);
  const [soktext, setSoktext] = useState('');
  const [valdKategori, setValdKategori] = useState('');
  const [sortering, setSortering] = useState('');

  // Ladda produkter när komponenten mountas
  useEffect(() => {
    fetch('/data/products.json')
      .then(response => response.json())
      .then(data => {
        setAllaProdukter(data);
        setVisadeProdukter(data);
      })
      .catch(error => {
        console.log('Fel vid laddning:', error);
      });
  }, []);

  // Filtrering och sortering
  useEffect(() => {
    let filtrerade = allaProdukter;

    // Filtrera på kategori
    if (valdKategori !== '') {
      filtrerade = filtrerade.filter(produkt => 
        produkt.kategori === valdKategori
      );
    }

    // Filtrera på söktext
    if (soktext !== '') {
      filtrerade = filtrerade.filter(produkt => 
        produkt.namn.toLowerCase().includes(soktext.toLowerCase()) ||
        produkt.beskrivning.toLowerCase().includes(soktext.toLowerCase())
      );
    }

    // Sortera produkter
    if (sortering === 'price-asc') {
      filtrerade = [...filtrerade].sort((a, b) => a.pris - b.pris);
    } else if (sortering === 'price-desc') {
      filtrerade = [...filtrerade].sort((a, b) => b.pris - a.pris);
    } else if (sortering === 'name') {
      filtrerade = [...filtrerade].sort((a, b) => {
        if (a.namn < b.namn) return -1;
        if (a.namn > b.namn) return 1;
        return 0;
      });
    }

    setVisadeProdukter(filtrerade);
  }, [soktext, valdKategori, sortering, allaProdukter]);

  // Hantera sökning
  const handleSearch = (e) => {
    setSoktext(e.target.value);
  };

  // Hantera kategorifiltrering
  const handleCategoryChange = (e) => {
    setValdKategori(e.target.value);
  };

  // Hantera sortering
  const handleSortChange = (e) => {
    setSortering(e.target.value);
  };

  return (
    <div className="container">
      <h1>Produktkatalog</h1>
      
      <div className="controls">
        <input 
          type="text" 
          placeholder="Sök produkter..." 
          value={soktext}
          onChange={handleSearch}
        />
        <select value={valdKategori} onChange={handleCategoryChange}>
          <option value="">Alla kategorier</option>
          <option value="Elektronik">Elektronik</option>
          <option value="Kläder">Kläder</option>
          <option value="Hem & Trädgård">Hem & Trädgård</option>
          <option value="Sport">Sport</option>
          <option value="Leksaker">Leksaker</option>
        </select>
        <select value={sortering} onChange={handleSortChange}>
          <option value="">Sortera efter...</option>
          <option value="price-asc">Pris: Lägst först</option>
          <option value="price-desc">Pris: Högst först</option>
          <option value="name">Namn: A-Ö</option>
        </select>
      </div>

      <div id="productCount">
        Visar {visadeProdukter.length} av {allaProdukter.length} produkter
      </div>

      <div id="productGrid">
        {visadeProdukter.map(produkt => (
          <div key={produkt.id} className="product-card">
            <span className="category">{produkt.kategori}</span>
            <h3>{produkt.namn}</h3>
            <div className="price">{produkt.pris} kr</div>
            <p className="description">{produkt.beskrivning}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default App