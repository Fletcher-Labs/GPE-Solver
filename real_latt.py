from gpe import LatticeGPE

#Load GPE
sim = LatticeGPE("Lattice",3,0,80)

# Grid parameters
sim.setGridSize(64)

# Contact interaction
# Only the product (atomNumber - 1) * scatteringLength is important
sim.set("atomNumber",       2)
sim.set("scatteringLength", 1)

# Dipolar interaction (switched off)
sim.set("dipolarLength", 1)
sim.set("evolutionDipolar", True)

# Number of threads. Equals number of cores if not set
# sim.setThreads(4)

sim.initialize()

# Real time evolution
sim.rte(steps=10000, monitorSteps=500, plotSteps=500)