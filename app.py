import streamlit as st
from dataclasses import dataclass
from typing import List, Optional, Tuple
import math
import requests
import base64
from textwrap import dedent

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
# KKS (KK-stiftelsen) project + logo
# ----------------------------
KKS_URL = "https://www.kks.se/"
KKS_LOGO_URL = "https://cdn-assets-cloud.frontify.com/s3/frontify-cloud-files-us/eyJwYXRoIjoiZnJvbnRpZnlcL2FjY291bnRzXC8zYVwvMjMxNjAwXC9wcm9qZWN0c1wvMzI5NjQzXC9hc3NldHNcLzYzXC82NDI0MjY1XC9iODhmN2Y5MDdkMTQ0MTJjODgxZjk0MzdjMTM1ODFhNS0xNjQ4NzIxNTAwLnBuZyJ9:frontify:Q0D4l2_6vfsqaiMfn-YmeMLwtvU7PqDgSgsNsf3o9aM"

# ----------------------------
# Interreg Aurora project + logo
# ----------------------------
AURORA_URL = "https://www.miun.se/en/Research/research-projects/ongoing-research-projects/trust---enhancing-wireless-communication--sensing-with-secure-resilient-and-trustworthy-solutions/"
AURORA_LOGO_URL = "https://www.interregaurora.eu/wp-content/uploads/AURORA-RGB-Color-1-1024x308.png"

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
    title="TrustAI Explain",
    subtitle="Interactive explainability demo for trustworthy AI, focused on transparent and interpretable model behavior.",
    url="https://trustaiexplain.streamlit.app/",
    tags=["Explainability", "Trustworthy AI", "Transparency"],
    icon="🧠",
    status="Live",
  ),
  Demo(
    title="AI for Leaders (Book)",
    subtitle="Practical guide for leaders on AI adoption, strategy, and responsible AI in real-world organizations.",
    url="https://khukt.github.io/AI-for-Leaders/",
    tags=["AI Leadership", "Education", "Responsible AI"],
    icon="📘",
    status="Live",
  ),
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
:root {
  --text-strong: rgba(15,23,42,1);
  --text-soft: rgba(100,116,139,1);
  --line-soft: rgba(148,163,184,0.22);
  --card-bg: rgba(255,255,255,0.82);
}

.stApp {
  background:
    radial-gradient(1000px 520px at 8% -8%, rgba(59,130,246,0.10), transparent 62%),
    radial-gradient(900px 520px at 92% 8%, rgba(16,185,129,0.10), transparent 58%),
    linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
}

.block-container { max-width: 1220px; padding-top: 1.4rem; padding-bottom: 2.8rem; }
header, footer, #MainMenu { visibility: hidden; height: 0px; }

html, body, [class*="css"] { font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; }
h1, h2, h3 { letter-spacing: -0.03em; }
p { color: rgba(71,85,105,1); }

.navbar {
  display:flex; align-items:center; justify-content:space-between;
  padding: 12px 16px;
  margin-bottom: 18px;
  border-radius: 16px;
  border: 1px solid rgba(148,163,184,0.24);
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(8px);
  box-shadow: 0 8px 28px rgba(2,6,23,0.05);
}
.brand { display:flex; gap:10px; align-items:center; }
.brand-title { font-weight: 860; font-size: 1.12rem; color: rgba(15,23,42,1); }
.brand-sub { font-size: 0.92rem; color: rgba(100,116,139,1); margin-top: 1px; }

a.btnPrimary {
  display:inline-flex; align-items:center; justify-content:center;
  padding: 11px 16px; border-radius: 14px;
  background: rgba(15,23,42,1);
  border: 1px solid rgba(15,23,42,1);
  color: white !important; font-weight: 780;
  text-decoration: none !important;
  transition: transform 140ms ease, box-shadow 140ms ease, opacity 140ms ease;
}
a.btnPrimary:hover { opacity: 0.95; transform: translateY(-1px); box-shadow: 0 10px 22px rgba(2,6,23,0.16); }

a.btnPrimary, a.btnSoft { white-space: nowrap; }

a.btnSoft {
  display:inline-flex; align-items:center; justify-content:center;
  padding: 11px 16px; border-radius: 14px;
  background: rgba(15,23,42,0.04);
  border: 1px solid rgba(148,163,184,0.28);
  color: rgba(15,23,42,1) !important; font-weight: 760;
  text-decoration: none !important;
  transition: transform 140ms ease, background 140ms ease;
}
a.btnSoft:hover { background: rgba(15,23,42,0.08); transform: translateY(-1px); }

