# from bs4 import BeautifulSoup
# import json
# import pandas as pd
# import logging

# logging.basicConfig(level=logging.INFO)

# class DataProcessor:
#     def __init__(self, html_content):
#         self.soup = BeautifulSoup(html_content, "html.parser")

#     def extract_faqs(self):
#         """Extract FAQs from the HTML content"""
#         faqs = []

#         # Identify FAQ sections
#         for faq_section in self.soup.find_all("article", class_="tease_faq"):  
#             question_tag = faq_section.find("h3", class_="tease_h")
#             answer_tag = faq_section.find("div", class_="tease_text")

#             question = question_tag.find("a", class_="tease_link").text.strip() if question_tag else "No Question Found"
#             answer = answer_tag.text.strip() if answer_tag else "No Answer Found"

#             faqs.append({"question": question, "answer": answer})

#         # Debugging output
#         print("\n===== Extracted FAQs =====\n")
#         for faq in faqs:
#             print(f"Q: {faq['question']}")
#             print(f"A: {faq['answer']}\n")
#         print("\n==========================\n")

#         return faqs

#     def save_to_json(self, data, filename="data/output.json"):
#         with open(filename, "w") as file:
#             json.dump(data, file, indent=4)
#         logging.info(f"Data saved to {filename}")

#     def save_to_csv(self, data, filename="data/output.csv"):
#         df = pd.DataFrame(data)
#         df.to_csv(filename, index=False)
#         logging.info(f"Data saved to {filename}")


from bs4 import BeautifulSoup
import json
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

class DataProcessor:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, "html.parser")

    def extract_faqs(self):
        """Extract FAQs from the HTML content"""
        faqs = []

        # Debugging: Print a large part of the parsed HTML
        print("\n===== Parsed HTML (First 5000 chars) =====\n")
        print(self.soup.prettify()[:5000])  # Print first 5000 characters
        print("\n==========================================\n")

        # Identify FAQ sections
        for faq_section in self.soup.find_all("article", class_="tease_faq"):
            question_tag = faq_section.find("a", class_="tease_link")
            answer_tag = faq_section.find("div", class_="tease_text")

            question = question_tag.text.strip() if question_tag else "No Question Found"
            answer = answer_tag.text.strip() if answer_tag else "No Answer Found"

            faqs.append({"question": question, "answer": answer})

        # Debugging: Print extracted FAQs
        print("\n===== Extracted FAQs =====\n")
        for faq in faqs:
            print(f"Q: {faq['question']}")
            print(f"A: {faq['answer']}\n")
        print("\n==========================\n")

        return faqs
    
    def save_to_json(self, data, filename="data/output.json"):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        logging.info(f"Data saved to {filename}")

    def save_to_csv(self, data, filename="data/output.csv"):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        logging.info(f"Data saved to {filename}")