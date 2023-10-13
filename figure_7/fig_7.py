import pandas as pd
import matplotlib.pyplot as plt
import os

plt.interactive(True)

pazarcik_df_fsm = pd.read_csv("figure_7/pazarcik_rp_fsm.csv")
elbistan_df_fsm = pd.read_csv("figure_7/elbistan_rp_fsm.csv")

pazarcik_tras_df_area = pd.read_csv("figure_7/pazarcik_tras_rp_area.csv")
pazarcik_lbas_df_area = pd.read_csv("figure_7/pazarcik_lbas_rp_area.csv")
elbistan_df_area = pd.read_csv("figure_7/elbistan_rp_area.csv")

MW_pazarcik = 7.8
MW_elbistan = 7.5
RETURN_PERIOD_pazarcik_tras_area = 3970
RETURN_PERIOD_pazarcik_lbas_area = 3492
RETURN_PERIOD_elbistan_area = 2593
RETURN_PERIOD_elbistan_fsm = 7766
RETURN_PERIOD_pazarcik_fsm = 1076

# %%
fig, axs = plt.subplots(1, 2, sharey=True, figsize=(10, 6))

# Plot Pazarcik-FSM
axs[0].plot(pazarcik_df_fsm["Magnitude"], pazarcik_df_fsm["Return Period"], color="red", lw=4, label="TRCF002")
axs[0].set_ylabel("Return Period (years)", fontsize=14)
axs[0].hlines(RETURN_PERIOD_pazarcik_fsm, 6.7, MW_pazarcik, color="red", ls="dotted", lw=2.5)
axs[0].vlines(MW_pazarcik, 0, RETURN_PERIOD_pazarcik_fsm, color="black", ls="dotted", lw=2.5)
axs[0].annotate(f"{RETURN_PERIOD_pazarcik_fsm:.0f} years", (6.7, RETURN_PERIOD_pazarcik_fsm),
                (6.9, RETURN_PERIOD_pazarcik_fsm * 0.6),
                arrowprops=dict(arrowstyle="-|>", color="darkred"), fontsize=13,
                bbox=dict(boxstyle="round4", fc="tab:red", alpha=1), zorder=10)

# Plot Pazarcik-TRAS-Area
axs[0].plot(pazarcik_tras_df_area["Magnitude"], pazarcik_tras_df_area["Return Period"], color="blue", lw=4,
            label="TRAS481")
axs[0].set_ylabel("Return Period (years)", fontsize=14)
axs[0].hlines(RETURN_PERIOD_pazarcik_tras_area, 6.7, MW_pazarcik, color="blue", ls="dotted", lw=2.5)
axs[0].vlines(MW_pazarcik, 0, RETURN_PERIOD_pazarcik_tras_area, color="black", ls="dotted", lw=2.5)
axs[0].annotate(f"{RETURN_PERIOD_pazarcik_tras_area:.0f} years", (6.7, RETURN_PERIOD_pazarcik_tras_area),
                (6.9, RETURN_PERIOD_pazarcik_tras_area * 1.8),
                arrowprops=dict(arrowstyle="-|>", color="darkblue"), fontsize=13,
                bbox=dict(boxstyle="round4", fc="dodgerblue", alpha=1), zorder=10)

# Plot Pazarcik-lbas-Area
axs[0].plot(pazarcik_lbas_df_area["Magnitude"], pazarcik_lbas_df_area["Return Period"], color="green", lw=4,
            label="LBAS341")
axs[0].set_ylabel("Return Period (years)", fontsize=14)
axs[0].hlines(RETURN_PERIOD_pazarcik_lbas_area, 6.7, MW_pazarcik, color="green", ls="dotted", lw=2.5)
axs[0].vlines(MW_pazarcik, 0, RETURN_PERIOD_pazarcik_lbas_area, color="black", ls="dotted", lw=2.5)
axs[0].annotate(f"{RETURN_PERIOD_pazarcik_lbas_area:.0f} years", (6.7, RETURN_PERIOD_pazarcik_lbas_area),
                (6.9, RETURN_PERIOD_pazarcik_lbas_area * 0.5),
                arrowprops=dict(arrowstyle="-|>", color="darkgreen"), fontsize=13,
                bbox=dict(boxstyle="round4", fc="tab:green", alpha=1), zorder=10)

