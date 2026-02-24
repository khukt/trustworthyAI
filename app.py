import streamlit as st
from dataclasses import dataclass
from typing import List, Optional

# ----------------------------
# Page setup
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
class Showcase:
    title: str
    subtitle: str
    url: str
    tags: List[str]
    icon: str = "✨"
    status: str = "Live"  # Live / Demo / Beta / Coming Soon
    image_url: Optional[str] = None  # optional hero image per showcase


# ----------------------------
# Add your showcases here (easy to extend)
# ----------------------------
SHOWCASES: List[Showcase] = [
    Showcase(
        title="SHIELD — Human-in-the-loop Intelligence",
        subtitle="Entity linking, detection, and structured extraction workflow.",
        url="https://YOUR-STREAMLIT-APP-URL-1.streamlit.app",
        tags=["Human-in-the-loop", "NLP", "Knowledge Graph"],
        icon="🧠",
        status="Live",
        image_url=None,
    ),
    Showcase(
        title="Robustness & Adversarial Resilience",
        subtitle="Stress-testing models under distribution shift and adversarial noise.",
        url="https://YOUR-STREAMLIT-APP-URL-2.streamlit.app",
        tags=["Robustness", "Security", "Evaluation"],
        icon="🛡️",
        status="Beta",
        image_url=None,
    ),
    Showcase(
        title="Transparency Dashboard",
        subtitle="Model behavior insights, failure patterns, and explainability views.",
        url="https://YOUR-STREAMLIT-APP-URL-3.streamlit.app",
        tags=["Transparency", "Monitoring", "Audit"],
        icon="🔎",
        status="Demo",
        image_url=None,
    ),
]


# ----------------------------
# Styling (pretty UI)
# ----------------------------
st.markdown(
    """
<style>
/* widen container a bit */
.block-container { padding-top: 2.0rem; padding-bottom: 2.5rem; }

/* hero */
.hero {
  border-radius: 18px;
  padding: 26px 26px 22px 26px;
  background: linear-gradient(135deg, rgba(30,58,138,0.16), rgba(16,185,129,0.14));
  border: 1px solid rgba(148,163,184,0.25);
}
.hero h1 { margin: 0; font-size: 2.2rem; line-height: 1.15; }
.hero p { margin: 10px 0 0 0; color: rgba(100,116,139,0.95); font-size: 1.02rem; }

/* badges */
.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 999px;
  border: 1px solid rgba(148,163,184,0.35);
  background: rgba(148,163,184,0.12);
  margin-right: 8px;
  font-size: 0.85rem;
}
.badge-live { border-color: rgba(16,185,129,0.35); background: rgba(16,185,129,0.12); }
.badge-beta { border-color: rgba(245,158,11,0.35); background: rgba(245,158,11,0.12); }
.badge-demo { border-color: rgba(59,130,246,0.35); background: rgba(59,130,246,0.12); }
.badge-soon { border-color: rgba(148,163,184,0.35); background: rgba(148,163,184,0.10); }

/* cards */
.card {
  border-radius: 18px;
  padding: 18px 18px 14px 18px;
  border: 1px solid rgba(148,163,184,0.25);
  background: rgba(2,6,23,0.02);
}
.card h3 { margin: 0 0 6px 0; font-size: 1.15rem; }
.card p { margin: 0 0 10px 0; color: rgba(100,116,139,0.95); }
.tag {
  display: inline-block;
  margin: 0 6px 6px 0;
  padding: 4px 10px;
  border-radius: 999px;
  background: rgba(99,102,241,0.10);
  border: 1px solid rgba(99,102,241,0.25);
  font-size: 0.82rem;
}
.small { color: rgba(100,116,139,0.90); font-size: 0.92rem; }
.footer { color: rgba(100,116,139,0.90); font-size: 0.9rem; margin-top: 26px; }
a.cleanlink { text-decoration: none; }
</style>
""",
    unsafe_allow_html=True,
)

# ----------------------------
# Hero section
# ----------------------------
st.markdown(
    """
<div class="hero">
  <h1>🛡️ Trustworthy AI Showcases</h1>
  <p>
    A curated set of interactive demos highlighting robust, transparent, secure, and human-centered AI systems.
    Add new showcases anytime by inserting another Streamlit URL.
  </p>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")
colA, colB, colC, colD = st.columns([1.2, 1, 1, 1])

with colA:
    st.markdown("<span class='badge badge-live'>✅ Live</span><span class='badge badge-demo'>🧪 Demo</span><span class='badge badge-beta'>⚠️ Beta</span>", unsafe_allow_html=True)
with colB:
    query = st.text_input("Search", placeholder="Type keywords (e.g., security, transparency, NLP)")
with colC:
    tag_filter = st.multiselect(
        "Filter by tags",
        sorted({t for s in SHOWCASES for t in s.tags}),
        default=[],
    )
with colD:
    sort_by = st.selectbox("Sort", ["Featured", "Title A→Z", "Status"], index=0)

# ----------------------------
# Filtering logic
# ----------------------------
def matches(showcase: Showcase) -> bool:
    if query:
        q = query.lower()
        blob = " ".join([showcase.title, showcase.subtitle, " ".join(showcase.tags), showcase.status]).lower()
        if q not in blob:
            return False
    if tag_filter:
        if not set(tag_filter).issubset(set(showcase.tags)):
            return False
    return True

filtered = [s for s in SHOWCASES if matches(s)]

status_rank = {"Live": 0, "Demo": 1, "Beta": 2, "Coming Soon": 3}
if sort_by == "Title A→Z":
    filtered.sort(key=lambda s: s.title.lower())
elif sort_by == "Status":
    filtered.sort(key=lambda s: status_rank.get(s.status, 99))

# ----------------------------
# Grid renderer
# ----------------------------
def status_badge(status: str) -> str:
    cls = "badge"
    if status.lower() == "live":
        cls += " badge-live"
    elif status.lower() == "beta":
        cls += " badge-beta"
    elif status.lower() == "demo":
        cls += " badge-demo"
    else:
        cls += " badge-soon"
    return f"<span class='{cls}'>{status}</span>"

st.write("")
st.markdown("### 🚀 Showcases")

if not filtered:
    st.info("No showcases match your search/filters. Try clearing filters or changing the query.")
else:
    # 3-column responsive-like layout using Streamlit columns
    cols = st.columns(3)
    for i, s in enumerate(filtered):
        with cols[i % 3]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)

            # optional image
            if s.image_url:
                st.image(s.image_url, use_container_width=True)

            st.markdown(
                f"""
                {status_badge(s.status)}
                <h3>{s.icon} {s.title}</h3>
                <p class="small">{s.subtitle}</p>
                """,
                unsafe_allow_html=True,
            )

            # tags
            tags_html = "".join([f"<span class='tag'>{t}</span>" for t in s.tags])
            st.markdown(tags_html, unsafe_allow_html=True)

            # button + link
            left, right = st.columns([1, 1])
            with left:
                st.link_button("Open showcase", s.url, use_container_width=True)
            with right:
                st.code(s.url, language=None)

            st.markdown("</div>", unsafe_allow_html=True)
            st.write("")

# ----------------------------
# Add-new instructions
# ----------------------------
st.markdown("---")
st.markdown("### ➕ Add another showcase")
st.markdown(
    """
1. Copy one entry in `SHOWCASES`  
2. Paste it below the others  
3. Update: `title`, `subtitle`, `url`, `tags`, and optionally `icon`, `status`, `image_url`
"""
)

st.markdown(
    "<div class='footer'>Maintained by Mid Sweden University • Trustworthy AI demo hub</div>",
    unsafe_allow_html=True,
)
