from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.services import ai_nlp

router = APIRouter(prefix="/doctor")
templates = Jinja2Templates(directory="app/templates")

# shared in-memory store (mock DB)
latest_reports = []

@router.get("/dashboard", response_class=HTMLResponse)
def doctor_dashboard(request: Request):
    return templates.TemplateResponse("doctor_dashboard.html", {"request": request})

@router.post("/generate-view", response_class=HTMLResponse)
def generate_view(request: Request, patient_id: int = Form(...)):
    report = ai_nlp.generate_report({"patient_id": patient_id})["content"]
    latest_reports.append(report)
    return templates.TemplateResponse("doctor_dashboard.html", {"request": request, "report": report})
