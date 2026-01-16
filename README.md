# Palladium Resonance Catalysis Model

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)  <!-- update with new DOI -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Theoretical simulation of resonance-driven barrier suppression in palladium-based systems, originally developed for low-energy nuclear reaction (LENR) pathways in superabundant vacancy (SAV) phases, now extended to ambient-temperature hydrogenation catalysis for pharmaceutical synthesis.

- Original LENR model (v1): [Zenodo DOI](https://doi.org/10.5281/zenodo.18070952)  
- Catalysis extension (this repo): Standalone simulation of nitroarene hydrogenation on Pd nanoparticles, predicting >99% yields at 25°C via resonance boost.

## Features
- Coupled oscillator resonance model with Thomas-Fermi screening and topological bundle proxy  
- Parameter sweeps (surface factor, detune) and Monte Carlo uncertainty analysis  
- Full ODE simulation of 4-step hydrogenation pathway (nitrobenzene → aniline)  
- Heatmap visualization of resonance boosts  
- Reproducible experimental protocol outline in `/protocol.md`

## Repository Structure
├── lenr_sav_nano.py               # Original LENR resonance code (unchanged)
├── catalysis_resonance_sim.py     # Extended simulation with hydrogenation ODE, sweeps, MC
├── MANUSCRIPT.md                  # Theoretical manuscript (catalysis focus)
├── PROTOCOL.md                    # Reproducible experimental validation protocol
├── figures/                       # Output plots (heatmap, trajectories, yield curves, MC hist)
├── boosts.npy                     # Saved sweep results (git ignored by default)
└── README.md


## Getting Started
`# Palladium Resonance Catalysis Model

Simulation of resonance-driven barrier suppression in palladium-based nanostructures.  
- Original LENR-focused model (superabundant vacancy phases): [Zenodo v1](https://doi.org/10.5281/zenodo.18070952)  
- Extension to ambient-temperature hydrogenation catalysis (pharma-relevant): this repo + forthcoming Zenodo entry

## Overview
Coupled oscillator resonance + Thomas-Fermi screening + topological bundle proxy → exponential rate boosts.  
Biotech application: Predicts >99% nitroarene hydrogenation yields at 25°C on Pd nanoparticles (vs. ~17% standard).

## Key Files
- `lenr_sav_nano.py` — Original LENR resonance code (unchanged)  
- `catalysis_resonance_sim.py` — Extended simulation: hydrogenation ODE, parameter sweeps, Monte Carlo, plots  
- `MANUSCRIPT.md` — Theoretical manuscript (catalysis focus)  
- `PROTOCOL.md` — Reproducible experimental validation guide (incl. DFT phase)  
- `figures/` — Output plots (heatmap, trajectories, yield curves, MC distribution)

## Quick Start
```bash
git clone https://github.com/bleuradience/palladium-resonance-catalysis.git
cd palladium-resonance-catalysis

pip install numpy scipy matplotlib  # minimal deps
python catalysis_resonance_sim.py
