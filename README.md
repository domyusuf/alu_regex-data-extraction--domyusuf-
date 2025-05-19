Regex Data Extraction

This project extracts structured data (like emails, URLs, phone numbers, credit card numbers, and HTML tags) from a raw text string using Python's `re` module.



FILE STRUCTURE

`main.py`

  - Defines regex functions
  - Parses a sample string
  - Prints matched results


It Extracts:

 - Email addresses
 - URLs (http/https and www)
 - Phone numbers (multiple formats)
 - Credit card numbers
 - HTML tags


HOW TO RUN

1. Make sure you have Python 3 installed:

```bash python3 --version```

2. Run the script:

```bash python3 main.py```


SAMPLE OUTPUT

- Email Address(es)
['support@example.com', 'billing-team123@my-company.org']

- URL(s)
['https://www.example.com', 'http://sub.domain.net/path/page', 'www.test-site.io/home']


REQUIREMENTS

Python
No external libraries required (uses only `re`)