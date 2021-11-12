from gpe import HarmonicTrapGPE

# Load GPE
sim = HarmonicTrapGPE("Real", 1.0, 5.0, 5.0)

# Grid parameters
sim.setGridSize(64)

# Contact interaction
# Only the product (atomNumber - 1) * scatteringLength is important
sim.set("atomNumber",       2)
sim.set("scatteringLength", 1)

# Dipolar interaction (switched on)
sim.set("dipolarLength", 1)
sim.set("evolutionDipolar", True)

# Number of threads. Equals number of cores if not set
# sim.setThreads(4)

sim.initialize()

# Imaginary time evolution
#sim.ite(steps=5000, monitorSteps=1000, plotSteps=1000)

# Real time evolution
sim.rte(steps=5000, monitorSteps=500, plotSteps=500)
