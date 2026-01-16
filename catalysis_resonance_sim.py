import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# =============================================
# Original LENR resonance model (unchanged from v1)
# =============================================
# Physical constants and parameters
r_dd = 2.75e-10          # Fixed D-D separation in SAV (m)
lambda_b = 0.577e-10     # Bulk Thomas-Fermi screening length (m)
E_th = 0.0388            # Thermal energy at 300K (eV = 38.8 meV)
x_0 = 0.1e-10            # Scaling length for oscillation amplitude (m)
omega_0 = 1e14           # Approximate vibration frequency (rad/s)

# Resonance ODE model (coupled oscillators)
def resonance_ode(y, tau, detune, g, k, A, om_d):
    X1, V1, X2, V2 = y
    dX1 = V1
    dV1 = -X1 - g * V1 - k * (X1 - X2)
    dX2 = V2
    dV2 = -detune**2 * X2 - g * V2 - k * (X2 - X1) + A * np.sin(om_d * tau)
    return [dX1, dV1, dX2, dV2]

# Run resonance simulation
def run_resonance(surface_factor=1.0, detune=1.05, g=0.01, k=0.1, A=0.1, om_d=None, plot=False):
    lambda_TF = lambda_b / np.sqrt(surface_factor)
    if om_d is None:
        om_d = (1 + detune) / 2
    
    tau = np.linspace(0, 200, 20000)  # Dimensionless time
    y0 = [1.0, 0.0, 0.0, 0.0]        # Initial conditions
    
    sol = odeint(resonance_ode, y0, tau, args=(detune, g, k, A, om_d), rtol=1e-6)
    
    dd_dist = np.abs(sol[:, 0] - sol[:, 2]) * x_0
    peak_amp = np.max(np.abs(sol[:, 0])) * x_0
    min_dd = np.min(dd_dist)
    
    effective_min = max(min_dd, 0.1e-10)  # Minimum physical separation ~0.1 Å
    delta_r = r_dd - effective_min
    rate_boost = np.exp(delta_r / lambda_TF)
    
    if plot:
        t_ps = tau / omega_0 * 1e12  # Convert to picoseconds
        plt.figure(figsize=(10, 6))
        plt.plot(t_ps, sol[:, 0] * x_0 * 1e10, label='D1 position (Å)')
        plt.plot(t_ps, sol[:, 2] * x_0 * 1e10, label='D2 position (Å)')
        plt.xlabel('Time (ps)')
        plt.ylabel('Position deviation (Å)')
        plt.title(f'Resonance Trajectory (detune={detune:.2f}, boost={rate_boost:.1e})')
        plt.legend()
        plt.grid(True)
        plt.savefig('figures/resonance_trajectory.png')
        plt.close()
    
    return peak_amp * 1e10, effective_min * 1e10, rate_boost

# Bundle-inspired topological boost (proxy)
def bundle_alpha_boost(base_alpha, fiber_dim=14, base_dim=4):
    alpha_vals = [base_alpha] * base_dim + [1 / base_alpha] * (fiber_dim - base_dim)
    M = np.diag(alpha_vals)
    tr_M = np.trace(M)
    M_tl = M - (tr_M / fiber_dim) * np.eye(fiber_dim)
    det_tl = np.linalg.det(M_tl)
    boost = max(1.0, np.abs(det_tl)**(1 / fiber_dim))
    return boost

# Barrier elimination equation
def barrier_eq(alpha, surface_factor=1.0, bundle_boost=1.0):
    eff_alpha = alpha * surface_factor * bundle_boost
    V_scr = (1.44e-9 / r_dd) * np.exp(-r_dd * np.sqrt(eff_alpha) / lambda_b)  # eV
    return V_scr - E_th

# =============================================
# Biotech extension: Hydrogenation simulation
# =============================================
# Realistic barriers from literature (eV)
barriers_standard = {
    'H2_diss': 0.30,
    'nitro_to_nitroso': 0.45,
    'nitroso_to_hydroxyl': 0.35,
    'hydroxyl_to_amine': 0.40
}

