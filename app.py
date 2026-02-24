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
    image_url: Optional[str] = None  # optional


# ----------------------------
# Add demos here (future-proof)
# ----------------------------
DEMOS: List[Demo] = [
    Demo(
        title="Wireless Trust AI",
        subtitle="Trustworthy AI for wireless systems: robustness, reliability, and practical evaluation views.",
        url="https://wirelesstrustai.streamlit.app/",
        tags=["Wireless AI", "6G", "Robustness", "Trustworthiness"],
        icon="📡",
        status="Live",
        image_url=None,
    ),
    # Add more later:
    # Demo(
    #     title="Your Next Demo",
    #     subtitle="One-line description of what it demonstrates.",
    #     url="https://your-next-demo.streamlit.app/",
    #     tags=["Security", "Transparency"],
    #     icon="🧠",
    #     status="Beta",
    # )
]

# ----------------------------
# Styling (professional website look)
# ----------------------------
st.markdown(
    """
<style>
.block-container { padding-top: 1.6rem; padding-bottom: 2.4rem; max-width: 1200px; }
header { visibility: hidden; height: 0px; }

h1, h2, h3 { letter-spacing: -0.02em; }
p, li { color: rgba(71,85,105,1); }

.hero {
  border-radius: 22px;
  padding: 34px 34px 28px 34px;
  border: 1px solid rgba(148,163,184,0.28);
  background:
    radial-gradient(1200px 400px at 10% 0%, rgba(59,130,246,0.18), transparent 60%),
    radial-gradient(900px 450px at 90% 20%, rgba(16,185,129,0.18), transparent 55%),
    linear-gradient(180deg, rgba(2,6,23,0.02), rgba(2,6,23,0.00));
}
.hero-title { font-size: 2.4rem; line-height: 1.1; margin: 0 0 10px 0; }
.hero-subtitle { font-size: 1.06rem; margin: 0 0 18px 0; color: rgba(71,85,105,1); max-width: 52rem; }

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

.card {
  border-radius: 18px;
  padding: 18px 18px 14px 18px;
  border: 1px solid rgba(148,163,184,0.25);
  background: rgba(255,255,255,0.70);
}
.card h3 { margin: 0 0 6px 0; font-size: 1.08rem; }
.card p { margin: 0 0 10px 0; color: rgba(71,85,105,1); }

.tag {
  display: inline-block;
  margin: 0 6px 6px 0;
  padding: 4px 10px;
  border-radius: 999px;
  background: rgba(99,102,241,0.10);
  border: 1px solid rgba(99,102,241,0.22);
  font-size: 0.82rem;
}

.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 999px;
  border: 1px solid rgba(148,163,184,0.28);
  background: rgba(148,163,184,0.10);
  margin-right: 8px;
  font-size: 0.84rem;
}
.badge-live { border-color: rgba(16,185,129,0.35); background: rgba(16,185,129,0.12); }
.badge-beta { border-color: rgba(245,158,11,0.35); background: rgba(245,158,11,0.12); }
.badge-demo { border-color: rgba(59,130,246,0.35); background: rgba(59,130,246,0.12); }
.badge-soon { border-color: rgba(148,163,184,0.35); background: rgba(148,163,184,0.08); }

.small-muted { color: rgba(100,116,139,1); font-size: 0.92rem; }
.footer {
  margin-top: 30px;
  padding-top: 16px;
  border-top: 1px solid rgba(148,163,184,0.22);
  color: rgba(100,116,139,1);
  font-size: 0.92rem;
}
</style>
""",
    unsafe_allow_html=True,
)

def status_badge(status: str) -> str:
    s = status.strip().lower()
    cls = "badge"
    if s == "live":
        cls += " badge-live"
    elif s == "beta":
        cls += " badge-beta"
    elif s == "demo":
        cls += " badge-demo"
    else:
        cls += " badge-soon"
    return f"<span class='{cls}'>{status}</span>"


# ----------------------------
# Top bar
# ----------------------------
top_left, top_right = st.columns([3, 1])
with top_left:
    st.markdown(
        "**🛡️ Trustworthy AI Showcases**  \n"
        "<span class='small-muted'>A professional hub of interactive demos for robust, transparent, and secure AI</span>",
        unsafe_allow_html=True,
    )

with top_right:
    # Show the first Live demo as the primary CTA if present
    primary = next((d for d in DEMOS if d.status.lower() == "live"), DEMOS[0])
    st.link_button(f"Open {primary.title}", primary.url, use_container_width=True)

st.write("")

# ----------------------------
# Hero section
# ----------------------------
st.markdown(
    """
<div class="hero">
  <div class="hero-title">A curated hub for <span style="color: rgba(30,58,138,1)">Trustworthy AI</span> demos</div>
  <div class="hero-subtitle">
    Explore interactive showcases focused on reliability, robustness, transparency, and security —
    presented in a clear, professional format suitable for research, industry, and public stakeholders.
  </div>
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

st.write("")

# ----------------------------
# Filters / search (for multiple demos)
# ----------------------------
all_tags = sorted({t for d in DEMOS for t in d.tags})
f1, f2, f3 = st.columns([1.3, 1.2, 1.0])

with f1:
    query = st.text_input("Search demos", placeholder="Search by title, tag, status...")
with f2:
    tag_filter = st.multiselect("Filter by tags", all_tags, default=[])
with f3:
    sort_by = st.selectbox("Sort", ["Featured", "Title A→Z", "Status"], index=0)

def matches(d: Demo) -> bool:
    if query:
        q = query.lower()
        blob = " ".join([d.title, d.subtitle, " ".join(d.tags), d.status]).lower()
        if q not in blob:
            return False
    if tag_filter:
        if not set(tag_filter).issubset(set(d.tags)):
            return False
    return True

filtered = [d for d in DEMOS if matches(d)]

status_rank = {"Live": 0, "Demo": 1, "Beta": 2, "Coming Soon": 3}
if sort_by == "Title A→Z":
    filtered.sort(key=lambda x: x.title.lower())
elif sort_by == "Status":
    filtered.sort(key=lambda x: status_rank.get(x.status, 99))

st.write("")

# ----------------------------
# Demo grid
# ----------------------------
st.markdown("## Demos")
st.markdown("<div class='small-muted'>Click a demo to open it. Add more demos anytime by appending to the DEMOS list.</div>", unsafe_allow_html=True)

if not filtered:
    st.info("No demos match your search/filters.")
else:
    cols = st.columns(3)
    for i, d in enumerate(filtered):
        with cols[i % 3]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)

            if d.image_url:
                st.image(d.image_url, use_container_width=True)

            st.markdown(
                f"""
                {status_badge(d.status)}
                <h3>{d.icon} {d.title}</h3>
                <p class="small-muted">{d.subtitle}</p>
                """,
                unsafe_allow_html=True,
            )

            tags_html = "".join([f"<span class='tag'>{t}</span>" for t in d.tags])
            st.markdown(tags_html, unsafe_allow_html=True)

            st.link_button("Open demo →", d.url, use_container_width=True)
            st.code(d.url, language=None)

            st.markdown("</div>", unsafe_allow_html=True)
            st.write("")

# ----------------------------
# Footer
# ----------------------------
st.markdown(
    """
<div class="footer">
  Maintained by Mid Sweden University • Trustworthy AI Demo Hub<br/>
  <span class="small-muted">© 2026 • Contact: kyi.thar@miun.se</span>
</div>
""",
    unsafe_allow_html=True,
)
