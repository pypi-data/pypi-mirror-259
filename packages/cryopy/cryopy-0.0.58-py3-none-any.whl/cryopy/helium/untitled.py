#%% 
def density(temperature,pressure):
    
    """
    ========== DESCRIPTION ==========

    This function return the density of pure Helium 4

    ========== VALIDITY ==========

    <temperature> : [0.8 -> 400]
    <pressure> : [1 -> 1e6] 

    ========== FROM ==========

    HEPAK was written by Vincent Arp, Bob McCarty, and Jeff Fox, formerly of 
    NIST and later of Cryodata, using code from Brian Hands while at the 
    Oxford University Cryogenics Laboratory.


    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of pure helium 4
        [K]

    <pressure>
        -- float --
        The pressure of pure helium 4
        [Pa]

    ========== OUTPUT ==========

    <density>
        -- float --
        The density of pure helium 4
        [kg].[m]**-3

    ========== STATUS ==========

    Status : Checked 2023-07-27
    
    ========== UPDATE ==========
    

    """
    
    ################## PACKAGES ###############################################
    
    import scipy
    import numpy
    import pandas
    
    ################## CONDITIONS #############################################
    
    assert temperature >= 0.8 and temperature <= 400 , 'This function is not valid for T = ' + str(temperature) + ' K'
    assert pressure >= 1 and pressure <=  1e6, 'This function is not valid for P = ' + str(pressure) + ' Pa'
    
    ################## INITIALISATION #########################################
    
    data_temperature = numpy.array([0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5,5.5,6,8,10,15,20,30,40,50,70,100,120,150,200,250,300,350,400])
    data_pressure = numpy.array([1, 2, 5, 1e1, 2e1, 5e1, 1e2, 2e2, 5e2, 1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6])
    data_density = numpy.transpose(numpy.array(pandas.read_csv('data/helium4_density.csv',delimiter = ';',decimal = ',', header=None).values))

    
    ################## FUNCTION ###############################################
    
    function = scipy.interpolate.RectBivariateSpline(data_temperature, data_pressure, data_density)

    result = function(temperature,pressure)[0][0]
    
    return result



