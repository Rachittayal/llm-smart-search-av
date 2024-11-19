# Analytics Vidhya Course Search Tool

## Project Overview
This project scrapes course data from Analytics Vidhya, builds embeddings for search, and deploys a search tool on Hugging Face Spaces using Gradio.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run `src/main.py` to scrape data and save to `data/scraped_courses.xlsx`.
3. Run `src/search_tool.py` to generate and save course embeddings.
4. Run `src/app.py` to start the Gradio app.

## Deployment
Deploy `app.py` on Hugging Face Spaces for public access.
