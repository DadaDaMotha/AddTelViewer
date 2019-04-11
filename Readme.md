# AddTelViewer

This is a simple experiment that tried to:

- customize Dash by Plotly by using another index.html template to inject a custom template, additional
javascript and html assets, Linkt to Routes
- using docker and docker-compose to run the app for development
- try out regex patterns and beautiful soup.
- try out a mapbox component with plz search from opendata.swiss.

## How to run this app

First, you need docker and docker compose. To run the app on `localhost:8080`:

    docker-compose up --build

**WARNING**: Web Scraping of the phone book and saving this data into a database is illegal. The creator of
this repo does not hold responsible for any abuse of this software.
