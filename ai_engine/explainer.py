def explain_event(event):

    explanations = {
        "AssumeRole": {
            "reason": "A role was assumed. This can indicate privilege usage.",
            "recommendation": "Verify the role owner and check if this activity was expected."
        },
        "CreateAccessKey": {
            "reason": "A new AWS access key was created.",
            "recommendation": "Confirm the user identity and enable MFA."
        },
        "AuthorizeSecurityGroupIngress": {
            "reason": "Network access rules were modified.",
            "recommendation": "Check if ports were exposed publicly."
        }
    }

    event_name = event.get("EventName")

    if event_name in explanations:
        return explanations[event_name]

    return {
        "reason": "Normal AWS operation detected.",
        "recommendation": "No action required."
    }
