import xarray as xr
import numpy as np
import glob
import natsort
import vtk
from paraview.simple import *
from vtk.util.numpy_support import vtk_to_numpy
from tqdm import trange
from scipy import ndimage
import tempfile
import glob
import os


def vtk_ascii2binary(adr_disp):
    '''
    Create temporary binary file from a vtk ascii file as there is a bug in reading vtk ascii file.
    '''
    vtk_binary = tempfile.NamedTemporaryFile(delete=False, mode='wb')
    # Create a temporary file
    ascii_file = LegacyVTKReader(registrationName=adr_disp.split('/')[-1], FileNames=[adr_disp])

    # save data
    SaveData(vtk_binary.name+'.vtk', proxy=ascii_file, ChooseArraysToWrite=0,FileType='Binary')


    # Return the path to the temporary file
    return vtk_binary.name+'.vtk'

def vtk2xarray(adr,res):
    '''
    Convert vtk file to xarray dataset object.
    '''
    reader = vtk.vtkDataSetReader()
    reader.SetFileName(adr)
    reader.Update()

    # Get the output
    ug = reader.GetOutput()
    # Get cell data
    cell_data = ug.GetCellData()

    # Get the number of arrays in the cell data
    num_cell_arrays = cell_data.GetNumberOfArrays()

    vtk_spacing=ug.GetSpacing()
    vtk_dim=ug.GetDimensions()

    ds=xr.Dataset()

    # Iterate over arrays and print their names
    #print("Cell Data:")
    for i in range(num_cell_arrays):
        array_name = cell_data.GetArrayName(i)
        # print("Array {}: {}".format(i, array_name))
        tmp_np=vtk_to_numpy(ug.GetCellData().GetArray(i))
        if len(tmp_np.shape)==1:
            shaped_np=tmp_np.reshape(vtk_dim[1]-1,vtk_dim[0]-1)
            dd=['y','x']
        elif tmp_np.shape[-1]==3:
            shaped_np=tmp_np.reshape(vtk_dim[1]-1,vtk_dim[0]-1,np.shape(tmp_np)[-1])*res
            shaped_np[:,:,1]=-shaped_np[:,:,1]
            dd=['y','x','d']
            array_name='displacement'
        elif tmp_np.shape[-1]==9:
            shaped_np=tmp_np.reshape(vtk_dim[1]-1,vtk_dim[0]-1,np.shape(tmp_np)[-1])
            shaped_np = shaped_np[..., [0, 4, 8, 1, 2, 5]]
            dd=['y','x','sT']
            if array_name=='e':
                array_name='strain'
        
        ds[array_name]=xr.DataArray(shaped_np,dims=dd)

    ds['x']=np.arange(vtk_dim[0]-1)*vtk_spacing[0]*res
    ds['y']=(np.arange(vtk_dim[1]-1)*vtk_spacing[1])[::-1]*res

    return ds


def load_spam1t(adr_disp,adr_strain,res=1):
    '''
    load on time step of displacement and strain
    '''
    # convert to binary
    adr_disp_bi=vtk_ascii2binary(adr_disp)
    adr_strain_bi=vtk_ascii2binary(adr_strain)
    # load data
    ds_disp=vtk2xarray(adr_disp_bi,res=res)
    ds_strain=vtk2xarray(adr_strain_bi,res=res)
    # merge
    ds=ds_disp.merge(ds_strain)

    return ds

def load_spamige(adr_fd,adr_fs,res=1,time_step=1):
    '''
    Load spamige output
    '''

    # read file name from list
    list_d=natsort.natsorted(glob.glob(os.path.join(adr_fd,'*.vtk')))
    list_s=natsort.natsorted(glob.glob(os.path.join(adr_fs,'*.vtk')))

    ds=[]
    
    for i in trange(len(list_d)):
        ds.append(load_spam1t(list_d[i],list_s[i],res=res).expand_dims('time'))

    tds=xr.concat(ds,'time')
    # applied filter
    if 'returnStatus' in list(tds.keys()):
        filter=tds.returnStatus[0,...]!=-5
        filter=ndimage.binary_erosion(filter)
        tds['mask']=xr.DataArray(filter,dims=['y','x'])
        tds=tds.where(tds.mask,drop=True)

    tds['time']=(tds['time']+1)*time_step

    return tds
