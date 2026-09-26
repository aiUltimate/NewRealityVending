# New Reality — Linux Dashboard

The Company OS dashboard is designed to run locally on Linux with no Node.js,
npm, Flask, database, or external runtime required.

## Quick start

From the repository:

    cd dashboard
    chmod +x run-dashboard.sh
    ./run-dashboard.sh

The launcher starts a small Python standard-library web server and opens the
dashboard in the default browser.

If the browser does not open automatically, use the URL printed in the
terminal. The default is:

    http://127.0.0.1:8765/index.html

## Requirements

- Linux
- Python 3
- A modern browser: Firefox, Chromium, Chrome, Brave, or another browser
  supporting modern JavaScript and CSS

No packages need to be installed.

## Why a local server?

The dashboard loads the shared Company OS data from:

    ../data/company-os.json

Modern browsers can restrict JavaScript fetch requests when an HTML file is
opened directly with `file://`. The included launcher avoids that problem
while keeping the dashboard completely local.

## What it does

- Reads the repository's live `data/company-os.json`
- Presents the Company OS as connected modules
- Includes Command Center, Founder Today, Roadmap, Constitution, Governance,
  AI Intelligence, Evidence, Compliance, Products, Hardware, Operations,
  Economics, Community, Risk, Data Model, and Repository views
- Provides global search across the Company OS data
- Exports the currently loaded Company OS JSON
- Supports fullscreen mode
- Works on desktop and mobile-sized Linux screens
- Requires no cloud service for normal dashboard use

## Update workflow

When `data/company-os.json` changes, stop and restart the local server, then
refresh the browser. The dashboard will load the updated data automatically.

## Repository

https://github.com/aiUltimate/NewRealityVending
