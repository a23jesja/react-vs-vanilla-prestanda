import { useState, useEffect } from 'react'
import './App.css'

function App() {
  // State för produkter
  const [allaProdukter, setAllaProdukter] = useState([]);
  const [visadeProdukter, setVisadeProdukter] = useState([]);
  const [soktext, setSoktext] = useState('');

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

  // Sökfunktion - körs när söktext ändras
  useEffect(() => {
    if (soktext === '') {
      setVisadeProdukter(allaProdukter);
    } else {
      const filtrerade = allaProdukter.filter(produkt => 
        produkt.namn.toLowerCase().includes(soktext.toLowerCase()) ||
        produkt.beskrivning.toLowerCase().includes(soktext.toLowerCase())
      );
      setVisadeProdukter(filtrerade);
    }
  }, [soktext, allaProdukter]);

  // Hantera sökning
  const handleSearch = (e) => {
    setSoktext(e.target.value);
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
        <select>
          <option value="">Alla kategorier</option>
          <option value="Elektronik">Elektronik</option>
          <option value="Kläder">Kläder</option>
          <option value="Hem & Trädgård">Hem & Trädgård</option>
          <option value="Sport">Sport</option>
          <option value="Leksaker">Leksaker</option>
        </select>
        <select>
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