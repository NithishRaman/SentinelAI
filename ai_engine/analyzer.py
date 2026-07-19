def analyze_event(event):

    event_name = event.get("EventName")

    high_risk_events = [
        "DeleteTrail",
        "DeleteBucket",
        "DisableMFADevice",
        "CreateAccessKey",
        "AuthorizeSecurityGroupIngress"
    ]

    medium_risk_events = [
        "AssumeRole",
        "CreateUser",
        "PutBucketPolicy"
    ]


    if event_name in high_risk_events:
        return {
            "event": event_name,
            "risk": "HIGH",
            "analysis": "Potential security threat detected"
        }


    elif event_name in medium_risk_events:
        return {
            "event": event_name,
            "risk": "MEDIUM",
            "analysis": "Suspicious activity requires review"
        }


    else:
        return {
            "event": event_name,
            "risk": "LOW",
            "analysis": "Normal AWS activity"
        }
