from gpe import HarmonicTrapGPE

# Load GPE
sim = HarmonicTrapGPE("Real", 75, 200, 75)

# Grid parameters
sim.setGridSize(64)

# Contact interaction
# Only the product (atomNumber - 1) * scatteringLength is important
sim.set("atomNumber", 5)
sim.set("scatteringLength", 11)

# Dipolar interaction (switched on)
sim.set("dipolarLength", 10)
sim.set("evolutionDipolar", True)

# Number of threads. Equals number of cores if not set
# sim.setThreads(4)

sim.initialize()

# Imaginary time evolution
sim.ite(steps=1500, monitorSteps=500, plotSteps=500)

# Real time evolution
sim.rte(steps=5500, monitorSteps=1000, plotSteps=1000)

# adjust trap/quench
#sim.set("omegaY",20.0)
sim.set("scatteringLength", 8.0)

#resume evolution
sim.rte(steps=7000, monitorSteps=1000, plotSteps=1000)