.hero {
  border-radius: 28px;
  padding: 48px 40px 36px 40px;
  border: 1px solid rgba(148,163,184,0.22);
  background:
    radial-gradient(1200px 520px at 12% 8%, rgba(59,130,246,0.30), transparent 58%),
    radial-gradient(900px 560px at 88% 28%, rgba(16,185,129,0.25), transparent 55%),
    linear-gradient(180deg, rgba(255,255,255,0.86), rgba(255,255,255,0.56));
  box-shadow: 0 22px 66px rgba(2,6,23,0.11);
}
.hero h1 { margin: 0; font-size: 3.0rem; line-height: 1.03; color: rgba(15,23,42,1); }
.hero p { margin: 14px 0 0 0; font-size: 1.1rem; line-height: 1.7; max-width: 58rem; }

.heroEyebrow {
  display:inline-flex;
  align-items:center;
  gap:8px;
  margin-bottom: 12px;
  padding: 7px 13px;
  border-radius: 999px;
  background: rgba(15,23,42,0.08);
  border: 1px solid rgba(148,163,184,0.24);
  font-size: 0.84rem;
  color: var(--text-strong);
  font-weight: 760;
}

.pills { margin-top: 20px; display:flex; flex-wrap:wrap; gap:10px; }
.pill {
  display:inline-flex; gap:8px; align-items:center;
  padding: 8px 13px; border-radius: 999px;
  background: rgba(15,23,42,0.05);
  border: 1px solid rgba(148,163,184,0.22);
  color: rgba(30,41,59,1);
  font-size: 0.9rem;
  transition: transform 140ms ease, background 140ms ease;
}
.pill:hover { transform: translateY(-1px); background: rgba(15,23,42,0.08); }

.sectionTitle { margin-top: 36px; margin-bottom: 10px; font-size: 1.52rem; font-weight: 890; color: rgba(15,23,42,1); }
.sectionSub { margin-top: 0; margin-bottom: 18px; color: rgba(100,116,139,1); font-size: 0.98rem; }

.card {
  border-radius: 22px;
  padding: 22px 22px 20px 22px;
  border: 1px solid rgba(148,163,184,0.20);
  background: rgba(255,255,255,0.76);
  box-shadow: 0 12px 36px rgba(2,6,23,0.06);
  transition: transform 150ms ease, box-shadow 150ms ease;
}
.card:hover { transform: translateY(-2px); box-shadow: 0 16px 36px rgba(2,6,23,0.08); }

.featuredCard {
  position: relative;
  overflow: hidden;
  background:
    radial-gradient(600px 220px at 12% 8%, rgba(99,102,241,0.10), transparent 62%),
    linear-gradient(180deg, rgba(255,255,255,0.90), rgba(255,255,255,0.80));
}

.featuredCard::after {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  width: 120px;
  height: 120px;
  background: radial-gradient(circle at top right, rgba(16,185,129,0.15), transparent 70%);
  pointer-events: none;
}

.featuredKicker {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-left: 8px;
  padding: 6px 11px;
  border-radius: 999px;
  border: 1px solid rgba(99,102,241,0.24);
  background: rgba(99,102,241,0.10);
  color: rgba(30,41,59,1);
  font-size: 0.8rem;
  font-weight: 760;
}

.featuredTitle {
  margin: 16px 0 8px 0;
  font-size: 2.9rem;
  line-height: 1.1;
  color: var(--text-strong);
}

.featuredSub {
  margin: 0 0 10px 0;
  color: var(--text-soft);
  font-size: 1rem;
  line-height: 1.65;
}

