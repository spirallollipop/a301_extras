import numpy as np

def calcScaleHeight(df):
    """
    Calculate the pressure scale height H_p
    
    Parameters
    ----------

    df: pd.DataFrame

    columns:
    
        T: vector (float)
          temperature (K)

        p: vector (float) of len(T)
          pressure (pa)

        z: vector (float) of len(T
          height (m)

    Returns
    -------
    
    Hbar: vector (float) of len(T)
      pressure scale height (m)
    
    """
    z=df['z'].values
    Temp=df['temp'].values
    dz=np.diff(z)
    TLayer=(Temp[1:] + Temp[0:-1])/2.
    oneOverH=g/(Rd*TLayer)
    Zthick=z[-1] - z[0]
    oneOverHbar=np.sum(oneOverH*dz)/Zthick
    Hbar = 1/oneOverHbar
    return Hbar

def calcDensHeight(df):
    """
    Calculate the density scale height H_rho
    
    Parameters
    ----------

    df: pd.DataFrame

    df columns:
    
        T: vector (float)
          temperature (K)

        p: vector (float) of len(T)
          pressure (pa)

        z: vector (float) of len(T
          height (m)
      
    Returns
    -------
    
    Hbar: vector (float) of len(T)
      density scale height (m)
    """
    z=df['z'].values
    Temp=df['temp'].values
    dz=np.diff(z)
    TLayer=(Temp[1:] + Temp[0:-1])/2.
    dTdz=np.diff(Temp)/np.diff(z)
    oneOverH=g/(Rd*TLayer) + (1/TLayer*dTdz)
    Zthick=z[-1] - z[0]
    oneOverHbar=np.sum(oneOverH*dz)/Zthick
    Hbar = 1/oneOverHbar
    return Hbar

c, h, k = 299792458.0, 6.62607004e-34, 1.38064852e-23
c1 = 2.0 * h * c ** 2.0
c2 = h * c / k
