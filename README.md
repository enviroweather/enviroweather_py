# Enviroweather API Documentation and Python Package

## **THIS PROJECT IS SUSPENDED IN FAVOR OF DIFFERENT APPROACH**

for new documentation approach, please see https://gitlab.msu.edu/Enviroweather/enviroweather_api_documentation

---- 

*previous readme*

[Enviroweather](https://enviroweather.msu.edu) is a sustainable weather-based information system that helps users
make pest, plant production, and natural resource management decisions in Michigan, hosted by Michigan State Unversity, 
led by Jeff Andresen, Professor of Meteorology/Climatology in the Department of Geography, the  State Climatologist for Michigan, 

For more information see our website. 

The Enviroweather system provides various APIs that provide information about our weather network, the data the network
creates and can "run" the models that are part of this system. These APIs are utilized by our main website (linked above)
and mobile applications developed by MABR/MSU. You do not need the code in this project to use Enviroweather - see our website
for more information. 

This project is a means to document our underlying APIs for those who want to access our data and models via code, starting 
with Python. 

The main documentation is available as an Active Code Notebook in the doc folder.   

This project is in very early draft stage and not complete at this time.   In the near future the documentation here
will be available as a webpage. 

For now, see [doc/ewxrmapiv1.py](doc/ewxrmapiv1.py)

## Developers

to contribute to the documentation, you need to install the requirements.  This is not needed to view the docs, only to 
edit them. 

- clone this repo
- recommended to use the uv package manager: https://docs.astral.sh/uv/getting-started/installation/
- uv 

### editing docs

The docs can be edited with VS code or the marimo in-browser editor.  The latter 
seems to be a more complete editing experience as these are pretty different 
from jupyter notebooks.  

`marimo edit .`  

### adding dependencies (other packages)

If additional packages are needed for the notebooks or modules, `uv` works well for this

For example, we use the `requests` package for testing the API, so had to use 

`uv add requests`  which adds to the package spec and installs.  

### Sharing Documentation.  

There are two ways to share the notebooks that document our APIs as . 

1. Marimo preview from github (interactive)
2. publish as a 'static' web page, on github pages

Neither requires the reader to install anything on their computer.  To the user
they are nearly equivalant ( except for links between notebooks, which is TBD).  

The second options requires the developer to export notebooks to HTML, and push
the HTML to github

### Sharing via Marimo service

The top of this readme and our table of contents in the docs 

### Building web documentation from notebooks

A developer To create a static HTML/web page from a notebook you've edited, for a notebook
named "apidoc.py", use the following command

`marimo export html-wasm doc/apidoc.py -o html/apidoc.html --mode run --show-code --no-include-cloudflare --execute`

The add to git and push.  Note in the future we will work to use github
workflows, this is the manual process, documented for now. 

```
## assuming you'ved edited a notebook in the docs folder
## assuming the main branch
git add docs/apidoc.py
git commit -m "your message, e.g. updated apidoc for new routes"
marimo export html-wasm doc/apidoc.py -o html/apidoc.html --mode run --show-code --no-include-cloudflare --execute
git add html
git commit -m "html export for apidoc"
git push github main
```

This does account for adding new notebooks that require updates to the documentation
table of contents (TBD!)

