import re

# AI generated (Randomly)
text_string = """
Contact us at support@example.com or billing-team123@my-company.org for any questions.
Visit https://www.example.com or http://sub.domain.net/path/page for more info. You can also check www.test-site.io/home.
You can call us at (123) 456-7890, 123-456-7890, or even 123.456.7890 for help.
Use your credit card 1234 5678 9012 3456 or 9876-5432-1098-7654 to complete the transaction.
Here is some HTML code: <div class="content"><p>Hello World!</p><img src="image.jpg" alt="pic"></div>
"""


def find_emails(text: str):
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)


def find_urls(text: str):
    return re.findall(r"https?:\/\/[^\s<>\"]+|www.[^\s<>\"]+", text)


def find_phone_numbers(text: str):
    return re.findall(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)


def find_credit_card(text: str):
    return re.findall(r"\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}", text)


def find_html_tags(text: str):
    return re.findall(r"<[^>]+>", text)


def print_matches(items: list, title: str):
    print(f"\n{title}")
    print(items)


print_matches(find_emails(text_string), "Email Address(es)")
print_matches(find_urls(text_string), "URL(s)")
print_matches(find_phone_numbers(text_string), "Phone Number(s)")
print_matches(find_credit_card(text_string), "Credit Card(s)")
print_matches(find_html_tags(text_string), "HTML Tag(s)")