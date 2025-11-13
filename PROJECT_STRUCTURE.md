# 📁 ORATIO Project Structure

```
oratio/
├── 📦 oratio/                      # Core language implementation
│   ├── compiler/                   # Parser and compiler
│   │   ├── parser.py              # Semantic parser
│   │   ├── local_parser.py        # GPU-based local parser
│   │   ├── languages.py           # Multi-language support
│   │   ├── validator.py           # IR validator
│   │   └── errors.py              # Custom exceptions
│   ├── runtime/                    # Execution engine
│   │   └── executor.py            # Runtime executor
│   └── ai/                         # AI auto-expansion system
│       ├── auto_expander.py       # Automatic operation generation
│       └── autonomous_growth.py   # Fully autonomous growth system
│
├── 🌐 website/                     # Public website (oratio.dev)
│   ├── index.html                 # Italian homepage
│   ├── index-en.html              # English homepage
│   ├── playground.html            # Interactive playground (IT)
│   ├── playground-en.html         # Interactive playground (EN)
│   ├── styles.css                 # Global styles
│   ├── logo_oratio.png            # Logo
│   ├── favicon_oratio.png         # Favicon
│   ├── CNAME                      # Custom domain config
│   ├── robots.txt                 # SEO
│   └── sitemap.xml                # SEO
│
├── 🚀 api/                         # Backend API
│   ├── main.py                    # FastAPI server
│   ├── requirements.txt           # API dependencies
│   └── README.md                  # API documentation
│
├── 📚 docs/                        # Documentation
│   ├── planning/                  # Architecture & roadmap
│   │   ├── ARCHITETTURA.md       # System architecture
│   │   ├── ROADMAP.md            # Development roadmap
│   │   ├── PROGRESS.md           # Progress tracking
│   │   └── MANIFESTO.md          # Project manifesto
│   ├── guides/                    # User guides
│   │   ├── GETTING_STARTED.md    # Quick start guide
│   │   ├── ESEMPI.md             # Examples
│   │   ├── PYPI_SETUP.md         # PyPI publishing guide
│   │   └── DEPLOY_WEBSITE.md     # Website deployment guide
│   └── marketing/                 # Marketing materials
│       ├── MARKETING_PLAN.md     # Marketing strategy
│       ├── ORATIO_LAUNCH.md      # Launch plan
│       ├── SCRIPT_VIDEO_DEMO.md  # Video demo script
│       └── reddit_posts.md       # Reddit posts templates
│
├── 🛠️ scripts/                     # Utility scripts
│   ├── setup_gpu.sh               # GPU setup script
│   ├── download_model.py          # Model downloader
│   ├── test_complete_system.py   # Full system test
│   ├── test_gpu_parser.py         # GPU parser test
│   └── README.md                  # Scripts documentation
│
├── 🧪 tests/                       # Test suite
│   ├── test_parser.py             # Parser tests
│   └── __init__.py                # Test package init
│
├── 📝 examples/                    # Example ORATIO code
│   ├── puntino_rosso.ora          # Red dot example
│   ├── test_english.ora           # English test
│   └── README.md                  # Examples documentation
│
├── 📄 README.md                    # Main README (English)
├── 📄 README_IT.md                 # Italian README
├── 📄 PROJECT_STRUCTURE.md         # This file
├── 📄 LICENSE                      # MIT License
├── 📄 pyproject.toml               # Python package config
├── 📄 .gitignore                   # Git ignore rules
└── 📄 .env                         # Environment variables

```

## 🎯 Main Components

### 1. **ORATIO Language** (`/oratio`)
Core programming language implementation
- Natural language parser (OpenAI API + Local GPU)
- Runtime executor with 50+ operations
- AI auto-expansion system

### 2. **Website** (`/website`)
Public-facing website
- Bilingual homepage (IT/EN)
- Interactive playground
- Live code execution

### 3. **API** (`/api`)
Backend API for playground
- FastAPI server
- Code execution endpoint
- CORS enabled

### 4. **Documentation** (`/docs`)
All project documentation
- Planning and architecture
- User guides
- Marketing materials

### 5. **Scripts** (`/scripts`)
Development and deployment scripts
- GPU setup
- Model download
- Testing utilities

## 🚀 Quick Commands

**Install:**
```bash
pip install oratio
```

**Run example:**
```bash
oratio examples/puntino_rosso.ora
```

**Start API:**
```bash
cd api && uvicorn main:app --reload --port 8001
```

**Setup GPU:**
```bash
./scripts/setup_gpu.sh
```

**Download model:**
```bash
python3 scripts/download_model.py
```

**Test system:**
```bash
python3 scripts/test_complete_system.py
```

**Run tests:**
```bash
pytest tests/
```

**Serve website locally:**
```bash
cd website && python -m http.server 8000
```

## 📦 Package Structure

The `oratio` package is published on PyPI and includes:
- Compiler (parser + validator)
- Runtime (executor)
- CLI tool
- AI expansion system (future)

## 🌐 Website Deployment

Website is automatically deployed to GitHub Pages:
- URL: https://manuzz88.github.io/oratio/
- Custom domain: oratio.dev (when configured)
- Auto-deploy on push to master

## 🔧 Development

**Local development:**
```bash
# Clone repo
git clone https://github.com/manuzz88/oratio.git
cd oratio

# Install in editable mode
pip install -e .

# Run tests
pytest tests/

# Start API
cd api && uvicorn main:app --reload
```

**Build package:**
```bash
python -m build
```

**Publish to PyPI:**
```bash
twine upload dist/*
```
