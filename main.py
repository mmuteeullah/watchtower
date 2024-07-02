from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import Request, HTTPException
from pydantic import BaseModel, ValidationError
from models.models import Alert
from enrich.enrich import enrich_critical_alert
from actions.action import take_action, take_critical_action
from typing import Dict, Any

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
        if alert.labels.severity == "CRITICAL":
            enriched_alert, set_pager_flag, kill_container_flag = enrich_critical_alert(alert)
            action_result = take_critical_action(enriched_alert, set_pager_flag=set_pager_flag, kill_container_flag=kill_container_flag)
        elif alert.labels.severity == "WARNING":
            enriched_alert = alert
            action_result = take_action(enriched_alert)
        else:
            raise HTTPException(status_code=400, detail="Invalid severity level")
        return {"enriched_alert": enriched_alert.model_dump(), "action_result": action_result}
    except ValidationError as e:
        raise e