# 3D Celestial Sphere
An interactive 3D Celestial Sphere visualization built with **Python**, **NumPy**, and **Plotly**. This project models the celestial coordinate system with stars, celestial poles, coordinate grids (Right Ascension and Declination), the celestial equator, and the ecliptic.


## Features
- **Translucent Celestial Sphere**: A 3D unit sphere representing the sky surrounding Earth.
- **Stars & Celestial Objects**: 1,500 randomly generated star positions projected onto the sphere using spherical coordinates $(x, y, z)$.
- **Celestial Equator & Poles**: Clearly marked Celestial Equator ($0^\circ$ Dec) and North/South Celestial Poles ($\pm 90^\circ$ Dec).
- **Ecliptic Plane**: Path of the Sun across the celestial sphere, inclined at an obliquity of $\approx 23.44^\circ$.
- **Coordinate Grid (RA & Dec)**:
  - **Right Ascension (RA) Meridians**: Drawn every $10^\circ$ from North to South Pole.
  - **Declination (Dec) Parallels**: Drawn every $10^\circ$ parallel to the celestial equator.
  - Optimized to render through segmented coordinates using single `Scatter3d` traces.
- **Export & Interactivity**: Interactive pan/zoom/rotate in the browser and exports automatically to an HTML file (`celestial_sphere.html`).


## Prerequisites & Installation
Ensure you have Python installed, then install the required dependencies:
```bash
pip install numpy plotly
```

## Usage
Run the main script:
```bash
python celestial_sphere.py
```

## Mathematical Formulation
Converting celestial coordinates (Right Ascension $\alpha$, Declination $\delta$) on a unit sphere ($R=1$) to 3D Cartesian coordinates $(x, y, z)$:
$$x = \cos(\delta) \cos(\alpha)$$
$$y = \cos(\delta) \sin(\alpha)$$
$$z = \sin(\delta)$$


## Project Structure
```text
3D Celestial Sphere/
├── celestial_sphere.py      # Main script to compute geometry and render 3D plot
├── celestial_sphere.html    # Standalone interactive Plotly HTML output
└── README.md      # Project overview and instructions
```
