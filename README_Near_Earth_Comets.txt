
NEAR-EARTH COMETS ORBITAL ANALYSIS

This project performs data analysis on Near-Earth Comets using real orbital datasets to understand:

- Orbital behaviour
- Earth proximity risk
- Stability of comet trajectories
- Inclination patterns
- Observational sources

The project is built using Python, Pandas, NumPy, and Matplotlib and provides an interactive CLI-based analysis menu.

OBJECTIVE

The goal of this project is to explore how comet orbital elements relate to:

- Their distance from Earth
- Potential threat level
- Orbit type & stability
- Orbital spread across the solar system

KEY CONCEPTS USED

- Data Cleaning
- Feature Engineering
- Risk Scoring Logic
- Scientific Data Visualization
- Orbit Classification

TECH STACK

- Python
- Pandas
- NumPy
- Matplotlib

DATASET

Near-Earth Comets Orbital Elements including:

- Perihelion Distance (q)
- Aphelion Distance (Q)
- Eccentricity (e)
- Orbital Period (P)
- Inclination (i)
- MOID (Minimum Orbit Intersection Distance with Earth)
- Reference Observatory

ANALYSIS FEATURES

1. Orbit Distance Visualization
Plots minimum vs maximum distance from the Sun and color-codes by eccentricity.

2. Orbital Period Distribution
Log-scale KDE plot showing distribution of comet orbital periods.

3. Orbit Classification
Classifies orbits into Circular, Elliptical, Hyperbolic.

4. Threat Detection
Identifies potentially dangerous comets using low perihelion distance and low MOID.

Risk Score:
risk_score = (1 / MOID) + (1 / q)

5. Orbital Range Analysis
Orbit Range = Q - q

6. Orbit vs Earth Proximity
Scatter plot comparing orbital spread and Earth intersection distance.

7. Inclination Analysis
HIGH inclination (>20°)
LOW inclination (≤20°)

8. Orbit Stability Check
Stable orbits → Elliptical + Short Period
Potentially unstable → Hyperbolic or Long Period

9. Observatory Source Analysis
Groups observations by reference source after filtering numeric-only codes.

HOW TO RUN

Step 1 — Install Dependencies
pip install pandas numpy matplotlib

Step 2 — Place Dataset
Near-Earth_Comets_-_Orbital_Elements_rows.csv in same folder

Step 3 — Run
python main.py

REAL-WORLD RELEVANCE

This project demonstrates how space science data can be used for:

- Risk modelling
- Orbit behaviour analysis
- Predictability of celestial objects

FUTURE IMPROVEMENTS

- Automated report generation
- Machine learning risk prediction
- Time-based orbit simulation
- Dashboard visualization

AUTHOR

Kenez Nonwar
Aspiring Data Analyst / AI Enthusiast

Skills applied:
Python • Pandas • NumPy • Matplotlib • Data Cleaning • Scientific Analysis
