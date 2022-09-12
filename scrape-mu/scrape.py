#!/usr/bin/env python3
from bs4 import BeautifulSoup
from dataknead import Knead
from pathlib import Path
import re
import requests
import sys

ROOT = "https://mu.nl"
URL = "https://mu.nl/nl/exhibitions/archive"

def fetch_article(link):
    print(f"Fetching <{link}>")
    slug = get_slug(link)
    path = slug["path_en"]

    # Check if this already exists
    if path.exists():
        print(f"Path <{path}> exists, skip")
        return

    req = requests.get(link)

    with open(path, "w") as f:
        f.write(req.text)

    print(f"Written site to <{path}>")

def get_slug(link):
    # Create an unique ID we can use as a base for saving the data
    slug = link.split("/")[-1]

    # Fetch English version
    path_en = Path("data") / f"{slug}-en.html"
    path_nl = Path("data") / f"{slug}-nl.html"

    return {
        "path_en" : path_en,
        "path_nl" : path_nl,
        "slug" : slug
    }

def get_data():
    lang = "en"

    with open(f"index-{lang}.html") as f:
        index_items = get_index(f.read())

    items = []

    for index, item in enumerate(index_items):
        slug = get_slug(item["href"])
        path = slug[f"path_{lang}"]

        with open(path) as f:
            print(f"Parsing {path}")
            article = parse_article(f.read())

        item.update(article)

        items.append({
            "index" : index,
            "slug" : slug["slug"],
            lang : item
        })

    return items

def get_index(html):
    soup = BeautifulSoup(html, "lxml")
    articles = soup.select(".articles article")
    return [ parse_link(a) for a in articles ]

def get_text(el):
    if not el:
        return None

    text = el.get_text()
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = text.replace("\u00a0", " ")
    text = re.sub(u"(\u2018|\u2019)", "'", text)
    text = text.strip()

    return text

def parse_article(html):
    soup = BeautifulSoup(html, "lxml")
    item = soup.select_one(".item")

    if not item:
        return {
            "_status" : "no-item"
        }

    info = item.select_one(".expo-info")
    on_show = None
    opening = None

    if info:
        events = info.select(".sub-event")

        if len(events) > 0:
            on_show = get_text(events[0].select_one("p"))

        if len(events) > 1:
            opening = get_text(events[1])

    images = item.select(".image-slider img")

    if images:
        images = [ {"src" : ROOT + i.get("src", ""), "alt" : i.get("alt", None)} for i in images]
    else:
        images = []

    link_nl = soup.select_one('.navigation-languages a[hreflang="nl"]').get("href")
    link_en = soup.select_one('.navigation-languages a[hreflang="en"]').get("href")

    return {
        "_page_status" : "ok",
        "page_images" : images,
        "link_en" : f"{ROOT}{link_en}",
        "link_nl" : f"{ROOT}{link_nl}",
        "on_show" : on_show,
        "opening" : opening,
        "page_subtitle" : get_text(item.select_one("h2")),
        "page_text" : get_text(soup.select_one(".item > .text")),
        "page_title" : get_text(item.select_one("h1"))
    }

def parse_articles():
    articles = []

    for article in Path("data").glob("*.html"):
        with open(article) as f:
            article = parse_article(f.read())

            # Remove images that can't be converted to CSV
            article.pop("images", None)

            articles.append(article)

    # Convert to a CSV but remove the images because that is nested
    Knead(articles).write("exhibitions.csv")

def parse_link(link):
    img = link.select_one("img").get("src", None)

    if img:
        img = f"{ROOT}{img}"

    href = link.select_one("a").get("href", None)

    if href:
        href = f"{ROOT}{href}"

    return {
        "index_date" : get_text(link.select_one("time")),
        "href" : href,
        "index_img" : img,
        "index_text" : get_text(link.select_one("p")),
        "index_title" : get_text(link.select_one("h3"))
    }

def scrape_index(html):
    index = get_index(html)

    for item in index:
        link = item["href"]
        fetch_article(link)

def write_csv(items):
    # Flatten our data
    lang = "en"

    for item in items:
        data = item[lang]

        # Flatten images
        if "page_images" in data and len(data["page_images"]):
            data["page_images"] = [ i.get("src") for i in data["page_images"] ]
            data["page_images"] = ",".join(data["page_images"])

        for key, value in data.items():
            item[f"{lang}_{key}"] = value

        item.pop(lang)

    Knead(items).write("exhibitions.csv")

if __name__ == "__main__":
    exhibitions = get_data()
    Knead(exhibitions).write("exhibitions.json", indent = 4)
    write_csv(exhibitions)