def arrhenius_rate(Ea, T=298, A=1e6):  # min^-1 scale
    kB = 8.617e-5  # eV/K
    return A * np.exp(-Ea / (kB * T))

def enhanced_barrier(Ea, boost):
    # Log-scaled reduction, capped at 30% for physical realism
    reduction = min(0.3 * Ea, 0.05 * np.log(boost + 1))
    return max(0.05, Ea - reduction)

def hydrogenation_ode(y, t, k1, k2, k3):
    nitro, nitroso, hydrox, amine = y
    d_nitro = -k1 * nitro
    d_nitroso = k1 * nitro - k2 * nitroso
    d_hydrox = k2 * nitroso - k3 * hydrox
    d_amine = k3 * hydrox
    return [d_nitro, d_nitroso, d_hydrox, d_amine]

def simulate_hydrogenation(boost=1.0, T=298, t_max=120, enhanced=True):
    rates = {}
    for step, Ea in barriers_standard.items():
        Ea_eff = enhanced_barrier(Ea, boost) if enhanced else Ea
        rates[step] = arrhenius_rate(Ea_eff, T)
    
    k1 = rates['nitro_to_nitroso']
    k2 = rates['nitroso_to_hydroxyl']
    k3 = rates['hydroxyl_to_amine']
    
    t = np.linspace(0, t_max, 300)
    y0 = [1.0, 0.0, 0.0, 0.0]
    sol = odeint(hydrogenation_ode, y0, t, args=(k1, k2, k3))
    
    yield_amine = sol[:, 3] * 100
    conv = (1 - sol[:, 0]) * 100
    sel = np.divide(yield_amine, conv, where=conv>0, out=np.zeros_like(yield_amine))
    
    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(t, yield_amine, label='Amine yield (%)')
    plt.xlabel('Time (min)')
    plt.ylabel('Yield (%)')
    plt.title(f'Hydrogenation at {T} K – Boost {boost:.1e} {"(enhanced)" if enhanced else "(standard)"}')
    plt.grid(True)
    plt.legend()
    plt.savefig('figures/yield_curves.png')
    plt.close()
    
    return sol, t, yield_amine[-1]

# Parameter sweeps & visualization
if __name__ == "__main__":
    # Example: Generate boost heatmap
    surface_factors = np.linspace(5, 100, 15)
    detunes = np.linspace(0.95, 1.05, 30)
    boosts = np.array([[run_resonance(sf, d)[2] for d in detunes] for sf in surface_factors])
    np.save('boosts.npy', boosts)
    
    plt.imshow(np.log10(boosts + 1), cmap='viridis', aspect='auto')
    plt.colorbar(label='log10(Boost + 1)')
    plt.xlabel('Detune index')
    plt.ylabel('Surface factor index')
    plt.title('Resonance Boost Heatmap')
    plt.savefig('figures/boost_heatmap.png')
    plt.close()
    
    # Monte Carlo uncertainty (50 runs)
    median_boost = np.median(boosts)
    mc_yields = []
    for _ in range(50):
        noisy_boost = median_boost * np.random.normal(1.0, 0.1)  # ±10%
        _, _, yld = simulate_hydrogenation(noisy_boost, enhanced=True)
        mc_yields.append(yld + np.random.normal(0, 5))  # ±5% yield noise
    
    plt.hist(mc_yields, bins=15)
    plt.xlabel('Final Amine Yield (%)')
    plt.ylabel('Frequency')
    plt.title(f'MC Distribution (median boost {median_boost:.1e})')
    plt.savefig('figures/mc_histogram.png')
    plt.close()
    
    # Demo runs
    print("Running standard simulation (25°C, no enhancement):")
    simulate_hydrogenation(boost=1.0, T=298, enhanced=False)
    
    print("\nRunning enhanced simulation (25°C, median resonance boost):")
    simulate_hydrogenation(boost=median_boost, T=298, enhanced=True)
