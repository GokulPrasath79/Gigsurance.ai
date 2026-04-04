from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, policy, claims, triggers

app = FastAPI(title="Gigsurance.ai API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(policy.router, prefix="/api/policy", tags=["Policy"])
app.include_router(claims.router, prefix="/api/claims", tags=["Claims"])
app.include_router(triggers.router, prefix="/api/triggers", tags=["Triggers"])

@app.get("/")
def root():
    return {"message": "Gigsurance.ai API is running"}
