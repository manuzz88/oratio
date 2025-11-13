# 🎬 Script Video Demo ORATIO

## Durata: 60-90 secondi

---

## 🎯 Scena 1: Intro (5 secondi)
**Schermata nera con testo:**
```
ORATIO
Il Linguaggio che Capisce Te
```

---

## 🎯 Scena 2: Il Problema (10 secondi)
**Split screen:**

**Sinistra - Python:**
```python
import pandas as pd
df = pd.read_csv('vendite.csv')
filtered = df[df['importo'] > 1000]
mean = filtered['importo'].mean()
print(f"Media: {mean}")
```
**Testo:** "Così programmi oggi"

**Destra - ORATIO:**
```ora
Carica vendite.csv.
Filtra dove importo > 1000.
Calcola la media.
Stampa il risultato.
```
**Testo:** "Così programmi con ORATIO"

---

## 🎯 Scena 3: Demo Live (40 secondi)

### Parte 1: Setup (5 sec)
**Schermata terminale:**
```bash
$ cd examples
$ ls
vendite.csv  analisi.ora
```

### Parte 2: Mostra il codice (10 sec)
**Editor con analisi.ora:**
```ora
# Analisi Vendite Mensili

Carica vendite.csv.

Mostra le prime 5 righe.

Filtra le righe dove importo > 1000.

Calcola la media della colonna importo.

Conta quante righe ci sono.

Crea un grafico a barre delle vendite per prodotto.

Stampa "Analisi completata con successo!"
```

### Parte 3: Esecuzione (15 sec)
**Terminale:**
```bash
$ oratio run analisi.ora
```

**Output animato:**
```
🔍 Parsing: analisi.ora
✅ Parsed: 7 operazioni

⚡ Esecuzione 7 operazioni...

  ▶ io.read_csv...
    ✓ Caricato: 10 righe, 4 colonne
  
  ▶ data.show...
    [Mostra tabella]
  
  ▶ data.filter...
    ✓ Filtrate 6 righe
  
  ▶ math.mean...
    ✓ Media: 458.33
  
  ▶ math.count...
    ✓ Conteggio: 6
  
  ▶ viz.bar...
    ✓ Grafico salvato: vendite_chart.png
  
  ▶ io.print...
    📄 Analisi completata con successo!

✅ Esecuzione completata in 1.2s
```

### Parte 4: Risultato (10 sec)
**Mostra il grafico generato**
- Grafico a barre colorato
- Dati chiari e leggibili

---

## 🎯 Scena 4: Multilingua (15 secondi)

**Split screen 3 colonne:**

**Italiano:**
```ora
Carica dati.csv.
Calcola la media.
```

**English:**
```ora
Load data.csv.
Calculate the average.
```

**Español (Coming):**
```ora
Carga datos.csv.
Calcula el promedio.
```

**Testo:** "Una lingua. Poi tutte le lingue."

---

## 🎯 Scena 5: Call to Action (10 secondi)

**Schermata finale:**
```
ORATIO
Parla. Programma. Rivoluziona.

oratio.dev

pip install oratio
```

---

## 🎬 Come Registrare

### Tool Consigliati:
1. **OBS Studio** (gratis, professionale)
2. **SimpleScreenRecorder** (Linux, semplice)
3. **Kazam** (Linux, veloce)

### Setup:
```bash
# Installa OBS
sudo apt install obs-studio

# Oppure SimpleScreenRecorder
sudo apt install simplescreenrecorder
```

### Impostazioni Registrazione:
- **Risoluzione:** 1920x1080 (Full HD)
- **FPS:** 30
- **Formato:** MP4 (H.264)
- **Audio:** Opzionale (musica di sottofondo)

### Preparazione:
1. Crea file vendite.csv con dati esempio
2. Prepara analisi.ora
3. Testa tutto prima di registrare
4. Usa terminale con font grande (16-18pt)
5. Tema scuro per il terminale

---

## 🎨 Post-Produzione

### Tool:
- **Kdenlive** (gratis, Linux)
- **DaVinci Resolve** (gratis, professionale)

### Aggiungi:
1. Musica di sottofondo (royalty-free)
2. Transizioni smooth
3. Testo overlay per enfasi
4. Logo ORATIO watermark

### Musica Royalty-Free:
- YouTube Audio Library
- Incompetech
- Bensound

---

## 📤 Export Finale

### Formati:
1. **Web (YouTube/Sito):** 1920x1080, MP4, H.264
2. **Social (Twitter/LinkedIn):** 1280x720, MP4
3. **Mobile:** 720x1280 (verticale), MP4

### Carica su:
- YouTube (pubblico)
- Vimeo (backup)
- Website (embed)

---

## ⚡ Quick Start

```bash
# 1. Prepara i file
cd /home/manuel/CascadeProjects/oratio
mkdir -p video_demo
cd video_demo

# 2. Crea vendite.csv
cat > vendite.csv << 'EOF'
data,prodotto,importo,quantita
2024-01-15,Laptop,1200,1
2024-01-16,Mouse,25,3
2024-01-17,Tastiera,80,2
2024-01-18,Monitor,350,1
2024-01-19,Webcam,120,2
2024-01-20,Cuffie,85,1
2024-01-21,SSD,150,2
2024-01-22,RAM,90,4
2024-01-23,Scheda Video,450,1
2024-01-24,Alimentatore,75,2
EOF

# 3. Crea analisi.ora
cat > analisi.ora << 'EOF'
# Analisi Vendite Mensili

Carica vendite.csv.

Mostra le prime 5 righe.

Filtra le righe dove importo > 100.

Calcola la media della colonna importo.

Conta quante righe ci sono.

Crea un grafico a barre.

Stampa "Analisi completata con successo!"
EOF

# 4. Testa
cd ..
./oratio-cli run video_demo/analisi.ora

# 5. Se funziona, registra!
```

---

## 🎯 Vuoi che ti Aiuti?

**A)** Preparo i file per la demo?
**B)** Creo uno script automatico per registrare?
**C)** Generiamo un video animato invece di registrazione?
**D)** Altro?
