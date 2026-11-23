from fastapi import FastAPI, HTTPException, Response, status
import uvicorn
from jinja2 import Environment, FileSystemLoader
from starlette.templating import Jinja2Templates
from urllib import request
from starlette.staticfiles import StaticFiles
from sqlalchemy import select
from database import session, Product, User



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



templates = Jinja2Templates(directory="templates")

@app.get("/")
def privet():
    with session() as sess:
        result = sess.execute(select(Product))
        data = result.scalars().all()
        qwe = []
        for i in data:
            qwe.append([i.id, i.category_id,  i.name, i.description, i.price, i.photo])

        return templates.TemplateResponse({"request":request}, name="index.html", context={"data": qwe})


@app.get("/catalog")
def catalog():
    with session() as sess:
        result = sess.execute(select(Product))
        data = result.scalars().all()
        qwe = []
        for i in data:
            qwe.append([i.id,  i.category_id, i.name, i.description, i.price, i.photo])


        return templates.TemplateResponse({"request":request}, name="catalog.html", context={"data": qwe})



@app.get("/cart")
def cart():
    return templates.TemplateResponse({"request":request}, name="cart.html")



@app.get("/login")
def login():
    return templates.TemplateResponse({"request":request}, name="login.html")

@app.post("/secret")
def login():
    return templates.TemplateResponse({"request":request}, name="secret.html")



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)

@app.post("/login")
def login_user(user: UserLogin, response: Response)
    if user:
        with session() as session:
            data = session.scalars((select(User).where(User.email == user.email))).first()
            if data:
                if data.password == user.password:
                    token = security.create_access_token(uid=str(data.id))
                    response.set_cookie(config.JT_ACCESS_COOKIE_NAME, token)
                else:
                    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="нема вас")
        raise HTTPException(status_code=401, detail="Incorrect usernameor password")
    

                
