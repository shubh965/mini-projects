import numpy as np
import plotly.graph_objects as go

# RA and Dec in degrees
ra_deg = np.random.uniform(0, 360, 1500) 
dec_deg = np.random.uniform(-90, 90, 1500)

# RA and Dec in radians
ra = np.radians(ra_deg) 
dec = np.radians(dec_deg)

# x, y, z coordinates of stars
x = np.cos(dec) * np.cos(ra) 
y = np.cos(dec) * np.sin(ra)
z = np.sin(dec)

# theta and phi for making the sphere
theta = np.linspace(0, 2*np.pi, 200) 
phi = np.linspace(-np.pi/2, np.pi/2, 200)
theta_grid, phi_grid = np.meshgrid(theta, phi)

# x, y, z coordinates of sphere
x_sphere = np.cos(phi_grid) * np.cos(theta_grid) 
y_sphere = np.cos(phi_grid) * np.sin(theta_grid)
z_sphere = np.sin(phi_grid)

# RA Lines (-90 to 90 every 10 degrees)
ra_line_x, ra_line_y, ra_line_z = [], [], []
dec_curve = np.linspace(-np.pi / 2, np.pi / 2, 200)

for ra_val in np.radians(range(0, 360, 10)):
    ra_line_x.extend(np.cos(dec_curve) * np.cos(ra_val))
    ra_line_y.extend(np.cos(dec_curve) * np.sin(ra_val))
    ra_line_z.extend(np.sin(dec_curve))
    ra_line_x.append(None) # telling plotly to lift the pen
    ra_line_y.append(None)
    ra_line_z.append(None)

# Dec Lines (0 to 360 every 10 degrees)
dec_line_x, dec_line_y, dec_line_z = [], [], []
ra_curve = np.linspace(0, 2 * np.pi, 100)

for dec_val in np.radians(range(-80, 90, 10)):
    r = np.cos(dec_val)
    dec_line_x.extend(r * np.cos(ra_curve))
    dec_line_y.extend(r * np.sin(ra_curve))
    dec_line_z.extend(np.full_like(ra_curve, np.sin(dec_val)))
    dec_line_x.append(None) # same thing
    dec_line_y.append(None)
    dec_line_z.append(None)

# x, y, z coordinates of equator
x_equator = np.cos(theta) 
y_equator = np.sin(theta)
z_equator = np.zeros_like(theta)

# x, y, z coordinates of North and South poles
x_poles = [0, 0]
y_poles = [0, 0]
z_poles = [1, -1]

# x, y, z coordinates of Ecliptic
eps = np.radians(23.44)
x_ecliptic = np.cos(theta) * np.cos(eps)
y_ecliptic = np.sin(theta) * np.cos(eps)
z_ecliptic = np.ones_like(theta) * np.sin(eps)




# Plotting begins
fig = go.Figure()

surfacecolor = np.ones_like(x_sphere)

sphere = go.Surface(
    x = x_sphere,
    y = y_sphere,
    z = z_sphere,
    opacity = 0.15,
    showscale = False,
    surfacecolor = surfacecolor,
    colorscale = [[0, "grey"], [1, "grey"]],
    name = "Celestial Sphere"
)

equator = go.Scatter3d(
    x = x_equator,
    y = y_equator,
    z = z_equator,
    mode = "lines+text",
    name = "Celestial Equator",
    text = ["Celestial Equator"],
    textposition = "top center",
    line = dict(
        color = "black",
        width = 2
    )
)

poles = go.Scatter3d(
    x = x_poles,
    y = y_poles,
    z = z_poles,
    name = "Celestial Poles",
    mode = "markers+text",
    text = ["North Celestial Pole", "South Celestial Pole"],
    textposition = ["top center", "bottom center"],
    marker = dict(
        size = 4,
        color = "red",
        opacity = 1
    )
)

ra_grid = go.Scatter3d(
    x=ra_line_x,
    y=ra_line_y,
    z=ra_line_z,
    mode="lines",
    showlegend = False,
    line = dict(
        color = "grey", 
        width = 1
    ),
    hoverinfo = "none"
)

dec_grid = go.Scatter3d(
    x=dec_line_x,
    y=dec_line_y,
    z=dec_line_z,
    mode="lines",
    showlegend = False,
    line = dict(
        color = "grey", 
        width = 1
    ),
    hoverinfo = "none"
)

ecliptic = go.Scatter3d(
    x = x_ecliptic,
    y = y_ecliptic,
    z = z_ecliptic,
    mode = "lines+text",
    name = "Ecliptic",
    text = ["Ecliptic"],
    textposition = "top center",
    line = dict(
        color = "red",
        width = 3
    )
)

stars = go.Scatter3d(
    x = x,
    y = y,
    z = z,
    mode = "markers",
    marker = dict(
        size = 2,
        color = "black",
        opacity = 1
    ),
    name = "Stars"
)

fig.update_layout(
    title = {
        "text" : "Celestial Sphere",
        "font" : {
            "family" : "Arial",
            "size" : 24,
            "color" : "black"
        },
        "y" : 0.99,
        "yanchor" : "top"
    },
    template = "ggplot2",
    scene = dict(
        xaxis = dict(visible = False),
        yaxis = dict(visible = False),
        zaxis = dict(visible = False),
        aspectmode = 'cube'
    ),
    margin = dict(l = 0, r = 0, b = 0, t = 30)
)

fig.add_trace(equator)
fig.add_trace(ecliptic)
fig.add_trace(sphere)
fig.add_trace(ra_grid)
fig.add_trace(dec_grid)
fig.add_trace(poles)
fig.add_trace(stars)

fig.write_html("celestial_sphere.html")
fig.show()