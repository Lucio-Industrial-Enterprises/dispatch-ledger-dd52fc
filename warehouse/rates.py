"""Shipping rate calculations."""

_ZONE_BASE = {"local": 5.0, "regional": 8.0}
_SERVICE_SURCHARGE = {"standard": 0.0, "express": 7.0}


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Return a shipping quote in dollars.

    Args:
        weight_kg: Shipment weight; must be positive.
        zone: Delivery zone — ``"local"`` or ``"regional"``.
        service: Service level — ``"standard"`` (default) or ``"express"``.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in _ZONE_BASE:
        raise ValueError("unknown zone")
    if service not in _SERVICE_SURCHARGE:
        raise ValueError("unknown service")
    base = _ZONE_BASE[zone] + _SERVICE_SURCHARGE[service]
    return round(base + 1.5 * weight_kg, 2)
