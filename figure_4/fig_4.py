import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

plt.interactive(True)

observed = 0.94
lat = 36.23808
lon = 36.13264

hazard_3125 = pd.read_csv("figure_4/PGA.csv")

levels = np.array([float(level.split("-")[1]) for level in hazard_3125.columns[3:]])
poes = np.array(hazard_3125.iloc[:, 3:]).flatten()
return_period_func = interp1d(levels, poes, kind="quadratic")
poe = return_period_func(observed)
return_period = poe ** -1

#%%
plt.figure()
plt.plot(levels, poes, color="black")
plt.xscale("log")
plt.yscale("log")
plt.grid(which="major", ls="dashed")
plt.grid(which="minor", ls="dotted")
plt.xlabel("Peak Ground Acceleration, $PGA (g)$", fontsize=14)
plt.ylabel("Annual Rate of Exceedance", fontsize=14)

plt.xlim(left=min(levels))
plt.ylim(bottom=min(poes))
plt.hlines(poe, min(levels), observed, color="gray", ls="dashed")
plt.vlines(observed, min(poes), poe, color="gray", ls="dashed")
xticks = [0.001, 0.01, 0.1, 1.0, 3.0]
plt.xticks(xticks, [str(tick) for tick in xticks])
text = f"Mean return period = ${poe:.6f}^{{-1}}\\approx{round(return_period, -1):.0f}\ years$"
t = plt.text(0.001, 0.0006, text)
t.set_bbox(dict(facecolor='lightgray', alpha=1, edgecolor='black'))
plt.tight_layout()
plt.savefig("figure_4/fig_4.svg")


