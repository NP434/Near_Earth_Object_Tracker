[![run-tests](https://github.com/NP434/Near_Earth_Object_Tracker/actions/workflows/python-test.yml/badge.svg)](https://github.com/NP434/Near_Earth_Object_Tracker/actions/workflows/python-test.yml)[![Docker-publish](https://github.com/NP434/Near_Earth_Object_Tracker/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/NP434/Near_Earth_Object_Tracker/actions/workflows/docker-publish.yml)

# Near Earth Object Tracker

This application retrieves data on Near Earth Objects (NEOs) from NASA's NEO API and visualizes their distance from Earth on a scaled graph.

Built with Streamlit, the app offers an interactive interface to explore potentially hazardous asteroids and other near-Earth objects in real time.
App Link: https://neo-tracker.streamlit.app

## Project structure
- The .app folder contains the streamlit home page code, as well as the additional data page, and the data fetch funtion.
- The .tests folder contains the tess for the data fetch and page generation, and are run using pytest.
- The github workflows contains the workflows that automically run tests upon a push, and once the tests pass, a docker container is generated.
