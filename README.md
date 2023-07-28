# eBay Products Scrapy Spider

## Introduction
This is a web scraping project aimed at extracting product details from eBay's deals section using the Scrapy framework. The scraper navigates through the deals categories and extracts details such as product name, price, image URLs, and product URL. The scraped data is stored in a PostgreSQL database and can be accessed through a REST API endpoint.

## Installation & Setup

### Requirements

- Python 3.11 or higher
- PostgreSQL (refer to the official [PostgreSQL docs](https://www.postgresql.org/docs/current/tutorial-install.html) for installation instructions)

### Steps

1. Clone the repository:
    ```
    git clone git@github.com:dabideee13/ebay_spider.git
    cd ebay_spider
    ```

2. Copy the sample environment variable file and fill in the details:
    ```
    cp .env.sample .env
    ```

3. Create a virtual environment, activate it, and install dependencies:
    ```
    poetry install
    source ./.venv/bin/activate
    ```

5. Setup PostgreSQL database:
    - Create a new database in PostgreSQL named `ebay`.
    - Update the `.env` file with your database details (`DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`).

6. Run the database migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

## Usage

To start the spider, navigate to the project root and run the following command:
```
python manage.py crawl
```
This will start the eBay spider. The scraped data will be stored in the PostgreSQL database specified in your `.env` file. The scraped data can be accessed through the `/api/products` REST API endpoint. This endpoint supports pagination, use the `page` query parameter to navigate through the pages (e.g., `/api/products?page=2`).

## Project Structure

- `product_spider/scrapy_spiders/scrapy_spiders/items.py`: This file contains the `ProductItem` class which Scrapy uses for data storage.

- `product_spider/scrapy_spiders/scrapy_spiders/spiders/ebay.py`: This file contains the main spider. The spider navigates through the categories and extracts the required product information.

- `product_spider/scrapy_spiders/scrapy_spiders/middlewares.py`: This file contains the middleware for the project, which includes user agent rotation and proxy rotation to avoid IP bans.

- `product_spider/scrapy_spiders/scrapy_spiders/settings.py`: This file contains all settings for the Scrapy spider, such as user-agent and proxy configurations, as well as other Scrapy-specific settings.

- `proxy_list.txt`: A list of proxies in CSV format that the spider uses to avoid IP bans.

- `.env`: This file should contain your environment variables. It's based on the `.env.sample` file in the repository, but should be updated with your actual values for `ENV`, `SECRET_KEY`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.

## Proxies

Proxies are used in this project to avoid IP bans from the server. The proxy list is stored in the `proxy_list.txt` file at the root of the project directory. This file is in CSV format and each line should contain a proxy in the following format:
```
ip,anonymityLevel,asn,country,isp,latency,org,port,protocols,responseTime,speed,updated_at,upTime,upTimeSuccessCount,upTimeTryCount
```
Note that only the `ip`, `port`, and `protocols` fields are used by the spider.

## User-Agents

The project uses random User-Agents for each request to avoid detection. The user agents are managed by the `scrapy-user-agents` middleware which is installed as part of the requirements.

## Database

This project uses a PostgreSQL database to store the scraped product data. You need to provide your database details in the `.env` file. Please ensure to run database migrations using Django's `makemigrations` and `migrate` commands before starting the scraper.

## Logging

Logging in this project is set to the `INFO` level and it is configured in `settings.py`. Logs are printed to the console and are also saved to a log file located in the `logs` directory. A new log file is created for each run of the spider.

## API Documentation

This project includes an auto-generated API documentation which can be accessed by navigating to `/api/schema/docs` in your web browser when the server is running. The documentation provides a comprehensive guide on how to interact with the REST API, including the available endpoints, request methods, request parameters, and response formats.

You can start the server by running the following command:
```
python manage.py runserver
```
Once the server is running, open your web browser and navigate to `http://localhost:8000/api/schema/docs` to access the API documentation. Please ensure that the server is running on port 8000, otherwise, replace `8000` in the URL with the port number your server is running on.

## Sample Data
The scraped data has also been exported from the PostgreSQL database to a Google Sheets document for easy viewing and sharing. The document can be accessed from the following link: https://docs.google.com/spreadsheets/d/1MKGJ7aYGck800pRC4koHSYHRbaYFzXq7wZCr0Ln6mJk/edit?usp=sharing