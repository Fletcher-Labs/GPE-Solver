from gpe import HarmonicTrapGPE

# Load GPE
sim = HarmonicTrapGPE("Real", 190.0, 15.0, 191.0)

# Grid parameters
sim.setGridSize(64)

# Contact interaction
# Only the product (atomNumber - 1) * scatteringLength is important
sim.set("atomNumber", 2)
sim.set("scatteringLength", 1.2)

# Dipolar interaction (switched on)
sim.set("dipolarLength", 1.0)
sim.set("evolutionDipolar", True)

# Number of threads. Equals number of cores if not set
# sim.setThreads(4)

sim.initialize()

# Imaginary time evolution
sim.ite(steps=2000, monitorSteps=500, plotSteps=500)

# Real time evolution
sim.rte(steps=4000, monitorSteps=500, plotSteps=500)

# adjust trap/quench
sim.set("omegaY",20.0)
sim.set("scatteringLength", 0.8)

#resume evolution
sim.rte(steps=4000, monitorSteps=500, plotSteps=500)
