# 🔥 GPU Setup Guide - ORATIO Local Parser

Guida completa per configurare il parser GPU locale con Qwen 2.5 Coder 14B.

---

## 🎯 Perché GPU Locale?

### Vantaggi
- ⚡ **Velocità**: 50-100ms vs 500-2000ms (OpenAI API)
- 💰 **Costo**: $0 vs $0.01 per richiesta
- 🔒 **Privacy**: Tutto locale, nessun dato inviato online
- 📈 **Scalabilità**: Lineare con operazioni, non con richieste
- 🌐 **Offline**: Funziona senza connessione internet

### Requisiti
- **GPU**: NVIDIA con almeno 20GB VRAM (es. RTX 4000 Ada, RTX 3090, A100)
- **CUDA**: 12.1 o superiore
- **RAM**: 32GB+ consigliati
- **Spazio disco**: ~30GB per il modello

---

## 📦 Modello: Qwen 2.5 Coder 14B Instruct

### Perché Qwen?

✅ **Stabile** - Architettura testata, nessun bug MoE  
✅ **Veloce** - Ottimizzato per inference  
✅ **Multi-GPU nativo** - Supporto out-of-the-box  
✅ **Ottimo per codice** - Trained specificamente su codice  
✅ **14B parametri** - Perfetto per 2x RTX 4000 Ada (40GB VRAM totale)

### vs DeepSeek V2 (DEPRECATED)

| Feature | Qwen 2.5 Coder | DeepSeek V2 |
|---------|----------------|-------------|
| Stabilità | ✅ Eccellente | ❌ Bug MoE multi-GPU |
| Performance | ✅ 50-100ms | ⚠️ 100-200ms |
| Setup | ✅ Plug & Play | ❌ Richiede fix manuali |
| Parametri | 14B | 16B |
| VRAM | ~28GB | ~32GB |

---

## 🛠️ Installazione

### Step 1: Setup Dipendenze

```bash
cd /path/to/oratio
./scripts/setup_gpu.sh
```

Questo installa:
- PyTorch 2.5.1 con CUDA 12.1
- Transformers 4.57+
- Accelerate (multi-GPU)
- Ottimizzazioni varie

### Step 2: Download Modello

```bash
python3 scripts/download_qwen.py
```

**Tempo:** ~40-50 minuti (28GB)  
**Spazio:** ~30GB in `~/.cache/oratio/models/`

### Step 3: Test

```bash
python3 scripts/test_qwen.py
```

Output atteso:
```
🔥 Testing GPU...
CUDA available: True
GPU count: 2

📦 Loading Qwen 2.5 Coder 14B...
✅ Model loaded!
✅ Device map: {'model.embed_tokens': 0, 'model.layers.0': 0, ...}

🧪 Testing inference...
📝 Output:
print('Hello World')

🎉 SUCCESS! Qwen 2.5 Coder is working!
```

---

## 🚀 Utilizzo

### In Python

```python
from oratio.compiler.local_parser import LocalGPUParser

# Inizializza parser (carica modello)
parser = LocalGPUParser()

# Parse codice
ir = parser.parse("Crea un puntino rosso", language="it")

# Esegui
from oratio.runtime.executor import Runtime
runtime = Runtime()
runtime.execute(ir)
```

### Da CLI

```bash
# Usa GPU automaticamente se disponibile
oratio examples/puntino_rosso.ora
```

### Fallback OpenAI

Se GPU non disponibile, ORATIO usa automaticamente OpenAI API:

```python
# In oratio/compiler/parser.py
try:
    parser = LocalGPUParser()  # Prova GPU
except:
    parser = SemanticParser()  # Fallback OpenAI
```

---

## ⚙️ Configurazione Avanzata

### Multi-GPU

Qwen supporta multi-GPU automaticamente:

```python
# Automatico (consigliato)
parser = LocalGPUParser()  # device_map="auto"

# Manuale
parser = LocalGPUParser()
parser.model.to("cuda:0")  # Solo GPU 0
```

### Ottimizzazione Memoria

```python
# 8-bit quantization (dimezza VRAM)
from transformers import BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(
    load_in_8bit=True,
    bnb_8bit_compute_dtype=torch.float16
)

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-Coder-14B-Instruct",
    quantization_config=quantization_config,
    device_map="auto"
)
```

### Performance Tuning

```python
# Genera con parametri ottimizzati
outputs = model.generate(
    **inputs,
    max_new_tokens=512,
    temperature=0.1,      # Più deterministico
    do_sample=True,
    top_p=0.95,
    repetition_penalty=1.1
)
```

---

## 🐛 Troubleshooting

### Out of Memory

**Problema:** `CUDA out of memory`

**Soluzione:**
```bash
# Usa quantization 8-bit
export ORATIO_USE_8BIT=1
python3 your_script.py
```

### Modello Non Trovato

**Problema:** `Model not found in cache`

**Soluzione:**
```bash
# Ri-scarica modello
rm -rf ~/.cache/oratio/models/models--Qwen*
python3 scripts/download_qwen.py
```

### Lento su Multi-GPU

**Problema:** Inference lenta con 2+ GPU

**Soluzione:**
```python
# Forza single-GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
```

---

## 📊 Benchmark

### Performance (2x RTX 4000 Ada, 40GB VRAM)

| Operazione | Tempo | vs OpenAI |
|------------|-------|-----------|
| Parse semplice | 50ms | 10x più veloce |
| Parse complesso | 100ms | 5x più veloce |
| Caricamento modello | 30s | Una tantum |

### Costi (1000 richieste/giorno)

| Soluzione | Costo/mese | Note |
|-----------|------------|------|
| GPU Locale | $43 | Solo elettricità |
| OpenAI API | $300 | $0.01 per richiesta |
| **Risparmio** | **$257/mese** | Break-even: 4 mesi |

---

## 🔄 Migrazione da DeepSeek

Se hai già DeepSeek installato:

```bash
# 1. Scarica Qwen
python3 scripts/download_qwen.py

# 2. ORATIO userà automaticamente Qwen (default in local_parser.py)

# 3. (Opzionale) Rimuovi DeepSeek per liberare spazio
rm -rf ~/.cache/oratio/models/models--deepseek-ai*
```

---

## 🆘 Supporto

- 📧 Email: manuel@oratio.dev
- 💬 Telegram: @manu_lz88
- 🐛 Issues: https://github.com/manuzz88/oratio/issues

---

## 📚 Risorse

- [Qwen 2.5 Coder Paper](https://arxiv.org/abs/2409.12186)
- [HuggingFace Model Card](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct)
- [Transformers Documentation](https://huggingface.co/docs/transformers)
- [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit)

---

**Ultima modifica:** 13 Novembre 2025  
**Versione ORATIO:** 0.2.0
