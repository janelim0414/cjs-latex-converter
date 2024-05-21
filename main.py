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
import sys

def converter(src, dst, n):
    EMAIL = "Email*"
    PHONE = "Phone Number*"
    COMPANY = "Please enter your organization name*"
    BILLING = "Billing Information"
    SKIP = False
    ASSIGN = False
    for i in range(1, n + 1):
        filename = src + str(i) + '.docx'
        text = textract.process(filename)
        text = text.decode("utf-8")
        text = text.split('\n')
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
                doc.generate_pdf(dst + company, clean_tex=True)
            if ASSIGN and x:
                ASSIGN = False
                doc.append(str(x) + '\n')
                company = x
                print(company)
                continue
            else:
                doc.append(str(x) + '\n')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    src = sys.argv[1]  # directory where word documents are stored
    dst = sys.argv[2]  # directory where pdf documents will be stored
    n = int(sys.argv[3])  # number of files to be converted
    converter(src, dst, n)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
