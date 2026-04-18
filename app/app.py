import json
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Neuro-ML Benchmark Dashboard", layout="wide")

REPO_ROOT = Path("/workspaces/neural-canvas")
RUNS_DIR = REPO_ROOT / "results" / "runs"

st.title("Neuro-ML Benchmark Dashboard")
st.caption("Inspect QC + baseline ML results from reproducible run folders.")

if not RUNS_DIR.exists():
    st.error(f"Runs directory not found: {RUNS_DIR}")
    st.stop()

runs = sorted([p for p in RUNS_DIR.iterdir() if p.is_dir()])
if not runs:
    st.warning("No runs found. Create results/runs/<run_id>/ with artifacts.")
    st.stop()

selected = st.sidebar.selectbox("Select run", [r.name for r in runs], index=0)
run_dir = RUNS_DIR / selected
st.sidebar.markdown(f"**Run folder:** `{run_dir}`")

metrics_path = run_dir / "metrics.json"
if metrics_path.exists():
    metrics = json.loads(metrics_path.read_text())
else:
    metrics = None
    st.warning("metrics.json not found in this run folder.")

if metrics:
    st.subheader("Metrics")
    m = metrics.get("metrics", {})
    col1, col2, col3 = st.columns(3)
    col1.metric("Accuracy", f"{m.get('accuracy', '—')}")
    col2.metric("F1", f"{m.get('f1', '—')}")
    col3.metric("Samples", f"{metrics.get('n_samples', '—')}")
    st.json(metrics)

st.subheader("QC & Evaluation Figures")
fig_files = ["qc_signal_examples.png", "qc_psd.png", "qc_timefreq.png", "confusion_matrix.png"]

cols = st.columns(2)
i = 0
for fname in fig_files:
    p = run_dir / fname
    if p.exists():
        cols[i % 2].image(str(p), caption=fname, use_container_width=True)
        i += 1
    else:
        st.info(f"Missing: {fname}")

ps = run_dir / "per_subject.csv"
if ps.exists():
    st.subheader("Per-subject performance")
    df = pd.read_csv(ps)
    st.dataframe(df, use_container_width=True)
