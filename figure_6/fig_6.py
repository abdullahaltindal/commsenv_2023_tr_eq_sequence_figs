import pygmt

fig = pygmt.Figure()
map_scale = 'f40/36/36/200+u'
topo_data = "@earth_relief_15s"
frame = ["WSne", "xaf+lx-axis", "yaf+ly-axis"]
style = "c0.3c"  # Style for the scatter for plotting stations
pen_t = "black"  # Pen outline
region = [34, 42, 35.5, 40]

FONT_SEHIR = "10p,Helvetica-Bold"

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

fig.plot(data="figure_6/boundaries.txt", pen="1p,black")

fig.plot(data='figure_6/LBAS341.txt', pen="3p,darkorange,2p_2p", label="LBAS341", fill="darkorange", transparency=50)
fig.plot(data='figure_6/LBAS341.txt', pen="3p,darkorange,2p_2p")

fig.plot(data='figure_6/TRAS434.txt', pen="3p,cyan,2p_2p", label="TRAS434", fill="cyan", transparency=50)
fig.plot(data='figure_6/TRAS434.txt', pen="3p,cyan,2p_2p")

fig.plot(data='figure_6/TRAS481.txt', pen="3p,mediumpurple4,4p_1p", label="TRAS481", fill="mediumpurple4", transparency=50)
fig.plot(data='figure_6/TRAS481.txt', pen="3p,mediumpurple4,4p_1p")


fig.plot(data='figure_6/TRCF002.txt', pen="5p,darkgreen,3p_1p", label="TRCF002")
fig.plot(data='figure_6/TRCF03H.txt', pen="5p,yellow,3p_1p", label="TRCF03H")

fig.plot(data='figure_6/fault1.txt', pen="5p,darkblue,5p_5p", label="Mw=7.8")
fig.plot(data='figure_6/fault2.txt', pen="5p,darkred,5p_5p", label="Mw=7.5")

fig.text(x=37.38, y=37, text="Gaziantep", font=FONT_SEHIR)

fig.plot(x=[35.5, 36.15], y=[36.1, 36.2], pen="1p,black")
fig.text(x=35.5, y=36.1, text="Hatay", font=FONT_SEHIR)

fig.text(x=38.2, y=37.76413947225471, text="Adiyaman", font=FONT_SEHIR)
fig.text(x=38, y=38.5, text="Malatya", font=FONT_SEHIR)
fig.text(x=35.3278830538338, y=37.2, text="Adana", font=FONT_SEHIR)
fig.text(x=35.48391085467958, y=38.5, text="Kayseri", font=FONT_SEHIR)
fig.text(x=36.9, y=37.7, text="Kahramanmaras", font=FONT_SEHIR)
fig.legend(position='JTL+jTL+o0.2c', box='+ggray+p1p',)
fig.savefig("figure_6/fig_6.pdf")
