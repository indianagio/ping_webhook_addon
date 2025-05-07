# Ping and Webhook Addon

This Home Assistant addon periodically:

- Pings `8.8.8.8` to measure latency.
- Gets the current external IP address using `https://api.ipify.org`.
- Sends both latency and external IP to a configurable webhook URL.

## Options

- `interval` (int): Number of seconds between each ping + webhook call. Default is 5 seconds.
- `webhook_url` (url): The full URL where the JSON payload will be sent.

## Example payload

```json
{
  "External IP": "93.184.216.34",
  "Machine latency": 25.3
}
```

## How it works

- The addon sends a POST request every interval to the `webhook_url`.
- If the external IP changes, it immediately sends an extra POST to notify.

## Healthcheck

The addon has a healthcheck to ensure the main Python script is running.

---

MIT License. Developed for Home Assistant.
