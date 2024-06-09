# monorepo-vercel
This is a simple demo app that is meant to run on Vercel.

## Structure
It's composed of one Flask API and one VueJS UI.

### API

### UI
The UI has one button that calls the /api endpoint and displays the returned JSON.


## How to setup the project?
Create two projects in Vercel, one with **backend** folder, another one with **frontend** folder.
Vercel should detect that the frontend needs a Vite runtime, there's nothing to do more than configuring the environment variable **VITE_API_URL** in the frontend project so that the frontend knows the URL of the API.
