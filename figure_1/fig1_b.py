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

fig.plot(data="figure_1/boundaries.txt", pen="1p,black")

fig.plot(data='figure_1/fault1.txt', pen="5p,darkblue", label="Mw=7.8")
fig.plot(data='figure_1/fault2.txt', pen="5p,darkred", label="Mw=7.5")


fig.plot(data="figure_1/erkenek.txt", pen="5p,red,4_2:1p", label="Erkenek (7.27)")
fig.plot(data="figure_1/pazarcik.txt", pen="5p,mediumorchid4,4_2:1p", label="Pazarcik (7.30)")
fig.plot(data="figure_1/amanos.txt", pen="5p,orange3,4_2:1p", label="Amanos (7.46)")
fig.plot(data="figure_1/narli.txt", pen="5p,maroon,4_2:1p", label="Narli (6.73)")
fig.plot(data="figure_1/sakcagoz.txt", pen="5p,green,4_2:1p", label="Sakcagoz (7.30)")

fig.plot(data="figure_1/cardak.txt", pen="5p,coral,4_2:1p", label="Cardak (7.32)")
fig.plot(data="figure_1/surgu-1.txt", pen="5p,cyan1,4_2:1p", label="Surgu-1 (6.90)")
fig.plot(data="figure_1/surgu-2.txt", pen="5p,cyan4,4_2:1p", label="Surgu-2 (6.71)")


fig.text(x=37.38, y=37, text="Gaziantep", font=FONT_SEHIR)

fig.plot(x=[36.75, 36.15], y=[36.1, 36.2], pen="1p,black")
fig.text(x=37, y=36.1, text="Hatay", font=FONT_SEHIR)

fig.text(x=38.2, y=37.76413947225471, text="Adiyaman", font=FONT_SEHIR)
fig.text(x=38, y=38.5, text="Malatya", font=FONT_SEHIR)
fig.text(x=35.4, y=37.4, text="Adana", font=FONT_SEHIR)
fig.text(x=35.48391085467958, y=38.5, text="Kayseri", font=FONT_SEHIR)
fig.text(x=36.9, y=37.7, text="Kahramanmaras", font=FONT_SEHIR)

fig.text(x=34.5, y=39.8, text="(b)", font="12p,Helvetica-Bold", fill="gray")


fig.legend(position='JBL+jBL+o0.2c', box='+ggray+p1p',)
fig.show()
fig.savefig("figure_1/fig1_b.pdf")
