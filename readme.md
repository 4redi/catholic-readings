# Daily catholic readings

A small command-line tool that prints today's Catholic Mass readings in your terminal, with color and a clean layout. Type `readings`, get the day's liturgical celebration, season, and scripture references.

```bash

✝  Saturday of the Twenty-Ninth Week in Ordinary Time
Saturday, October 24, 2026  |  Ordinary Time
════════════════════════════════════════════════════════════

First Reading   Ephesians 4:7-16
Psalm           Psalm 122:1-2, 3-4ab, 4cd-5
Gospel          Luke 13:1-9

Full text: https://bible.usccb.org/bible/readings/...
```

> (Example output. Actual readings depend on the day.)

## Features

* Today's First Reading, Psalm, Second Reading (when there is one), and Gospel
* Name of the day's liturgical celebration and the liturgical season
* Featured quote of the day, when available
* Link to the full text on the USCCB website
* Colored output that works on Windows, macOS, and Linux
* Clear error messages if you're offline or no data exists for the date

## Requirements

* Python 3.8 or newer
* An internet connection (readings are fetched live)
* Python packages: [`requests`](https://pypi.org/project/requests/) and [`colorama`](https://pypi.org/project/colorama/) (installed automatically in the steps below)

## Installation

### Recommended: install as a command

Clone the repo and install it with pip:

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
pip install -e .
```

That's it. Open a terminal anywhere and run:

```bash
readings
```

Prefer to keep it isolated from your other Python packages? Use [pipx](https://pipx.pypa.io/) instead:

```bash
pipx install .
```

### Alternative: run the script directly

If you don't want to install anything as a command:

```bash
pip install requests colorama
python main.py
```

### Alternative (Windows): use the launcher

The repo includes a `readings.bat` launcher that sets UTF-8 mode and runs `main.py`. Add the project folder to your `PATH`, then type `readings` in any new terminal.

## Usage

```bash
readings
```

There are no arguments or options. It always shows today's readings, based on your computer's date.

## How it works

The tool pulls data from the free [Catholic Readings API](https://cpbjr.github.io/catholic-readings-api), a static JSON API hosted on GitHub Pages. For today's date it makes two requests:

Read more about it on the website.

The script then formats everything with ANSI colors (via `colorama`, which makes them work in the Windows console) and prints it.

If the readings request returns a 404, the tool tells you no data exists for that date. If the liturgical calendar request returns nothing, it falls back to the title "Daily Readings."

## Project structure

```bash
.
├── main.py          # The whole program: fetching, formatting, printing
├── pyproject.toml   # Packaging config; defines the `readings` command
└── README.md
```

## Troubleshooting

**`readings` is not recognized as a command**
Make sure the install finished without errors, then open a *new* terminal. If it still fails, your Python `Scripts` folder may not be on your `PATH`. Running `python -m pip install -e .` and checking where pip placed the script usually shows the location.

**Weird characters instead of `✝` or `═`**
Your terminal isn't using UTF-8. The program already switches its output to UTF-8, but older terminals may still need a font that supports those symbols. On Windows, [Windows Terminal](https://aka.ms/terminal) works well.

**"Couldn't fetch readings"**
You're probably offline, or the API is temporarily unreachable. Check your connection and try again.

**"No readings data found for ..."**
The API doesn't have data for today's date, which can happen near the edge of the years it covers.

## Credits

* Reading data from the [Catholic Readings API](https://cpbjr.github.io/catholic-readings-api) by cpbjr
* Full readings text and links via the [United States Conference of Catholic Bishops](https://bible.usccb.org/)

### "Go into all the world and preach the Gospel to every creature." - Mark 16:15"
