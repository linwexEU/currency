from fastapi import APIRouter, Depends, status 
from fastapi.responses import JSONResponse
from app.api.endpoints.currency import Currency
from app.api.models.user import Currencies, User, ErrorCurrencies
from app.exception import ExchangeError
from app.core.security import get_current_user 
from typing import Union


router = APIRouter(
    prefix="/currency", 
    tags=["Currency"]
)


@router.get("/list")
async def currency_list(user: User = Depends(get_current_user)) -> JSONResponse: 
    return Currency.currency_data_list() 


@router.get("/exchange")
async def convert_currency(
    to: str, 
    from_: str, 
    amount: int | float,
    user: User = Depends(get_current_user), 
) -> Union[Currencies, ErrorCurrencies]: 
    result = Currency.convert_currency(to, from_, amount)
    
    if result.get("error"): 
        raise ExchangeError(status_code=status.HTTP_400_BAD_REQUEST, detail=result.get("error").get("info"))

    return result 




