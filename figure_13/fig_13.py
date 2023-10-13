import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.interactive(True)

df_nga = pd.read_csv("figure_13/nga_west2_selected.csv", index_col=0)
periods = [float(col.split("T")[1].split("S")[0]) for col in df_nga.columns]

df_observed = pd.read_csv("figure_13/resp_spectra.csv", index_col=0)

colors_main = ["tab:blue", "tab:red", "tab:green", "tab:orange", "tab:brown"]
colors_bg = sns.color_palette("husl", n_colors=len(df_nga))


# %%
plt.figure()
for i, spec in df_nga.iterrows():
    color = colors_bg[i % len(colors_bg)]
    plt.plot(periods, np.array(spec), lw=1., zorder=98, color=color, ls="dashed", alpha=0.7)
for i, (label, spec) in enumerate(df_observed.iterrows()):
    plt.plot(periods, spec, label=label, zorder=99, lw=4,
             color=colors_main[i])

plt.plot()
plt.xlim(left=0.01, right=10)
plt.legend(loc="lower left", prop=dict(size=13))
plt.xlabel("Vibration Period (s)", fontsize=15)
plt.ylabel("Spectral Acceleration (g)", fontsize=15)
plt.grid(which="major", ls="dashed", alpha=0.5)
plt.grid(which="minor", ls="dotted", alpha=0.5)
plt.xscale("log")
plt.yscale("log")
xticks = [0.01, 0.1, 1, 10]
yticks = [0.01, 0.1, 1.0]
plt.xticks(xticks, [str(tick) for tick in xticks])
plt.yticks(yticks, [str(tick) for tick in yticks])
plt.tight_layout()
plt.savefig("figure_13/fig_13.svg")
