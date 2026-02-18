import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def cleanup(df):
    df = df.rename(columns={'q (AU)': 'q',
                            'Q (AU)': 'Q',
                            'i (deg)': 'i',
                            'P (yr)': 'p',
                            'MOID (AU)': 'moid_earth'
                            })
    df = df.dropna(subset=['Q', 'q','e'])
    df = df[df['Q'] >= df['q']]
    return df

def plot_perihelion_aphelion(df):
    Q = df['Q']
    q = df['q']
    plt.plot([Q.min(), Q.max()], [q.min(), q.max()], linestyle='--')
    plt.scatter(Q, q, c=df['e'], cmap='viridis',s=5)
    plt.colorbar(label='Eccentricity (e)')
    plt.xlabel('Max distance from sun')
    plt.ylabel('Min distance from sun')
    plt.title('Min and Max distance from sun in AU unit')
    plt.show()

def orbital_period(df):
    p = pd.to_numeric(df['p'], errors='coerce')
    p = p[p > 0]
    yr = np.log10(p)
    yr.plot(kind='kde',color='black')
    plt.xlabel('(Orbital Period in years)\nin log10 scale')
    plt.ylabel('Number of comets')
    plt.title('Distribution of Comet Orbital Periods')
    plt.show()

def orbit_type(e):
    if e < 0.05:
        return 'circular'
    elif e<1:
        return 'elliptical'
    else :
        return 'hyperbolic'
def orbital_assignment(df):
    df=df.dropna(subset=['e'])
    df['Orbit Type']=df['e'].apply(orbit_type)
    print(df['Orbit Type'].head(100))
    #df.to_csv(r'Near-Earth_Comets_cleaned.csv',index=False)

def threat_comet(df):
    #MOID- minimum orbital intersection distance and q- min distance from sun
    #for lows value of MOID and q can be dangerous to earth or potential danger
    danger = df.loc[(df['q'] < 1.3) & (df['moid_earth'] < 0.05), ['Object_name', 'q', 'moid_earth']]
    danger['risk_score'] = (1 / danger['moid_earth']) + (1 / danger['q'])
    top_risk = danger.sort_values(by='risk_score', ascending=False)
    print("Top 10 Highest Risk Comets")
    print(top_risk[['Object_name', 'q', 'moid_earth', 'risk_score']].head(10))
    #Biela comet was subsequently observed to  be split in two and last observed in 1852 it is considered to have destroyed as meteor shower The Andromedis

def plot_orbit_range(df):
    df['orbit_range'] = df['Q'] - df['q']
    print('ORBIT RANGE\n', df['orbit_range'])
    df['orbit_range'].plot(kind='kde')
    plt.xlabel('Number of comets')
    plt.ylabel('Orbital Range')
    plt.title('Orbital range distribution')
    plt.show()

def orbit_vs_risk(df):
    df['orbit_range'] = df['Q'] - df['q']
    plt.scatter(df['orbit_range'], df['moid_earth'], s=5)
    plt.xlabel("Orbit Range")
    plt.ylabel("MOID Earth")
    plt.title("Orbit Range vs Earth Proximity")
    plt.show()

def inclination(df):
    df['inclination'] = np.where(df['i'] > 20, 'HIGH', 'LOW')
    high_count=(df['inclination']=='HIGH').sum()
    print(" HIGH Inclination",high_count, "\nLow Inclination=",(len(df['inclination'])-high_count))
    print('Inclination\n', df[['inclination','i','Object_name']])

def orbit_stability(df):
    stable = df[(df['e'] < 1) & (df['p'] < 200)]
    unstable = df[(df['e'] >= 1) | (df['p'] > 200)]
    print("Stable Orbits:", len(stable))
    print("Potentially Unstable:", len(unstable))
    #Shorter period + elliptical = predictable, Hyperbolic = comets from deep space

def reference(df):
    df = df[~df['ref'].astype(str).str.isdigit()]
    count=df['ref'].value_counts()
    print('Observatory\tNumber of observation',count)

def main():
    path = r'Near-Earth_Comets_-_Orbital_Elements_rows.csv'
    df = pd.read_csv(path)
    df = cleanup(df)

    while True:
        print("\n NEAR EARTH COMETS ANALYSIS ")
        print("1. Perihelion vs Aphelion Plot")
        print("2. Orbital Period Analysis")
        print("3. Threat Comet Analysis")
        print("4. Orbit Range Plot")
        print("5. Inclination Analysis")
        print("6. Reference Grouping")
        print("7. Orbit vs Risk Analysis")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            plot_perihelion_aphelion(df)

        elif choice == '2':
            orbital_period(df)

        elif choice == '3':
            threat_comet(df)

        elif choice == '4':
            plot_orbit_range(df)

        elif choice == '5':
            inclination(df)

        elif choice == '6':
            reference(df)

        elif choice == '7':
            orbit_vs_risk(df)

        elif choice == '0':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ ==      '__main__':
    main()