import pygmt

fig = pygmt.Figure()
map_scale = 'f39/36.2/36.2/400+u'
topo_data = "@earth_relief_15s"
frame = ["WSne", "xaf+lx-axis", "yaf+ly-axis"]
style = "c0.3c"  # Style for the scatter for plotting stations
pen_t = "black"  # Pen outline
region = [34, 42, 35.5, 40]

FONT_SEHIR = "10p,Helvetica-Bold"


fig = pygmt.Figure()


region_inset = [25, 46, 35, 43]
pygmt.makecpt(
    cmap='gray',
    series='-8000/5000/1000',  # min elevation of -8000m and max of 5000m
    continuous=True
)
fig.grdimage(
    grid=topo_data,
    region=region_inset,
    projection='M15c',
    shading=True, )
fig.coast(borders=["1/0.5p,black", "3/1p,black"], shorelines=True, frame=frame, map_scale=map_scale)


fig.plot(data="figure_1/boundaries.txt", pen="0.3p,black")


rectangle = [[region[0], region[2], region[1], region[3]]]
fig.plot(data=rectangle, style="r+s", pen="3p,blue")


fig.text(x=26, y=42.3, text="(a)", font="12p,Helvetica-Bold", fill="gray")

fig.plot(data='figure_1/fault1.txt', pen="3p,darkblue", label="Mw=7.8")
fig.plot(data='figure_1/fault2.txt', pen="3p,darkred", label="Mw=7.5")

fig.plot(data="figure_1/EAF.txt", pen="2p,darkgreen,4_2:2p", label="EAFZ")
fig.plot(data="figure_1/NAF.txt", pen="2p,darkorange,4_2:2p", label="NAFZ")

fig.text(x=32.83001681429794, y=39.93463694351935, text="Ankara", font="10p,Helvetica-Bold", fill="gray")
fig.text(x=29.0, y=40.9, text="Istanbul", font="10p,Helvetica-Bold", fill="gray")


fig.legend(position='JBL+jBL+o0.2c', box='+ggray+p1p')
fig.show()
fig.savefig("figure_1/fig1_a.pdf")