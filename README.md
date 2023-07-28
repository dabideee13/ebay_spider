# eBay Products Scrapy Spider

## Introduction

This is a web scraping project aimed at extracting product details from eBay's deals section using the Scrapy framework. The scraper navigates through the deals categories and extracts details such as product name, price, image URLs, and product URL.

## Installation & Setup

This project requires Python 3.8 or higher. Below are the steps to setup and run the project:

1. Clone the repository:
    ```
    git clone git@github.com:dabideee13/ebay_spider.git
    cd ebay_spider
    ```
2. Create a virtual environment, activate it, and install dependencies:
    ```
    poetry install
    source ./.venv/bin/activate
    ```

## Usage

To start the scraper, navigate to the project root and run the following command:
```
python manage.py crawl
```
This will start the spider named "ebay". The scraped data will be stored in the `items.json` file at the root of the project directory.

## Project Structure

- `product_spider/scrapy_spiders/scrapy_spiders/items.py`: This file contains the `ProductItem` class which Scrapy uses for data storage.

- `product_spider/scrapy_spiders/scrapy_spiders/spiders/ebay.py`: This file contains the main spider. The spider navigates through the categories and extracts the required product information.

- `product_spider/scrapy_spiders/scrapy_spiders/middlewares.py`: This file contains the middleware for the project, which includes user agent rotation and proxy rotation to avoid IP bans.

- `product_spider/scrapy_spiders/scrapy_spiders/settings.py`: This file contains all settings for the Scrapy spider, such as user-agent and proxy configurations, as well as other Scrapy-specific settings.

- `proxy_list.txt`: A list of proxies in CSV format that the spider uses to avoid IP bans.

## Proxies

Proxies are used in this project to avoid IP bans from the server. The proxy list is stored in the `proxy_list.txt` file at the root of the project directory. This file is in CSV format and each line should contain a proxy in the following format:
```
ip,anonymityLevel,asn,country,isp,latency,org,port,protocols,responseTime,speed,updated_at,upTime,upTimeSuccessCount,upTimeTryCount
```
Note that only the `ip`, `port`, and `protocols` fields are used by the spider.

## User-Agents

The project uses random User-Agents for each request to avoid detection. The user agents are managed by the `scrapy-user-agents` middleware which is installed as part of the requirements.

## Logging

The logging in this project is set to the `INFO` level and it is configured in `settings.py`. Logs are printed to the console.

