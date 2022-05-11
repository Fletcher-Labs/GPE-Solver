from gpe import HarmonicTrapGPE

# Load GPE
sim = HarmonicTrapGPE("Real", 200, 10, 200)

# Grid parameters
sim.setGridSize(64)

# Contact interaction
# Only the product (atomNumber - 1) * scatteringLength is important
sim.set("atomNumber",       10**5)
sim.set("scatteringLength", 100)

# Dipolar interaction (switched on)
sim.set("dipolarLength", 80)
sim.set("evolutionDipolar", True)

# Number of threads. Equals number of cores if not set
# sim.setThreads(4)

sim.initialize()

# Imaginary time evolution
sim.ite(steps=2000, monitorSteps=500, plotSteps=500)

# Real time evolution
sim.rte(steps=4000, monitorSteps=500, plotSteps=500)

# adjust trap
sim.set("omegaY",20)
sim.set("scatteringLength", 60)

#resume evolution
sim.rte(steps=4000, monitorSteps=500, plotSteps=500)
