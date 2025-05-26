from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes.doctor import latest_reports

router = APIRouter(prefix="/patient")
templates = Jinja2Templates(directory="app/templates")

@router.get("/dashboard", response_class=HTMLResponse)
def patient_dashboard(request: Request):
    return templates.TemplateResponse("patient_dashboard.html", {"request": request, "reports": latest_reports})