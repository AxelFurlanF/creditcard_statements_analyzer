from openai import OpenAI

client = OpenAI(
    organization='org-fHxX4JFL89k7SQ8SgCfGqTYD',
)


def organize_pdf_text(response_text):
    complete_text = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """I'm going to give you the csv output of some spendings I made.
            This output may have some errors, so I want you to fix them.
            Some spendings are overlapped in one line, please give me one line per spending.
            Remove spendings that have amount of $0.
            Whenever you see "products,clothing", convert it to "products/clothing".
            Whenever you see "products", convert it to "products/clothing".

            Please do not respond to this message.

            I'll give you the text on the next message. Respond to that message with the csv."""},
            {"role": "user", "content": response_text}
        ]
    )
    return complete_text.choices[0].message.content


def ask_gpt_for_spendings(text_pages):
    # user_messages = []
    # for pdf_text in text_pages:
    #     user_messages.append({"role": "user", "content": pdf_text})

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """I'm going to give a list of pdfs statements in text format.
            They're credit card statements in Spanish, and I want you to give me a comma separated list of 2 columns: the category of spending
            and the total amount. Similar to a csv response. In the statement, you'll find spending similar to:
            23 Febrero 09 004521 *  ZENRISE_CASAROLLER          C.10/12                        7.057,08
            means that I spent 7.057,08 euros in a product called "ZENRISE_CASAROLLER" and should be in the category of "products".
            C.10/12 means that I paid the 10th installment of 12 installments. 7.057,08 means that I spent $7057.08.
            There is a lot of extra text in those credit card statements, like addresses, names, etc. You can ignore that.
            Please also ignore all spendings which description is similar to "SU PAGO EN PESOS", that is NOT a spending but a payment.

            Here are a few rules:
            Whenever you see a spending similar to "MERPAGO*BOUNCE" it means that I spent money in a shop called "BOUNCE". Most likely, it
            is clothing unless the name is obvious like "BOUNCE RESTAURANT", in which case it is a restaurant.
            If it has famous brands like "ZARA", "ADIDAS", "NIKE", "PUMA", "LEVIS", etc, it's clothing.
            If the spending contains something like "C.10/12" it has installments.
            If the spending contains installments, it's probably a product or a service. When in doubt, use "products".
            If the name has "CAFE" in it, it is a coffee shop.
            Whenever you see "UBER", "CABIFY" or "DIDI" in the spending's name, it is a "transportation".
            Whenever you see "PEDIDOSYA", "PEDIDOS YA", "PROPINAS", "RAPPI" or something similar, it's a delivery.
            "METROGAS", "TELECENTRO", "TUENTI", "OBRA SOC L PASTE", "CABLEVISION", "AYSA", "EDENOR", "EDESUR", "METROGAS", "METROVISION" those
            are utilities.
            Website related spendings are usually clothing or services.
            Whenever you see "IMPUESTO", "AFIP", "ARBA", "RENTAS", "MONOTRIBUTO", "INGRESOS BRUTOS", "GANANCIAS", "IVA", "AUTONOMOS", "AUTONOMO" that
            is tax.
            Please categorize everything into these categories: "delivery", "food", "tax", "products/clothing", "services", "utilities", "transportation", "other".
            You can consider coffee shops as "food".
            If you're less than 50% sure about the category, please use "other".
            For clothing and products, please use one category called "products/clothing".
            Spendings lower than $10000 and without installments are probably food.

            Please ignore spendings in USD, they're not that much.
            Please make the amounts be without a dot, like 7057.08 instead of 7.057,08.

            I do not you need to respond to this message.
            I'll send you multiple messages with the statements.
            """},
            {"role": "user", "content": text_pages}
        ],
        temperature=0.0,
    )

    return completion.choices[0].message.content
