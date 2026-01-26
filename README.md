# Neuro-ML Benchmark

Minimal, reproducible pipeline for neuro-machine-learning experiments with explicit signal quality control.

## Summary
This repository implements an end-to-end neuro-ML workflow on real EEG/MEG data using MNE.  
The focus is on correct preprocessing, mandatory QC, transparent evaluation, and reproducible artifacts rather than model novelty.

## Functionality
- Event-based epoching of brain signals
- Signal quality control (raw signal, PSD, time–frequency)
- Baseline supervised decoding (auditory vs visual)
- Saved evaluation artifacts and metrics
- Lightweight inspection dashboard

