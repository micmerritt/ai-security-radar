# AI Security Radar

AI Security Radar tracks emerging research, tools, and attack techniques in artificial intelligence security. 
Simple Goal: Identify signals early and translate them into practical security insights.

This project monitors:
• AI security research papers  
• open-source AI security tools  
• emerging attack techniques  
• security implications for enterprise systems  

Each week the radar highlights:
- important research
- notable tools
- emerging attack patterns
- ideas for security tooling

---

## Weekly Radar

See the latest findings here:

- [Latest Radar](radar/latest.md) – Most recent research signals discovered by the radar.
- [Weekly Digest](radar/weekly-digest.md) – Running log of radar runs and emerging patterns.

## Development

The collector uses only the Python standard library. Run the test suite before
changing its collection, filtering, or categorization logic:

```bash
python -m unittest discover -s tests -v
```

The scheduled collector retries temporary arXiv failures three times. If the
source is still unavailable, the workflow records a warning and preserves the
last successful radar snapshot instead of replacing it or sending a failure
notification. The next daily run automatically tries again.

### Testing weekly email delivery

Run the **AI Security Radar Weekly Email** workflow manually and leave
`test_email` enabled. The workflow sends a subject prefixed with `[TEST]` using
the configured SMTP secrets, without querying issues or generating a report.
Disable `test_email` on a manual run to send the normal weekly report.
