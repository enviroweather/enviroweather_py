# df is pandas data frame


def df_to_geojson(df, properties:list[str], lat:str='latitude', lon:str='longitude'):
    """convert any data frame with lat lon coords to geojson.  Assumes standard CRS
    stolen from https://geoffboeing.com/2015/10/exporting-python-data-geojson/
    and documented here.  hard to believe geopandas was a thing in 2015

    For example, a data frame with columns 
    street_address, status, latitude, longitude
    
    property_cols = ['street_address', 'status']
    geojson = df_to_geojson(df, properties = property_cols)
    
    Args:
        df (dataframe): dataframe with a latitude and longitude
        properties (list[str]): list of columns in the df to use as point props
        lat (str, optional): _description_. Defaults to 'latitude'.
        lon (str, optional): _description_. Defaults to 'longitude'.

    Returns:
        dict[str, Any]: valid geojson collection of point 'features
    """
    
    geojson = {'type':'FeatureCollection', 'features':[]}
    for _, row in df.iterrows():
        feature = {'type':'Feature',
        'properties':{},
        'geometry':{'type':'Point',
        'coordinates':[]}}
        feature['geometry']['coordinates'] = [row[lon],row[lat]]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
        
    return geojson