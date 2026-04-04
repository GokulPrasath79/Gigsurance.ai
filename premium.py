"""
Dynamic Weekly Premium Calculator
Uses a risk scoring model to personalise premiums per worker.
"""

ZONE_RISK = {
    # pincode prefix → flood/disruption risk score (0-1)
    "600": 0.75,  # Chennai — high flood risk
    "110": 0.60,  # Delhi — high AQI + curfew risk
    "400": 0.55,  # Mumbai — flood risk
    "560": 0.35,  # Bengaluru — relatively low
    "500": 0.45,  # Hyderabad — moderate
    "700": 0.50,  # Kolkata — moderate flood
}

PLATFORM_RELIABILITY = {
    "amazon_flex": 0.92,
    "flipkart_ekart": 0.88,
}

SEASONAL_MULTIPLIER = {
    1: 1.0, 2: 1.0, 3: 1.1, 4: 1.2,   # Jan-Apr: summer heat rising
    5: 1.3, 6: 1.5, 7: 1.6, 8: 1.6,   # May-Aug: monsoon season
    9: 1.4, 10: 1.3, 11: 1.1, 12: 1.0 # Sep-Dec: post monsoon
}

TIER_CONFIG = {
    "basic":    {"base": 29,  "max_payout": 1500, "coverage_days": 2},
    "standard": {"base": 49,  "max_payout": 3000, "coverage_days": 4},
    "pro":      {"base": 79,  "max_payout": 5000, "coverage_days": 6},
}

from datetime import datetime

def calculate_premium(pincode: str, platform: str, daily_earnings: float, tier: str) -> dict:
    prefix = pincode[:3]
    zone_risk = ZONE_RISK.get(prefix, 0.5)
    platform_risk = 1 - PLATFORM_RELIABILITY.get(platform, 0.9)
    month = datetime.now().month
    seasonal = SEASONAL_MULTIPLIER.get(month, 1.0)
    earnings_factor = min(daily_earnings / 700, 1.5)  # normalise around ₹700/day

    # Composite risk score (0-100)
    risk_score = round(
        (zone_risk * 40 + platform_risk * 20 + (seasonal - 1) * 30 + (earnings_factor - 1) * 10),
        2
    )
    risk_score = max(0, min(100, risk_score * 100))

    # Risk multiplier (0.8x to 1.8x)
    risk_multiplier = 0.8 + (risk_score / 100) * 1.0

    config = TIER_CONFIG[tier]
    final_premium = round(config["base"] * risk_multiplier, 2)

    return {
        "tier": tier,
        "base_premium": config["base"],
        "risk_score": round(risk_score, 1),
        "risk_multiplier": round(risk_multiplier, 2),
        "weekly_premium": final_premium,
        "max_payout": config["max_payout"],
        "coverage_days": config["coverage_days"],
        "zone_risk": zone_risk,
        "seasonal_factor": seasonal,
    }
