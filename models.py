from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import uuid

# ── In-memory store (replace with PostgreSQL in production) ──
db = {
    "workers": {},
    "policies": {},
    "claims": [],
    "triggers": []
}

# ── Schemas ──
class WorkerRegister(BaseModel):
    name: str
    phone: str
    email: str
    platform: str        # amazon_flex | flipkart_ekart
    city: str
    pincode: str
    upi_id: str
    daily_earnings: float

class WorkerLogin(BaseModel):
    phone: str

class PolicyCreate(BaseModel):
    worker_id: str
    tier: str            # basic | standard | pro

class ClaimCreate(BaseModel):
    worker_id: str
    trigger_type: str
    description: str

class Worker(BaseModel):
    id: str
    name: str
    phone: str
    email: str
    platform: str
    city: str
    pincode: str
    upi_id: str
    daily_earnings: float
    trust_score: float = 100.0
    created_at: str

class Policy(BaseModel):
    id: str
    worker_id: str
    tier: str
    weekly_premium: float
    max_payout: float
    coverage_days: int
    risk_score: float
    status: str          # active | expired | cancelled
    start_date: str
    end_date: str

class Claim(BaseModel):
    id: str
    worker_id: str
    policy_id: str
    trigger_type: str
    description: str
    status: str          # pending | approved | rejected | flagged
    payout_amount: float
    fraud_score: float
    created_at: str
