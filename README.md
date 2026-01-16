# Palladium Resonance Catalysis Model

Simulation of resonance-driven barrier suppression in palladium-based nanostructures, originally developed for low-energy nuclear reaction (LENR) pathways in superabundant vacancy (SAV) phases and now extended to ambient-temperature hydrogenation catalysis relevant to pharmaceutical synthesis.

- Original LENR model: [Zenodo v1](https://doi.org/10.5281/zenodo.18070952)
- Catalysis extension: This repository + forthcoming separate Zenodo entry

## Overview
The model uses coupled oscillator resonance, Thomas-Fermi screening, and a topological bundle proxy to generate exponential rate enhancements.  
The biotech/pharma application simulates selective hydrogenation of nitroarenes (nitrobenzene → aniline as a model for oncology API intermediates) on Pd nanoparticles, predicting near-complete yields (>99%) at room temperature (25°C) under resonance enhancement — versus very low yields (~17%) in standard Pd NP catalysis.

## Key Files
- `lenr_sav_nano.py`          Original LENR resonance code (unchanged from v1)
- `catalysis_resonance_sim.py` Extended simulation: hydrogenation ODE, parameter sweeps, Monte Carlo uncertainty, automatic plot generation
- `MANUSCRIPT.md`             Theoretical manuscript describing the catalysis mapping and results
- `PROTOCOL.md`               Reproducible experimental validation guide (synthesis, testing, DFT phase)
- `figures/`                  Output plots (generated when you run the code)

## Quick Start
```bash
# Clone the repository
git clone https://github.com/bleuradience/palladium-resonance-catalysis.git
cd palladium-resonance-catalysis

# Install minimal dependencies (one time)
pip install numpy scipy matplotlib

# Run the simulation — generates figures in /figures/
python catalysis_resonance_sim.py
Generated Outputs
Running the script produces four figures in the figures/ folder:

resonance_trajectory.png — Coupled oscillator positions over time (example detune=1.00)
boost_heatmap.png — Log-scale resonance boost across surface factors and detunes
yield_curves.png — Amine yield vs. time (standard vs. enhanced at 25°C)
mc_histogram.png — Distribution of final yields from 50 Monte Carlo runs

These visuals demonstrate the dramatic predicted difference: standard catalysis is slow at room temperature, while resonance enhancement achieves near-instant high yields.
To regenerate or customize:

Modify sweep ranges, temperature, pre-factor A, MC count, etc. directly in catalysis_resonance_sim.py
Re-run the script — new figures overwrite the old ones

Related Work

Zenodo v1 (LENR original model): https://doi.org/10.5281/zenodo.18070952
Forthcoming Zenodo entry: catalysis extension (DOI to be added after publication)

License
MIT — see LICENSE
Open to feedback, experimental collaborations, validation proposals, or suggestions for further extensions.
— BleuRadience / Cassandra D. Harrison
Independent Researcher, Houston, TX  # minimal deps
python catalysis_resonance_sim.py
