import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

epsilon_df_pazarcik = pd.read_csv("figure_11/epsilon_df_pazarcik.csv", index_col=0)
epsilon_df_elbistan = pd.read_csv("figure_11/epsilon_df_elbistan.csv", index_col=0)

mean_epsilons_pazarcik = epsilon_df_pazarcik.mean(axis=0)
std_epsilons_pazarcik = epsilon_df_pazarcik.std(axis=0)

mean_epsilons_elbistan = epsilon_df_elbistan.mean(axis=0)
std_epsilons_elbistan = epsilon_df_elbistan.std(axis=0)

def get_station(filename):
    station = filename.split("_")[1]
    if station.startswith("0"):
        return station[1:]
    else:
        return station

periods = np.array([0.01, 0.02, 0.03, 0.05, 0.075, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0,
                    4.0, 5.0, 7.5, 10])

plt.interactive(True)

fig, axs = plt.subplots(1, 2, sharey=True, figsize=(8, 5))

for fname, row in epsilon_df_pazarcik.iterrows():
    if get_station(fname) == "3135":
        axs[0].plot(periods, row, color="darkblue", lw=2, label="$\epsilon_{3135}$", zorder=99)
    else:
        axs[0].plot(periods, row, color="gray", lw=0.3)

for fname, row in epsilon_df_elbistan.iterrows():
    axs[1].plot(periods, row, color="gray", lw=0.3)

axs[0].plot(periods, mean_epsilons_pazarcik, color="black", lw=3, label="$\mu_{\epsilon}$", zorder=90)
axs[0].plot(periods, mean_epsilons_pazarcik+std_epsilons_pazarcik, color="black", lw=2, ls="dashed", label="$\mu_{\epsilon}\pm\sigma_{\epsilon}$", zorder=90)
axs[0].plot(periods, mean_epsilons_pazarcik-std_epsilons_pazarcik, color="black", lw=2, ls="dashed", zorder=90)

axs[1].plot(periods, mean_epsilons_elbistan, color="black", lw=3, label="$\mu_{\epsilon}$", zorder=90)
axs[1].plot(periods, mean_epsilons_elbistan+std_epsilons_elbistan, color="black", lw=2, ls="dashed", label="$\mu_{\epsilon}\pm\sigma_{\epsilon}$", zorder=90)
axs[1].plot(periods, mean_epsilons_elbistan-std_epsilons_elbistan, color="black", lw=2, ls="dashed", zorder=90)

yticklabels = [
    "-3 $(99.9\%)$",
    "-2 $(97.7\%)$",
    "-1 $(84.1\%)$",
    "0 $(50.0\%)$",
    "1 $(15.9\%)$",
    "2 $(2.3\%)$",
    "3 $(0.1\%)$"
]

for i, ax in enumerate(axs):
    ax.axhline(0, lw=2, color="darkred", label="$\epsilon=0$", zorder=2)
    ax.axhline(1, lw=2, color="darkred", ls="dashed", label="$\epsilon=\pm1$", zorder=2)
    ax.axhline(-1, lw=2, color="darkred", ls="dashed", zorder=2)
    ax.set_xlim(left=0.01, right=10)
    ax.set_ylim(bottom=-3.5, top=3.5)
    ax.set_xlabel("Vibration Period (s)", fontsize=14)
    ax.set_xscale("log")
    ax.set_xticks([0.01, 0.1, 1, 10])
    ax.set_xticklabels(["0.01", "0.1", "1.0", "10.0"])
    ax.set_yticks([-3, -2, -1, 0, 1, 2, 3])
    ax.set_yticklabels(yticklabels)
    ax.grid(which="major", ls="dashed", zorder=0)
    ax.grid(which="minor", ls="dotted", zorder=0)
    ax.legend()
    ax.set_title(["(a)", "(b)"][i], x=-0.05)

axs[0].set_ylabel("Residual Spectral Acceleration, $\epsilon$", fontsize=12)
plt.tight_layout()
plt.savefig("figure_11/fig_11.svg")
