import streamlit as st
from dataclasses import dataclass
from typing import List, Optional

# ----------------------------
# Config
# ----------------------------
st.set_page_config(
    page_title="Trustworthy AI Showcases",
    page_icon="🛡️",
    layout="wide",
)

@dataclass
class Demo:
    title: str
    subtitle: str
    url: str
    tags: List[str]
    icon: str = "✨"
    status: str = "Live"   # Live / Demo / Beta / Coming Soon
    image_url: Optional[str] = None  # optional banner image (wide)


DEMOS: List[Demo] = [
    Demo(
        title="Wireless Trust AI",
        subtitle="Trustworthy AI for wireless systems — robustness, reliability, and practical evaluation views.",
        url="https://wirelesstrustai.streamlit.app/",
        tags=["Wireless AI", "6G", "Robustness", "Trustworthiness"],
        icon="📡",
        status="Live",
        image_url=None,  # you can add a banner image later
    ),
]

# ----------------------------
# CSS (make Streamlit look like a website)
# ----------------------------
st.markdown("""
<style>
/* Page width + remove Streamlit padding vibe */
.block-container { max-width: 1150px; padding-top: 1.2rem; padding-bottom: 2.8rem; }

/* Hide Streamlit default header/footer */
header { visibility: hidden; height: 0px; }
footer { visibility: hidden; height: 0px; }
#MainMenu { visibility: hidden; }

/* Typography */
html, body, [class*="css"]  { font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; }
h1, h2, h3 { letter-spacing: -0.02em; }
p { color: rgba(71,85,105,1); }

/* Top nav */
.navbar {
  display: flex; align-items: center; justify-content: space-between;
  padding: 10px 0 18px 0;
}
.brand {
  display: flex; gap: 10px; align-items: center;
}
.brand-title { font-weight: 700; font-size: 1.05rem; color: rgba(15,23,42,1); }
.brand-sub { font-size: 0.92rem; color: rgba(100,116,139,1); margin-top: 1px; }

/* Primary button (HTML) */
a.cta {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 10px 14px;
  border-radius: 12px;
  border: 1px solid rgba(148,163,184,0.35);
  background: rgba(15,23,42,1);
  color: white !important;
  text-decoration: none !important;
  font-weight: 600;
}
a.cta:hover { opacity: 0.92; }

/* Hero */
.hero {
  border-radius: 22px;
  padding: 34px 34px 28px 34px;
  border: 1px solid rgba(148,163,184,0.25);
  background:
    radial-gradient(1200px 460px at 12% 10%, rgba(59,130,246,0.23), transparent 55%),
    radial-gradient(900px 520px at 90% 25%, rgba(16,185,129,0.20), transparent 55%),
    linear-gradient(180deg, rgba(255,255,255,0.70), rgba(255,255,255,0.40));
}
.hero h1 { margin: 0; font-size: 2.55rem; line-height: 1.08; color: rgba(15,23,42,1); }
.hero p { margin: 12px 0 0 0; font-size: 1.05rem; max-width: 54rem; }
.hero-meta { margin-top: 16px; display: flex; gap: 10px; flex-wrap: wrap; }

/* Pills */
.pill {
  display:inline-flex; align-items:center; gap:8px;
  padding: 7px 12px;
  border-radius: 999px;
  background: rgba(15,23,42,0.05);
  border: 1px solid rgba(148,163,184,0.25);
  color: rgba(30,41,59,1);
  font-size: 0.88rem;
}

/* Section title */
.section-title { margin-top: 28px; margin-bottom: 8px; font-size: 1.35rem; font-weight: 750; color: rgba(15,23,42,1); }
.section-sub { margin-top: 0; margin-bottom: 14px; color: rgba(100,116,139,1); }

/* Featured card */
.featured {
  border-radius: 20px;
  padding: 22px;
  border: 1px solid rgba(148,163,184,0.25);
  background: rgba(255,255,255,0.75);
  box-shadow: 0 10px 30px rgba(2,6,23,0.06);
}
.featured-top { display:flex; justify-content: space-between; align-items: start; gap: 16px; flex-wrap: wrap; }
.badge {
  display:inline-block;
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 0.86rem;
  border: 1px solid rgba(16,185,129,0.35);
  background: rgba(16,185,129,0.12);
  color: rgba(15,23,42,1);
  font-weight: 650;
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
.kpis { display:flex; gap:10px; flex-wrap:wrap; margin-top: 12px; }
.kpi {
  border-radius: 14px; padding: 10px 12px;
  border: 1px solid rgba(148,163,184,0.20);
  background: rgba(15,23,42,0.03);
  min-width: 160px;
}
.kpi .k { font-weight: 750; color: rgba(15,23,42,1); }
.kpi .v { color: rgba(100,116,139,1); font-size: 0.92rem; margin-top: 2px; }

/* Demo grid card */
.gridcard {
  border-radius: 18px;
  padding: 16px;
  border: 1px solid rgba(148,163,184,0.22);
  background: rgba(255,255,255,0.70);
  transition: transform 140ms ease, box-shadow 140ms ease;
}
.gridcard:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 26px rgba(2,6,23,0.08);
}
.gridcard h3 { margin: 0 0 6px 0; font-size: 1.06rem; }
.gridcard p { margin: 0 0 10px 0; color: rgba(71,85,105,1); }

/* Footer */
.footerline {
  margin-top: 30px;
  padding-top: 16px;
  border-top: 1px solid rgba(148,163,184,0.22);
  color: rgba(100,116,139,1);
  font-size: 0.92rem;
}
</style>
""", unsafe_allow_html=True)


