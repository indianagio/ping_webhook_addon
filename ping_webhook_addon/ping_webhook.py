import argparse
import requests
import subprocess
import time

def get_latency():
    try:
        result = subprocess.run(['ping', '-c', '1', '8.8.8.8'], capture_output=True, text=True)
        if result.returncode == 0:
            for line in result.stdout.split('\n'):
                if 'time=' in line:
                    return float(line.split('time=')[1].split(' ')[0])
    except Exception as e:
        print(f"Error getting latency: {e}")
    return None

def get_external_ip():
    try:
        result = subprocess.run(['curl', '-s', 'https://api.ipify.org'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception as e:
        print(f"Error getting external IP: {e}")
    return None

def main(interval, webhook_url):
    last_ip = None
    while True:
        latency = get_latency()
        external_ip = get_external_ip()

        payload = {
            "External IP": external_ip,
            "Machine latency": latency
        }

        try:
            response = requests.post(webhook_url, json=payload, timeout=10)
            print(f"Sent to {webhook_url} | Status: {response.status_code} | Payload: {payload}")
        except Exception as e:
            print(f"Failed to send webhook: {e}")

        if external_ip != last_ip:
            last_ip = external_ip
            print(f"External IP changed: {external_ip} (sending extra notification)")
            try:
                response = requests.post(webhook_url, json=payload, timeout=10)
                print(f"Sent IP change to {webhook_url} | Status: {response.status_code}")
            except Exception as e:
                print(f"Failed to send webhook on IP change: {e}")

        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ping and Webhook Addon')
    parser.add_argument('--interval', type=int, required=True)
    parser.add_argument('--webhook_url', type=str, required=True)
    args = parser.parse_args()
    main(args.interval, args.webhook_url)
