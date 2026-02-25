import streamlit as st
from dataclasses import dataclass
from typing import List, Optional, Tuple
import requests

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Trustworthy AI Showcases",
    page_icon="🛡️",
    layout="wide",
)

# ----------------------------
# VINNOVA project + logo (public page)
# ----------------------------
PROJECT_URL = "https://www.vinnova.se/en/p/trustworthy-ai-and-mobile-generative-ai-for-6g-networks-and-smart-industry-applications/"
PROJECT_REF = "2024-03570"
VINNOVA_LOGO_URL = (
    "https://www.vinnova.se/globalassets/mikrosajter/nyhetsrum/bilder/logotyp/"
    "vinnova_green_payoff_eng_rgb.png"
)

# ----------------------------
# Data model
# ----------------------------
@dataclass
class Demo:
    title: str
    subtitle: str
    url: str
    tags: List[str]
    icon: str = "✨"
    status: str = "Live"  # Live / Demo / Beta / Coming Soon
    image_url: Optional[str] = None


DEMOS: List[Demo] = [
    Demo(
        title="Wireless Trust AI",
        subtitle="Trustworthy AI for wireless systems — robustness, reliability, and practical evaluation views.",
        url="https://wirelesstrustai.streamlit.app/",
        tags=["Wireless AI", "6G", "Robustness", "Trustworthiness"],
        icon="📡",
        status="Live",
    ),
]

primary = next((d for d in DEMOS if d.status.lower() == "live"), DEMOS[0])

# ----------------------------
# Caching helpers (speed)
# ----------------------------
@st.cache_data(show_spinner=False)
def get_all_tags(demos: List[Demo]) -> List[str]:
    return sorted({t for d in demos for t in d.tags})

@st.cache_data(show_spinner=False)
def filter_demos(demos: List[Demo], query: str, tag_filter: Tuple[str, ...], sort_by: str) -> List[Demo]:
    q = (query or "").strip().lower()
    tf = set(tag_filter) if tag_filter else set()

    def matches(d: Demo) -> bool:
        if q:
            blob = " ".join([d.title, d.subtitle, " ".join(d.tags), d.status]).lower()
            if q not in blob:
                return False
        if tf and not tf.issubset(set(d.tags)):
            return False
        return True

    out = [d for d in demos if matches(d)]

    status_rank = {"Live": 0, "Demo": 1, "Beta": 2, "Coming Soon": 3}
    if sort_by == "Title A→Z":
        out.sort(key=lambda x: x.title.lower())
    elif sort_by == "Status":
        out.sort(key=lambda x: status_rank.get(x.status, 99))

    return out

@st.cache_data(show_spinner=False)
def fetch_logo_bytes(url: str) -> bytes:
    # Cache the remote logo once per Streamlit container
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.content

