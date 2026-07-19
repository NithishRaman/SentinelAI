def analyze_event(event):

    event_name = event.get("EventName")

    risky_events = [
        "CreateUser",
        "CreateAccessKey",
        "DeleteTrail",
        "StopLogging",
        "AuthorizeSecurityGroupIngress"
    ]

    if event_name in risky_events:
        risk = "HIGH"
    else:
        risk = "LOW"

    return {
        "event": event_name,
        "risk": risk,
        "analysis": f"Event {event_name} detected"
    }