.featuredActions {
  margin-top: 16px;
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.featureList {
  margin-top: 10px;
  padding-left: 18px;
  color: rgba(71,85,105,1);
}

.featureList li {
  margin: 7px 0;
}

.cardActions {
  display:flex;
  align-items:center;
  gap:10px;
  flex-wrap:wrap;
}

@media (max-width: 900px) {
  .hero h1 { font-size: 2.05rem; }
  .cardActions { width: 100%; }
  .cardActions a { flex: 1; text-align: center; }
}
.cardFlat {
  border-radius: 20px;
  padding: 18px;
  border: 1px solid rgba(148,163,184,0.20);
  background: rgba(255,255,255,0.78);
}

.badgeLive {
  display:inline-block;
  padding: 6px 13px;
  border-radius: 999px;
  font-size: 0.84rem;
  border: 1px solid rgba(16,185,129,0.35);
  background: rgba(16,185,129,0.12);
  color: rgba(15,23,42,1);
  font-weight: 850;
}
.tag {
  display:inline-block;
  padding: 5px 10px;
  border-radius: 999px;
  margin: 10px 8px 0 0;
  background: rgba(99,102,241,0.08);
  border: 1px solid rgba(99,102,241,0.14);
  font-size: 0.81rem;
  color: rgba(30,41,59,1);
  transition: background 120ms ease, border-color 120ms ease;
}
.tag:hover { background: rgba(99,102,241,0.14); border-color: rgba(99,102,241,0.24); }

.catalogCard {
  border-radius: 22px;
  padding: 20px;
  border: 1px solid rgba(148,163,184,0.20);
  background: rgba(255,255,255,0.90);
  box-shadow: 0 12px 30px rgba(2,6,23,0.06);
  margin-bottom: 16px;
  transition: transform 150ms ease, box-shadow 150ms ease, border-color 150ms ease;
}
.catalogCard:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 34px rgba(2,6,23,0.09);
  border-color: rgba(99,102,241,0.24);
}
.catalogTop {
  display:flex;
  justify-content:space-between;
  align-items:center;
  gap:10px;
  flex-wrap:wrap;
}
.catalogTitle {
  font-weight:900;
  font-size:1.16rem;
  color: var(--text-strong);
}
.statusBadge {
  padding:5px 10px;
  border-radius:999px;
  font-size:0.8rem;
  font-weight:800;
}
.statusLive {
  background: rgba(16,185,129,0.12);
  border: 1px solid rgba(16,185,129,0.35);
}
.statusNeutral {
  background: rgba(15,23,42,0.06);
  border: 1px solid rgba(148,163,184,0.25);
}
.catalogSubtitle { color: var(--text-soft); margin-top: 10px; font-size: 0.99rem; line-height: 1.6; }
.catalogTags { margin-top: 13px; }
.catalogActions {
  margin-top: 18px;
  display:flex;
  gap:12px;
  flex-wrap: wrap;
}

.catalogToolbar {
  margin: 4px 0 12px 0;
  color: var(--text-soft);
  font-size: 0.92rem;
}

.compactRow {
  border: 1px solid rgba(148,163,184,0.20);
  background: rgba(255,255,255,0.92);
  border-radius: 16px;
  padding: 12px 14px;
  margin-bottom: 10px;
}

.compactTop {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  flex-wrap: wrap;
}

.compactTitle {
  font-weight: 860;
  color: var(--text-strong);
  font-size: 1.03rem;
}

.compactSubtitle {
  margin-top: 6px;
  color: var(--text-soft);
  font-size: 0.93rem;
}

.compactTags {
  margin-top: 8px;
}

