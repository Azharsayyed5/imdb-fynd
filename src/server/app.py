from fastapi import FastAPI
from .imdb.routes.views import router as IMDBRouter
from .accounts.routes.views import router as AccountsRouter

app = FastAPI()
app.include_router(IMDBRouter, tags=["IMDB"], prefix="/v1/imbd")
app.include_router(AccountsRouter, tags=["Accounts"], prefix="/v1/accounts")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to IMBD!"}
