# neuro-ml-benchmark

# Reproducible Neuro-ML Benchmark Framework

This project provides a reproducible, modality-agnostic benchmark framework for brain data,
with an initial reference implementation on EEG.

## Motivation
Neuro-ML results are often unreliable due to data leakage, unclear preprocessing,
and irreproducible evaluation. This project focuses on:
- leakage-safe splits (e.g., subject-wise / site-wise)
- standardized preprocessing and QC
- baseline and comparable models
- reproducible artifacts and provenance
- clear inspection of results via a Streamlit dashboard

## Current Status
- EEG reference implementation: in progress
- Neuroimaging support: scaffolded (planned)

## Scope (v1)
- One EEG dataset
- One well-defined classification task
- Subject-wise evaluation
- Baseline model + evaluation artifacts
- Streamlit dashboard for inspection
