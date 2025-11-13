# 💡 ESEMPI - Codice in Linguaggio Naturale

## 🎯 Filosofia

**Il codice È la lingua parlata.**

Non sintassi artificiale.
Non regole rigide.
Parli e basta.

---

## 📊 ESEMPIO 1: Analisi Dati Base

### Codice (file: analisi.lingua)

```
Carica il file vendite.csv.
Mostra le prime 5 righe.
Calcola la media della colonna "importo".
Stampa "La media è: {media}".
```

### Cosa Succede

```
1. Sistema legge il file
2. Mostra preview dati
3. Calcola media
4. Stampa risultato
```

### Output

```
   data       prodotto  importo
0  2024-01-15  Laptop   1200
1  2024-01-16  Mouse    25
2  2024-01-17  Tastiera 80
3  2024-01-18  Monitor  350
4  2024-01-19  Webcam   120

La media è: 355.0
```

---

## 🔍 ESEMPIO 2: Filtraggio e Aggregazione

### Codice

```
Carica vendite.csv.

Filtra solo le righe dove importo è maggiore di 100.
Salva il risultato in vendite_grandi.

Raggruppa vendite_grandi per prodotto.
Calcola la somma degli importi per ogni gruppo.

Mostra i risultati ordinati dal più alto al più basso.
```

### Sintassi Alternativa (Equivalente)

```
Apri il file vendite.csv.

Prendi solo le vendite sopra i 100 euro.
Chiamale vendite_grandi.

Raggruppa per prodotto.
Somma gli importi.

Ordina dal più grande al più piccolo e mostra.
```

**Entrambe funzionano! L'AI capisce l'intent.**

---

## 📈 ESEMPIO 3: Visualizzazione

### Codice

```
Carica vendite.csv.

Raggruppa per mese.
Calcola il totale per ogni mese.

Crea un grafico a barre con:
  - asse X: mesi
  - asse Y: totale vendite
  - titolo: "Vendite Mensili 2024"
  - colore: blu

Salva il grafico come "vendite_mensili.png".
Mostra il grafico.
```

### Output

```
Grafico salvato in: vendite_mensili.png
[Mostra finestra con grafico]
```

---

## 🔄 ESEMPIO 4: Loop e Condizioni

### Codice

```
Carica clienti.csv.

Per ogni cliente:
  se il cliente ha speso più di 1000:
    aggiungi alla lista vip.
  altrimenti:
    aggiungi alla lista standard.

Stampa "Clienti VIP: {numero_vip}".
Stampa "Clienti Standard: {numero_standard}".

Salva la lista vip in "clienti_vip.csv".
```

### Sintassi Naturale

```
Carica clienti.csv.

Scorri tutti i clienti.
Quelli che hanno speso oltre 1000 sono VIP.
Gli altri sono standard.

Dimmi quanti sono in ogni categoria.
Salva i VIP in un file separato.
```

**Stessa cosa, parole diverse. Funziona uguale.**

---

## 🌐 ESEMPIO 5: API e Web

### Codice

```
Scarica i dati da "https://api.example.com/vendite".
Salva la risposta in dati_api.

Converti dati_api da JSON a tabella.

Filtra solo i record degli ultimi 30 giorni.

Calcola il totale delle vendite.
Stampa "Vendite ultimi 30 giorni: {totale} euro".
```

---

## 📧 ESEMPIO 6: Automazione

### Codice

```
Carica vendite_oggi.csv.

Se il totale delle vendite è maggiore di 10000:
  crea un messaggio:
    "Ottima giornata! Vendite: {totale} euro"
  invia email a "manager@azienda.com" con il messaggio.
altrimenti:
  stampa "Vendite sotto target".
```

---

## 🔧 ESEMPIO 7: Funzioni Personalizzate

### Codice

```
Definisci una funzione chiamata "analizza_vendite" che:
  prende come input un file CSV.
  calcola la media, il minimo e il massimo.
  ritorna tutti e tre i valori.

Chiama analizza_vendite con "gennaio.csv".
Salva i risultati in stats_gennaio.

Chiama analizza_vendite con "febbraio.csv".
Salva i risultati in stats_febbraio.

Confronta le medie dei due mesi.
Stampa quale mese ha venduto di più.
```

---

## 📊 ESEMPIO 8: Analisi Complessa

### Codice

```
Carica vendite_2024.csv.

Crea una nuova colonna "mese" estraendo il mese dalla data.
Crea una nuova colonna "categoria" basata sul prodotto:
  - se prodotto contiene "laptop" o "pc": categoria = "Computer"
  - se prodotto contiene "mouse" o "tastiera": categoria = "Accessori"
  - altrimenti: categoria = "Altro"

Raggruppa per mese e categoria.
Calcola il totale per ogni gruppo.

Crea una tabella pivot con:
  - righe: mesi
  - colonne: categorie
  - valori: totale vendite

Mostra la tabella.

Crea un grafico a linee per ogni categoria.
Salva come "trend_categorie.png".
```

---

## 🎨 ESEMPIO 9: Dashboard Interattivo

### Codice

```
Carica vendite.csv.

Crea un dashboard con:
  - titolo: "Dashboard Vendite"
  - grafico 1: vendite per mese (linea)
  - grafico 2: top 10 prodotti (barre)
  - grafico 3: distribuzione per categoria (torta)
  - tabella: ultimi 10 ordini

Rendi il dashboard interattivo:
  - filtro per data
  - filtro per categoria
  - aggiornamento automatico ogni 5 minuti

Avvia il dashboard su http://localhost:8080
```

---

## 🔄 ESEMPIO 10: ETL Pipeline

### Codice

