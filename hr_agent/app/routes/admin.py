from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes.doctor import latest_reports

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="app/templates")

users = [
    {"id": 1, "name": "Admin User", "role": "admin"},
    {"id": 2, "name": "Doctor User", "role": "doctor"},
    {"id": 3, "name": "Patient User", "role": "patient"},
]

@router.get("/dashboard", response_class=HTMLResponse)
def admin_dashboard(request: Request):
    return templates.TemplateResponse("admin_dashboard.html", {"request": request, "users": users})

@router.get("/view-reports", response_class=HTMLResponse)
def view_reports(request: Request, role: str = Query(...)):
    return templates.TemplateResponse("patient_dashboard.html", {"request": request, "reports": latest_reports})
