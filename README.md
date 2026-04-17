# Prestandajämförelse: React vs Vanilla JavaScript

Examensarbete - Högskolan i Skövde  
Student: Jesper Jansson (a23jesja)  
Handledare: Johan Bjurén  
Examinator: Henrik Gustavsson

## Om projektet

Detta projekt jämför prestanda mellan React och Vanilla JavaScript för en produktkatalog med 500 produkter. Jämförelsen fokuserar på Core Web Vitals (LCP, INP, CLS) och andra prestandamått.

## Struktur

react-vs-vanilla-prestanda/
├── vanilla-js/          # Vanilla JavaScript-version
│   ├── index.html
│   ├── style.css
│   └── app.js
├── react-app/           # React-version (Vite)
│   ├── src/
│   └── public/
├── testdata/            # Produktdata (500 produkter)
│   └── products.json
└── generate-products.js # Script för att generera testdata

## Funktioner

Båda versionerna har identisk funktionalitet:

- Visa 500 produkter i rutnät
- Sökfunktion (namn och beskrivning)
- Kategorifiltrering (5 kategorier)
- Sortering (pris och namn)
- Responsiv design

## Hur man kör projektet

### Vanilla JavaScript-version

1. Öppna `vanilla-js/index.html` i webbläsaren
2. Inga dependencies krävs!

### React-version

1. Gå till React-mappen:
```bash
cd react-app
```

2. Installera dependencies (första gången):
```bash
npm install
```

3. Starta utvecklingsserver:
```bash
npm run dev
```

4. Öppna http://localhost:5173/ i webbläsaren

## Generera ny testdata

Om man vill generera ny produktdata:

```bash
node generate-products.js
```

Detta skapar en ny `testdata/products.json` med 500 slumpmässiga produkter.

## Testning

Prestanda kommer att testas med:
- Google Lighthouse (Core Web Vitals)
- Chrome DevTools Performance
- Upprepad mätning (20 gånger per version)
- Statistisk analys (ANOVA)

## Status

 **Under utveckling**

- [x] Vanilla JavaScript-version (klar)
- [x] React-version (klar)
- [ ] Lighthouse-testning
- [ ] Prestandaanalys
- [ ] Slutrapport

## Teknisk stack

**Vanilla JavaScript:**
- HTML5
- CSS3
- Vanilla JavaScript (ES6)

**React:**
- React 18
- Vite
- JavaScript (ES6+)

## Commits & Progression

Detta projekt dokumenterar utvecklingsprocessen genom regelbundna commits som visar progression och arbetsmetodik.