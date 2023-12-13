from fastapi import FastAPI 
from app.core.security import router as router_auth
from app.utils.external_api import router as router_currency


app = FastAPI() 


app.include_router(router_auth)
app.include_router(router_currency)







