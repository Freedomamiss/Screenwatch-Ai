from pathlib import Path
import time

from screenwatch.analyzer import analyze_image


SCREENSHOT_DIR = Path(r"C:\Users\abbal\OneDrive\Pictures\Screenshots")
POLL_INTERVAL_SECONDS = 2


def get_latest_screenshot():
    files = list(SCREENSHOT_DIR.glob("Screenshot *.png"))

    if not files:
        return None

    files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    return files[0]


def main():
    print("[ScreenWatch] Started. Monitoring screenshots...")

    last_seen_file = None

    try:
        while True:
            latest_file = get_latest_screenshot()

            if latest_file is None:
                time.sleep(POLL_INTERVAL_SECONDS)
                continue

            if latest_file != last_seen_file:
                print(f"\n[ScreenWatch] New screenshot detected: {latest_file.name}")

                try:
                    result = analyze_image(str(latest_file))

                    print("[ScreenWatch] Observation:")
                    print(result)

                    # Future integration point:
                    # send_to_agent(result)

                except Exception as e:
                    print(f"[ScreenWatch] Error analyzing image: {e}")

                last_seen_file = latest_file

            time.sleep(POLL_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print("\n[ScreenWatch] Stopped by user.")


if __name__ == "__main__":
    main()