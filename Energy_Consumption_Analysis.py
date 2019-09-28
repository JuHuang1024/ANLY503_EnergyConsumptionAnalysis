# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:00:58 2019

@author: rbshu
"""

import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='juhuang', api_key='3ulNsW3VBPDO3KzEKYvn')
#import chart_studio
#import pylab as pl
#from matplotlib.pyplot import figure

energy = pd.read_csv('2_Energy_Consumption.csv')
energy.columns = ["State", "Natural_gas", "Distillate_fuel_diesel", 
                  "Jet_fuel", "Motor_gasoline", "Residual_fuel", "Other", 
                  "Total_petroleum", "Ethanol","Electricity","Net_energy",
                  "Electrical_system_energy_losses","Total"]

####################### FIGURE 1 ################################
energy_cp = energy.sort_values(by=['Total_petroleum'],ascending=True)
name_list = list(energy_cp['State'])
num_list = list(energy_cp['Total_petroleum'])

fig = plt.figure(figsize=(18,15),dpi = 120)
ax = fig.add_subplot(111)
ax.barh(range(len(num_list)), num_list,color='lightblue',tick_label=name_list)
#pl.xticks(rotation=90)
for i ,v in enumerate(num_list):
    ax.text(v, i, str(int(num_list[i])), color='blue', fontweight='bold')
ax.set_title('The petroleum usage of each state in the US',fontsize=25)
ax.set_xlabel('Petroleum usage (Trillion Btu)', fontsize = 15)
plt.savefig('Python The petroleum usage of each state in the US.png')
###################### FIGURE 2 ################################
fig = plt.figure(figsize=(18,15),dpi = 100)
ax = plt.subplot()
petroleum_use = [energy["Distillate_fuel_diesel"],energy["Jet_fuel"],
              energy["Motor_gasoline"], energy["Residual_fuel"], 
              energy["Other"]]
labels = ["Distillate_fuel_diesel", "Jet_fuel", "Motor_gasoline",
          "Residual_fuel", "Other"]
bplot = ax.boxplot(petroleum_use, patch_artist=True, labels=labels, 
                   notch=True)
ax.set_title('Different petroleum energy usage in the US',fontsize=25)
ax.set_xlabel('Different petroleum energy', fontsize = 15)
ax.set_ylabel('Petroleum usage (Trillion Btu)', fontsize = 15)
axes = plt.gca()
axes.set_ylim([-30,650])
colors = ['#2ae0c8','#a2e1d4','#acf6ef','#cbf5fb','#bdf3d4']
#colors = ['#e6e2c3','#e3c887','#fad8be','#fbb8ac','#fe6673']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
plt.grid(axis='y')
plt.savefig('Python Boxplot of different petroleum energy usage in the US.png')
plt.show()


###################### FIGURE 3 ################################


trace1 = go.Bar(
    x=energy['State'],
    y=energy['Distillate_fuel_diesel'],
    name='Distillate_fuel_diesel'
)
trace2 = go.Bar(
    x=energy['State'],
    y=energy['Jet_fuel'],
    name='Jet_fuel'
)
trace3 = go.Bar(
    x=energy['State'],
    y=energy['Motor_gasoline'],
    name='Motor_gasoline'
)
trace4 = go.Bar(
    x=energy['State'],
    y=energy['Residual_fuel'],
    name='Residual_fuel'
)
trace5 = go.Bar(
    x=energy['State'],
    y=energy['Other'],
    name='Other'
)
 
data = [trace1, trace2, trace3, trace4, trace5]
layout = go.Layout(
        title='Different petroleum energy usage of each state in the US',
        yaxis=dict(title='Petroleum Usage (Trillion Btu)'),
        barmode='stack')
#                

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='python plotly Different petroleum energy usage of each state in the US')