# ----------------------------
# Premium styling (same as before)
# ----------------------------
st.markdown(
    """
<style>
.block-container { max-width: 1180px; padding-top: 1.0rem; padding-bottom: 2.3rem; }
header, footer, #MainMenu { visibility: hidden; height: 0px; }

html, body, [class*="css"] { font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; }
h1, h2, h3 { letter-spacing: -0.03em; }
p { color: rgba(71,85,105,1); }

.navbar { display:flex; align-items:center; justify-content:space-between; padding: 6px 0 18px 0; }
.brand { display:flex; gap:10px; align-items:center; }
.brand-title { font-weight: 850; font-size: 1.05rem; color: rgba(15,23,42,1); }
.brand-sub { font-size: 0.92rem; color: rgba(100,116,139,1); margin-top: 1px; }

a.btnPrimary {
  display:inline-flex; align-items:center; justify-content:center;
  padding: 10px 14px; border-radius: 12px;
  background: rgba(15,23,42,1);
  border: 1px solid rgba(15,23,42,1);
  color: white !important; font-weight: 750;
  text-decoration: none !important;
}
a.btnPrimary:hover { opacity: 0.93; }

a.btnSoft {
  display:inline-flex; align-items:center; justify-content:center;
  padding: 10px 14px; border-radius: 12px;
  background: rgba(15,23,42,0.04);
  border: 1px solid rgba(148,163,184,0.28);
  color: rgba(15,23,42,1) !important; font-weight: 750;
  text-decoration: none !important;
}
a.btnSoft:hover { background: rgba(15,23,42,0.06); }

.hero {
  border-radius: 24px;
  padding: 38px 36px 30px 36px;
  border: 1px solid rgba(148,163,184,0.22);
  background:
    radial-gradient(1200px 520px at 12% 8%, rgba(59,130,246,0.26), transparent 58%),
    radial-gradient(900px 560px at 88% 28%, rgba(16,185,129,0.22), transparent 55%),
    linear-gradient(180deg, rgba(255,255,255,0.78), rgba(255,255,255,0.48));
  box-shadow: 0 18px 60px rgba(2,6,23,0.08);
}
.hero h1 { margin: 0; font-size: 2.7rem; line-height: 1.07; color: rgba(15,23,42,1); }
.hero p { margin: 12px 0 0 0; font-size: 1.06rem; max-width: 56rem; }

.pills { margin-top: 18px; display:flex; flex-wrap:wrap; gap:10px; }
.pill {
  display:inline-flex; gap:8px; align-items:center;
  padding: 7px 12px; border-radius: 999px;
  background: rgba(15,23,42,0.05);
  border: 1px solid rgba(148,163,184,0.22);
  color: rgba(30,41,59,1);
  font-size: 0.88rem;
}

.sectionTitle { margin-top: 28px; margin-bottom: 8px; font-size: 1.35rem; font-weight: 880; color: rgba(15,23,42,1); }
.sectionSub { margin-top: 0; margin-bottom: 14px; color: rgba(100,116,139,1); }

.card {
  border-radius: 20px;
  padding: 18px 18px 16px 18px;
  border: 1px solid rgba(148,163,184,0.20);
  background: rgba(255,255,255,0.76);
  box-shadow: 0 12px 36px rgba(2,6,23,0.06);
}
.cardFlat {
  border-radius: 18px;
  padding: 16px;
  border: 1px solid rgba(148,163,184,0.20);
  background: rgba(255,255,255,0.78);
}

.badgeLive {
  display:inline-block;
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 0.86rem;
  border: 1px solid rgba(16,185,129,0.35);
  background: rgba(16,185,129,0.12);
  color: rgba(15,23,42,1);
  font-weight: 850;
}
.tag {
  display:inline-block;
  padding: 4px 9px;
  border-radius: 999px;
  margin: 8px 8px 0 0;
  background: rgba(99,102,241,0.08);
  border: 1px solid rgba(99,102,241,0.14);
  font-size: 0.80rem;
  color: rgba(30,41,59,1);
}

.metric {
  border-radius: 18px;
  padding: 14px 14px 12px 14px;
  border: 1px solid rgba(148,163,184,0.18);
  background: rgba(15,23,42,0.03);
}
.metricK { font-weight: 900; color: rgba(15,23,42,1); font-size: 1.05rem; }
.metricV { color: rgba(100,116,139,1); font-size: 0.92rem; margin-top: 2px; }

.fundingWrap { margin-top: 40px; padding-top: 18px; border-top: 1px solid rgba(148,163,184,0.22); }
.fundingTitle { text-align:center; font-weight: 880; color: rgba(15,23,42,1); font-size: 1.02rem; }
.fundingText { text-align:center; margin-top:6px; color: rgba(100,116,139,1); font-size: 0.92rem; }
.fundingLink a { color: rgba(15,23,42,1); font-weight: 800; text-decoration: none !important; }
.fundingLink a:hover { opacity: 0.92; }

.footerline {
  margin-top: 22px;
  padding-top: 14px;
  border-top: 1px solid rgba(148,163,184,0.18);
  color: rgba(100,116,139,1);
  font-size: 0.92rem;
  text-align:center;
}
</style>
""",
    unsafe_allow_html=True,
)

