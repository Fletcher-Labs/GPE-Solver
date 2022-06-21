from gpe import HarmonicTrapGPE

# Load GPE
sim = HarmonicTrapGPE("Real", 75, 200, 75)

# Grid parameters
sim.setGridSize(64)

# Contact interaction
# Only the product (atomNumber - 1) * scatteringLength is important
sim.set("atomNumber", 2)
sim.set("scatteringLength", 11.0)

# Dipolar interaction (switched on)
sim.set("dipolarLength", 9.0)
sim.set("evolutionDipolar", True)

# Number of threads. Equals number of cores if not set
# sim.setThreads(4)

sim.initialize()

# initial imaginary time evolution
sim.ite(steps=1000, monitorSteps=500, plotSteps=500)

# Real time evolution
sim.rte(steps=2000, monitorSteps=1000, plotSteps=1000)


# ROUGH QUENCH RAMP (small adjustment, equilibration, short evolution)
sim.set("scatteringLength", 10.0)
sim.ite(steps=500, monitorSteps=500, plotSteps=500)
sim.rte(steps=1000, monitorSteps=1000, plotSteps=1000)
sim.set("scatteringLength", 9.0)
sim.ite(steps=500, monitorSteps=500, plotSteps=500)
sim.rte(steps=1000, monitorSteps=1000, plotSteps=1000)
sim.set("scatteringLength", 8.0)
sim.ite(steps=500, monitorSteps=500, plotSteps=500)
sim.rte(steps=1000, monitorSteps=1000, plotSteps=1000)
sim.set("scatteringLength", 7.0)
sim.ite(steps=500, monitorSteps=500, plotSteps=500)
sim.rte(steps=1000, monitorSteps=1000, plotSteps=1000)

#resume evolution to see droplet formation
sim.rte(steps=5000, monitorSteps=1000, plotSteps=1000)