.compactActions {
  margin-top: 10px;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.metric {
  border-radius: 18px;
  padding: 14px 14px 12px 14px;
  border: 1px solid rgba(148,163,184,0.18);
  background: rgba(15,23,42,0.03);
}
.metricK { font-weight: 900; color: rgba(15,23,42,1); font-size: 1.05rem; }
.metricV { color: rgba(100,116,139,1); font-size: 0.92rem; margin-top: 2px; }

.fundingWrap { margin-top: 46px; padding-top: 20px; border-top: 1px solid rgba(148,163,184,0.22); }
.fundingTitle { text-align:center; font-weight: 880; color: rgba(15,23,42,1); font-size: 1.08rem; }
.fundingText { text-align:center; margin-top:8px; color: rgba(100,116,139,1); font-size: 0.96rem; }
.fundingLink a { color: rgba(15,23,42,1); font-weight: 800; text-decoration: none !important; }
.fundingLink a:hover { opacity: 0.92; }

.fundingLogoSlot {
  margin-top: 18px;
  height: 140px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.fundingLogo {
  display: block;
  width: auto;
  max-width: 100%;
  object-fit: contain;
}
.fundingLogo.vinnova { height: 100px; }
.fundingLogo.kks { height: 122px; }
.fundingLogo.aurora { height: 82px; }

.fundingGrid {
  margin-top: 14px;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
}

.fundingItem {
  border: 1px solid rgba(148,163,184,0.20);
  border-radius: 16px;
  background: rgba(255,255,255,0.68);
  padding: 10px 12px 12px 12px;
}

@media (max-width: 900px) {
  .fundingGrid { grid-template-columns: 1fr; gap: 10px; }
  .fundingLogoSlot { height: 118px; }
  .fundingLogo.vinnova { height: 84px; }
  .fundingLogo.kks { height: 102px; }
  .fundingLogo.aurora { height: 70px; }
}

.footerline {
  margin-top: 30px;
  padding-top: 14px;
  border-top: 1px solid rgba(148,163,184,0.18);
  color: rgba(100,116,139,1);
  font-size: 0.94rem;
  text-align:center;
}

@media (max-width: 900px) {
  .hero {
    padding: 34px 24px 26px 24px;
    border-radius: 22px;
  }
  .hero h1 { font-size: 2.3rem; line-height: 1.08; }
  .hero p { font-size: 1.0rem; line-height: 1.62; }
  .sectionTitle { margin-top: 28px; font-size: 1.34rem; }
  .sectionSub { font-size: 0.94rem; }
  .catalogCard { padding: 16px; }
  .catalogTitle { font-size: 1.05rem; }
}
</style>
""",
    unsafe_allow_html=True,
)

def render_html(html: str) -> None:
  st.markdown(dedent(html).strip(), unsafe_allow_html=True)

def tags_html(tags: List[str]) -> str:
    return "".join([f"<span class='tag'>{t}</span>" for t in tags])

def logo_src(url: str, logo_bytes: Optional[bytes]) -> str:
  if logo_bytes:
    b64 = base64.b64encode(logo_bytes).decode("ascii")
    return f"data:image/png;base64,{b64}"
  return url

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
  <div class="heroEyebrow">✨ Curated demo hub</div>
  <h1>Trustworthy AI — explained through interactive demos</h1>
  <p>
    Trustworthy AI refers to intelligent systems that are robust under uncertainty, transparent in their decision-making,
    secure against manipulation, and reliable in mission-critical environments.
    This interactive showcase translates these principles into practical evaluation frameworks for next-generation wireless and industrial AI systems.
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
# Featured demo
# ----------------------------
st.markdown("<div class='sectionTitle'>Featured demo</div>", unsafe_allow_html=True)
st.markdown("<div class='sectionSub'>The primary live showcase. More demos will be added over time.</div>", unsafe_allow_html=True)

left, right = st.columns([1.7, 1])
with left:
    render_html(
        f"""
        <div class="card featuredCard">
          <span class="badgeLive">{primary.status}</span>
          <span class="featuredKicker">🌟 Featured now</span>
          <h2 class="featuredTitle">{primary.icon} {primary.title}</h2>
          <p class="featuredSub">{primary.subtitle}</p>
          {tags_html(primary.tags)}
          <div class="featuredActions">
            <a class="btnPrimary" href="{primary.url}" target="_blank">Launch featured demo →</a>
            <a class="btnSoft" href="#catalog">Browse all demos</a>
          </div>
        </div>
        """
    )

with right:
    render_html(
        """
        <div class="cardFlat">
          <b>Why this is featured</b>
          <ul class="featureList">
            <li>Interactive and intuitive for first-time visitors</li>
            <li>Demonstrates core Trustworthy AI principles</li>
            <li>Useful for research, education, and stakeholder communication</li>
          </ul>
        </div>
        <div style="height:12px;"></div>
        <div class="cardFlat">
          <b>What you’ll see</b>
          <ul class="featureList">
            <li>Transparency and explainability views</li>
            <li>Practical evaluation workflow</li>
            <li>Clear outputs for technical and non-technical users</li>
          </ul>
        </div>
        """
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
if "catalog_view" not in st.session_state:
  st.session_state.catalog_view = "Compact"
if "catalog_page_size" not in st.session_state:
  st.session_state.catalog_page_size = 10
if "catalog_page" not in st.session_state:
  st.session_state.catalog_page = 1

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
    c_info, c_view, c_size, c_page = st.columns([1.8, 1, 1, 1])
    with c_info:
        st.markdown(
            f"<div class='catalogToolbar'>Showing <b>{len(filtered)}</b> demos</div>",
            unsafe_allow_html=True,
        )
    with c_view:
        view_mode = st.selectbox(
            "View",
            ["Compact", "Cards"],
            index=["Compact", "Cards"].index(st.session_state.catalog_view),
        )
    with c_size:
        page_size = st.selectbox(
            "Per page",
            [10, 20, 50],
            index=[10, 20, 50].index(st.session_state.catalog_page_size),
        )

    st.session_state.catalog_view = view_mode
    st.session_state.catalog_page_size = page_size

    total_pages = max(1, math.ceil(len(filtered) / st.session_state.catalog_page_size))
    if st.session_state.catalog_page > total_pages:
        st.session_state.catalog_page = total_pages

    with c_page:
        st.session_state.catalog_page = int(
            st.number_input(
                "Page",
                min_value=1,
                max_value=total_pages,
                value=st.session_state.catalog_page,
                step=1,
            )
        )

    start_idx = (st.session_state.catalog_page - 1) * st.session_state.catalog_page_size
    end_idx = start_idx + st.session_state.catalog_page_size
    page_items = filtered[start_idx:end_idx]

    st.markdown(
        f"<div class='catalogToolbar'>Page <b>{st.session_state.catalog_page}</b> of <b>{total_pages}</b></div>",
        unsafe_allow_html=True,
    )

    for demo in page_items:
        status_class = "statusLive" if demo.status.lower() == "live" else "statusNeutral"

        if st.session_state.catalog_view == "Cards":
            html = f"""
        <div class="catalogCard">
          <div class="catalogTop">
            <div class="catalogTitle">
              {demo.icon} {demo.title}
            </div>
            <span class="statusBadge {status_class}">
              {demo.status}
            </span>
          </div>

          <div class="catalogSubtitle">
            {demo.subtitle}
          </div>

          <div class="catalogTags">
            {tags_html(demo.tags)}
          </div>

          <div class="catalogActions">
            <a class="btnPrimary" href="{demo.url}" target="_blank">Open demo →</a>
            <a class="btnSoft" href="{demo.url}" target="_blank">Visit page</a>
          </div>
        </div>
        """
        else:
            html = f"""
        <div class="compactRow">
          <div class="compactTop">
            <div class="compactTitle">{demo.icon} {demo.title}</div>
            <span class="statusBadge {status_class}">{demo.status}</span>
          </div>
          <div class="compactSubtitle">{demo.subtitle}</div>
          <div class="compactTags">{tags_html(demo.tags)}</div>
          <div class="compactActions">
            <a class="btnPrimary" href="{demo.url}" target="_blank">Open demo →</a>
            <a class="btnSoft" href="{demo.url}" target="_blank">Visit page</a>
          </div>
        </div>
        """

        st.markdown(html, unsafe_allow_html=True)

# ----------------------------
# Funding acknowledgement (VINNOVA + KKS) — centered + cached logos
# ----------------------------
vinnova_logo_bytes: Optional[bytes] = None
try:
  vinnova_logo_bytes = fetch_logo_bytes(VINNOVA_LOGO_URL)
except Exception:
  vinnova_logo_bytes = None

kks_logo_bytes: Optional[bytes] = None
try:
  kks_logo_bytes = fetch_logo_bytes(KKS_LOGO_URL)
except Exception:
  kks_logo_bytes = None

aurora_logo_bytes: Optional[bytes] = None
try:
  aurora_logo_bytes = fetch_logo_bytes(AURORA_LOGO_URL)
except Exception:
  aurora_logo_bytes = None

vinnova_logo_src = logo_src(VINNOVA_LOGO_URL, vinnova_logo_bytes)
kks_logo_src = logo_src(KKS_LOGO_URL, kks_logo_bytes)
aurora_logo_src = logo_src(AURORA_LOGO_URL, aurora_logo_bytes)

st.markdown(
    f"""
<div class="fundingWrap">
  <div class="fundingTitle">Funding acknowledgement</div>
  <div class="fundingText">
    This demo hub is supported by <b>VINNOVA</b> (Sweden's Innovation Agency),
    Project reference: <b>{PROJECT_REF}</b>, by <b>KK-stiftelsen</b> (The Knowledge Foundation),
    and by <b>Interreg Aurora</b>.
  </div>
</div>
""",
    unsafe_allow_html=True,
)
render_html(
    f"""
    <div class="fundingGrid">
      <div class="fundingItem">
        <div class="fundingLogoSlot">
          <img class="fundingLogo vinnova" src="{vinnova_logo_src}" alt="VINNOVA logo" />
        </div>
        <div class='fundingText fundingLink' style='margin-top:8px;'>
          <a href='{PROJECT_URL}' target='_blank'>View VINNOVA project page →</a>
        </div>
      </div>

      <div class="fundingItem">
        <div class="fundingLogoSlot">
          <img class="fundingLogo kks" src="{kks_logo_src}" alt="KKS logo" />
        </div>
        <div class='fundingText fundingLink' style='margin-top:8px;'>
          <a href='{KKS_URL}' target='_blank'>View KKS website →</a>
        </div>
      </div>

      <div class="fundingItem">
        <div class="fundingLogoSlot">
          <img class="fundingLogo aurora" src="{aurora_logo_src}" alt="Interreg Aurora logo" />
        </div>
        <div class='fundingText fundingLink' style='margin-top:8px;'>
          <a href='{AURORA_URL}' target='_blank'>View Interreg Aurora project →</a>
        </div>
      </div>
    </div>
    """
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
