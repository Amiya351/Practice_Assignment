import psutil
import time

THRESHOLD = 80  # CPU usage percentage threshold

def monitor_cpu():
    print("Monitoring CPU usage...")
    try:
        while True:
            usage = psutil.cpu_percent(interval=1)
            if usage > THRESHOLD:
                print(f"Alert! CPU usage exceeds threshold: {usage}%")
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu()