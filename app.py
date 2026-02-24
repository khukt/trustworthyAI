import streamlit as st

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Trustworthy AI Showcases",
    page_icon="🛡️",
    layout="wide",
)

SHOWCASE_URL = "https://wirelesstrustai.streamlit.app/"

# ----------------------------
# Professional styling
# ----------------------------
st.markdown(
    """
<style>
/* Layout */
.block-container { padding-top: 1.6rem; padding-bottom: 2.4rem; max-width: 1200px; }

/* Remove extra top gap under header */
header { visibility: hidden; height: 0px; }

/* Typography */
h1, h2, h3 { letter-spacing: -0.02em; }
p, li { color: rgba(71,85,105,1); }

/* Hero */
.hero {
  border-radius: 22px;
  padding: 34px 34px 28px 34px;
  border: 1px solid rgba(148,163,184,0.28);
  background:
    radial-gradient(1200px 400px at 10% 0%, rgba(59,130,246,0.18), transparent 60%),
    radial-gradient(900px 450px at 90% 20%, rgba(16,185,129,0.18), transparent 55%),
    linear-gradient(180deg, rgba(2,6,23,0.02), rgba(2,6,23,0.00));
}
.hero-title {
  font-size: 2.4rem;
  line-height: 1.1;
  margin: 0 0 10px 0;
}
.hero-subtitle {
  font-size: 1.06rem;
  margin: 0 0 18px 0;
  color: rgba(71,85,105,1);
  max-width: 48rem;
}

/* Pill badges */
.pills { margin-top: 10px; }
.pill {
  display: inline-block;
  padding: 6px 12px;
  margin: 0 8px 8px 0;
  border-radius: 999px;
  font-size: 0.86rem;
  border: 1px solid rgba(148,163,184,0.30);
  background: rgba(148,163,184,0.12);
  color: rgba(30,41,59,1);
}

/* Cards */
.card {
  border-radius: 18px;
  padding: 18px 18px 14px 18px;
  border: 1px solid rgba(148,163,184,0.25);
  background: rgba(255,255,255,0.70);
}
.card h3 { margin: 0 0 6px 0; font-size: 1.05rem; }
.card p { margin: 0; color: rgba(71,85,105,1); }

/* Section titles */
.section-title { margin-top: 8px; margin-bottom: 8px; }
.section-sub { margin-top: 0px; margin-bottom: 14px; color: rgba(71,85,105,1); }

/* Footer */
.footer {
  margin-top: 30px;
  padding-top: 16px;
  border-top: 1px solid rgba(148,163,184,0.22);
  color: rgba(100,116,139,1);
  font-size: 0.92rem;
}

/* Links */
a { text-decoration: none !important; }
.small-muted { color: rgba(100,116,139,1); font-size: 0.92rem; }
</style>
""",
    unsafe_allow_html=True,
)

# ----------------------------
# Top bar (simple brand header)
# ----------------------------
top_left, top_right = st.columns([3, 1])
with top_left:
    st.markdown("**🛡️ Trustworthy AI Showcases**  \n<span class='small-muted'>Interactive demos for robust, transparent, and secure AI</span>", unsafe_allow_html=True)
with top_right:
    st.link_button("Open Wireless Trust AI", SHOWCASE_URL, use_container_width=True)

st.write("")

# ----------------------------
# Hero section
# ----------------------------
st.markdown(
    f"""
<div class="hero">
  <div class="hero-title">A professional hub for <span style="color: rgba(30,58,138,1)">Trustworthy AI</span> demos</div>
  <div class="hero-subtitle">
    Explore a curated interactive showcase focused on reliability, robustness, and practical evaluation —
    designed to communicate results clearly to both technical and non-technical audiences.
  </div>
  <div class="pills">
    <span class="pill">📡 Wireless AI</span>
    <span class="pill">🛡️ Robustness</span>
    <span class="pill">🔎 Transparency</span>
    <span class="pill">🔐 Security</span>
    <span class="pill">⚙️ Evaluation</span>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")
cta1, cta2, cta3 = st.columns([1.2, 1.2, 1])
with cta1:
    st.link_button("🚀 Launch the showcase", SHOWCASE_URL, use_container_width=True)
with cta2:
    st.link_button("🔗 Copy share link", SHOWCASE_URL, use_container_width=True)
with cta3:
    st.markdown("<div class='small-muted'>Tip: Pin this page as your main entry point.</div>", unsafe_allow_html=True)

st.write("")

# ----------------------------
# What you'll find (3 cards)
# ----------------------------
st.markdown("## Overview")
st.markdown("<div class='section-sub'>A clean, website-like landing page that points users to the live Streamlit demo.</div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        """
<div class="card">
  <h3>Clarity-first presentation</h3>
  <p>Designed like a professional website: clear value proposition, clean sections, and strong calls-to-action.</p>
</div>
""",
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
<div class="card">
  <h3>Trustworthiness focus</h3>
  <p>Highlights robustness, reliability, transparency, and security — without overwhelming visitors with jargon.</p>
</div>
""",
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        """
<div class="card">
  <h3>Easy to extend</h3>
  <p>When you're ready, you can add more showcase URLs and render them as a grid of cards.</p>
</div>
""",
        unsafe_allow_html=True,
    )

st.write("")

# ----------------------------
# Featured showcase section (single)
# ----------------------------
st.markdown("## Featured Showcase")
left, right = st.columns([1.6, 1])
with left:
    st.markdown(
        """
### 📡 Wireless Trust AI
A live Streamlit demo showcasing trustworthy AI concepts for wireless systems — with an emphasis on
practical evaluation, robustness, and decision confidence.
"""
    )
    st.markdown(
        """
**Key themes**
- Robustness under noise and distribution shift  
- Reliability-oriented evaluation views  
- Transparent presentation of results and failure modes  
- Security mindset for model behavior in critical environments  
"""
    )
    st.link_button("Open Wireless Trust AI →", SHOWCASE_URL, use_container_width=True)

with right:
    st.markdown(
        """
<div class="card">
  <h3>Live Demo</h3>
  <p><b>Status:</b> ✅ Live</p>
  <p><b>Platform:</b> Streamlit Community Cloud</p>
  <p><b>Link:</b> <span class="small-muted">wirelesstrustai.streamlit.app</span></p>
</div>
""",
        unsafe_allow_html=True,
    )
    st.write("")
    st.code(SHOWCASE_URL, language=None)

# ----------------------------
# Footer
# ----------------------------
st.markdown(
    """
<div class="footer">
  Maintained by Mid Sweden University • Trustworthy AI Demo Hub<br/>
  <span class="small-muted">© {year} • Contact: kyi.thar@miun.se</span>
</div>
""".format(year=2026),
    unsafe_allow_html=True,
)
