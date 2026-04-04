"""
5-Layer Fraud Detection Engine — Gigsurance.ai
Adversarial Defense against GPS spoofing and coordinated fraud rings.
"""
import random
from datetime import datetime, timedelta
from app.models import db

def calculate_fraud_score(worker_id: str, trigger_type: str) -> dict:
    worker = db["workers"].get(worker_id, {})
    trust_score = worker.get("trust_score", 100.0)

    flags = []
    fraud_score = 0.0

    # ── Layer 1: Behavioural GPS Check ──
    gps_variance = random.uniform(1.5, 8.0)  # Simulated — real GPS drifts 3-5m
    if gps_variance < 0.5:
        fraud_score += 35
        flags.append("GPS_STATIC_NO_VARIANCE")
    else:
        fraud_score += max(0, 5 - gps_variance)

    # ── Layer 2: Truth Triangle (GPS + Cell Tower + Platform Login) ──
    cell_tower_match = random.random() > 0.05   # 95% match rate for real workers
    platform_login_active = random.random() > 0.1
    if not cell_tower_match:
        fraud_score += 30
        flags.append("CELL_TOWER_MISMATCH")
    if not platform_login_active:
        fraud_score += 20
        flags.append("PLATFORM_NOT_LOGGED_IN")

    # ── Layer 3: Claim Burst Detection (Social Graph) ──
    recent_claims = [
        c for c in db["claims"]
        if (datetime.now() - datetime.fromisoformat(c["created_at"])).seconds < 90
    ]
    if len(recent_claims) > 50:
        fraud_score += 25
        flags.append("BURST_CLAIM_RING_DETECTED")

    # ── Layer 4: Duplicate Claim Prevention ──
    worker_recent = [
        c for c in db["claims"]
        if c["worker_id"] == worker_id
        and c["trigger_type"] == trigger_type
        and (datetime.now() - datetime.fromisoformat(c["created_at"])).days < 1
    ]
    if len(worker_recent) > 0:
        fraud_score += 40
        flags.append("DUPLICATE_CLAIM_SAME_DAY")

    # ── Layer 5: Trust Score Adjustment ──
    trust_adjustment = (100 - trust_score) * 0.1
    fraud_score += trust_adjustment

    fraud_score = min(100, max(0, fraud_score))

    # Decision
    if fraud_score >= 60:
        decision = "flagged"
    elif fraud_score >= 30:
        decision = "review"
    else:
        decision = "approved"

    return {
        "fraud_score": round(fraud_score, 1),
        "decision": decision,
        "flags": flags,
        "gps_variance": round(gps_variance, 2),
        "cell_tower_match": cell_tower_match,
        "platform_login_active": platform_login_active,
    }
