# /// script
# dependencies = ["marimo"]
# requires-python = ">=3.12"
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Mapping Enviroweather Stations

    This is an abbreviated demonstration of how to get a list of stations, make a maps and select one to show details.
    """)
    return


@app.cell
def _():
    # imports
    import requests
    import json
    from datetime import datetime, date
    from os import path


    return date, json, path, requests


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    setup
    """)
    return


@app.cell
def _(date):
    # setup 

    todays_date = date.today().isoformat()
    todays_date
    return (todays_date,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Configuration
    """)
    return


@app.cell
def _(json):
    # alternatively read JSON from disk with multiple environments in it

    config_json = """
    {
        "production": {
            "api_url": "https://api.enviroweather.msu.edu/ewx-api/api",
            "rm_api_url": "https://api.enviroweather.msu.edu/ewx-api/api"
        }
    }
    """

    # request file ewx_environments.json for full list of environments
    # some environments require MSU VPN access
    # config_file = 'ewx_environments.json'
    # with open(config_file,"r") as f: ewx_env_dict  = json.load(f)

    ewx_env_dict = json.loads(config_json)

    ewx_env = 'production'
    api_url = ewx_env_dict[ewx_env]["api_url"]
    rm_api_url = ewx_env_dict[ewx_env]["rm_api_url"]

    api_url
    return (api_url,)


@app.cell
def _(api_url, path, requests):
    # confirm urls exist

    try:
        response = requests.options(path.dirname(api_url))
        if response.ok: 
            url_check_msg = "Success - API is accessible."
        else:
            url_check_msg = response.status_code
    except Exception as e:
         url_check_msg  = f"Failure to connect to API - Unknown error occurred: {e}."

    url_check_msg
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### auth/token
    """)
    return


@app.cell
def _(api_url, requests):
    token_url = f"{api_url}/db2/siteToken"
    token_response = requests.request(method='GET', url=token_url)
    token_response_data = token_response.json()
    if not(token_response_data["error"]):
        anonymous_token = token_response_data['data']['token']
    else:
        anonymous_token = ""
        print(f"error in response when acquiring token: {token_response.status}")

    anonymous_token
    return (anonymous_token,)


@app.cell
def _(api_url, requests):
    def get_anonymous_token(url):
        token_url = f"{url}/db2/siteToken"
        token_response = requests.request(method='GET', url=token_url)
        token_response_data = token_response.json()
        if not(token_response_data["error"]):
            anonymous_token = token_response_data['data']['token']
        else:
            anonymous_token = ""
            print(token_response_data)
            print(f"error in response when acquiring token: {token_response.status}")

    api_token = get_anonymous_token(api_url)
    print(api_token)
    if not api_token:
        print("no token, stop here")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### get stations
    """)
    return


@app.cell
def _(
    anonymous_token,
    api_url,
    pd,
    requests,
    station_list_container,
    todays_date,
):
    token_header = {"Authorization": f"Bearer {anonymous_token}"}
    station_list_url = f"{api_url}/db2/places?show=ewxstation"
    station_list_response = requests.request(method='GET', url=station_list_url, headers = token_header )
    station_list = station_list_container[0]['options']
    active_station_list = [s for s in station_list if s['endDate'] == todays_date]
    stations_df = pd.DataFrame(active_station_list)
    stations_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### create map-able data

    convert for mapping using GeoPandas

    see https://eoda-dev.github.io/py-openlayers/concepts/geopandas/
    """)
    return


@app.cell
def _():
    #
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Map with OpenLayers

    see https://pypi.org/project/openlayers/

    examples https://molab.marimo.io/github/marimo-team/gallery-examples/blob/main/notebooks/geo/earthquake.py/wasm
    """)
    return


if __name__ == "__main__":
    app.run()
