# main.py
from fastapi import FastAPI
app = FastAPI()
scripts: {
"dev": "react-scripts start",
"start": "serve -s build",
"build": "react-scripts build",
"test": "react-scripts test --env=jsdom",
"eject": "react-scripts eject",
"heroku-postbuild": "npm run build"
}
@app.get("/")
def hello():
    return {"message":"Hello TutLinks.com"}
