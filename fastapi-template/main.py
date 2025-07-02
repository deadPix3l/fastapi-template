#!/usr/bin/env python3
#from typing import Annotated

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# HTMX support for UI
from fastapi.templating import Jinja2Templates
from fasthx import Jinja


app = FastAPI()
templates = Jinja2Templates("frontend/templates")
jinja = Jinja(templates)

# so that we can get our CSS and SVGs, etc.
app.mount("/assets", StaticFiles(directory="frontend/assets", html=False), name="assets")

@app.get("/example")
async def example_endpoint():
    """ Example endpoint """
    pass

# WARNING: if mounting at /, it will shadow all routes except those defined above this!
@app.get("/")
@jinja.page("pages/index.html")
async def home_page():
    """ The frontend """
    return {}

