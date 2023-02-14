BASEURL = "https://develop.vecindario.com"
BASEURLSIMULADOR = "BASEURLSIMULADOR"
BASEURLAGENDADOR = "BASEURLAGENDADOR"
BASEURLPREAPROVADOS = 'BASEURLPREAPROVADOS'
NAVEGADOR = "chrome"
NAME_TOWERS = 'NAME_TOWERS'
NAME = "name"
LASTNAME = "LASTNAME"
MOBILE = "MOBILE"
EMAIL = "EMAIL"
NUMBERDOCUMENT = "NUMBERDOCUMENT"
INCOMEUSERFAMILY = "INCOMEUSERFAMILY"
#Configuracion de simulador para validar que aplique el subsidio en una simjulacion de cuota inicial
SIMULACIONWHITSUBSIDY = 'SIMULACIONWHITSUBSIDY'
CAJACOMPENSACION = "COLSUBSIDIO"
PRIMAS = "100000"
CESANTIAS = "100000"
CUOTASPERZONA = "100000"
perzonalizeproperty = 'si'
personalizesubsidy = 'si'


#VARIABLES PARA EL AGENDADOR

TYPE = "TYPE"
NAME = "NAME"
COUNTRY = "COUNTRY"

#variables preaprobados
OTHERPHONE = 'OTHERPHONE'
ADRESS = 'ADRESS'
AMOUNTSOLI = 'AMOUNTSOLI'

caps=[
      {
      "os_version": "10",
      "os": "Windows",
      "browser": "firefox",
      "browser_version": "89.0",
      "name": "Parallel Test2",
      "build": "browserstack-build-1"
      },
      {
      "os_version": "Big Sur",
      "os": "OS X",
      "browser": "chrome",
      "browser_version": "90.0",
      "name": "Parallel Test3",
      "build": "browserstack-build-1"
}]

capx= [{
      "os_version": "10",
      "os": "Windows",
      "browser": "chrome",
      "browser_version": "latest",
      "name": "Parallel Test1", # test name
      "build": "browserstack-build-1" # Your tests will be organized within this build
      },
      {
      "os_version": "10",
      "os": "Windows",
      "browser": "firefox",
      "browser_version": "latest",
      "name": "Parallel Test2",
      "build": "browserstack-build-1"
      },
      {
      "os_version": "Big Sur",
      "os": "OS X",
      "browser": "safari",
      "browser_version": "latest",
      "name": "Parallel Test3",
      "build": "browserstack-build-1"
}]
