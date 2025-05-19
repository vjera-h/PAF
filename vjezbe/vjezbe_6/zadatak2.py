from harmonic_oscillator import HarmonicOscillator

if __name__ == "__main__":
    osc = HarmonicOscillator(m=1.0, k=1.0, x0=1.0, v0=0.0, dt=0.01)
    osc.sim(t_max=20)
    osc.graf()
    period = osc.izracunaj_period()
    print('period oscilacije: ',period)