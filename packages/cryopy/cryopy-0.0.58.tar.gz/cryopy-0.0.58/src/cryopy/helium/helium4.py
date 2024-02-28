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

    Status : Checked 2024-02-27
    
    ========== UPDATE ==========
    

    """
    
    ################## PACKAGES ###############################################
    
    import scipy
    import numpy
    import pandas
    
    ################## CONDITIONS #############################################
    
    assert temperature >= 0.8 and temperature <= 400 , 'The function helium4.density is not valid for T = ' + str(temperature) + ' K'
    assert pressure >= 1 and pressure <=  1e6, 'The function helium4.density  is not valid for P = ' + str(pressure) + ' Pa'
    
    ################## INITIALISATION #########################################
    
    data_temperature = numpy.array([0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5,5.5,6,8,10,15,20,30,40,50,70,100,120,150,200,250,300,350,400])
    data_pressure = numpy.array([1, 2, 5, 1e1, 2e1, 5e1, 1e2, 2e2, 5e2, 1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6])
    data = numpy.transpose(numpy.array(pandas.read_csv('data/helium4_density.csv',delimiter = ';',decimal = ',', header=None).values))

    
    ################## FUNCTION ###############################################
    
    function = scipy.interpolate.RectBivariateSpline(data_temperature, data_pressure, data)

    result = function(temperature,pressure)[0][0]
    
    return result


#%% 
def compressibility(temperature,pressure):
    
    """
    ========== DESCRIPTION ==========

    This function return the compressibility of pure Helium 4

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

    <compressibility>
        -- float --
        The compressibility of pure helium 4
        []

    ========== STATUS ==========

    Status : Checked 2024-02-27
    
    ========== UPDATE ==========
    

    """
    
    ################## PACKAGES ###############################################
    
    import scipy
    import numpy
    import pandas
    
    ################## CONDITIONS #############################################
    
    assert temperature >= 0.8 and temperature <= 400 , 'The function helium4.compressibility is not valid for T = ' + str(temperature) + ' K'
    assert pressure >= 1 and pressure <=  1e6, 'The function helium4.compressibility  is not valid for P = ' + str(pressure) + ' Pa'
    
    ################## INITIALISATION #########################################
    
    data_temperature = numpy.array([0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5,5.5,6,8,10,15,20,30,40,50,70,100,120,150,200,250,300,350,400])
    data_pressure = numpy.array([1, 2, 5, 1e1, 2e1, 5e1, 1e2, 2e2, 5e2, 1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6])
    data = numpy.transpose(numpy.array(pandas.read_csv('data/helium4_compressibility.csv',delimiter = ';',decimal = ',', header=None).values))

    
    ################## FUNCTION ###############################################
    
    function = scipy.interpolate.RectBivariateSpline(data_temperature, data_pressure, data)

    result = function(temperature,pressure)[0][0]
    
    return result


#%% 
def enthalpy(temperature,pressure,unit):
    
    """
    ========== DESCRIPTION ==========

    This function return the enthalpy of pure Helium 4

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
        
    <unit>
        -- string --
        Either kg or mol

    ========== OUTPUT ==========

    <enthalpy>
        -- float --
        The enthalpy of pure helium 4
        if 'kg' : [J].[kg]**(-1)
        if 'mol' : [J].[mol]**(-1)

    ========== STATUS ==========

    Status : Checked 2024-02-27
    
    ========== UPDATE ==========
    

    """
    
    ################## PACKAGES ###############################################
    
    import scipy
    import numpy
    import pandas
    
    ################## CONDITIONS #############################################
    
    assert temperature >= 0.8 and temperature <= 400 , 'The function helium4.enthalpy is not valid for T = ' + str(temperature) + ' K'
    assert pressure >= 1 and pressure <=  1e6, 'The function helium4.enthalpy  is not valid for P = ' + str(pressure) + ' Pa'
    
    ################## INITIALISATION #########################################
    
    data_temperature = numpy.array([0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5,5.5,6,8,10,15,20,30,40,50,70,100,120,150,200,250,300,350,400])
    data_pressure = numpy.array([1, 2, 5, 1e1, 2e1, 5e1, 1e2, 2e2, 5e2, 1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6])
    data = numpy.transpose(numpy.array(pandas.read_csv('data/helium4_enthalpy.csv',delimiter = ';',decimal = ',', header=None).values))

    ################## FUNCTION ###############################################
    
    function = scipy.interpolate.RectBivariateSpline(data_temperature, data_pressure, data)

    result = function(temperature,pressure)[0][0]
    
    if unit == 'kg':
        return result
    
    if unit == 'mol':
        return result*molar_mass()
    
#%% 
def entropy(temperature,pressure,unit):
    
    """
    ========== DESCRIPTION ==========

    This function return the entropy of pure Helium 4

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
        
    <unit>
        -- string --
        Either kg or mol

    ========== OUTPUT ==========

    <entropy>
        -- float --
        The entropy of pure helium 4
        if 'kg' : [J].[kg]**(-1).[K]**(-1)
        if 'mol' : [J].[mol]**(-1).[K]**(-1)

    ========== STATUS ==========

    Status : Checked 2024-02-27
    
    ========== UPDATE ==========
    

    """
    
    ################## PACKAGES ###############################################
    
    import scipy
    import numpy
    import pandas
    
    ################## CONDITIONS #############################################
    
    assert temperature >= 0.8 and temperature <= 400 , 'The function helium4.entropy is not valid for T = ' + str(temperature) + ' K'
    assert pressure >= 1 and pressure <=  1e6, 'The function helium4.entropy  is not valid for P = ' + str(pressure) + ' Pa'
    
    ################## INITIALISATION #########################################
    
    data_temperature = numpy.array([0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5,5.5,6,8,10,15,20,30,40,50,70,100,120,150,200,250,300,350,400])
    data_pressure = numpy.array([1, 2, 5, 1e1, 2e1, 5e1, 1e2, 2e2, 5e2, 1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6])
    data = numpy.transpose(numpy.array(pandas.read_csv('data/helium4_entropy.csv',delimiter = ';',decimal = ',', header=None).values))

    ################## FUNCTION ###############################################
    
    function = scipy.interpolate.RectBivariateSpline(data_temperature, data_pressure, data)

    result = function(temperature,pressure)[0][0]
    
    if unit == 'kg':
        return result
    
    if unit == 'mol':
        return result*molar_mass()
    

#%% 
def gibbs_energy(temperature,pressure,unit):
    
    """
    ========== DESCRIPTION ==========

    This function return the gibbs energy of pure Helium 4

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
        
    <unit>
        -- string --
        Either kg or mol

    ========== OUTPUT ==========

    <gibbs_energy>
        -- float --
        The gibbs energy of pure helium 4
        if 'kg' : [J].[kg]**(-1)
        if 'mol' : [J].[mol]**(-1)

    ========== STATUS ==========

    Status : Checked 2024-02-27
    
    ========== UPDATE ==========
    

    """
    
    ################## PACKAGES ###############################################
    
    import scipy
    import numpy
    import pandas
    
    ################## CONDITIONS #############################################
    
    assert temperature >= 0.8 and temperature <= 400 , 'The function helium4.gibbs_energy is not valid for T = ' + str(temperature) + ' K'
    assert pressure >= 1 and pressure <=  1e6, 'The function helium4.gibbs_energy  is not valid for P = ' + str(pressure) + ' Pa'
    
    ################## INITIALISATION #########################################
    
    data_temperature = numpy.array([0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5,5.5,6,8,10,15,20,30,40,50,70,100,120,150,200,250,300,350,400])
    data_pressure = numpy.array([1, 2, 5, 1e1, 2e1, 5e1, 1e2, 2e2, 5e2, 1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6])
    data = numpy.transpose(numpy.array(pandas.read_csv('data/helium4_gibbs_energy.csv',delimiter = ';',decimal = ',', header=None).values))

    ################## FUNCTION ###############################################
    
    function = scipy.interpolate.RectBivariateSpline(data_temperature, data_pressure, data)

    result = function(temperature,pressure)[0][0]
    
    if unit == 'kg':
        return result
    
    if unit == 'mol':
        return result*molar_mass()


#%% 
def internal_energy(temperature,pressure,unit):
    
    """
    ========== DESCRIPTION ==========

    This function return the internal energy of pure Helium 4

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
        
    <unit>
        -- string --
        Either kg or mol

    ========== OUTPUT ==========

    <gibbs_energy>
        -- float --
        The gibbs energy of pure helium 4
        if 'kg' : [J].[kg]**(-1)
        if 'mol' : [J].[mol]**(-1)

    ========== STATUS ==========

    Status : Checked 2024-02-27
    
    ========== UPDATE ==========
    

    """
    
    ################## PACKAGES ###############################################
    
    import scipy
    import numpy
    import pandas
    
    ################## CONDITIONS #############################################
    
    assert temperature >= 0.8 and temperature <= 400 , 'The function helium4.internal_energy is not valid for T = ' + str(temperature) + ' K'
    assert pressure >= 1 and pressure <=  1e6, 'The function helium4.internal_energy  is not valid for P = ' + str(pressure) + ' Pa'
    
    ################## INITIALISATION #########################################
    
    data_temperature = numpy.array([0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5,5.5,6,8,10,15,20,30,40,50,70,100,120,150,200,250,300,350,400])
    data_pressure = numpy.array([1, 2, 5, 1e1, 2e1, 5e1, 1e2, 2e2, 5e2, 1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6])
    data = numpy.transpose(numpy.array(pandas.read_csv('data/helium4_internal_energy.csv',delimiter = ';',decimal = ',', header=None).values))

    ################## FUNCTION ###############################################
    
    function = scipy.interpolate.RectBivariateSpline(data_temperature, data_pressure, data)

    result = function(temperature,pressure)[0][0]
    
    if unit == 'kg':
        return result
    
    if unit == 'mol':
        return result*molar_mass()



#%% 
def sound_velocity(temperature,pressure):
    
    """
    ========== DESCRIPTION ==========

    This function return the sound velocity of pure Helium 4

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

    <sound_velocity>
        -- float --
        The sound velocity of pure helium 4
        [m].[s]**(-1)

    ========== STATUS ==========

    Status : Checked 2024-02-27
    
    ========== UPDATE ==========
    

    """
    
    ################## PACKAGES ###############################################
    
    import scipy
    import numpy
    import pandas
    
    ################## CONDITIONS #############################################
    
    assert temperature >= 0.8 and temperature <= 400 , 'The function helium4.sound_velocity is not valid for T = ' + str(temperature) + ' K'
    assert pressure >= 1 and pressure <=  1e6, 'The function helium4.sound_velocity  is not valid for P = ' + str(pressure) + ' Pa'
    
    ################## INITIALISATION #########################################
    
    data_temperature = numpy.array([0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5,5.5,6,8,10,15,20,30,40,50,70,100,120,150,200,250,300,350,400])
    data_pressure = numpy.array([1, 2, 5, 1e1, 2e1, 5e1, 1e2, 2e2, 5e2, 1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6])
    data = numpy.transpose(numpy.array(pandas.read_csv('data/helium4_sound_velocity.csv',delimiter = ';',decimal = ',', header=None).values))

    
    ################## FUNCTION ###############################################
    
    function = scipy.interpolate.RectBivariateSpline(data_temperature, data_pressure, data)

    result = function(temperature,pressure)[0][0]
    
    return result


#%% 
def specific_heat(temperature,pressure, unit,constant):
    
    """
    ========== DESCRIPTION ==========

    This function return the specific heat of pure Helium 4

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
        
    <unit>
        -- string --
        Either kg or mol

    <constant>
        -- string --
        Either p or v

    ========== OUTPUT ==========

    <specific_heat>
        -- float --
        The specific heat of pure helium 4
        if 'kg' : [J].[kg]**(-1)
        if 'mol' : [J].[mol]**(-1)

    ========== STATUS ==========

    Status : Checked 2024-02-27
    
    ========== UPDATE ==========
    

    """
    
    ################## PACKAGES ###############################################
    
    import scipy
    import numpy
    import pandas
    
    ################## CONDITIONS #############################################
    
    assert temperature >= 0.8 and temperature <= 400 , 'The function helium4.internal_energy is not valid for T = ' + str(temperature) + ' K'
    assert pressure >= 1 and pressure <=  1e6, 'The function helium4.internal_energy  is not valid for P = ' + str(pressure) + ' Pa'
    
    ################## INITIALISATION #########################################
    
    data_temperature = numpy.array([0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5,5.5,6,8,10,15,20,30,40,50,70,100,120,150,200,250,300,350,400])
    data_pressure = numpy.array([1, 2, 5, 1e1, 2e1, 5e1, 1e2, 2e2, 5e2, 1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6])
    
    if constant == 'p':
        data = numpy.transpose(numpy.array(pandas.read_csv('data/helium4_specific_heat_pressure.csv',delimiter = ';',decimal = ',', header=None).values))
        
    if constant == 'v':
        data = numpy.transpose(numpy.array(pandas.read_csv('data/helium4_specific_heat_volume.csv',delimiter = ';',decimal = ',', header=None).values))

    ################## FUNCTION ###############################################
    
    function = scipy.interpolate.RectBivariateSpline(data_temperature, data_pressure, data)

    result = function(temperature,pressure)[0][0]
    
    if unit == 'kg':
        return result
    
    if unit == 'mol':
        return result*molar_mass()



#%% 
def specific_volume(temperature,pressure):
    
    """
    ========== DESCRIPTION ==========

    This function return the specific volume of pure Helium 4

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

    <specific_volume>
        -- float --
        The specific volume of pure helium 4
        [m]**3.[kg]**(-1)

    ========== STATUS ==========

    Status : Checked 2024-02-27
    
    ========== UPDATE ==========
    

    """
    
    ################## PACKAGES ###############################################
    
    ################## CONDITIONS #############################################
    
    ################## INITIALISATION #########################################
    
    ################## FUNCTION ###############################################
    
    result = 1/density(temperature,pressure)
    
    return result



#%% 
def thermal_conductivity(temperature,pressure):
    
    """
    ========== DESCRIPTION ==========

    This function return the thermal conductivity of pure Helium 4

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

    <thermal_conductivity>
        -- float --
        The thermal conductivity of pure helium 4
        [W].[m]**(-1).[K]**(-1)

    ========== STATUS ==========

    Status : Checked 2024-02-27
    
    ========== UPDATE ==========
    

    """
    
    ################## PACKAGES ###############################################
    
    import scipy
    import numpy
    import pandas
    
    ################## CONDITIONS #############################################
    
    assert temperature >= 0.8 and temperature <= 400 , 'The function helium4.thermal_conductivity is not valid for T = ' + str(temperature) + ' K'
    assert pressure >= 1 and pressure <=  1e6, 'The function helium4.thermal_conductivity  is not valid for P = ' + str(pressure) + ' Pa'
    
    ################## INITIALISATION #########################################
    
    data_temperature = numpy.array([0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5,5.5,6,8,10,15,20,30,40,50,70,100,120,150,200,250,300,350,400])
    data_pressure = numpy.array([1, 2, 5, 1e1, 2e1, 5e1, 1e2, 2e2, 5e2, 1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6])
    data = numpy.transpose(numpy.array(pandas.read_csv('data/helium4_thermal_conductivity.csv',delimiter = ';',decimal = ',', header=None).values))

    
    ################## FUNCTION ###############################################
    
    function = scipy.interpolate.RectBivariateSpline(data_temperature, data_pressure, data)

    result = function(temperature,pressure)[0][0]
    
    return result


#%% 
def dynamic_viscosity(temperature,pressure,):
    
    """
    ========== DESCRIPTION ==========

    This function return the dynamic viscosity of pure Helium 4

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

    <dynamic_viscosity>
        -- float --
        The dynamic viscosity of pure helium 4
        [Pa].[s]

    ========== STATUS ==========

    Status : Checked 2024-02-27
    
    ========== UPDATE ==========
    

    """
    
    ################## PACKAGES ###############################################
    
    import scipy
    import numpy
    import pandas
    
    ################## CONDITIONS #############################################
    
    assert temperature >= 0.8 and temperature <= 400 , 'The function helium4.dynamic_viscosity is not valid for T = ' + str(temperature) + ' K'
    assert pressure >= 1 and pressure <=  1e6, 'The function helium4.dynamic_viscosity  is not valid for P = ' + str(pressure) + ' Pa'
    
    ################## INITIALISATION #########################################
    
    data_temperature = numpy.array([0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5,5.5,6,8,10,15,20,30,40,50,70,100,120,150,200,250,300,350,400])
    data_pressure = numpy.array([1, 2, 5, 1e1, 2e1, 5e1, 1e2, 2e2, 5e2, 1e3, 2e3, 5e3, 1e4, 2e4, 5e4, 1e5, 2e5, 5e5, 1e6])
    data = numpy.transpose(numpy.array(pandas.read_csv('data/helium4_dynamic_viscosity.csv',delimiter = ';',decimal = ',', header=None).values))

    
    ################## FUNCTION ###############################################
    
    function = scipy.interpolate.RectBivariateSpline(data_temperature, data_pressure, data)

    result = function(temperature,pressure)[0][0]
    
    return result


#%%
def mass():
    """
    ========== DESCRIPTION ==========

    Return the constant mass of a single atom of helium 4

    ========== VALIDITY ==========

    ========== FROM ==========

    ========== OUTPUT ==========

    <mass>
        -- float --
    	The mass of a single atom of Helium 4
        [kg]

    ========== STATUS ==========

    Status : Checked

    """

    ################## MODULES ################################################
    
    from cryopy import constant

    ################## RETURN #################################################

    return molar_mass() / constant.avogadro()


#%%
def molar_mass():
    """
    ========== DESCRIPTION ==========

    Return the constant molar mass of a single mole of helium 4

    ========== VALIDITY ==========

    Always

    ========== FROM ==========

    P. J. Mohr, B. N. Taylor, and D. B. Newell, Rev. Mod. Phys. 84, 1531 (2012).

    ========== OUTPUT ==========

    <molar_mass>
        -- float --
        The molar mass of a single mole of helium 4
        [kg].[mol]**(-1)

    ========== STATUS ==========

    Status : Checked

    """

    ################## RETURN #################################################

    return 4.002602e-3













#%%
def molar_volume(temperature, pressure):
    """
    ========== DESCRIPTION ==========

    This function return the molar volume of a mole of Helium 4

    ========== VALIDITY ==========

    <temperature> : [0.05 -> 1.8]
    <pressure> : [0 -> 15.7e5]


    ========== FROM ==========

    Tanaka et al (2000)
        Molar volume of pure liquide 4He : dependence on temperature 
        (50-1000mK) and pressure (0-1.57 MPa) - Equation (25)

    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of Helium 4
        [K]

    <pressure>
        -- float --
        The pressure of Helium 4
        [Pa]

    ========== OUTPUT ==========

    <molar_volume>
        -- float --
        The molar volume of Helium 4
        [m]**3.[mol]**(-1)

    ========== STATUS ==========

    Status : Checked 2022-12-24
    
    ========== UPDATE ==========
    
    2021-05-07:
        On Chaudhry et al. (2012) - P59, we can continue up to 1.8K with
        an error of 0.1% 

    """

    ################## MODULES ################################################

    import numpy as np
    from scipy.special import erfc

    ################## CONDITIONS #############################################

    assert 15.7e5 >= pressure >= 0, 'The function Helium4.molar_volume is not defined for P = ' + str(pressure) + ' Pa'
    assert 1.8 >= temperature >= 0.05, 'The function Helium4.molar_volume is not defined for T = ' + str(temperature) + 'K '

    ################## INITIALISATION #########################################

    V = np.array([2.757930e-5, -3.361585e-12, 1.602419e-18,-1.072604e-24,7.979064e-31, -5.356076e-37, 2.703689e-43, -9.004790e-50,1.725962e-56,-1.429411e-63])
    D = np.array([8.618, -7.487e-7,5.308e-14])
    A = np.array([1.863e8,7.664e6])
    B = np.array([2.191,-1.702e-7])
    pc = -1.00170e6
    
    result_polynome_A = 0
    result_polynome_B = 0
    result_polynome_D = 0
    result_polynome_V = 0
    

    ################## FUNCTION ###############################################

    for i in range(len(V)):
        result_polynome_V = result_polynome_V + V[i] * pressure ** i
    
    for i in range(len(D)):
        result_polynome_D = result_polynome_D + D[i] * pressure ** i
        
    result_polynome_A = (A[0] / ((pressure - pc) ** 2) + A[1] / ((pressure - pc) ** (5 / 3)))

    result_polynome_B =  B[0] + B[1] * pressure

    result = result_polynome_V*(1+result_polynome_A*temperature**4/4-result_polynome_B*erfc(np.sqrt((result_polynome_D/temperature))))
    
    return result



#%%
def thermal_expansion_phonon(temperature, pressure):
    """
    ========== DESCRIPTION ==========

    This function return the contribution of phonons to the thermal expansion of helium 4

    ========== VALIDITY ==========

    <temperature> : [0.05 -> 1.8]
    <pressure> : [0 -> 15.7e5]


    ========== FROM ==========

    Tanaka et al (2000) 
        Molar volume of pure liquide 4He : dependence on temperature 
        (50-1000mK) and pressure (0-1.57 MPa) - Equation (23)

    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of Helium 4
        [K]

    <pressure>
        -- float --
        The pressure of Helium 4
        [Pa]

    ========== OUTPUT ==========

    <thermal_expansion_phonon>
        -- float --
        The thermal expansion of helium 4 due to phonons 
        [K]**{-1}

    ========== STATUS ==========

    Status : 
    
    ========== UPDATE ==========

    """

    ################## MODULES ################################################

    import numpy as np

    ################## CONDITIONS #############################################

    assert 15.7e5 >= pressure >= 0, 'The function Helium4.molar_volume is not defined for P = ' + str(pressure) + ' Pa'
    assert 1.8 >= temperature >= 0.05, 'The function Helium4.molar_volume is not defined for T = ' + str(temperature) + 'K '

    ################## INITIALISATION #########################################

    A = np.array([1.863e8,7.664e6])
    pc = -1.00170e6

    ################## FUNCTION ###############################################

    result = (A[0] / ((pressure - pc) ** 2) + A[1] / ((pressure - pc) ** (5 / 3)))

    return result

#%%
def thermal_expansion_roton(temperature, pressure):
    """
    ========== DESCRIPTION ==========

    This function return the contribution of rotons to the thermal expansion of helium 4

    ========== VALIDITY ==========

    <temperature> : [0.05 -> 1.8]
    <pressure> : [0 -> 15.7e5]


    ========== FROM ==========

    TANAKA (2000) - Molar volume of pure liquide 4He : dependence on 
    temperature (50-1000mK) and pressure (0-1.57 MPa) - Equation (24)

    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of Helium 4
        [K]

    <pressure>
        -- float --
        The pressure of Helium 4
        [Pa]

    ========== OUTPUT ==========

    <thermal_expansion_roton>
        -- float --
        The thermal expansion of helium 4 due to rotons 
        [K]**{-1}

    ========== STATUS ==========

    Status : 
    
    ========== UPDATE ==========

    """

    ################## MODULES ################################################

    import numpy as np

    ################## CONDITIONS #############################################

    assert 15.7e5 >= pressure >= 0, 'The function Helium4.molar_volume is not defined for P = ' + str(pressure) + ' Pa'
    assert 1.8 >= temperature >= 0.05, 'The function Helium4.molar_volume is not defined for T = ' + str(temperature) + 'K '

    ################## INITIALISATION #########################################

    D = np.array([8.618, -7.487e-7,5.308e-14])
    B = np.array([2.191,-1.702e-7])
    result_polynome_D = 0
    
    ################## FUNCTION ###############################################
    
    for i in range(len(D)):
        result_polynome_D = result_polynome_D + D[i] * pressure ** i

    result_polynome_B =  B[0] + B[1] * pressure
    
    result_b = result_polynome_B*np.sqrt(np.pi/result_polynome_D)

    result = -result_b*temperature**(-3/2)*np.exp(-result_polynome_D/temperature)
    
    return result




#%%
def molar_specific_heat(temperature, pressure):
    """
    ========== DESCRIPTION ==========

    This function return the molar specific heat of pure Fermi liquid helium-3

    ========== VALIDITY ==========

    <temperature> : [0 -> 1.8]
    <pressure> : [0]

    ========== FROM ==========

    KUERTEN - Thermodynamic properties of liquid 3He-4He mixtures
    at zero pressure for temperatures below 250 mK and 3He concentrations
    below 8% - Equation (46)
   
    CHAUDHRY - Thermodynamic properties of liquid 3He-4he mixtures
    between 0.15 K and 1.8 K - Equation (A15)

    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of helium-3
        [K]

    <pressure>
        -- float --
        The pressure of helium-3
        [Pa]

    ========== OUTPUT ==========

    <molar_specific_heat>
        -- float --
        The molar specific heat of pure Fermi liquid helium-3
        [J].[K]**(-1).[mol]**(-1)

    ========== STATUS ==========

    Status : Checked

    ========== NOTES ===========

    This function requires the implementation of pressure changes


    """

    ################## CONDITIONS #############################################

    assert pressure <= 0 <= pressure, 'The function Helium4.molar_specific_heat is not defined for P = ' + str(pressure) + ' Pa'
    assert 1.8 >= temperature >= 0.000, 'The function Helium4.molar_specific_heat is not defined for T = ' + str(temperature) + ' K'

    ################## MODULES ################################################

    import numpy as np
    import pandas as pd

    ################## INITIALISATION #########################################

    result = 0
    coefficients = pd.DataFrame(np.array([[0.08137],
                                          [0],
                                          [-0.0528],
                                          [0.05089],
                                          [0.019]]),
                                columns=['B'])

    ################## FUNCTION ###############################################

    if 0.4 >= temperature >= 0:
        for j in [0, 1, 2, 3, 4]:
            result = result + coefficients.B[j] * temperature ** (j + 3)
        return result

    else:
        first = 82.180127 * temperature ** 3 - 87.45899 * temperature ** 5 + 129.12758 * temperature ** 6 - 6.6314726 * temperature ** 7
        second = 70198.836 * (8.8955141 / temperature) ** (3 / 2) * np.exp(-8.8955141 / temperature) * (
                1 + (temperature / 8.8955141) + 0.75 * ((temperature / 8.8955141) ** 2))
        third = (10244.198 / temperature) * (22.890183 / temperature) ** 2 * np.exp(-22.890183 / temperature) * (
                1 - 2 * (temperature / 22.890183))
        value = (first + second + third) * 1e-3

        return value


#%%
def molar_enthalpy(temperature, pressure):
    """
    ========== DESCRIPTION ==========

    This function can return the molar enthalpy of Helium 4

    ========== VALIDITY ==========

    <temperature> : [0 -> 0.400]
    <pressure> : [0]

    ========== FROM ==========
    
    KUERTEN - Thermodynamic properties of liquid 3He-4He mixtures
    at zero pressure for temperatures below 250 mK and 3He concentrations
    below 8% - Table (17)

    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of Helium 4
        [K]

    <pressure>
        -- float --
        The pressure of Helium 4
        [Pa]

    ========== OUTPUT ==========

    <molar_enthalpy>
        -- float --
        The molar enthalpy of pure Helium 4
        [J].[mol]**(-1)


    ========== STATUS ==========

    Status : Checked

    ========== NOTES ===========

    This function requires the implementation of pressure changes


    """

    ################## CONDITIONS #############################################

    assert pressure <= 0 <= pressure, 'The function Helium4.molar_enthalpy is not defined for P = ' + str(pressure) + ' Pa'
    assert 0.400 >= temperature >= 0.000, 'The function  Helium4.molar_enthalpy is not defined for T = ' + str(temperature) + ' K'

    ################## MODULES ################################################

    import numpy as np

    ################## INITIALISATION #########################################

    coefficients = [3.19794159e-03, -6.48309258e-03, 2.19933824e-02, -2.09571258e-04,
                    1.23491357e-05, -2.67718222e-07, 1.07444578e-09]
    polynom = np.poly1d(coefficients)

    ################## FUNCTION ###############################################

    return polynom(temperature)

#%%
def molar_entropy(temperature, pressure):
    """
    ========== DESCRIPTION ==========

    This function can return the molar entropy of Helium 4

    ========== VALIDITY ==========

    <temperature> : [0 -> 0.400]
    <pressure> : [0]

    ========== FROM ==========

    KUERTEN - Thermodynamic properties of liquid 3He-4He mixtures
    at zero pressure for temperatures below 250 mK and 3He concentrations
    below 8% - Table (17)

    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of Helium 4
        [K]

    <pressure>
        -- float --
        The pressure of Helium 4
        [Pa]

    ========== OUTPUT ==========

    <molar_entropy>
        -- float --
        The molar entropy of pure Helium 4
        [J].[K]**(-1).[mol]**(-1)


    ========== STATUS ==========

    Status : Checked

    ========== NOTES ===========

    This function requires the implementation of pressure changes


    """

    ################## MODULES ################################################

    import numpy as np

    ################## CONDITIONS #############################################

    assert pressure <= 0 <= pressure, 'The function Helium3.molar_entropy is not defined for P = ' + str(pressure) + ' Pa'
    assert 0.400 >= temperature >= 0.000, 'The function Helium3.molar_entropy is not defined for T = ' + str(temperature) + ' K'

    ################## INITIALISATION #########################################

    coefficients = [-2.08468571e-03, 2.73347674e-03,
                    -5.46990881e-03, 2.81129291e-02,
                    -7.81349812e-05, 2.17304932e-06,
                    -1.05591438e-08]
    polynom = np.poly1d(coefficients)

    ################## FUNCTION ###############################################

    return polynom(temperature)


#%% 
def chemical_potential(temperature, pressure):
    """
    ========== DESCRIPTION ==========

    This function return the chemical potential of Helium 4

    ========== VALIDITY ==========

    Always

    ========== FROM ==========

    KUERTEN - Thermodynamic properties of liquid 3He-4He mixtures
    at zero pressure for temperatures below 250 mK and 3He concentrations
    below 8% - Equation (38)
    
    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of Helium 4
        [K]

    <pressure>
        -- float --
        The pressure of Helium 4
        [Pa]

    ========== OUTPUT ==========

    <chemical_potential>
        -- float --
        The chemical potential of pure Helium 4
        [J].[mol]**(-1)

    ========== STATUS ==========

    Status : In progress (need to be verified with new values of pressure)

    """

    ################## MODULES ################################################

    from cryopy.Helium import Helium4

    ################## RETURN #################################################

    return Helium4.molar_enthalpy(temperature, pressure) - temperature * Helium4.molar_entropy(temperature, pressure)




# %%
def is_liquid(temperature, pressure):
    """
    ========== DESCRIPTION ==========

    This function determine if the current Helium 4 is liquid or not

    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of Helium 4
        [K]

    <pressure>
        -- float --
        The pressure of Helium 4
        [Pa]

    ========== OUTPUT ==========

    <is_liquid>
        -- boolean --
        Helium 4 is liquid or not
        []

    ========== STATUS ==========

    Status : Checked

    """

    ################## FUNCTION ##############################################

def is_solid(temperature, pressure):
    """
    ========== DESCRIPTION ==========

    This function determine if the current Helium 4 is solid or not

    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of Helium 4
        [K]

    <pressure>
        -- float --
        The pressure of Helium 4
        [Pa]

    ========== OUTPUT ==========

    <is_solid>
        -- boolean --
        Helium 4 is solid or not
        []

    ========== STATUS ==========

    Status : Checked

    """

    ################## FUNCTION ##############################################


def is_gaseous(temperature, pressure):
    """
    ========== DESCRIPTION ==========

    This function determine if the current Helium 4 is gaseous or not

    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of Helium 4
        [K]

    <pressure>
        -- float --
        The pressure of Helium 4
        [Pa]

    ========== OUTPUT ==========

    <is_gaseous>
        -- boolean --
        Helium 4 is gaseous or not
        []

    ========== STATUS ==========

    Status : Checked

    """

    ################## FUNCTION ##############################################


def is_superfluid(temperature, pressure):
    """
    ========== DESCRIPTION ==========

    This function determine if the current Helium 4 is superfluid or not

    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of Helium 4
        [K]

    <pressure>
        -- float --
        The pressure of Helium 4
        [Pa]

    ========== OUTPUT ==========

    <is_superfluid>
        -- boolean --
        Helium 4 is superfluid or not
        []

    ========== STATUS ==========

    Status : Checked

    """


def superfluid_ratio(temperature, pressure):
    """
    ========== DESCRIPTION ==========

    This function determine the current proportion of superfluid Helium 4

    ========== INPUT ==========

    <temperature>
        -- float --
        The temperature of Helium 4
        [K]

    <pressure>
        -- float --
        The pressure of Helium 4
        [Pa]

    ========== OUTPUT ==========

    <superfluid_ratio>
        -- float --
        Proportion of superfluid Helium 4
        []

    ========== STATUS ==========

    Status : Checked

    """

