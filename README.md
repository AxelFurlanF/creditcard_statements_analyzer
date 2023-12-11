# Credit Card Statements Analyzer

## What's this?
I've spent quite a lot of money recently and I wanted to find out what did I spend it on. My bank doesn't give me my credit card statements in an analyzable format like csv or txt to run some data analysis on it, so I decided to just load the PDF files and analyze them with ChatGPT.

This code grabs your pdf statements, parses them with ChatGPT and writes csvs with just 2 columns, category and amount. My goal was to perform very simple analysis on the categories.

## How to run
Set `OPENAI_ORGANIZATION` environment variable with your OpenAI org.

Set `OPENAI_API_KEY` environment variable with yours.

Install `poetry` with `pip`.

Then `poetry install` to install everything.

Place your PDF credit card statements in the `statement_pdfs` folder.

Then `poetry run python main.py` to run the code. A bunch of csv files will be created in `results`. They may not be perfect so if you want, you can give it an eye and fix minor mistakes.

Run `poetry run jupyter lab` to run jupyter. Open the `quick_analysis.ipynb` and run it to see some charts printed with the stats.

