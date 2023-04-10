from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    detail = exc.errors()[0]["msg"]
    return JSONResponse(content={"info": detail}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    detail = exc.errors()[0]["msg"]
    return JSONResponse(content={"info": detail}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
