import streamlit as st
from dataclasses import dataclass
from typing import List, Optional

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Trustworthy AI Showcases",
    page_icon="🛡️",
    layout="wide",
)

# Official VINNOVA logo (English version) from VINNOVA newsroom assets
VINNOVA_LOGO_URL = "https://www.vinnova.se/globalassets/mikrosajter/nyhetsrum/bilder/logotyp/vinnova_green_payoff_eng_rgb.png"

@dataclass
class Demo:
    title: str
    subtitle: str
    url: str
    tags: List[str]
    icon: str = "✨"
    status: str = "Live"  # Live / Demo / Beta / Coming Soon
    image_url: Optional[str] = None  # optional banner image


DEMOS: List[Demo] = [
    Demo(
        title="Wireless Trust AI",
        subtitle="Trustworthy AI for wireless systems — robustness, reliability, and practical evaluation views.",
        url="https://wirelesstrustai.streamlit.app/",
        tags=["Wireless AI", "6G", "Robustness", "Trustworthiness"],
        icon="📡",
        status="Live",
        image_url=None,
    ),
]

# ----------------------------
# Premium styling (Apple-like + Research Lab)
# ----------------------------
st.markdown(
    """
<style>
/* Page layout */
.block-container { max-width: 1180px; padding-top: 1.0rem; padding-bottom: 2.6rem; }
header, footer, #MainMenu { visibility: hidden; height: 0px; }

/* Typography */
html, body, [class*="css"] { font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; }
h1, h2, h3 { letter-spacing: -0.03em; }
p { color: rgba(71,85,105,1); }

/* Top nav */
.navbar { display:flex; align-items:center; justify-content:space-between; padding: 6px 0 18px 0; }
.brand { display:flex; gap:10px; align-items:center; }
.brand-title { font-weight: 800; font-size: 1.05rem; color: rgba(15,23,42,1); }
.brand-sub { font-size: 0.92rem; color: rgba(100,116,139,1); margin-top: 1px; }

/* Buttons (HTML) */
a.btnPrimary {
  display:inline-flex; align-items:center; justify-content:center;
  padding: 10px 14px; border-radius: 12px;
  background: rgba(15,23,42,1);
  border: 1px solid rgba(15,23,42,1);
  color: white !important; font-weight: 700;
  text-decoration: none !important;
}
a.btnPrimary:hover { opacity: 0.93; }

a.btnSoft {
  display:inline-flex; align-items:center; justify-content:center;
  padding: 10px 14px; border-radius: 12px;
  background: rgba(15,23,42,0.04);
  border: 1px solid rgba(148,163,184,0.28);
  color: rgba(15,23,42,1) !important; font-weight: 700;
  text-decoration: none !important;
}
a.btnSoft:hover { background: rgba(15,23,42,0.06); }

/* Hero */
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

/* Pills */
.pills { margin-top: 18px; display:flex; flex-wrap:wrap; gap:10px; }
.pill {
  display:inline-flex; gap:8px; align-items:center;
  padding: 7px 12px; border-radius: 999px;
  background: rgba(15,23,42,0.05);
  border: 1px solid rgba(148,163,184,0.22);
  color: rgba(30,41,59,1);
  font-size: 0.88rem;
}

/* Section */
.sectionTitle { margin-top: 30px; margin-bottom: 8px; font-size: 1.35rem; font-weight: 850; color: rgba(15,23,42,1); }
.sectionSub { margin-top: 0; margin-bottom: 14px; color: rgba(100,116,139,1); }

/* Premium cards */
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

/* Featured */
.badgeLive {
  display:inline-block;
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 0.86rem;
  border: 1px solid rgba(16,185,129,0.35);
  background: rgba(16,185,129,0.12);
  color: rgba(15,23,42,1);
  font-weight: 800;
}
.tag {
  display:inline-block;
  padding: 5px 10px;
  border-radius: 999px;
  margin: 8px 8px 0 0;
  background: rgba(99,102,241,0.10);
  border: 1px solid rgba(99,102,241,0.18);
  font-size: 0.82rem;
  color: rgba(30,41,59,1);
}

/* Metrics strip */
.metric {
  border-radius: 18px;
  padding: 14px 14px 12px 14px;
  border: 1px solid rgba(148,163,184,0.18);
  background: rgba(15,23,42,0.03);
}
.metricK { font-weight: 900; color: rgba(15,23,42,1); font-size: 1.05rem; }
.metricV { color: rgba(100,116,139,1); font-size: 0.92rem; margin-top: 2px; }

/* Partners strip (no logo effects, clean background) */
.partners {
  border-radius: 18px;
  padding: 14px 16px;
  border: 1px solid rgba(148,163,184,0.20);
  background: rgba(255,255,255,0.85);
}
.partnerRow { display:flex; align-items:center; gap:18px; flex-wrap:wrap; }
.partnerLabel { font-weight: 800; color: rgba(15,23,42,1); margin-right: 6px; }
.partnerNote { color: rgba(100,116,139,1); font-size: 0.92rem; }

/* Demo grid cards */
.gridcard {
  border-radius: 18px;
  padding: 16px;
  border: 1px solid rgba(148,163,184,0.20);
  background: rgba(255,255,255,0.74);
  transition: transform 140ms ease, box-shadow 140ms ease;
}
.gridcard:hover { transform: translateY(-2px); box-shadow: 0 16px 38px rgba(2,6,23,0.08); }
.gridTitle { font-weight: 900; color: rgba(15,23,42,1); }
.gridSub { color: rgba(100,116,139,1); font-size: 0.92rem; margin-top: 4px; }

/* Footer */
.footerline {
  margin-top: 34px;
  padding-top: 16px;
  border-top: 1px solid rgba(148,163,184,0.22);
  color: rgba(100,116,139,1);
  font-size: 0.92rem;
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
primary = next((d for d in DEMOS if d.status.lower() == "live"), DEMOS[0])
st.markdown(
    f"""
<div class="navbar">
  <div class="brand">
    <div style="font-size:1.25rem;">🛡️</div>
    <div>
      <div class="brand-title">Trustworthy AI Showcases</div>
      <div class="brand-sub">Professional demo hub • Research & industry ready</div>
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
# Research-lab metrics strip
# ----------------------------
st.markdown("<div class='sectionTitle'>At a glance</div>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown("<div class='metric'><div class='metricK'>Live demos</div><div class='metricV'>Growing showcase catalog</div></div>", unsafe_allow_html=True)
with m2:
    st.markdown("<div class='metric'><div class='metricK'>Focus</div><div class='metricV'>Trust • Robustness • Security</div></div>", unsafe_allow_html=True)
with m3:
    st.markdown("<div class='metric'><div class='metricK'>Domain</div><div class='metricV'>Wireless / 6G & IIoT</div></div>", unsafe_allow_html=True)
with m4:
    st.markdown("<div class='metric'><div class='metricK'>Format</div><div class='metricV'>Interactive Streamlit apps</div></div>", unsafe_allow_html=True)

# ----------------------------
# Partners strip (VINNOVA logo)
# ----------------------------
st.markdown("<div class='sectionTitle'>Partners & funding</div>", unsafe_allow_html=True)
st.markdown("<div class='sectionSub'>Selected organisations supporting or connected to the showcased work.</div>", unsafe_allow_html=True)

st.markdown("<div class='partners'><div class='partnerRow'>"
            "<span class='partnerLabel'>Supported by</span>"
            "<span class='partnerNote'>(logos shown in official form)</span>"
            "</div></div>", unsafe_allow_html=True)

# Place logos in columns to control sizing cleanly
p1, p2, p3, p4 = st.columns([1.2, 1, 1, 1])
with p1:
    st.image(VINNOVA_LOGO_URL, width=220)  # official VINNOVA logo (English)
with p2:
    st.markdown("<div class='cardFlat'><b>Mid Sweden University</b><div class='gridSub'>Host organisation</div></div>", unsafe_allow_html=True)
with p3:
    st.markdown("<div class='cardFlat'><b>Industry partners</b><div class='gridSub'>To be added</div></div>", unsafe_allow_html=True)
with p4:
    st.markdown("<div class='cardFlat'><b>Research networks</b><div class='gridSub'>To be added</div></div>", unsafe_allow_html=True)

# ----------------------------
# Featured demo (premium)
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
  <b>Why visitors like it</b>
  <div class="gridSub" style="margin-top:6px;">
    Clear story • Interactive exploration • Stakeholder-friendly visuals
  </div>
</div>
""",
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown(
        """
<div class="cardFlat">
  <b>Future-ready</b>
  <div class="gridSub" style="margin-top:6px;">
    This page automatically scales into a full demo catalog.
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

# ----------------------------
# Catalog (future multi-demo)
# ----------------------------
st.markdown("<div id='catalog'></div>", unsafe_allow_html=True)
st.markdown("<div class='sectionTitle'>Demo catalog</div>", unsafe_allow_html=True)
st.markdown("<div class='sectionSub'>Use search and tags once you have multiple demos.</div>", unsafe_allow_html=True)

all_tags = sorted({t for demo in DEMOS for t in demo.tags})
f1, f2, f3 = st.columns([1.4, 1.2, 1.0])

with f1:
    query = st.text_input("Search demos", placeholder="Search by title or keyword…", label_visibility="collapsed")
with f2:
    tag_filter = st.multiselect("Filter by tags", all_tags, default=[], label_visibility="collapsed", placeholder="Filter by tags…")
with f3:
    sort_by = st.selectbox("Sort", ["Featured", "Title A→Z", "Status"], index=0, label_visibility="collapsed")

def matches(demo: Demo) -> bool:
    if query:
        q = query.lower()
        blob = " ".join([demo.title, demo.subtitle, " ".join(demo.tags), demo.status]).lower()
        if q not in blob:
            return False
    if tag_filter and not set(tag_filter).issubset(set(demo.tags)):
        return False
    return True

filtered = [demo for demo in DEMOS if matches(demo)]
status_rank = {"Live": 0, "Demo": 1, "Beta": 2, "Coming Soon": 3}
if sort_by == "Title A→Z":
    filtered.sort(key=lambda x: x.title.lower())
elif sort_by == "Status":
    filtered.sort(key=lambda x: status_rank.get(x.status, 99))

cols = st.columns(3)
for i, demo in enumerate(filtered):
    with cols[i % 3]:
        st.markdown(
            f"""
<div class="gridcard">
  <div class="gridTitle">{demo.icon} {demo.title}</div>
  <div class="gridSub">{demo.subtitle}</div>
  <div style="margin-top:10px;">{tags_html(demo.tags)}</div>
</div>
""",
            unsafe_allow_html=True,
        )
        st.link_button("Open →", demo.url, use_container_width=True)

# ----------------------------
# Footer
# ----------------------------
st.markdown(
    """
<div class="footerline">
  Maintained by Mid Sweden University • Trustworthy AI Demo Hub<br/>
  Contact: kyi.thar@miun.se
</div>
""",
    unsafe_allow_html=True,
)
