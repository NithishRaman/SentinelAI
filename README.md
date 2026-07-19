# SentinelAI

SentinelAI is an AI-powered AWS Cloud Security Monitoring tool.

## Features

- Monitor AWS CloudTrail events
- Analyze security events
- Assign risk levels
- Explain why an event is suspicious
- Provide remediation recommendations

## Technologies

- Python
- AWS CloudTrail
- Boto3
- Git
- GitHub

## Project Structure

```
SentinelAI/
│
├── ai_engine/
│   ├── analyzer.py
│   └── explainer.py
│
├── collectors/
│   └── cloudtrail.py
│
├── README.md
└── .gitignore
```

## Run

```bash
python -m collectors.cloudtrail
```

## Roadmap

- [x] Phase 1 – CloudTrail Collector
- [ ] Phase 2 – Detection Engine
- [ ] Phase 3 – Dashboard
- [ ] Phase 4 – AI Threat Reports
- [ ] Phase 5 – Deployment