def tags_html(tags: List[str]) -> str:
    return "".join([f"<span class='tag'>{t}</span>" for t in tags])

# ----------------------------
# Navbar
# ----------------------------
st.markdown(
    f"""
<div class="navbar">
  <div class="brand">
    <div style="font-size:1.25rem;">🛡️</div>
    <div>
      <div class="brand-title">Trustworthy AI Showcases</div>
      <div class="brand-sub">Modern demo hub • Research & industry ready</div>
    </div>
  </div>
  <div style="display:flex; gap:10px; align-items:center;">
    <a class="btnSoft" href="#catalog">Browse demos</a>
    <a class="btnPrimary" href="{primary.url}" target="_blank">Open {primary.title} →</a>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ----------------------------
# Hero
# ----------------------------
st.markdown(
    """
<div class="hero">
  <h1>Trustworthy AI — explained through interactive demos</h1>
  <p>
    A research-lab style showcase hub: clean storytelling, premium visuals, and stakeholder-friendly navigation.
    Built to scale from one demo today to many demos tomorrow.
  </p>
  <div class="pills">
    <span class="pill">🛡️ Robustness</span>
    <span class="pill">🔎 Transparency</span>
    <span class="pill">🔐 Security</span>
    <span class="pill">⚙️ Evaluation</span>
    <span class="pill">📡 Wireless / 6G</span>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ----------------------------
# Metrics
# ----------------------------
st.markdown("<div class='sectionTitle'>At a glance</div>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown("<div class='metric'><div class='metricK'>Live demos</div><div class='metricV'>Growing showcase catalog</div></div>", unsafe_allow_html=True)
with m2:
    st.markdown("<div class='metric'><div class='metricK'>Focus</div><div class='metricV'>Trust • Robustness • Security</div></div>", unsafe_allow_html=True)
with m3:
    st.markdown("<div class='metric'><div class='metricK'>Domain</div><div class='metricV'>Wireless / 6G & Smart industry</div></div>", unsafe_allow_html=True)
with m4:
    st.markdown("<div class='metric'><div class='metricK'>Format</div><div class='metricV'>Interactive Streamlit apps</div></div>", unsafe_allow_html=True)

# ----------------------------
# Featured demo
# ----------------------------
st.markdown("<div class='sectionTitle'>Featured demo</div>", unsafe_allow_html=True)
st.markdown("<div class='sectionSub'>The primary live showcase. More demos will be added over time.</div>", unsafe_allow_html=True)

left, right = st.columns([1.7, 1])
with left:
    st.markdown(
        f"""
<div class="card">
  <span class="badgeLive">{primary.status}</span>
  <h2 style="margin:10px 0 6px 0;">{primary.icon} {primary.title}</h2>
  <p style="margin:0 0 10px 0;">{primary.subtitle}</p>
  {tags_html(primary.tags)}
</div>
""",
        unsafe_allow_html=True,
    )

with right:
    st.link_button("🚀 Launch demo", primary.url, use_container_width=True)
    st.write("")
    st.markdown(
        """
<div class="cardFlat">
  <b>What you’ll see</b>
  <div style="margin-top:6px; color: rgba(100,116,139,1); font-size:0.92rem;">
    Robustness views • Practical evaluation • Clear, stakeholder-friendly outputs
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

# ----------------------------
# Catalog (fast + premium list)
# ----------------------------
st.markdown("<div id='catalog'></div>", unsafe_allow_html=True)
st.markdown("<div class='sectionTitle'>Demo catalog</div>", unsafe_allow_html=True)
st.markdown("<div class='sectionSub'>Search and open demos (filters are optional).</div>", unsafe_allow_html=True)

# Use session state for stable UX
if "catalog_query" not in st.session_state:
    st.session_state.catalog_query = ""
if "catalog_tags" not in st.session_state:
    st.session_state.catalog_tags = []
if "catalog_sort" not in st.session_state:
    st.session_state.catalog_sort = "Featured"

# Search form avoids rerun per keypress
with st.form("catalog_search", clear_on_submit=False):
    q = st.text_input("Search", value=st.session_state.catalog_query, placeholder="Search demos…", label_visibility="collapsed")
    submitted = st.form_submit_button("Search")

if submitted:
    st.session_state.catalog_query = q

with st.expander("Advanced filters", expanded=False):
    all_tags = get_all_tags(DEMOS)
    t = st.multiselect("Filter by tags", all_tags, default=st.session_state.catalog_tags, placeholder="Filter by tags…")
    s = st.selectbox("Sort", ["Featured", "Title A→Z", "Status"], index=["Featured", "Title A→Z", "Status"].index(st.session_state.catalog_sort))
    apply_filters = st.button("Apply filters")
    if apply_filters:
        st.session_state.catalog_tags = t
        st.session_state.catalog_sort = s

filtered = filter_demos(
    DEMOS,
    st.session_state.catalog_query,
    tuple(st.session_state.catalog_tags),
    st.session_state.catalog_sort,
)

if not filtered:
    st.info("No demos match your search/filters.")
else:
    for demo in filtered:
        status_bg = "rgba(16,185,129,0.12)" if demo.status.lower() == "live" else "rgba(15,23,42,0.06)"
        status_border = "rgba(16,185,129,0.35)" if demo.status.lower() == "live" else "rgba(148,163,184,0.25)"

        st.markdown(
            f"""
<div style="
  border-radius: 20px;
  padding: 16px 18px;
  border: 1px solid rgba(148,163,184,0.20);
  background: rgba(255,255,255,0.78);
  box-shadow: 0 12px 30px rgba(2,6,23,0.06);
  margin-bottom: 12px;
">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:14px; flex-wrap:wrap;">
    <div style="min-width: 260px; flex: 1;">
      <div style="display:flex; align-items:center; gap:10px;">
        <div style="font-weight:900; color: rgba(15,23,42,1); font-size: 1.05rem;">
          {demo.icon} {demo.title}
        </div>
        <span style="
          display:inline-block;
          padding: 5px 10px;
          border-radius: 999px;
          font-size: 0.82rem;
          font-weight: 800;
          background: {status_bg};
          border: 1px solid {status_border};
          color: rgba(15,23,42,1);
        ">{demo.status}</span>
      </div>

      <div style="color: rgba(100,116,139,1); font-size: 0.95rem; margin-top: 6px;">
        {demo.subtitle}
      </div>

      <div style="margin-top: 10px;">
        {tags_html(demo.tags)}
      </div>
    </div>

    <div style="display:flex; align-items:center; gap:10px;">
      <a class="btnPrimary" href="{demo.url}" target="_blank">Open demo →</a>
      <a class="btnSoft" href="{demo.url}" target="_blank">Share</a>
    </div>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )

# ----------------------------
# Funding acknowledgement (VINNOVA only) — centered + cached logo
# ----------------------------
logo_bytes = fetch_logo_bytes(VINNOVA_LOGO_URL)

st.markdown(
    f"""
<div class="fundingWrap">
  <div class="fundingTitle">Funding acknowledgement</div>
  <div class="fundingText">
    This demo hub is supported by VINNOVA (Sweden’s Innovation Agency).
    Project reference: <b>{PROJECT_REF}</b>.
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("<div style='text-align:center; margin-top:18px;'>", unsafe_allow_html=True)
st.image(logo_bytes, width=320)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    f"""
<div class="fundingText fundingLink" style="margin-top:14px;">
  <a href="{PROJECT_URL}" target="_blank">View the official VINNOVA project page →</a>
</div>
""",
    unsafe_allow_html=True,
)

# ----------------------------
# Footer (maintained by you)
# ----------------------------
st.markdown(
    """
<div class="footerline">
  Trustworthy AI Demo Hub — Developed and maintained by Kyi Thar • Contact: kyi.thar@miun.se
</div>
""",
    unsafe_allow_html=True,
)
