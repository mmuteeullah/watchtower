from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import Request
from pydantic import ValidationError
from models import Alert
from core import AlertManager

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors(), "body": exc.body}
    )

@app.exception_handler(ValidationError)
async def pydantic_validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()}
    )

@app.get("/")
async def healthCheck():
    return {"Hello": "World"}

@app.post("/webhook")
async def receive_alert(alert: Alert):
    try:
        AlertManager(alert).enrich().notify()
        return {"message": "ok"}
    except ValidationError as e:
        raise e