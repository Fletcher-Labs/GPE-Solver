from gpe import HarmonicTrapGPE

# Load GPE
sim = HarmonicTrapGPE("Real", 0.33, 0.33, 1.0)

# Grid parameters
sim.setGridSize(64)

# Contact interaction
# Only the product (atomNumber - 1) * scatteringLength is important
sim.set("atomNumber", 15000)
sim.set("scatteringLength", 0.009)

# Dipolar interaction (switched on)
sim.set("dipolarLength", 0.01)
sim.set("evolutionDipolar", True)

# Number of threads. Equals number of cores if not set
# sim.setThreads(4)

sim.initialize()

# initial imaginary time evolution
sim.ite(steps=3000, monitorSteps=500, plotSteps=500)

# Real time evolution
#sim.rte(steps=4000, monitorSteps=1000, plotSteps=1000)


# ROUGH QUENCH RAMP (small adjustment, equilibration, short evolution)
#sim.set("scatteringLength", 10.0)
#sim.rte(steps=100, monitorSteps=100, plotSteps=100)
#sim.set("scatteringLength", 9.0)
#sim.rte(steps=100, monitorSteps=100, plotSteps=100)
#sim.set("scatteringLength", 8.0)
#sim.rte(steps=100, monitorSteps=100, plotSteps=100)
#sim.set("scatteringLength", 7.0)

# resume evolution to see droplet formation
#sim.rte(steps=12700, monitorSteps=1000, plotSteps=1000)

# imaginary time evolution to find droplet ground state
sim.ite(steps=3000, monitorSteps=500, plotSteps=500)


