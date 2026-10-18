import datetime as dt
import colorama
import sys

import requests

BASE = "https://cpbjr.github.io/catholic-readings-api"
WIDTH = 60


colorama.just_fix_windows_console()  
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
GOLD = "\033[38;5;221m"
CYAN = "\033[38;5;80m"
ROSE = "\033[38;5;211m"
GREEN = "\033[38;5;114m"
GRAY = "\033[38;5;245m"
RED = "\033[31m"


def paint(text, *styles):
    return "".join(styles) + str(text) + RESET


def get_json(kind: str, date: dt.date):
    url = f"{BASE}/{kind}/{date.year}/{date:%m-%d}.json"
    resp = requests.get(url, timeout=10)
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json()


def main():
    date = dt.date.today()

    try:
        readings = get_json("readings", date)
        calendar = get_json("liturgical-calendar", date)
    except requests.RequestException as e:
        sys.exit(paint(f"Couldn't fetch readings: {e}", RED))

    if not readings:
        sys.exit(paint(f"No readings data found for {date:%Y-%m-%d}.", RED))

    celebration = (calendar or {}).get("celebration", {})
    r = readings.get("readings", {})

    print()
    print(paint("✝  " + (celebration.get("name") or "Daily Readings"), BOLD, GOLD))
    print(
        paint(f"{date:%A, %B %d, %Y}", GRAY)
        + paint("  |  ", DIM)
        + paint(readings.get("season", ""), ITALIC, GREEN)
    )
    print(paint("═" * WIDTH, GOLD))
    print()

    labels = [
        ("firstReading", "First Reading"),
        ("psalm", "Psalm"),
        ("secondReading", "Second Reading"),
        ("gospel", "Gospel"),
    ]
    for key, label in labels:
        if r.get(key):
            print(paint(f"{label:<16}", BOLD, CYAN) + paint(r[key], ROSE))

    if celebration.get("quote"):
        print()
        print(paint(f"“{celebration['quote']}”", ITALIC, GRAY))

    if readings.get("usccbLink"):
        print()
        print(paint("Full text: ", DIM) + paint(readings["usccbLink"], UNDERLINE, CYAN))
    print()


if __name__ == "__main__":
    main()