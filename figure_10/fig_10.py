import pandas as pd
import matplotlib.pyplot as plt
plt.interactive(True)


df_pazarcik = pd.read_csv("figure_10/return_periods_pazarcik.csv").sort_values(by="Station ID")
df_elbistan = pd.read_csv("figure_10/return_periods_elbistan.csv").sort_values(by="Station ID")

df_pazarcik_16 = pd.read_csv("figure_10/return_periods_pazarcik_16.csv").sort_values(by="Station ID")
df_elbistan_16 = pd.read_csv("figure_10/return_periods_elbistan_16.csv").sort_values(by="Station ID")
df_pazarcik_84 = pd.read_csv("figure_10/return_periods_pazarcik_84.csv").sort_values(by="Station ID")
df_elbistan_84 = pd.read_csv("figure_10/return_periods_elbistan_84.csv").sort_values(by="Station ID")

resp_spec_pazarcik = pd.read_csv("figure_10/sa_vals_pazarcik.csv")
filt_pazarcik = [st in list(df_pazarcik["Station ID"].astype(str)) for st in list(resp_spec_pazarcik["Station ID"].astype(str))]
resp_spec_pazarcik = resp_spec_pazarcik[filt_pazarcik].sort_values(by="Station ID")

resp_spec_elbistan = pd.read_csv("figure_10/sa_vals_elbistan.csv")
filt_elbistan = [st in list(df_elbistan["Station ID"].astype(str)) for st in list(resp_spec_elbistan["Station ID"].astype(str))]
resp_spec_elbistan = resp_spec_elbistan[filt_elbistan].sort_values(by="Station ID")


fig, axs = plt.subplots(1, 3, sharey=True, figsize=(10, 5))

axs[0].scatter(resp_spec_pazarcik["PGA"], df_pazarcik["PGA"], ec="black", fc="tab:red", zorder=99, s=60, label="Mw=7.8")
axs[0].scatter(resp_spec_elbistan["PGA"], df_elbistan["PGA"], ec="black", fc="tab:blue", zorder=99, s=60, label="Mw=7.5")

axs[1].scatter(resp_spec_pazarcik["SA(0.5)"], df_pazarcik["SA(0.5)"], ec="black", fc="tab:red", zorder=99, s=60, label="$Mw=7.8$")
axs[1].scatter(resp_spec_elbistan["SA(0.5)"], df_elbistan["SA(0.5)"], ec="black", fc="tab:blue", zorder=99, s=60, label="$Mw=7.5$")

axs[2].scatter(resp_spec_pazarcik["SA(1.0)"], df_pazarcik["SA(1.0)"], ec="black", fc="tab:red", zorder=99, s=60, label="Mw=7.8")
axs[2].scatter(resp_spec_elbistan["SA(1.0)"], df_elbistan["SA(1.0)"], ec="black", fc="tab:blue", zorder=99, s=60, label="Mw=7.5")


for st in df_elbistan_16['Station ID']:
    pga = float(resp_spec_elbistan[resp_spec_elbistan['Station ID'] == st]['PGA'])
    low_pga = float(df_elbistan_16[df_elbistan_16['Station ID'] == st]["PGA"])
    high_pga = float(df_elbistan_84[df_elbistan_84['Station ID'] == st]["PGA"])
    axs[0].plot([pga, pga], [low_pga, high_pga], color='tab:blue', alpha=0.5)

    sa0p5 = float(resp_spec_elbistan[resp_spec_elbistan['Station ID'] == st]['SA(0.5)'])
    low_sa0p5 = float(df_elbistan_16[df_elbistan_16['Station ID'] == st]["SA(0.5)"])
    high_sa0p5 = float(df_elbistan_84[df_elbistan_84['Station ID'] == st]["SA(0.5)"])
    axs[1].plot([sa0p5, sa0p5], [low_sa0p5, high_sa0p5], color='tab:blue', alpha=0.5)

    sa1p0 = float(resp_spec_elbistan[resp_spec_elbistan['Station ID'] == st]['SA(1.0)'])
    low_sa1p0 = float(df_elbistan_16[df_elbistan_16['Station ID'] == st]["SA(1.0)"])
    high_sa1p0 = float(df_elbistan_84[df_elbistan_84['Station ID'] == st]["SA(1.0)"])
    axs[2].plot([sa1p0, sa1p0], [low_sa1p0, high_sa1p0], color='tab:blue', alpha=0.5)

for st in df_pazarcik_16['Station ID']:
    pga = float(resp_spec_pazarcik[resp_spec_pazarcik['Station ID'] == st]['PGA'])
    low_pga = float(df_pazarcik_16[df_pazarcik_16['Station ID'] == st]["PGA"])
    high_pga = float(df_pazarcik_84[df_pazarcik_84['Station ID'] == st]["PGA"])
    axs[0].plot([pga, pga], [low_pga, high_pga], color='tab:red', alpha=0.5)

    sa0p5 = float(resp_spec_pazarcik[resp_spec_pazarcik['Station ID'] == st]['SA(0.5)'])
    low_sa0p5 = float(df_pazarcik_16[df_pazarcik_16['Station ID'] == st]["SA(0.5)"])
    high_sa0p5 = float(df_pazarcik_84[df_pazarcik_84['Station ID'] == st]["SA(0.5)"])
    axs[1].plot([sa0p5, sa0p5], [low_sa0p5, high_sa0p5], color='tab:red', alpha=0.5)

    sa1p0 = float(resp_spec_pazarcik[resp_spec_pazarcik['Station ID'] == st]['SA(1.0)'])
    low_sa1p0 = float(df_pazarcik_16[df_pazarcik_16['Station ID'] == st]["SA(1.0)"])
    high_sa1p0 = float(df_pazarcik_84[df_pazarcik_84['Station ID'] == st]["SA(1.0)"])
    axs[2].plot([sa1p0, sa1p0], [low_sa1p0, high_sa1p0], color='tab:red', alpha=0.5)

for i, ax in enumerate(axs):
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(["$PGA(g)$", "$SA_{T=0.5s}(g)$", "$SA_{T=1s}(g)$"][i], fontsize=14)
    ax.set_title(["(a)", "(b)", "(c)"][i], x=-0.05, fontsize=16)
    ax.set_xlim(left=0.015, right=3)
    ax.set_ylim(bottom=10, top=4e5)
    ax.grid(which="major", ls="dashed")
    ax.grid(which="minor", ls="dotted")
    ax.set_xticks([0.1, 0.3, 1, 3])
    ax.set_xticklabels(["0.1", "0.3", "1.0", "3.0"])
    ax.set_yticks([100, 1000, 10000, 100000])

axs[0].set_ylabel("Return Period (years)", fontsize=14)
axs[1].legend(prop=dict(size=12))

plt.tight_layout()
plt.savefig("figure_10/fig_10.svg")

