## EnviroweatherPy: client for Enviroweather APIs



this is a set of classes for interacting with the API, and for handling the
information returned from the api, 

- ewxapi: class for interacting with that API
  - read config
  - set base URLs
  - set up routes which can be changed in v2 class
  - get data from the API
  - tokens
  - auth
  - validate/format params sent (e.g. dates)

this class _could_ be responsible for determine the routes used by 
different data objects but by then the class will do almost everything
need 

however because the APIs are current not exactly 'resource based',
we could use extra APIs to add methods for handling and delivering the data 
returned by the API.  For example, a "mesonet" class could be a list of stations
to choose from.   the "station" class doesn't know how to 
get the info about a station, just how to handle and use that data

this becomes a 'binding' or translation layer from the API 
to python.  Is that necessary?  It is if we want to use the data in 
a python-based analysis but want to insulate the weather analysis from 
getting the data.   This allows us to change both the production API and this 
published library but still have the same interface for downstream 
analyses.  

the goal is to be able to swap our token or auth schemes and use the same
data classes.  

the data classes are pydantic data classes that have all the stuff that
pydantic offers.   Therefore this is an API-> pydantic binding

another goal is to inform a javascript/typescript set of data classes
based https://zod.dev/ which can validate or handle diversity of data from 
the API (e.g. errors) to define data classes that know how to 
get their own data from the API, so the JS FE does not have URLs and 
request calls littered through out the codebase.  Instead the codebase
interacts with data classs/models 