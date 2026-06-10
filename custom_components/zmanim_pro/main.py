name: Generate Daily Zmanim JSON for Loxone

on:
  schedule:
    - cron: '0 1 * * *' # Draait elke nacht om 01:00 UTC (02:00 / 03:00 Nederlandse tijd)
  workflow_dispatch: # Hiermee kun je de actie handmatig starten in GitHub om te testen

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run Zmanim script
        env:
          TIMEZONE: "Europe/Amsterdam" # Vervang door jouw tijdzone indien nodig
          LATITUDE: "52.3676"          # VERVANG DOOR JOUW EXACTE LATITUDE
          LONGITUDE: "4.9041"          # VERVANG DOOR JOUW EXACTE LONGITUDE
          CITY: "MijnHuis"
        run: python main.py

      - name: Commit and Push JSON
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@://github.com"
          git add zmanim.json
          git commit -m "Update daily zmanim JSON" || exit 0
          git push
