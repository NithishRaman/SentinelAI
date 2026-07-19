import boto3
from datetime import datetime, timedelta
from ai_engine.analyzer import analyze_event
from ai_engine.explainer import explain_event


def get_cloudtrail_events():

    cloudtrail = boto3.client("cloudtrail")

    end_time = datetime.now()
    start_time = end_time - timedelta(hours=24)

    response = cloudtrail.lookup_events(
        StartTime=start_time,
        EndTime=end_time,
        MaxResults=10
    )

    events = response.get("Events", [])

    for event in events:

        result = analyze_event(event)

        details = explain_event(event)

        result["reason"] = details["reason"]
        result["recommendation"] = details["recommendation"]

        print("=" * 50)
        print(result)


if __name__ == "__main__":
    get_cloudtrail_events()
