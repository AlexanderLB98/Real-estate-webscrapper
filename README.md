# Real-estate-webscrapper

This project is a web scraper designed to extract property listing data for sale in the city of Barcelona from the [Idealista](https://www.idealista.com) website. It utilizes [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [undetected_chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) to efficiently handle scraping while simulating browser behavior. The dataset can be accesed in [Zenodo.org](https://zenodo.org/records/14109828).

## Files

- `main.py`: Main script that performs web scraping and saves results to a CSV file.
- `web_scrapper.ipynb`: Jupyter Notebook version of the script, useful for step-by-step testing and analysis.

## Features

- **Extracted Data**: Captures essential information for each property listing, including:
  - Property ID
  - Title
  - Link to item
  - Price
  - Additional details (size, location, etc.)
  - Short description
- **Automatic CSV Export**: Data is appended to a CSV file after each listing is processed.
- **Pagination Handling**: The script navigates through multiple pages of listings automatically.

## Installation

- Python 3.x
- Required packages (install via `pip`):

### Option 1: Create a new env with Conda or Venv

Create a new Conda env

```bash
conda env create -n webscrapper python
```

Then install the following required libraries

```bash
pip install pandas beautifulsoup4 undetected-chromedriver
```

### Option 2: import conda env from file
Alternatively, you can create a virtual environment using the environment file (environment.yml) provided. This will ensure that all necessary packages are installed with the exact versions used in this project.

Create the environment:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate webscrapper
```


## Usage

Run main.py:
```python
python main.py
```

Alternatively, you can run the ```web_scrapper.ipynb``` notebook.

## Notes

- Make sure to use this scraper responsibly, as excessive scraping may violate website terms of service.
- The script includes random delays to avoid overloading the server, although this may not be enough.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

