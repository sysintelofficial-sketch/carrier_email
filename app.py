import streamlit as st
import os

# 1. Page Configuration
st.set_page_config(page_title="System Intelligence | Ahsan Khan", layout="wide", page_icon="💠")

# --- Configuration & Links ---
website_url = "https://sysintelofficial.com"
whatsapp_url = "https://wa.me/923245277654"
si_url = "https://edusi.sysintelofficial.com"

# 2. Premium Cinematic UI Styling
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top right, #040811, #0a0f1c);
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stSidebar"] {
        background-color: rgba(10, 15, 28, 0.95) !important;
        border-right: 2px solid #00e5ff;
    }
    .sidebar-btn {
        text-decoration: none;
        display: block;
        border: 2px solid #00e5ff;
        padding: 14px;
        text-align: center;
        border-radius: 6px;
        color: #00e5ff !important;
        font-weight: 800;
        margin-bottom: 15px;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    .sidebar-btn:hover {
        background-color: #00e5ff !important;
        color: #040411 !important;
        box-shadow: 0 0 30px #00e5ff;
    }
    .feature-card {
        background: #101827; 
        padding: 25px; 
        border-radius: 8px;
        border: 1px solid #1e293b; 
        text-align: left;
        margin-bottom: 8px;
        height: 100%;
    }
    .sec-id { font-size: 0.75rem; color: #64748b; font-weight: 600; display: block; margin-bottom: 6px; text-transform: uppercase; }
    .feature-card h3 { color: #ffeb3b; margin: 0 0 10px; font-size: 1.15rem; font-weight: 700; }
    .feature-card p { margin: 0 0 15px 0; font-size: 0.9rem; color: #cbd5e1; line-height: 1.5; }
    .progress-ui { width: 100%; background: rgba(255,255,255,0.05); height: 6px; border-radius: 3px; overflow: hidden; }
    .progress-fill { height: 100%; }
    .impact-tag { font-size: 0.8rem; font-weight: 700; display: block; margin-top: 8px; }
    .stButton>button {
        width: 100% !important;
        background-color: #101827 !important;
        color: #00e5ff !important;
        border: 2px solid #00e5ff !important;
        font-weight: 800 !important;
    }
    .stButton>button:hover {
        background-color: #00e5ff !important;
        color: #040411 !important;
    }
    .phase-title {
        font-family: 'Orbitron', sans-serif;
        color: #00e5ff;
        font-size: 1.4rem;
        margin-top: 25px;
        margin-bottom: 20px;
    }
    .video-hide-wrapper {
        width: 100%; height: 430px; border-radius: 15px; border: 2px solid #00e5ff; overflow: hidden; position: relative; margin: 25px auto; background: #000;
    }
    .video-hide-wrapper iframe {
        position: absolute; top: -60px; left: 0; width: 100%; height: calc(100% + 120px); pointer-events: none;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Configuration
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#00e5ff;'>CORE ENGINE</h2>", unsafe_allow_html=True)
    st.markdown(f'<a href="{whatsapp_url}" class="sidebar-btn" target="_blank">💬 WHATSAPP SUPPORT</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{website_url}" class="sidebar-btn" target="_blank">🌐 OFFICIAL WEBSITE</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{si_url}" class="sidebar-btn" target="_blank">📄 DOCUMENTATION</a>', unsafe_allow_html=True)

# 4. Center Aligned Title Section
st.markdown("""
    <div style='text-align: center; width: 100%; padding: 10px 0;'>
        <h1 style="font-family: 'Orbitron', sans-serif; font-size: 3.5rem; color: #00e5ff; text-shadow: 0 0 20px rgba(0,229,255,0.8); letter-spacing: 4px; margin: 0 0 10px 0;">
            SYSTEM INTELLIGENCE
        </h1>
        <h2 style="color: #ffeb3b; font-size: 1.6rem; font-weight: 800; letter-spacing: 1px; margin: 0 0 12px 0;">
            Industrial Optimization & Operations Research Suite
        </h2>
        <p style="color: #cbd5e1; font-size: 1.15rem; font-weight: 500; margin: 0 0 20px 0;">
            Providing Deterministic Logic & Linear Programming Solutions for Global Enterprises
        </p>
        <div style="display: inline-block; padding: 8px 20px; background: #0b1724; border: 1px solid #00e5ff; border-radius: 20px; color: #00e5ff; font-size: 0.95rem; font-weight: 600;">
            Architected by <span style="color: #fff;">Ahsan Khan</span> | Mathematics | OR Specialist
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. Background Video Layout Block
video_id = "aDIUEaVF8v4"
st.markdown(f'<div class="video-hide-wrapper"><iframe src="https://www.youtube.com/embed/{video_id}?autoplay=1&mute=1&loop=1&playlist={video_id}&controls=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></div>', unsafe_allow_html=True)

# --- فنکشن: جو چیک کرے گا کہ فائل موجود ہے یا نہیں اور پیج سوئچ کرے گا ---
def launch_project_page(filename):
    expected_path = os.path.join("pages", filename)
    if os.path.exists(expected_path):
        st.switch_page(expected_path)
    else:
        st.warning(f"Project Framework for '{filename}' is incoming soon! Create this file in pages/ folder to activate.")

# =========================================
# PHASE 1: BASIC PLAN SUITE (01-06)
# =========================================
st.markdown("<div class='phase-title'>Phase 1: Basic Plan Suite (01-06)</div>", unsafe_allow_html=True)
cols_p1 = st.columns(3)

with cols_p1[0]:
    st.markdown("""<div class='feature-card'><span class='sec-id'>SEC-PROD-01</span><h3>NexusAPI Load Streamer</h3><p>High-speed data ingestion platform connecting to DAT & Truckstop networks to fetch and stream live spot market freight options.</p><span class='impact-tag' style='color:#FF1744;'>Market Ready: 95%</span><div class='progress-ui'><div class='progress-fill' style='width:95%; background:#FF1744;'></div></div></div>""", unsafe_allow_html=True)
    if st.button("Launch Nexus API", key="btn_01", use_container_width=True): 
        launch_project_page("01_BSC_NexusAPI.py")

with cols_p1[1]:
    st.markdown("""<div class='feature-card'><span class='sec-id'>SEC-PROD-02</span><h3>Chronos ELD Telematics</h3><p>An automated telematics interface syncing directly with enterprise ELD hardware to track driver availability and hours.</p><span class='impact-tag' style='color:#F50057;'>Market Ready: 92%</span><div class='progress-ui'><div class='progress-fill' style='width:92%; background:#F50057;'></div></div></div>""", unsafe_allow_html=True)
    if st.button("Launch Chronos ELD", key="btn_02", use_container_width=True): 
        launch_project_page("02_BSC_ChronosELD.py")

with cols_p1[2]:
    st.markdown("""<div class='feature-card'><span class='sec-id'>SEC-PROD-03</span><h3>FleetCore Asset Matrix</h3><p>Centralized database engine managing active truck locations, trailer types, driver preferences, and configurations.</p><span class='impact-tag' style='color:#D500F9;'>Market Ready: 94%</span><div class='progress-ui'><div class='progress-fill' style='width:94%; background:#D500F9;'></div></div></div>""", unsafe_allow_html=True)
    if st.button("Launch Fleet Core", key="btn_03", use_container_width=True): 
        launch_project_page("03_BSC_FleetCore.py")

cols_p1_b = st.columns(3)
with cols_p1_b[0]:
    st.markdown("""<div class='feature-card'><span class='sec-id'>SEC-PROD-04</span><h3>YieldCPM Cost-Per-Mile</h3><p>Financial baseline engine that continuously computes operational fixed and variable cost-per-mile metrics for assets.</p><span class='impact-tag' style='color:#651FFF;'>Market Ready: 90%</span><div class='progress-ui'><div class='progress-fill' style='width:90%; background:#651FFF;'></div></div></div>""", unsafe_allow_html=True)
    if st.button("Launch Yield CPM", key="btn_04", use_container_width=True): 
        launch_project_page("04_BSC_YieldCPM.py")

with cols_p1_b[1]:
    st.markdown("""<div class='feature-card'><span class='sec-id'>SEC-PROD-05</span><h3>CrediCheck Risk Filter</h3><p>Automated security gate checking broker credit ratings, micro-risk scores, and bond validity indexes before selection.</p><span class='impact-tag' style='color:#2979FF;'>Market Ready: 96%</span><div class='progress-ui'><div class='progress-fill' style='width:96%; background:#2979FF;'></div></div></div>""", unsafe_allow_html=True)
    if st.button("Launch Credi Check", key="btn_05", use_container_width=True): 
        launch_project_page("05_BSC_CrediCheck.py")

with cols_p1_b[2]:
    st.markdown("""<div class='feature-card'><span class='sec-id'>SEC-PROD-06</span><h3>LaneIntel Rate Auditor</h3><p>A statistical intelligence module archiving historical lane data to evaluate if streaming loads match market realities.</p><span class='impact-tag' style='color:#00B0FF;'>Market Ready: 88%</span><div class='progress-ui'><div class='progress-fill' style='width:88%; background:#00B0FF;'></div></div></div>""", unsafe_allow_html=True)
    if st.button("Launch Lane Intel", key="btn_06", use_container_width=True): 
        launch_project_page("06_BSC_LaneIntel.py")


# =========================================
# PHASE 2: TURBO MATRIX PLAN TIER (07-14)
# =========================================
st.markdown("<div class='phase-title'>Phase 2: Turbo Matrix Plan Tier (07-14)</div>", unsafe_allow_html=True)

phase2_projects = [
    ("AutoSched Linear Matcher", "07_TRB_AutoSched.py"),
    ("TriHaul Loop Architect", "08_TRB_TriHaul.py"),
    ("RouteTSP Sequencer", "09_TRB_RouteTSP.py"),
    ("NegotiatePro Simulator", "10_TRB_NegotiatePro.py"),
    ("SpatialPack LTL Solver", "11_TRB_SpatialPack.py"),
    ("EcoRoute Tax Optimizer", "12_TRB_EcoRoute.py"),
    ("RateConParser Matrix", "13_TRB_RateConParser.py"),
    ("DispatchFlow Comm Hub", "14_TRB_DispatchFlow.py")
]

idx_p2 = 7
# 3 کے گروپس میں ڈیوائیڈ کرنا
for i in range(0, len(phase2_projects), 3):
    cols_p2 = st.columns(3)
    for j in range(3):
        if i + j < len(phase2_projects):
            title, fname = phase2_projects[i+j]
            with cols_p2[j]:
                st.markdown(f"""<div class='feature-card'><span class='sec-id'>SEC-PROD-{idx_p2:02d}</span><h3>{title}</h3><p>The matrix optimization engine executing mathematical models to enhance fleet yield margins dynamically.</p><span class='impact-tag' style='color:#00E676;'>Market Ready: 95%</span><div class='progress-ui'><div class='progress-fill' style='width:95%; background:#00E676;'></div></div></div>""", unsafe_allow_html=True)
                if st.button(f"Launch {title.split()[0]}", key=f"btn_{idx_p2}", use_container_width=True):
                    launch_project_page(fname)
            idx_p2 += 1


# =========================================
# PHASE 3: ENTERPRISE PRO SUITE (15-36)
# =========================================
st.markdown("<div class='phase-title'>Phase 3: Enterprise Pro Plan - Logistics Infrastructure (15-36)</div>", unsafe_allow_html=True)

remaining_projects = [
    ("Appoint Track", "15_ENT_AppointTrack.py"), ("Geo Fence", "16_ENT_GeoFence.py"), 
    ("Maintenance", "17_ENT_Maintenance.py"), ("Safe Drive", "18_ENT_SafeDrive.py"), 
    ("Cargo Guard", "19_ENT_CargoGuard.py"), ("Bill Swift", "20_ENT_BillSwift.py"),
    ("Claim Shield", "21_ENT_ClaimShield.py"), ("Lane Predict", "22_ENT_LanePredict.py"), 
    ("Yard Master", "23_ENT_YardMaster.py"), ("Blacklist", "24_ENT_Blacklist.py"), 
    ("Driver Pay", "25_ENT_DriverPay.py"), ("Multi Modal", "26_ENT_MultiModal.py"),
    ("Detention", "27_ENT_Detention.py"), ("Fuel Hedge", "28_ENT_FuelHedge.py"), 
    ("Border Pass", "29_ENT_BorderPass.py"), ("Intercom", "30_ENT_Intercom.py"), 
    ("IFTA", "31_ENT_IFTA.py"), ("Pod Scanner", "32_ENT_PodScanner.py"),
    ("Weather", "33_ENT_Weather.py"), ("Broker CRM", "34_ENT_BrokerCRM.py"), 
    ("Escrow", "35_ENT_Escrow.py"), ("Master Control", "36_ENT_MasterControl.py")
]

idx_p3 = 15
for i in range(0, len(remaining_projects), 3):
    cols_p3 = st.columns(3)
    for j in range(3):
        if i + j < len(remaining_projects):
            title, fname = remaining_projects[i+j]
            with cols_p3[j]:
                st.markdown(f"""<div class='feature-card'><span class='sec-id'>SEC-PROD-{idx_p3:02d}</span><h3>{title} Engine</h3><p>Enterprise level real-time operations engine executing deep-matrix algorithms to synchronize core data pipelines.</p><span class='impact-tag' style='color:#EA80FC;'>Market Ready: 98%</span><div class='progress-ui'><div class='progress-fill' style='width:98%; background:#EA80FC;'></div></div></div>""", unsafe_allow_html=True)
                if st.button(f"Launch {title}", key=f"btn_{idx_p3}", use_container_width=True):
                    launch_project_page(fname)
            idx_p3 += 1
