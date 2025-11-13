# 🤖 ORATIO Marketing Bot

Bot automatico per pubblicizzare ORATIO su piattaforme social.

---

## 🎯 Cosa Fa

Il bot automatizza:
- 📱 **Twitter/X**: Thread automatici, risposte, monitoraggio
- 🔴 **Reddit**: Post su subreddit, cross-posting
- 📝 **Dev.to**: Pubblicazione articoli

---

## 🚀 Setup

### 1. Installa Dipendenze

```bash
pip install tweepy praw requests
```

### 2. Configura API Keys

#### Twitter/X
1. Vai su https://developer.twitter.com
2. Crea un'app
3. Genera API keys
4. Aggiungi a `.env`:
```bash
TWITTER_API_KEY=your-key
TWITTER_API_SECRET=your-secret
TWITTER_ACCESS_TOKEN=your-token
TWITTER_ACCESS_SECRET=your-token-secret
```

#### Reddit
1. Vai su https://www.reddit.com/prefs/apps
2. Crea un'app (script type)
3. Aggiungi a `.env`:
```bash
REDDIT_CLIENT_ID=your-client-id
REDDIT_CLIENT_SECRET=your-secret
REDDIT_USERNAME=your-username
REDDIT_PASSWORD=your-password
```

#### Dev.to
1. Vai su https://dev.to/settings/extensions
2. Genera API key
3. Aggiungi a `.env`:
```bash
DEVTO_API_KEY=your-api-key
```

### 3. Lancia il Bot

```bash
python3 scripts/marketing_bot.py
```

---

## ⚠️ IMPORTANTE

### Rate Limits
- **Twitter**: 50 tweets/giorno (Free tier)
- **Reddit**: 1 post ogni 10 minuti
- **Dev.to**: 10 articoli/giorno

### Best Practices
- ✅ Non spammare
- ✅ Rispondi ai commenti manualmente
- ✅ Varia i contenuti
- ✅ Monitora le reazioni
- ❌ Non postare lo stesso contenuto ovunque

### Rischi
- **Ban**: Se usi il bot troppo aggressivamente
- **Shadowban**: Se sembri spam
- **Reputazione**: Se il contenuto è di bassa qualità

---

## 💡 Raccomandazioni

### Meglio Fare Manualmente
- ❌ Hacker News (no API, meglio manuale)
- ❌ Product Hunt (richiede interazione umana)
- ❌ LinkedIn (API limitata)

### Automazione OK
- ✅ Twitter thread (schedulati)
- ✅ Dev.to articoli (cross-posting)
- ⚠️ Reddit (con cautela)

---

## 🎯 Strategia Consigliata

### Fase 1: Setup (Oggi)
1. Configura solo Twitter
2. Testa con 1-2 tweet
3. Verifica che funzioni

### Fase 2: Lancio Soft (Domani)
1. Thread Twitter automatico
2. Post Reddit manuale (più sicuro)
3. Articolo Dev.to automatico

### Fase 3: Monitoraggio (Settimana 1)
1. Rispondi a TUTTI i commenti (manualmente)
2. Monitora metriche
3. Aggiusta strategia

### Fase 4: Scala (Settimana 2+)
1. Se funziona → Automatizza di più
2. Se non funziona → Torna al manuale

---

## 📊 Metriche da Tracciare

- 👁️ Impressions
- 💬 Engagement (like, retweet, commenti)
- 🔗 Click su GitHub
- ⭐ GitHub stars
- 📈 Traffico sito web

---

## 🆘 Troubleshooting

### "API not configured"
→ Verifica che le chiavi siano in `.env`

### "Rate limit exceeded"
→ Aspetta 15 minuti e riprova

### "Invalid credentials"
→ Rigenera le API keys

### "Shadowban on Reddit"
→ Usa account più vecchio, posta meno frequentemente

---

## 🚫 NON FARE

- ❌ Postare ogni 5 minuti
- ❌ Stesso contenuto su tutti i subreddit
- ❌ Ignorare i commenti
- ❌ Usare bot per rispondere
- ❌ Comprare follower/upvote

---

## ✅ FARE

- ✅ Contenuto di qualità
- ✅ Rispondere personalmente
- ✅ Variare i messaggi
- ✅ Essere autentico
- ✅ Ascoltare il feedback

---

**Remember: Il bot è uno strumento. La vera crescita viene dall'engagement umano!** 🚀
