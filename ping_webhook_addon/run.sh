#!/usr/bin/with-contenv bashio

INTERVAL=$(bashio::config 'interval')
WEBHOOK_URL=$(bashio::config 'webhook_url')

echo "Starting Ping and Webhook Addon"
echo "Interval: ${INTERVAL} seconds"
echo "Webhook URL: ${WEBHOOK_URL}"

exec python3 /ping_webhook.py --interval "${INTERVAL}" --webhook_url "${WEBHOOK_URL}"
