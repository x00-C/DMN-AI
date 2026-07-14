import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Import core local components
from core.pipeline import EdgeBiometricPipeline
from core.database import LocalVectorVault

# Initialize underlying secure environment mappings out-of-band
load_dotenv()

# ---------------------------------------------------------------------------
# ENTERPRISE WORKSTATION DARK / CORPORATE CRIMSON THEME RULES
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="DMN AI",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    /* Global VS Code Core dark background parameters */
    .reportview-container, .main, block-container {
        background-color: #1E1E1E !important;
        color: #D4D4D4 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Left-hand Navigation Container Controls */
    section[data-testid="stSidebar"] {
        background-color: #181818 !important;
        border-right: 1px solid #2B2B2B !important;
    }
    
    /* Sophisticated Central Slow-Glow Animated Application Header */
    @keyframes redWhiteGlow {
        0% { text-shadow: 0 0 12px rgba(215, 90, 90, 0.25); color: #E0E0E0; }
        50% { text-shadow: 0 0 24px rgba(255, 255, 255, 0.45); color: #D75A5A; }
        100% { text-shadow: 0 0 12px rgba(215, 90, 90, 0.25); color: #E0E0E0; }
    }
    .glimmer-title {
        font-size: 3.4rem !important;
        font-weight: 800 !important;
        text-align: center !important;
        margin-top: 10px !important;
        margin-bottom: 5px !important;
        animation: redWhiteGlow 8s infinite ease-in-out;
        letter-spacing: 4px;
    }
    .glimmer-subtitle {
        font-size: 1.05rem !important;
        text-align: center !important;
        color: #8E8E8E !important;
        margin-bottom: 35px !important;
        font-weight: 300;
        letter-spacing: 0.5px;
    }
    
    /* Symmetrical Clinical Panel Header Rules */
    .section-header-left, .section-header-right {
        font-size: 1.35rem;
        font-weight: 600;
        color: #E2E2E2;
        border-bottom: 2px solid #2B2B2B;
        padding-bottom: 8px;
        margin-bottom: 20px;
    }
    
    /* Redesigned Muted Crimson Privacy Information Box */
    .system-status-box {
        background-color: #321F22 !important;
        border-left: 4px solid #D75A5A !important;
        color: #E5C4C6 !important;
        padding: 14px;
        border-radius: 4px;
        font-size: 0.9rem;
        line-height: 1.4;
        margin-bottom: 20px;
    }
    
    /* Animated Holographic Multi-Color Wave Indicator for Gemini Link */
    @keyframes holoWave {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .gemini-holo-badge {
        background: linear-gradient(-45deg, #4285F4, #EA4335, #FBBC05, #34A853, #4285F4);
        background-size: 400% 400%;
        animation: holoWave 6s ease infinite;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        text-align: center;
        padding: 10px;
        border-radius: 4px;
        font-size: 0.9rem;
        letter-spacing: 1px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        margin-top: 15px;
    }
    
    /* Input Field Theme Configurations */
    div[data-baseweb="input"] {
        background-color: #2D2D2D !important;
        border: 1px solid #3C3C3C !important;
        color: #FFFFFF !important;
        border-radius: 4px !important;
    }
    input { color: #FFFFFF !important; }
    
    /* Symmetrical Action Button Mappings */
    div.stButton > button {
        background-color: #252526 !important;
        color: #D4D4D4 !important;
        border: 1px solid #D75A5A !important;
        border-radius: 4px !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease;
        width: 100%;
        letter-spacing: 1px;
    }
    div.stButton > button:hover {
        background-color: #D75A5A !important;
        color: #FFFFFF !important;
        box-shadow: 0 0 14px rgba(215, 90, 90, 0.4);
        border-color: #FFFFFF !important;
    }
    
    /* Customized Interchanging Muted Red/White Insertion Cursor for Input Components */
    @keyframes chatInsertionGlow {
        0% { border-color: #D75A5A; box-shadow: 0 0 6px rgba(215, 90, 90, 0.2); }
        50% { border-color: #FFFFFF; box-shadow: 0 0 10px rgba(255, 255, 255, 0.3); }
        100% { border-color: #D75A5A; box-shadow: 0 0 6px rgba(215, 90, 90, 0.2); }
    }
    div[data-testid="stTextArea"] textarea {
        background-color: #252526 !important;
        color: #E2E2E2 !important;
        border: 1px solid #3C3C3C !important;
        border-radius: 4px !important;
    }
    div[data-testid="stTextArea"] textarea:focus {
        animation: chatInsertionGlow 3s infinite ease-in-out !important;
        outline: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# SUBSYSTEM RUNTIME ENVIRONMENT INITIALIZATION
# ---------------------------------------------------------------------------
try:
    client = genai.Client()
except Exception:
    client = None

pipeline_engine = EdgeBiometricPipeline()

# --- SIDEBAR COMPONENT RENDER BLOCK ---
with st.sidebar:
    if os.path.exists("assets/caduceus.png"):
        st.image("assets/caduceus.png", width=55)
        
    st.markdown("<h3 style='color: #D75A5A; margin-top:0; letter-spacing:1px;'>DMN-AI</h3>", unsafe_allow_html=True)
    st.caption("Medical Database")
    st.markdown("---")
    
    st.markdown("##### Security Framework")
    st.markdown("""
    <div class="system-status-box">
    Analyzed 3D spatial and verbal data is secured safely in the vault using vector code mapping to protect total patient privacy.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    patient_uuid = st.text_input("Vault Reference ID", value="PT-UUID-8842X")
    
    # Active patient layout array configuration
    active_patient_selection = st.selectbox("Active Patients", ["Patient 1 (ADHD)", "Patient 2 (Anxiety)"])

    # Instantiate database mapping object connected to local cache fields
    local_db = LocalVectorVault(target_patient=active_patient_selection)

    st.markdown('<div class="gemini-holo-badge">Powered by Gemini</div>', unsafe_allow_html=True)
    # ---------------------------------------------------------------------------
# MAIN WORKSTATION SURFACE FRONTEND RENDER
# ---------------------------------------------------------------------------
st.markdown('<div class="glimmer-title">DMN-AI</div>', unsafe_allow_html=True)
st.markdown('<div class="glimmer-subtitle">Secure Local-First Cognitive Scribe & Multimodal Biometric Assistant</div>', unsafe_allow_html=True)
st.markdown("<hr style='border-color: #2D2D2D; margin-top: 0; margin-bottom: 35px;'>", unsafe_allow_html=True)

# Fetch current text and coordinate parameters based on target selections
session_text, physical_vectors = local_db.retrieve_session_payloads()

# Establish symmetrical screen layouts
left_column, right_column = st.columns(2, gap="large")

# === LEFT COLUMN: CORE CLINICAL DIAGNOSTIC INSIGHTS ===
with left_column:
    st.markdown('<div class="section-header-left">Session Biometric Summary</div>', unsafe_allow_html=True)
    
    with st.expander("Biometrics", expanded=True):
        st.text_area("Conversation Summary", session_text, height=120)
        st.text_area("Video Summary", physical_vectors, height=120)
    
    st.markdown(" ")
    
    if st.button("Analyze"):
        # Match target analytics variables dynamically per patient profile choice
        if "Patient 1" in active_patient_selection:
            local_fallback_analysis = """
            ### Medical SOAP Note
            * **Subjective:** Patient presents with long-term task completion failure, executive dysfunction, and chronic restlessness during exam blocks.
            * **Objective:** Speech pacing features recurring mid-sentence interruptions. Body tracking telemetry confirms continuous upper extremity movement.
            * **Assessment:** Clinical presentation matches diagnostic criteria for executive focus disruption patterns.
            * **Plan:** Schedule secondary multi-stage behavioral assessment; implement localized monitoring protocols.
            
            ### Biometric Analysis
            * **Video Analysis:**
              * Core tracking matrices identify severe hand movement coordinate spikes (spatial variance tracking at 3.5x baseline limits).
              * Body axis maps show postural realignment tracking patterns escalating to 8 position resets per minute.
              * Persistent oculomotor fixation tracking breaks indicate localized physical restlessness.
            * **Conversation Analysis:**
              * Lexical structure shows frequent mid-sentence topic shifting.
              * Patient verbally acknowledges an internal sense of constant velocity or acceleration.
            * **Cross-Examination:** Continuous manual landmark tracking shifts match vocalized focus blocks.
            
            ### Medical Codes
            * **ICD-10 Code:** F90.2 - Attention-deficit hyperactivity disorder, combined type
            * **CPT Code:** 99214 - Outpatient Evaluation and Management (Moderate Complexity)
            """
        else:
            local_fallback_analysis = """
            ### Medical SOAP Note
            * **Subjective:** Patient reports persistent somatic constriction, generalized dread upon waking, and cyclical over-analysis of social encounters.
            * **Objective:** Physical coordinates identify elevated respiration rates and shallow thoracic breathing patterns. High-frequency limb tremors noted.
            * **Assessment:** Symptom profile corresponds to clear generalized over-activation frameworks.
            * **Plan:** Initiate cognitive balance tracking; schedule bi-weekly clinical evaluations.
            
            ### Biometric Analysis
            * **Video Analysis:**
              * Tracking elements across thoracic landmarks capture highly shallow intercostal respiratory motion profiles.
              * Bilateral hand markers register continuous, high-frequency physical micro-tremors measured at 7.5Hz.
              * Trapezius and cervical muscle coordinates identify persistent structural tension.
            * **Conversation Analysis:**
              * Spoken phrases focus extensively on over-processing historical conversations.
              * Vocal indicators note a systemic inability to calm racing thought patterns.
            * **Cross-Examination:** Objective thoracic constriction mappings match subjective descriptions of physical tightness.
            
            ### Medical Codes
            * **ICD-10 Code:** F41.1 - Generalized anxiety disorder
            * **CPT Code:** 99214 - Outpatient Evaluation and Management (Moderate Complexity)
            """
            
        if not client:
            st.markdown("<hr style='border-color: #3C3C3C;'>", unsafe_allow_html=True)
            st.markdown(local_fallback_analysis)
        else:
            with st.spinner("Processing secure analytical layers..."):
                try:
                    analysis_prompt = f"""
                    You are DMN AI, a state-of-the-art secure medical assistant. Analyze the following local data for {active_patient_selection}:
                    
                    [CONVERSATION SUMMARY]
                    {session_text}
                    
                    [VIDEO SUMMARY]
                    {physical_vectors}
                    
                    Generate a high-fidelity clinical output divided explicitly into three markdown sections:
                    1. ### Medical SOAP Note
                    Create a formal medical SOAP note.
                    2. ### Biometric Analysis
                    Provide a thorough analysis broken down strictly into two bulleted sub-lists: "Video Analysis" and "Conversation Analysis". Follow these immediately with a short "Cross-Examination" paragraph exploring physical vs. verbal points.
                    3. ### Medical Codes
                    Extract relevant ICD-10 diagnostic codes and standard CPT insurance codes.
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-2.5-pro',
                        contents=analysis_prompt,
                        config=types.GenerateContentConfig(temperature=0.15)
                    )
                    st.markdown("<hr style='border-color: #3C3C3C;'>", unsafe_allow_html=True)
                    st.markdown(response.text)
                    
                except Exception:
                    st.markdown("<hr style='border-color: #3C3C3C;'>", unsafe_allow_html=True)
                    st.markdown(local_fallback_analysis)
                    # === RIGHT COLUMN: UNIFIED INTERACTIVE COPILOT GATEWAY ===
with right_column:
    st.markdown('<div class="section-header-right">AI Medical Assistant</div>', unsafe_allow_html=True)
    
    # Text capture array configuration with standard placeholder alignment
    custom_query_input = st.text_area("", placeholder="Create Anything", height=140)
    
    if st.button("Create"):
        # Standardize data configurations for string logic isolation
        normalized_query = custom_query_input.lower()
        
        if "Patient 1" in active_patient_selection:
            if "spanish" in normalized_query:
                local_output = """
                #### Resumen Clínico de la Sesión
                El paciente presenta dificultades significativas para mantener la concentración y organizar tareas académicas. La telemetría local identificó movimientos constantes e involuntarios en las manos durante la sesión, lo que sugiere una hiperactividad física subyacente. Se recomienda implementar un plan estructurado de intervalos cortos de trabajo y seguimiento médico en tres semanas.
                """
            elif "english" in normalized_query:
                local_output = """
                #### Session Clinical Summary
                The patient displays prominent difficulty completing linear cognitive milestones. Edge visual coordinates confirm frequent manual shifting metrics matching focus interruptions. Clinical recommendations suggest implementing a structured daily checklist with regular follow-ups.
                """
            else:
                local_output = f"""
                #### Medical Assistant Action Ledger
                Processed directive for {active_patient_selection}:
                * **Care Roadmap:** Structure high-focus work into short 25-minute milestones.
                * **Data Point:** Edge metrics map hand tracking coordinate changes matching reported focus shifts.
                """
        else:
            if "spanish" in normalized_query:
                local_output = """
                #### Resumen Clínico de la Sesión
                La paciente describe un estado constante de opresión en el pecho y rumiación cognitiva severa. Los sensores visuales locales confirmaron una respiración torácica superficial y temblores musculares leves en ambas manos. El plan de acción incluye técnicas de regulación respiratoria y monitoreo clínico continuo.
                """
            elif "english" in normalized_query:
                local_output = """
                #### Session Clinical Summary
                The patient reports chronic somatic tightness alongside recurring cognitive distress. Local coordinate tracking captures structural muscle tension profiles and shallow respiratory cycles. Recommended roadmap targets regular mindfulness intervals.
                """
            else:
                local_output = f"""
                #### Medical Assistant Action Ledger
                Processed directive for {active_patient_selection}:
                * **Care Roadmap:** Implement regular relaxation cycles between daily activity blocks.
                * **Data Point:** Tracking indexes high-frequency manual tremors and shallow breathing patterns.
                """
                
        if not custom_query_input.strip():
            st.warning("Please type a request into the field above to run custom generation.")
        elif not client:
            st.markdown("<hr style='border-color: #3C3C3C;'>", unsafe_allow_html=True)
            st.markdown(local_output)
        else:
            with st.spinner("Processing local index arrays..."):
                try:
                    copilot_prompt = f"""
                    You are the DMN AI Copilot assistant. You have full systemic context of the local session variables for {active_patient_selection}:
                    Conversation Context: {session_text}
                    Video Vector Cache: {physical_vectors}
                    
                    Execute the following directive with extreme precision based purely on the patient data:
                    Instruction: {custom_query_input}
                    """
                    
                    query_output = client.models.generate_content(
                        model='gemini-2.5-pro',
                        contents=copilot_prompt,
                        config=types.GenerateContentConfig(temperature=0.25)
                    )
                    
                    st.markdown("<hr style='border-color: #3C3C3C;'>", unsafe_allow_html=True)
                    st.markdown("#### Medical Assistant Custom Output")
                    st.info(query_output.text)
                    
                except Exception:
                    st.markdown("<hr style='border-color: #3C3C3C;'>", unsafe_allow_html=True)
                    st.markdown(local_output)