def tags_html(tags: List[str]) -> str:
    return "".join([f"<span class='tag'>{t}</span>" for t in tags])


# ----------------------------
# Navbar
# ----------------------------
primary = next((d for d in DEMOS if d.status.lower() == "live"), DEMOS[0])

st.markdown(f"""
<div class="navbar">
  <div class="brand">
    <div style="font-size:1.25rem;">🛡️</div>
    <div>
      <div class="brand-title">Trustworthy AI Showcases</div>
      <div class="brand-sub">A professional hub of interactive demos</div>
    </div>
  </div>
  <a class="cta" href="{primary.url}" target="_blank">Open {primary.title} →</a>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# Hero
# ----------------------------
st.markdown("""
<div class="hero">
  <h1>A curated hub for Trustworthy AI demos</h1>
  <p>
    Explore interactive showcases focused on reliability, robustness, transparency, and security —
    presented in a clear, professional format suitable for research, industry, and public stakeholders.
  </p>
  <div class="hero-meta">
    <span class="pill">🛡️ Robustness</span>
    <span class="pill">🔎 Transparency</span>
    <span class="pill">🔐 Security</span>
    <span class="pill">⚙️ Evaluation</span>
    <span class="pill">📡 Wireless / 6G</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# Featured demo (premium)
# ----------------------------
st.markdown("<div class='section-title'>Featured demo</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>The primary live showcase — more demos will be added over time.</div>", unsafe_allow_html=True)

d = primary
left, right = st.columns([1.55, 1])

with left:
    st.markdown(f"""
<div class="featured">
  <div class="featured-top">
    <div>
      <span class="badge">{d.status}</span>
      <h2 style="margin:10px 0 6px 0;">{d.icon} {d.title}</h2>
      <p style="margin:0 0 10px 0;">{d.subtitle}</p>
      {tags_html(d.tags)}
      <div class="kpis">
        <div class="kpi"><div class="k">Focus</div><div class="v">Trustworthiness evaluation</div></div>
        <div class="kpi"><div class="k">Domain</div><div class="v">Wireless / 6G systems</div></div>
        <div class="kpi"><div class="k">Format</div><div class="v">Interactive Streamlit demo</div></div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

with right:
    st.write("")
    st.link_button("🚀 Launch demo", d.url, use_container_width=True)
    st.write("")
    st.markdown(
        "<div class='gridcard'><h3>Why this matters</h3>"
        "<p>Shows trustworthy AI concepts in a clear, stakeholder-friendly interface — ready for research and industry demos.</p>"
        "</div>",
        unsafe_allow_html=True
    )
    st.write("")
    st.markdown(
        "<div class='gridcard'><h3>For future growth</h3>"
        "<p>This page automatically scales into a multi-demo catalog when you add more entries to <b>DEMOS</b>.</p>"
        "</div>",
        unsafe_allow_html=True
    )

# ----------------------------
# Catalog section (future multi-demo)
# ----------------------------
st.markdown("<div class='section-title'>Demo catalog</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>Search and filter will become useful when you add more demos.</div>", unsafe_allow_html=True)

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

# Grid
cols = st.columns(3)
for i, demo in enumerate(filtered):
    with cols[i % 3]:
        st.markdown(f"""
<div class="gridcard">
  <div style="display:flex; justify-content: space-between; align-items:start; gap:10px;">
    <div>
      <div style="font-weight:800; color: rgba(15,23,42,1);">{demo.icon} {demo.title}</div>
      <div style="color: rgba(100,116,139,1); font-size:0.92rem; margin-top:4px;">{demo.subtitle}</div>
    </div>
    <div class="badge" style="border-color: rgba(148,163,184,0.25); background: rgba(15,23,42,0.04);">{demo.status}</div>
  </div>
  <div style="margin-top:10px;">{tags_html(demo.tags)}</div>
</div>
""", unsafe_allow_html=True)
        st.link_button("Open →", demo.url, use_container_width=True)

# ----------------------------
# Footer
# ----------------------------
st.markdown("""
<div class="footerline">
  Maintained by Mid Sweden University • Trustworthy AI Demo Hub<br/>
  <span style="color: rgba(148,163,184,1);">Contact: kyi.thar@miun.se</span>
</div>
""", unsafe_allow_html=True)