```
# Estrazione
Scarica dati da "https://api.vendite.com/data".
Salva in vendite_raw.json.

Carica vendite_raw.json.
Converti in tabella.

# Trasformazione
Rimuovi le righe con valori mancanti.
Converti la colonna "data" in formato data.
Converti la colonna "importo" in numero.

Aggiungi colonna "anno" dalla data.
Aggiungi colonna "trimestre" dalla data.

# Caricamento
Connettiti al database PostgreSQL:
  - host: "localhost"
  - database: "vendite_db"
  - user: "admin"
  - password: "secret"

Inserisci i dati nella tabella "vendite_clean".

Stampa "ETL completato: {numero_righe} righe processate".
```

---

## 🧪 ESEMPIO 11: Machine Learning

### Codice

```
Carica dati_clienti.csv.

Dividi i dati in:
  - 80% training
  - 20% test

Crea un modello di classificazione per predire se un cliente comprerà.
Usa come features: età, reddito, visite_sito.
Usa come target: ha_comprato.

Addestra il modello sui dati di training.

Valuta il modello sui dati di test.
Stampa l'accuratezza.

Se l'accuratezza è maggiore di 0.8:
  salva il modello come "modello_clienti.pkl".
  stampa "Modello salvato con successo".
altrimenti:
  stampa "Modello non abbastanza accurato".
```

---

## 🎯 ESEMPIO 12: Context-Aware

### Codice

```
Carica vendite.csv.

Filtra i valori anomali.
# Il sistema sa cosa sono "anomali" per te dopo averlo usato

Calcola le statistiche.
# Sa quali statistiche ti interessano

Crea il grafico.
# Sa che tipo di grafico preferisci

Invia il report.
# Sa a chi e come inviarlo

# Tutto personalizzato sul TUO modo di lavorare
```

---

## 🔥 ESEMPIO 13: Tolleranza Errori

### Codice (con errori)

```
Carica vendite.csv.
Calola la meda.  # Errori di battitura
Mostra grafiko.  # Ancora errori
```

### Cosa Succede

```
Sistema: Ho corretto automaticamente:
  - "Calola" → "Calcola"
  - "meda" → "media"
  - "grafiko" → "grafico"

Eseguo il codice corretto...
[Mostra risultati]
```

---

## 🌟 ESEMPIO 14: Linguaggio Misto

### Codice

```
Carica vendite.csv.

# Puoi anche usare variabili esplicite
Salva in $dati.

# Puoi fare operazioni matematiche
Calcola $totale = somma di importo in $dati.
Calcola $media = $totale diviso numero di righe.

# Puoi usare condizioni
Se $media > 500:
  stampa "Ottimo!".

# Tutto flessibile
```

---

## 🎭 ESEMPIO 15: Stili Diversi

### Stile Imperativo

```
Carica il file.
Filtra i dati.
Calcola la media.
Mostra il risultato.
```

### Stile Dichiarativo

```
Voglio analizzare vendite.csv.
Mi interessano solo i valori sopra 100.
Mostrami la media.
```

### Stile Conversazionale

```
Apri vendite.csv per favore.
Puoi filtrare solo le vendite grandi?
Quanto è la media?
Fammi vedere un grafico.
```

**Tutti e tre funzionano! Scegli il tuo stile.**

---

## 🚀 ESEMPIO 16: Evoluzione nel Tempo

### Giorno 1

```
Carica il file chiamato vendite.csv che si trova nella cartella dati.
Filtra tutte le righe dove la colonna importo ha un valore maggiore di 1000.
Calcola la media della colonna importo per le righe filtrate.
Stampa il risultato con il testo "La media è: " seguito dal valore.
```

### Giorno 30 (Sistema ha imparato)

```
Carica vendite.csv.
Filtra importo > 1000.
Media.
Stampa.
```

### Giorno 90 (Sistema ti conosce)

```
Analizza vendite.
```

**Il sistema sa già cosa vuoi fare!**

---

## 💎 CARATTERISTICHE CHIAVE

### 1. Sintassi Flessibile

Non c'è "un modo giusto".
Parli come vuoi.
L'AI capisce l'intent.

### 2. Context-Aware

Il sistema ricorda:
- Cosa hai fatto prima
- Quali variabili hai creato
- Cosa ti interessa

### 3. Tollerante

Errori di battitura? No problem.
Grammatica imperfetta? Funziona.
Parole diverse? Capisce.

### 4. Evolutivo

Più lo usi, più diventa tuo.
Impara il tuo stile.
Si adatta alle tue preferenze.

### 5. Naturale

Non devi pensare alla sintassi.
Pensi al problema.
Parli la soluzione.

---

## 🎯 CONFRONTO CON PYTHON

### Python

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vendite.csv')
filtered = df[df['importo'] > 1000]
mean_value = filtered['importo'].mean()
print(f"Media: {mean_value}")

monthly = df.groupby(df['data'].dt.to_period('M'))['importo'].sum()
plt.figure(figsize=(10, 6))
monthly.plot(kind='bar')
plt.title('Vendite Mensili')
plt.xlabel('Mese')
plt.ylabel('Importo')
plt.savefig('vendite.png')
plt.show()
```

### Nostro Linguaggio

```
Carica vendite.csv.
Filtra importo > 1000.
Calcola e stampa la media.

Raggruppa per mese e somma gli importi.
Crea grafico a barre con titolo "Vendite Mensili".
Salva come vendite.png e mostra.
```

**Stessa cosa. 10x più semplice.**

---

## 🌍 MULTILINGUA (Futuro)

### Italiano

```
Carica vendite.csv e calcola la media.
```

### Inglese

```
Load sales.csv and calculate the average.
```

### Spagnolo

```
Carga ventas.csv y calcula el promedio.
```

**Stesso codice, lingue diverse. Funziona uguale.**

---

**"Programmare non è mai stato così naturale."**

Creato: 13 Novembre 2025
