from fastapi import FastAPI
from app.auth.login_route import router as auth_router
from app.user_policy.user_policy_routes import router as user_policy_router
from app.organization.organization_routes import router as organization_router
from app.projects.project_routes import router as project_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_policy_router)
app.include_router(organization_router)
app.include_router(project_router)

app.add_middleware(
       CORSMiddleware,
       allow_credentials=True,
       allow_origins=["*"],
       allow_methods=["*"],
       allow_headers=["*"],
   )

@app.get("/health")
def health():
    return {
        "application_status": "running"
    }