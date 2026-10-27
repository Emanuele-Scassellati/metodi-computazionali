import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

#punto 1
df = pd.read_csv('kplr010666592-2011240104155_slc.csv')

#punto 2
print(df.columns)   

#punto 3
plt.figure()
plt.plot(df['TIME'], df['PDCSAP_FLUX'], 'o' )
plt.grid()
plt.show()

#punto 4/5
plt.figure()
plt.errorbar(df['TIME'], df['PDCSAP_FLUX'], fmt='o', yerr=df['PDCSAP_FLUX_ERR'])
plt.xlabel('Time [s]')
plt.ylabel('Light Flux [e*s]')
plt.grid()
plt.show()

#punto 6
plt.figure()
plt.errorbar(df['TIME'], df['PDCSAP_FLUX'], fmt='o', yerr=df['PDCSAP_FLUX_ERR'], color='blue')
plt.xlim(948, 948.3)
plt.ylim(1012000, 1025000)
plt.xlabel('Time [s]')
plt.ylabel('Light Flux [e*s]')
plt.grid()
plt.show()

#punto 7
fig, ax = plt.subplots(figsize=(8, 5))

ax.errorbar(df['TIME'], df['PDCSAP_FLUX'], fmt='o', yerr=df['PDCSAP_FLUX_ERR'],color='grey')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Light Flux [e*s]')
ax.grid()

axins = inset_axes(ax, width='40%', height='40%', loc='upper right')

axins.errorbar(df['TIME'],df['PDCSAP_FLUX'],fmt='o',yerr=df['PDCSAP_FLUX_ERR'],color='blue')
axins.set_xlim(948, 948.3)
axins.set_ylim(1012000, 1025000)
axins.grid()
plt.show()