# Plot Elbistan-fsm
axs[1].plot(elbistan_df_fsm["Magnitude"], elbistan_df_fsm["Return Period"], color="red", lw=4,
            label="TRCF03H")
axs[1].set_ylabel("Return Period (years)", fontsize=14)
axs[1].hlines(RETURN_PERIOD_elbistan_fsm, 6.7, MW_elbistan, color="red", ls="dotted", lw=2.5)
axs[1].vlines(MW_elbistan, 0, RETURN_PERIOD_elbistan_fsm, color="black", ls="dotted", lw=2.5)
axs[1].annotate(f"{RETURN_PERIOD_elbistan_fsm:.0f} years", (6.7, RETURN_PERIOD_elbistan_fsm),
                (6.9, RETURN_PERIOD_elbistan_fsm * 1.9),
                arrowprops=dict(arrowstyle="-|>", color="darkred"), fontsize=13,
                bbox=dict(boxstyle="round4", fc="tab:red", alpha=1))

# Plot Elbistan-area
axs[1].plot(elbistan_df_area["Magnitude"], elbistan_df_area["Return Period"], color="green", lw=4,
            label="TRAS434")
axs[1].set_ylabel("Return Period (years)", fontsize=14)
axs[1].hlines(RETURN_PERIOD_elbistan_area, 6.7, MW_elbistan, color="green", ls="dotted", lw=2.5)
axs[1].vlines(MW_elbistan, 0, RETURN_PERIOD_elbistan_area, color="black", ls="dotted", lw=2.5)
axs[1].annotate(f"{RETURN_PERIOD_elbistan_area:.0f} years", (6.7, RETURN_PERIOD_elbistan_area),
                (6.9, RETURN_PERIOD_elbistan_area * 1.4),
                arrowprops=dict(arrowstyle="-|>", color="darkgreen"), fontsize=13,
                bbox=dict(boxstyle="round4", fc="tab:green", alpha=1))


axs[0].set_xlim(left=6.7, right=7.9)
axs[1].set_xlim(left=6.7, right=7.9)
axs[1].set_xticks([6.7, 6.9, 7.1, 7.3, 7.5, 7.7, 7.9])


for i, ax in enumerate(axs):
    ax.set_yscale("log")
    ax.set_xlabel("Moment Magnitude, $Mw$", fontsize=14)
    ax.grid(which="major", ls="dashed")
    ax.grid(which="minor", ls="dotted")
    ax.yaxis.set_tick_params(labelleft=True)
    ax.legend(prop=dict(size=14), loc="upper left")
    ax.set_title(["(a)", "(b)"][i], x=-0.05, fontsize=14)

for fname in os.listdir('figure_7/trcf002'):
    df_ = pd.read_csv(f"figure_7/trcf002/{fname}")
    axs[0].plot(df_["Magnitude"], df_["Return Period"], color='red', lw=0.3, zorder=-10, alpha=0.5)
    
for fname in os.listdir('figure_7/lbas341'):
    df_ = pd.read_csv(f"figure_7/lbas341/{fname}")
    axs[0].plot(df_["Magnitude"], df_["Return Period"], color='green', lw=0.3, zorder=-10, alpha=0.5)

for fname in os.listdir('figure_7/tras481'):
    df_ = pd.read_csv(f"figure_7/tras481/{fname}")
    axs[0].plot(df_["Magnitude"], df_["Return Period"], color='blue', lw=0.3, zorder=-10, alpha=0.5)

for fname in os.listdir('figure_7/trcf03h'):
    df_ = pd.read_csv(f"figure_7/trcf03h/{fname}")
    axs[1].plot(df_["Magnitude"], df_["Return Period"], color='red', lw=0.3, zorder=-10, alpha=0.5)


for fname in os.listdir('figure_7/tras434'):
    df_ = pd.read_csv(f"figure_7/tras434/{fname}")
    axs[1].plot(df_["Magnitude"], df_["Return Period"], color='green', lw=0.3, zorder=-10, alpha=0.5)

axs[0].set_ylim(40, 400000)
axs[1].set_ylim(40, 400000)

plt.tight_layout()
plt.savefig("figure_7/fig_7.svg")
