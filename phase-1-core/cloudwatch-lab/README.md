# Lab 4 — CloudWatch (Logs & Metrics)

**Goal:** understand AWS observability by creating a log group, writing and reading log
events (the exact loop you'll use to debug Lambdas/containers), and peeking at metrics.
Then tear the log group down.

## Mental model
**CloudWatch is AWS's eyes and ears** — it collects telemetry from nearly everything:
- **Metrics** — numbers over time (CPU %, request count, errors, latency). AWS auto-publishes these.
- **Logs** — the text your code prints. **Every Lambda, ECS task, and app streams logs here.** This is where you debug.
- **Alarms** — fire an action when a metric crosses a threshold (e.g. errors > 5).
- **Dashboards** — visualize metrics.

## Logs hierarchy
```
Log Group   (e.g. /aws/lambda/my-func)   ← one per application/service
  └─ Log Stream   (one per source/instance)
       └─ Log Event   (a single timestamped line)
```

## Key commands
| Command | Does |
|---|---|
| `aws logs create-log-group` | make a log group |
| `aws logs create-log-stream` | make a stream inside it |
| `aws logs put-log-events` | write log line(s) |
| `aws logs tail <group> --follow` | live-tail logs (like `tail -f`) |
| `aws logs filter-log-events` | search logs |
| `aws logs delete-log-group` | teardown |

## Cost
Tiny at this scale (Free Tier: 5 GB logs ingestion/storage). We delete the group at the end.
