This python script automates docx to pdf conversion using pylatex library.
It was developed during my workstudy at the Office of Career Development at Columbia Journalism School.

By iterating through .docx files in the specified directory, the script redacts personal information while appending necessary information like name of the recruiter and company.
Upon reaching the end of each file, the script generates a latex pdf file in the specified directory.

## To run
1. Rename each word document to "#.docx" where # is the count.
2. Run `python main.py {source directory} {destination directory} {number of files}` in terminal.
Test example: `python main.py ./new-companies/ ./new-companies/ 2`
