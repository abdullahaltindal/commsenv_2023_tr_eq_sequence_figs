import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pygmt

plt.interactive(True)

df = pd.read_csv("figure_3/sa_vals_m77.csv")


#%%
region = [34, 41, 35.5, 40]
map_scale = 'f39/36/36/200+u'
topo_data = "@earth_relief_15s"
frame = ["WSne", "xaf+lx-axis", "yaf+ly-axis"]
style = "c0.3c"  # Style for the scatter for plotting stations
pen_t = "black"  # Pen outline

FONT_SEHIR = "10p,Helvetica-Bold"


def plot_rp(df_, col, savename, label):
    z = df_.iloc[:, col] * 981
    lower_lim = 1
    upper_lim = 3.05
    fig = pygmt.Figure()

    pygmt.makecpt(
        cmap='gray',
        series='-8000/5000/1000',  # min elevation of -8000m and max of 5000m
        continuous=True
    )
    fig.grdimage(
        grid=topo_data,
        region=region,
        projection='M15c',
        shading=True, )
    fig.coast(shorelines=True, frame=frame, map_scale=map_scale)

    fig.plot(data="figure_3/boundaries.txt", pen="1p,black")
    fig.plot(data='figure_3/fault2.txt', pen="5p,darkred", label="Mw=7.8")

    fig.plot(x=[38, 37.38], y=[36.5, 37], pen="1p,black")
    fig.text(x=38, y=36.5, text="Gaziantep", font=FONT_SEHIR)

    fig.text(x=36.15, y=36.2, text="Hatay", font=FONT_SEHIR)

    fig.text(x=38.2, y=37.76413947225471, text="Adiyaman", font=FONT_SEHIR)
    fig.text(x=38, y=38.5, text="Malatya", font=FONT_SEHIR)
    fig.text(x=35.3278830538338, y=37.2, text="Adana", font=FONT_SEHIR)
    fig.text(x=35.48391085467958, y=38.5, text="Kayseri", font=FONT_SEHIR)
    fig.text(x=36.9, y=37.7, text="Kahramanmaras", font=FONT_SEHIR)

    pygmt.makecpt(cmap="jet", reverse=False, series=[lower_lim, upper_lim], log=True)
    fig.plot(x=df_["Longitude"],
             y=df_["Latitude"],
             fill=z,
             cmap=True,
             style=style,
             pen=pen_t,
             transparency=0)

    fig.colorbar(frame=["af", f'y+l"{label}"'], position="JTC+o0c/0.25c+w5c/0.3c", Q=True)
    fig.show()
    fig.savefig(f"{savename}.pdf")


plot_rp(df.sort_values(by="PGA"), 4, "figure_3/fig3_a", label=" ")
plot_rp(df.sort_values(by="SA(0.5)"), 5, "figure_3/fig3_b", label=" ")
plot_rp(df.sort_values(by="SA(1.0)"), 6, "figure_3/fig3_c", label=" ")
