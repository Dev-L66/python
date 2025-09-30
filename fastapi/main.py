from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Hello world!", "home":"Ths is home page."}

@app.post('/')
def hello():
    return {"message":"Hi world, from post request!"}


@app.put('/')
def hello():
    return {"message":"Hi world, from put request!"}