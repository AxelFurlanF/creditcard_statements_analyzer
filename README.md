# Credit Card Statements Analyzer

## How to run
Set `OPENAI_ORGANIZATION` environment variable with your OpenAI org.

Set `OPENAI_API_KEY` environment variable with yours.

Install `poetry` with `pip`.

Then `poetry install` to install everything.

Place your PDF credit card statements in the `statement_pdfs` folder.

Then `poetry run python main.py` to run the code. A bunch of csv files will be created in `results`. They may not be perfect so if you want, you can give it an eye and fix minor mistakes.

Run `poetry run jupyter lab` to run jupyter. Open the `quick_analysis.ipynb` and run it to see some charts printed with the stats.

