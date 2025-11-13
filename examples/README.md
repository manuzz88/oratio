# 📚 Esempi Lingua

Questa cartella contiene esempi di programmi scritti in Lingua.

## 🚀 Come Eseguire

```bash
# Dalla root del progetto
./lingua-cli run examples/nome.lingua

# Con output verbose
./lingua-cli run examples/nome.lingua -v

# Mostra IR generato
./lingua-cli run examples/nome.lingua --show-ir
```

## 📝 Esempi Disponibili

### 1. primo.lingua
**Livello:** Principiante  
**Operazioni:** Carica CSV, mostra dati, calcola media

```
Carica il file vendite.csv.
Mostra le prime 5 righe.
Calcola la media della colonna importo.
Stampa il risultato.
```

### 2. filtro.lingua
**Livello:** Principiante  
**Operazioni:** Carica, filtra, conta

```
Carica il file vendite.csv.
Filtra le righe dove importo è maggiore di 100.
Conta quante righe ci sono.
Stampa "Prodotti costosi: {conteggio}".
```

### 3. statistiche.lingua
**Livello:** Intermedio  
**Operazioni:** Somma, media, conteggio

```
Carica vendite.csv.
Calcola la somma della colonna importo.
Calcola la media della colonna importo.
Conta le righe.
Stampa statistiche.
```

### 4. grafico.lingua
**Livello:** Intermedio  
**Operazioni:** Visualizzazione dati

```
Carica vendite.csv.
Crea un grafico a barre della colonna importo.
Salva il grafico come "vendite_grafico.png".
```

### 5. completo.lingua
**Livello:** Avanzato  
**Operazioni:** Pipeline completa di analisi

```
Carica, filtra, calcola statistiche, ordina, salva.
Esempio completo di workflow di analisi dati.
```

## 📊 Dati di Test

### vendite.csv
File CSV con dati di vendita:
- data: Data della vendita
- prodotto: Nome prodotto
- importo: Prezzo in euro
- quantita: Quantità venduta

10 righe di esempio con vari prodotti e prezzi.

## 🎯 Operazioni Supportate

### I/O
- `Carica file.csv` → io.read_csv
- `Salva in file.csv` → io.write_csv
- `Stampa "testo"` → io.print

### Data Manipulation
- `Mostra le prime N righe` → data.show
- `Filtra dove colonna > valore` → data.filter
- `Ordina per colonna` → data.sort
- `Raggruppa per colonna` → data.group

### Math
- `Calcola la media` → math.mean
- `Calcola la somma` → math.sum
- `Conta le righe` → math.count

### Visualizzazione
- `Crea grafico` → viz.plot
- `Crea grafico a barre` → viz.bar

## 💡 Tips

1. **Path relativi**: I file sono cercati relativamente alla cartella dell'esempio
2. **Variabili implicite**: Non serve dichiarare variabili, il sistema le gestisce
3. **Sintassi flessibile**: Puoi scrivere in modi diversi, l'AI capisce l'intent
4. **Errori tollerati**: Piccoli errori di battitura vengono corretti automaticamente

## 🚀 Prossimi Esempi

- [ ] Loop e condizioni
- [ ] Funzioni personalizzate
- [ ] API integration
- [ ] Machine learning base
- [ ] Dashboard interattivo

---

**Crea i tuoi esempi e condividili!** 🌟
