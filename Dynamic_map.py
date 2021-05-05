# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:35:26 2020

@author: rezac
"""

import pandas as pd

import geopandas as gpd

import PIL

import io

#data=pd.read_csv(r"C:\On going Research Works\Dynamics Heatmap\COVID-19-master\COVID-19-master\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_global.csv")

data=pd.read_csv(r"C:\On going Research Works\Dynamics Heatmap\COVID-19-master\COVID-19-master\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_US.csv")
data=data[data['Province_State']=='Florida']
data=data.drop(columns=['UID', 'iso2', 'iso3', 'code3','Admin2', 'Country_Region', 'Lat', 'Long_'])

florida=gpd.read_file(r'C:\On going Research Works\Dynamics Heatmap\tl_2016_12_cousub\tl_2016_12_cousub.shp')

florida['FIPS']=(florida['STATEFP'])+(florida['COUNTYFP'])

florida['FIPS']=florida['FIPS'].astype(int)

#county=florida.filter(['FIPS','NAME'])


data=data.groupby('FIPS').sum()

'''
for index, row in data.iterrows():
    print(index)
    if index not in florida['FIPS'].to_list():
        print(index +" index is not in the list")
    else:
        pass

'''
    
    
merge=florida.join(data,on="FIPS", how="right")



image_frames=[]


import pylab as plot
params = {'legend.fontsize': 25,
          'legend.handlelength': 2}
plot.rcParams.update(params)


for dates in merge.columns.to_list()[59:]:
    ax=merge.plot(column=dates,
              cmap='OrRd',
              figsize=(20,15),
              legend=True,
              scheme='user_defined',
              classification_kwds={'bins':[10,100,500,1000,5000,10000,20000]},
              edgecolor='black',
              linewidth=0.4)
    
    
    ax.set_title('Total Confirmed Coronavirus Cases: '+dates, fontdict={'fontsize':20},pad=12.5)
    
    ax.set_axis_off()
    
    
    ax.get_legend().set_bbox_to_anchor((0.4,0.4))

    
    img =ax.get_figure()
    
    f=io.BytesIO()
    img.savefig(f,format='png',bbox_inches='tight')
    f.seek(0)
    image_frames.append(PIL.Image.open(f))
    

#create a GIF animation

image_frames[0].save(r'C:\On going Research Works\Dynamics Heatmap\Dynamic Covid-19 Florida Map.gif', format='GIF', append_images=image_frames[1:],save_all=True, duration=300,loop=0)


    
f.close()



data=data.drop(columns=['Lat', 'Long'])


# create a transpose of the dataframe


data_transpose=data.T


data_transpose.plot(y=['Australia','China','US','Italy'], use_index=True,figsize=(10,10),marker="*")


world=gpd.read_file(r'C:\On going Research Works\Dynamics Heatmap\Dynamic Mapping of COVID-19 Progression-20200428T061748Z-001\Dynamic Mapping of COVID-19 Progression\World_map.shp')


world.replace('Viet Nam', 'Vietnam',inplace=True)

world.replace('Brunei Darussalam', 'Brunei',inplace=True)

world.replace('United States', 'US',inplace=True)

world.replace('Iran (Islamic Republic of', 'Iran',inplace=True)

world.replace('Cape Verde', 'Cabo Verde ',inplace=True)

world.replace('Democratic Republic of Congo', 'Congo (Kisnshasa',inplace=True)

world.replace('Czech Republic', 'Czechia',inplace=True)

world.replace('Swaziland', 'Eswatini',inplace=True)

world.replace('Korea, Republic of', 'Korea, South',inplace=True)

world.replace('Palestine', 'West Bank and Gaza',inplace=True)

world.replace('United Republic of Tanzania', 'Tanzania',inplace=True)

world.replace('Syrian Arab Republic', 'Syria',inplace=True)

world.replace('Taiwan', 'Taiwan*',inplace=True)



for index, row in data.iterrows():
    if index not in world['NAME'].to_list():
        print(index +" index is not in the list")
    else:
        pass
    
    
    
merge=world.join(data,on="NAME", how="right")


image_frames=[]


for dates in merge.columns.to_list()[20:25]:
    ax=merge.plot(column=dates,
              cmap='OrRd',
              figsize=(20,15),
              legend=True,
              scheme='user_defined',
              classification_kwds={'bins':[10,20,50,500,10000,500000]},
              edgecolor='black',
              linewidth=0.4)
    
    
    ax.set_title('Total Confirmed Coronavirus Cases: '+dates, fontdict={'fontsize':20},pad=12.5)
    
    ax.set_axis_off()
    
    
    ax.get_legend().set_bbox_to_anchor((0.18,0.6))
    
    
    img =ax.get_figure()
    
    f=io.BytesIO()
    img.savefig(f,format='png',bbox_inches='tight')
    f.seek(0)
    image_frames.append(PIL.Image.open(f))
    
    



#create a GIF animation

image_frames[0].save('Dynamic Covid-19 Map.gif', format='GIF', append_images=image_frames[1:],save_all=True, duration=300,loop=0)


    
f.close()





