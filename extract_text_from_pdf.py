import os
from PyPDF2 import PdfReader
from chat_gpt_api import ask_gpt_for_spendings, organize_pdf_text

FOLDER = "statement_pdfs/"
IGNORE_LAST_PAGES = 7

files = os.listdir(FOLDER)
pdf_files = [file for file in files if file.endswith(".pdf")]


for i, file in enumerate(pdf_files):
    final_csv = ""
    print(f"Reading file: {file}")
    # creating a pdf reader object
    reader = PdfReader(FOLDER + file)

    # printing number of pages in pdf file
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

        # final_csv += organize_pdf_text(final_csv)

    # write csv_text to csv
    with open(f"results/{file}_statement.csv", "w") as f:
        f.write("category,amount\n")
        f.write(final_csv)
