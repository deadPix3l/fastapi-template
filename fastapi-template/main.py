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

# example global variable (bad form, only for demo)
app.customer_count = 12

# so that we can get our CSS and SVGs, etc.
app.mount("/assets", StaticFiles(directory="frontend/assets", html=False), name="assets")
app.mount("/images", StaticFiles(directory="frontend/assets/images", html=False), name="images")


@app.get("/customers")
def customer_count():
    """ Get Customers - Example Endpoint """
    app.customer_count += 1
    return app.customer_count

# Prerendered html template
# (utilize build step before server start if using jinja)
# WARNING: if mounting at /, it will shadow all routes except those defined above this!
app.mount("/", StaticFiles(directory="frontend/templates/build", html=True), name="built")

# ALTERNATIVE FRONTEND:
# Jinja template, rendered at runtime
# WARNING: if mounting at /, it will shadow all routes except those defined above this!
#@app.get('/')
#@jinja.page('pages/index.html')
#def index_page():
    #return {} # pass template variables here
