myfamily.com-scrape
===================

myfamily.com is shutting down in September, this repo contains scrips that scrape the site to a json file, then serve it as a flask app.

The urls in this script are tied to a specific myfamily.com site. They should be easy to change as needed.

## Requirements

Run `pip3 install flask frozen_flask beautifulsoup4 selenium` to make sure you have all the requirements.

You will also need firefox installed.

## Usage

### Scraping Data

Open `scrape-news.py` and change the username and password variables to your myfamily.com credentials. Then, run the script. It should open and start downloading the pages of each news item to `data/raw-html/news/`.

### Processing Data

Now that you have all the news postings saved, they need to be converted into a useful format. Run `extract-news-to-json.py` after a few minutes, it will output `news.json` in 	`data/output-json/news.json`.

### Displaying Data

Run `serve_data.py` in `serve-data`. This will serve `data/output-json/news.json` as html at `http://localhost:5000`. If you want to export the html, run `freeze.py` in `serve-data`. This will save html files in `serve-data/build/`.

## License

This project is licensed under GPL 3.0, see LICENSE