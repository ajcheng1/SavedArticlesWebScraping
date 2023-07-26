import pandas as pd
from bs4 import BeautifulSoup
from datetime import date

'''To tranfer bookmarks to excel. Ensure the bookmarks are saved as an html file. Search "PycharmProjects" for folder'''

def extract_bookmarks(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    bookmarks = []
    for link in soup.find_all('a'):
        url = link.get('href', '')
        title = link.string.strip() if link.string else ''
        if url and title:
            bookmarks.append((title, url))

    return bookmarks

def save_to_excel(bookmarks_data, output_file):
    df = pd.DataFrame(bookmarks_data, columns=['Title', 'URL'])
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    bookmarks_file = "C:\\Users\\Shado\\Downloads\\bookmarks_7_24_23.html"  # Replace with the actual path of your exported HTML bookmarks file
    output_excel_file = "Saved_Articles_Linked " + str(date.today()) +".xlsx"  # Replace with the desired output Excel file name

    bookmarks_data = extract_bookmarks(bookmarks_file)
    save_to_excel(bookmarks_data, output_excel_file)
    print("Excel File Saved")
