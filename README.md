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
```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/palladium-resonance-catalysis.git
cd palladium-resonance-catalysis

# Install dependencies (minimal)
pip install numpy scipy matplotlib

python catalysis_resonance_sim.py

