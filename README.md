### DMN AI (Default Mode Network Artificial Intelligence)

A local-first, multi-modal medical assistant and next-generation clinical scribe. DMN AI captures unstructured clinical conversations alongside objective, physical biometric telemetry vectors (processed completely on the edge in volatile RAM) to uncover diagnostic insights that voice-only scribes miss.

---
#### System Demonstration


<p align="center">
  <img src="assets/DMN AI - UI 1.png" width="32%" />
  <img src="assets/DMN AI - UI 2.png" width="32%" />
  <img src="assets/DMN AI - UI 3.png" width="32%" />
</p>


* **Biometrics (Left)** – Pressing Analyze creates a full biometric analysis from all visual and conversational data. The system writes medical SOAP notes and generates medical ICD-10 and CPT codes for insurance metadata. 
* **Create Anything (Center)** – Pressing Create allows creation of whatever the user needs including custom cross-examination prompts directly over the local vector database (e.g., dynamic multi-language translation requests). 
* **Creating a Care Plan (Right)** – Using the Create Anything feature a care plan can be created that will correlate to the biometric analysis.

---
#### Key Features

- **Local-First Privacy Architecture:** Isolates raw audio and video streams inside local volatile registers. All raw health data is destroyed at the frame-step boundary; only mathematical vector metadata is cached in the local vault.
- **Dual-Channel Clinical Auditing:** Uses Google Gemini (`gemini-2.5-pro`) to cross-examine verbal transcripts side-by-side with localized 3D spatial movement indices.
- **Automated Insurance Coding:** Instantly maps clinical findings to standardized billing matrices, generating corresponding ICD-10 diagnostic classifications and CPT evaluation codes.
- **On-Demand Custom Conversions:** Features an interactive query terminal to dynamically transform underlying session contexts into customized care plans, referral notes, or multilingual summaries.

---
#### Repository Layout


```
C:\labs\DMN-AI\
│
├── assets/
│   ├── caduceus.png        # Medical iconography branding asset
│   ├── DMN AI - UI 1.png   # Biometrics Analysis Dashboard
│   ├── DMN AI - UI 2.png   # Multi-Language Prompting Sandbox
│   └── DMN AI - UI 3.png   # Clinical Care Planner Blueprint
│
├── core/
│   ├── __init__.py         # Package namespace declaration
│   ├── database.py         # Local data profile routing index
│   └── pipeline.py         # Edge vision telemetry rendering matrix
│
├── .env                    # Local environment secrets (Git ignored)
├── .gitignore              # Repository exclusion rules manifest
├── app.py                  # Dual-panel user interface presentation engine
├── README.md               # Main repository documentation & guide
├── requirements.txt        # Python package dependency manifest
└── SUMMARY.md              # Project architecture abstract manifest
```

---
#### Prerequisites & Installation

To deploy this system from scratch or connect to the cloud environment, you must have **Python 3.11** installed on your workstation. The total environmental footprint of this project is approximately **1.35 GB**.

- **`Python 3.11`**: The base computing environment (~500 MB).
- **`google-genai`**: Official modern Google AI Studio SDK framework (~50 MB).
- **`streamlit`**: High-fidelity reactive presentation layer (~100 MB).
- **`opencv-python-headless`**: Server-optimized video capture matrix framework (~90 MB).
- **`mediapipe`**: Open-source 3D structural landmark coordinate engine (~150 MB).
- **`chromadb`**: Local-first vector storage vault instance (~450 MB).
- **`python-dotenv`**: Volatile configuration and API key isolate (~10 MB).

1. Clone or download this repository to your machine:

```
cd C:\labs\DMN-AI
```

2. Download and install all required framework modules using pip:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root project directory to manage your out-of-band security token:

```
GEMINI_API_KEY=your_actual_google_ai_studio_api_key_here
```

---
#### Getting Started (Local Development)

To launch the local clinical database and interface surface, run the following script:

```bash
streamlit run app.py
```

---
#### Cloud Production Infrastructure (Google Cloud Run)

The live production application utilizes a decoupled serverless container framework deployed directly onto Google Cloud Run.

- **Live Demo URL:** 
https://dmn-ai-app-674941016267.us-central1.run.app/

Serverless Deployment Command Workflow

1. Elevate local session script execution policies inside PowerShell:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```


2. Build an explicit, clean UTF-8 text encoding manifest to block local cache syncing crashes:

```powershell
[System.IO.File]::WriteAllLines("$pwd\.gcloudignore", @('.git/', 'node_modules/', 'venv/', '__pycache__/', 'chroma/', 'assets/', '*.png', '*.jpg', '*.jpeg', '*.db', '.env'))
```

3. Submit the source code to Cloud Build to automatically compile dependencies and system graphics packages via the project `Dockerfile`:

```powershell
gcloud builds submit --tag gcr.io/gen-lang-client-0261345601/dmn-ai-app .
```

4. Initialize the immutable container image live on Cloud Run with environment secrets enforced:

```powershell
gcloud run deploy dmn-ai-app --image gcr.io/gen-lang-client-0261345601/dmn-ai-app --allow-unauthenticated --region us-central1 --set-env-vars GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

