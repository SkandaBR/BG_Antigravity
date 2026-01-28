# System Installation Guide

## Bhagavad Gita Knowledge Repository - RAG-based Q&A System

---

### 1. System Requirements

| Component | Minimum Requirement |
|-----------|---------------------|
| **Operating System** | Windows 10/11, Linux (Ubuntu 20.04+), macOS 12+ |
| **Python Version** | Python 3.10 - 3.12 (Recommended: 3.12) |
| **RAM** | 8 GB (16 GB recommended for optimal performance) |
| **Storage** | 5 GB free disk space |
| **Internet Connection** | Required for initial setup and Text-to-Speech functionality |

---

### 2. Software Dependencies

The application relies on the following key Python libraries:

| Library | Version | Purpose |
|---------|---------|---------|
| Streamlit | 1.53.1 | Web application framework |
| ChromaDB | 1.4.1 | Vector database for semantic search |
| Sentence-Transformers | 5.2.0 | Text embedding generation |
| PyTorch | 2.10.0 | Deep learning backend |
| Scikit-learn | 1.8.0 | Cosine similarity computation |
| gTTS | 2.5.4 | Google Text-to-Speech integration |
| NumPy | 2.4.1 | Numerical computations |
| Pandas | 2.3.3 | Data manipulation |

---

### 3. Installation Steps

#### Step 1: Clone or Download the Project
```bash
git clone <repository-url>
cd BG_Antigravity
```

#### Step 2: Create Virtual Environment
```bash
python -m venv .venv
```

#### Step 3: Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

#### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 5: Verify Installation
```bash
pip list | grep -E "streamlit|chromadb|sentence-transformers"
```

---

### 4. Running the Application

Execute the following command to start the Streamlit application:

```bash
streamlit run app.py
```

The application will be accessible at:
- **Local URL:** http://localhost:8501
- **Network URL:** http://<your-ip>:8501

---

### 5. Directory Structure

```
BG_Antigravity/
├── app.py                    # Main application file
├── requirements.txt          # Python dependencies
├── bhagavadgita_Chapter_2.json   # Bhagavad Gita verse data
├── chroma_db/                # Persistent vector database
├── audio_files/              # Pre-generated audio files
│   ├── en/                   # English audio
│   ├── kn/                   # Kannada audio
│   └── sa/                   # Sanskrit audio
└── .venv/                    # Virtual environment
```

---

### 6. Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure virtual environment is activated and run `pip install -r requirements.txt` |
| ChromaDB import error | Verify Python version is 3.10-3.12; reinstall chromadb |
| Audio not playing | Check internet connectivity for gTTS; verify audio_files directory exists |
| Port 8501 in use | Run `streamlit run app.py --server.port 8502` |

---

### 7. Hardware Specifications (Development Environment)

| Component | Specification |
|-----------|---------------|
| Processor | Intel Core i5 / AMD Ryzen 5 or higher |
| GPU | Optional (CPU inference supported) |
| RAM | 16 GB DDR4 |
| Storage | SSD recommended for faster vector operations |

---

*Document Version: 1.0 | Last Updated: January 2026*
