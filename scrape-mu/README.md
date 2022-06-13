# Scraping the MU Exhibitions page
This scrapes the archive of exhibitions on the site of MU: https://mu.nl/nl/exhibitions/archive

## Run this yourself
1. Make sure you have `pyenv` installed 
2. Activate the correct python version: `pyenv local`
3. Create a new venv: `python -m venv env`
4. Install the requirements `pip install -r requirements.txt` 
5. Make `scrape.py` executable: `chmod +x ./scrape.py`
6. Check out the code in `scrape.py` to see what is possible, right now you can either scrape all items on the index, of scrape individual pages