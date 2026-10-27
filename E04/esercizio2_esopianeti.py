import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#punto 1
df2 = pd.read_csv('ExoplanetsPars_2025.csv', comment ='#')

#punto 2
print(df2.columns)

#punto 3
print(df2.iloc[5:8])

#punto 4
plt.figure()
plt.scatter(df2['pl_orbper'], df2['pl_bmassj'], color='royalblue',s=64 )
plt.xlabel('Periodo di orbitazione [s]')
plt.ylabel(('Massa pianeta [kg]'))
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.show()

#punto 5 
plt.figure()
plt.scatter(df2['pl_orbper'], df2['pl_orbsmax']**2 / df2['st_mass'], color='royalblue',s=64 )
plt.xlabel('Periodo di orbitazione [s]')
plt.ylabel(('R_max**2 / m_stellar'))
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.show()

#punto 6
sotto_df_transit = df2.loc[ (df2['discoverymethod'] == 'Transit')]
sotto_df_radial = df2.loc[(df2['discoverymethod'] == 'Radial Velocity' )]


plt.figure()
plt.scatter(sotto_df_transit['pl_orbper'], sotto_df_transit['pl_bmassj'], color='lightgreen', s=32, alpha =0.5)
plt.scatter(sotto_df_radial['pl_orbper'], sotto_df_radial['pl_bmassj'], color='red', s=32, alpha = 0.1 )
plt.xlabel('Periodo di orbitazione [s]')
plt.ylabel(('Massa pianeta [kg]'))
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid()
plt.show()

