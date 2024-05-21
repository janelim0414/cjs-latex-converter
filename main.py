# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import textract
import pylatex
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat
from pylatex.utils import italic, bold
import os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    N = 10  # set number of documents to convert
    EMAIL = "Email*"
    PHONE = "Phone Number*"
    COMPANY = "Please enter your organization name*"
    BILLING = "Billing Information"
    SKIP = False
    ASSIGN = False
    for i in range(1, N):
        filename = '/Users/jane/new companies/' + str(i) + '.docx'
        text = textract.process(filename)
        text = text.decode("utf-8")
        text = text.split('\n')
        # with open(text, 'rb') as f:
        doc = Document(documentclass='article', indent=False)
        for x in text:
            if x == EMAIL or x == PHONE:
                SKIP = True
                continue
            if x == COMPANY:
                doc.append(str(x) + '\n')
                ASSIGN = True
                SKIP = False
                continue
            if SKIP and x:
                SKIP = False
                continue
            if x == BILLING:
                doc.generate_pdf('/Users/jane/new companies/' + company, clean_tex=True)
            if ASSIGN and x:
                ASSIGN = False
                doc.append(str(x) + '\n')
                company = x
                print(company)
                continue
            else:
                doc.append(str(x) + '\n')

    #
    # section = Section('hello')
    # subsection = Subsection('my name is Jane')
    # section.append(subsection)
    # doc.append(section)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
