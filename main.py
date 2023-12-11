import os
from PyPDF2 import PdfReader
from chat_gpt_api import ask_gpt_for_spendings, organize_pdf_text

FOLDER = "statement_pdfs/"
RESULTS_FOLDER = "results/"
IGNORE_LAST_PAGES = 7


def main():
    files = os.listdir(FOLDER)
    pdf_files = [file for file in files if file.endswith(".pdf")]

    for i, file in enumerate(pdf_files):
        final_csv = ""
        print(f"Reading file: {file}")
        reader = PdfReader(FOLDER + file)

        print(f"File has {len(reader.pages)} pages.")

        pages = reader.pages[:-IGNORE_LAST_PAGES]
        for page in pages:
            text = page.extract_text()
            # remove whitespace
            text = " ".join(text.split())
            # remove new line
            text = text.replace("\n", " ")

            unorganized_spendings = ask_gpt_for_spendings(text)
            organized_spendings = organize_pdf_text(unorganized_spendings)

            final_csv += organized_spendings
            final_csv += "\n"

        with open(f"{RESULTS_FOLDER}/{file}_statement.csv", "w") as f:
            f.write("category,amount\n")
            f.write(final_csv)


if __name__ == "__main__":
    main()
