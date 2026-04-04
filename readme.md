# Real Estate Lead Scoring Automation

Automated system designed to detect real estate investment opportunities by analyzing price fluctuations across property listings.

## Overview

Identifying strong real estate opportunities is inefficient. The market contains a large volume of listings, but there is no clear way to quickly determine which properties are undervalued or worth analyzing.

This system processes property data and highlights opportunities based on measurable price drops. It reduces manual effort and provides a structured way to evaluate listings.

## Problem

Real estate data is abundant but lacks clarity. The main difficulties are:
- Identifying properties that have actually dropped in price
- Detecting negotiation potential
- Filtering valuable opportunities from noise

## Solution

This project builds a data pipeline that analyzes property information and identifies opportunities based on price evolution.

The system:
- Ingests property data from a dataset
- Cleans and structures the data
- Builds price history
- Calculates price variations
- Ranks the best opportunities

## Architecture

Pipeline:

datos.csv → lector.py → main.py → SQLite database → analisis.py

## Project Structure

- main.py: data ingestion, processing, and database population  
- analisis.py: opportunity detection and analysis  
- db.py: database structure and ID management  
- lector.py: data cleaning and filtering  
- logger.py: validation and filtering logic  
- scraper.py: data extraction module (in development)  
- datos.csv: source dataset  
- requirements.txt: project dependencies  

## Business Logic

Drop (%) = ((Initial Price - Current Price) / Initial Price) * 100

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the data pipeline:

```bash
python main.py
```

Run the analysis:

```bash
python analisis.py
```

## Example Output

```text
TOP OPPORTUNITIES

Apartment | Palermo
Current Price: 120000
Drop: 18.7%
```

## Value

- Reduces manual analysis of large datasets  
- Identifies undervalued properties efficiently  
- Applies structured decision logic  
- Demonstrates an end-to-end data system  

## Limitations

- Uses static CSV data  
- Historical data is simulated  
- No graphical interface  

## Next Steps

- Integrate real-time data sources (scraping or APIs)  
- Build a dashboard (Streamlit or Power BI)  
- Automate alerts via messaging systems  

## Example Case

Dataset: 500 properties analyzed  
Detected: 23 opportunities (>15% drop)  
Best case: Property undervalued by 18.7%

## Author

Julio Mariano Campuzano
