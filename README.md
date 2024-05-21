This python script automates docx to pdf conversion using pylatex library.
It was developed during my workstudy at the Office of Career Development at Columbia Journalism School.

By iterating through .docx files in the specified directory, the script redacts personal information while appending necessary information like name of the recruiter and company.
Upon reaching the end of each file, the script generates a latex pdf file in the specified directory.

## To run
1. Update variable `N` to reflect the number of documents to convert.
2. Rename each word document to "#.docx" where # is the count.
3. Update variable `filename` to the directory path in which the documents can be found.
4. Update line `doc.generate_pdf('/Users/jane/new companies/' + company, clean_tex=True)` to an appropriate path where the converted pdf files will be stored.
