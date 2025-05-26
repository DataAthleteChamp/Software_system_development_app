from fastapi import FastAPI
from db.database import Base, engine
from app.routes import auth, doctor, patient, admin
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(doctor.router)
app.include_router(patient.router)
app.include_router(admin.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def root():
    return {"message": "HR Agent API is running!"}