---
#### Systems Engineering & DevOps
To ensure cross-platform consistency and zero-downtime scalability, the production environment is fully containerized and deployed to Google Cloud Run as an isolated serverless microservice.

* **Infrastructure Architecture:** Serverless Containerized Deployment
* **Container Core Base Image:** `python:3.11-slim` (Debian Linux Runtime)
* **Secret Isolation Model:** Decoupled Runtime Environment Variable Injection (`--set-env-vars`)
* **Graphics Dependency Resolution:** Embedded OS-level `apt-get` patching for `libgl1` and `libglib2.0-0` layers

##### Orchestration & Cloud Engineering
```powershell
# 1. Authorize session script execution boundaries
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# 2. Enforce explicit UTF-8 ignore matrices to isolate binary database weight artifacts
[System.IO.File]::WriteAllLines("$pwd\.gcloudignore", @('.git/', 'node_modules/', 'venv/', '__pycache__/', 'chroma/', 'assets/', '*.png', '*.jpg', '*.jpeg', '*.db', '.env'))

# 3. Stream source modules to Google Cloud Build for container image compilation
gcloud builds submit --tag gcr.io/gen-lang-client-0261345601/dmn-ai-app .

# 4. Initialize image on Cloud Run with zero-cache environment variables enforced
gcloud run deploy dmn-ai-app --image gcr.io/gen-lang-client-0261345601/dmn-ai-app --allow-unauthenticated --region us-central1 --set-env-vars GEMINI_API_KEY="SECURE_VARIABLE_STRING"
```

---
#### AI Medical Assistant - Input Suggestions

- **Create a summary in Spanish** (Generates a translated medical summary for families)
- **Create a summary in English** (Generates a clean clinical summary layout)
- **Create a care roadmap** (Generates actionable at-home steps and checklist items)
- **Create an email summary** (Drafts a clean message summarizing session data)
- **Create a referral letter** (Outlines a formal note to an outside specialist)
- **Create a task list** (Extracts immediate behavioral follow-ups for the patient)

---

#### Operational Resilience

This system includes an integrated logical parser fallback routine to handle remote server rate limitations or account testing blocks (`429 RESOURCE_EXHAUSTED`). If network communication interruptions occur, the UI layer automatically routes data requests to secure local heuristic fallbacks, ensuring seamless, zero-downtime presentations during evaluations.

---
#### Architectural Design

As a solo systems architect, my design pattern for **DMN AI** balances the line between intense local data sovereignty requirements (HIPAA compliance, patient privacy) and cloud-scale semantic reasoning. The core value proposition to investors is simple: **We are eliminating the single biggest blind spot in modern medical scribes—non-verbal behavioral analytics.** Traditional digital scribes listen to what a patient says, but they miss objective physical metrics. During a neurobehavioral assessment, an experienced physician looks for structural anomalies like micro-oscillations in hand gestures, rapid postural shifting, or shallow respiratory cycles.

DMN AI processes live multi-modal data at the edge. The system routes video and audio input through an on-device computer vision pipeline using **OpenCV** and **MediaPipe**. This data lives strictly in volatile memory (RAM); it is never recorded, saved as raw media, or broadcast to external networks. The local pipeline reduces raw pixel matrices into highly compressed, 3D coordinate vector arrays. These anonymized vector footprints are stored in a local embedded database vault using **ChromaDB**, which routes files dynamically via an **Active Patients** profile interface (Patient 1 for ADHD diagnostics and Patient 2 for Anxiety metrics).

When a clinical session summary is requested, only the structured text transcript and the mathematical vector coordinate matrices are sent out-of-band to the flagship **Google Gemini API** (`gemini-2.5-pro`). Gemini acts as our heavy-reasoning multi-agent engine: it audits conversational text against objective physical behaviors within a unified **Session Biometric Summary**, automatically builds structured **Medical SOAP Notes**, maps specialized **Biometric Analysis** (Video and Conversation tracking breakdowns), and extracts proper **Medical Codes** (ICD-10 and CPT insurance metadata). The clinician can then use the integrated **AI Medical Assistant** interface with the **"Create Anything"** section to input requests to cross-examine underlying session context variables on-demand—instantly generating custom care roadmaps, specialist referral notes, or multilingual session translations via a dedicated "Create" **execution pipeline**.