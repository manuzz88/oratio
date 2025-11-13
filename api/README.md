# 🌐 ORATIO Playground API

Backend API per eseguire codice ORATIO dal browser.

## 🚀 Quick Start

### Installazione

```bash
cd api
pip install -r requirements.txt
```

### Avvio Server

```bash
python main.py
```

Server disponibile su: http://localhost:8000

## 📡 Endpoints

### GET /
Health check

### POST /execute
Esegue codice ORATIO

**Request:**
```json
{
  "code": "Crea un puntino rosso.\nSalva come output.png.",
  "language": "it"
}
```

**Response:**
```json
{
  "success": true,
  "output": "Output del programma",
  "error": "",
  "image": "base64_encoded_image",
  "execution_time": 1.23
}
```

### GET /examples
Ritorna esempi predefiniti

## 🔒 Sicurezza

**IMPORTANTE per produzione:**

1. **Rate Limiting**: Limita richieste per IP
2. **Timeout**: Max 30 secondi per esecuzione
3. **Sandbox**: Esegui in container isolato
4. **CORS**: Permetti solo il tuo dominio
5. **Auth**: API key per utenti registrati

## 🐳 Deploy con Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
docker build -t oratio-api .
docker run -p 8000:8000 oratio-api
```

## ☁️ Deploy Cloud

### Railway
```bash
railway init
railway up
```

### Render
1. Connetti repo GitHub
2. Seleziona `api/` come root
3. Deploy automatico

### Fly.io
```bash
fly launch
fly deploy
```

## 🧪 Test

```bash
# Test health
curl http://localhost:8000/

# Test execution
curl -X POST http://localhost:8000/execute \
  -H "Content-Type: application/json" \
  -d '{"code": "Stampa \"Ciao!\"", "language": "it"}'

# Get examples
curl http://localhost:8000/examples
```

## 📊 Monitoring

Aggiungi logging e metriche:
- Richieste/secondo
- Tempo medio esecuzione
- Errori
- Uso risorse

## 🔐 Variabili Ambiente

```bash
# .env
OPENAI_API_KEY=your_key_here
MAX_EXECUTION_TIME=30
RATE_LIMIT_PER_MINUTE=10
ALLOWED_ORIGINS=https://oratio.dev
```

---

**API pronta per il playground!** 🚀
