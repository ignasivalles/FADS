import xarray as xr
import pandas as pd
import numpy as np
from os.path import exists
import pickle

datavel=pd.read_pickle(r'DataVel')
times=datavel['timevel']

vtotal_int=([])
utotal_int=([])
vstk_int=([])
ustk_int=([])

for t in range(len(times)):
        tname=str(datavel['timevel'][t])[0:10]
        if (exists('/mnt/lustre/users/valles/DATA/CMEMS_forecast_PHY_surf/'+tname+'.nc')):
                data=xr.open_dataset('/mnt/lustre/users/valles/DATA/CMEMS_forecast_PHY_surf/'+tname+'.nc')
                vtotal=data.vtotal
                utotal=data.utotal
                vsdy=data.vsdy
                vsdx=data.vsdx
                vint=vtotal.interp(longitude=datavel['lonvel'][t],latitude=datavel['latvel'][t],time=datavel['timevel'][t],method='linear')
                uint=utotal.interp(longitude=datavel['lonvel'][t],latitude=datavel['latvel'][t],time=datavel['timevel'][t],method='linear')
                vstk=vsdy.interp(longitude=datavel['lonvel'][t],latitude=datavel['latvel'][t],time=datavel['timevel'][t],method='linear')
                ustk=vsdx.interp(longitude=datavel['lonvel'][t],latitude=datavel['latvel'][t],time=datavel['timevel'][t],method='linear')
                #print(datavel['velocidad'][t]-vint.values)
                vtotal_int.append(vint.values)
                utotal_int.append(uint.values)
                vstk_int.append(vstk.values)
                ustk_int.append(ustk.values)
        else:
                vtotal_int.append(np.nan)
                utotal_int.append(np.nan)
                vstk_int.append(np.nan)
                ustk_int.append(np.nan)


datavel['vtotal_int']=np.array(vtotal_int)
datavel['utotal_int']=np.array(utotal_int)
datavel['vstk_int']=np.array(vstk_int)
datavel['ustk_int']=np.array(ustk_int)

# Store data (serialize)
with open('Datavel_int.pickle', 'wb') as handle:
    pickle.dump(datavel, handle, protocol=pickle.HIGHEST_PROTOCOL)

#datavel.to_pickle('Datavel_int')
                #print(vint.values)

print(data)