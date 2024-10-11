import re
import argparse
from bs4 import BeautifulSoup

class DEF14AParser:
    def __init__(self, file_path):
        self.soup = self.load_html(file_path)

    def load_html(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return BeautifulSoup(file, 'html.parser')

    def get_compensation_discussion_and_analysis(self):
        start_heading = self.soup.find(lambda tag: tag.name in ['h1', 'h2', 'h3', 'h4', 'h5'] and
                                       'compensation discussion and analysis' in tag.get_text().strip().lower())
        end_heading = self.soup.find(lambda tag: tag.name in ['h1', 'h2', 'h3', 'h4', 'h5'] and
                                     'people and compensation committee report' in tag.get_text().strip().lower())

        if not start_heading or not end_heading:
            return "Section not found."

        content = []
        current = start_heading.find_next()

        while current and current != end_heading:
            text = current.get_text(separator=' ', strip=True)
            if text:
                content.append(text)
            current = current.find_next()

        section_text = '\n\n'.join(content).strip()
        return section_text if section_text else "Section not found."

def main():
    parser = argparse.ArgumentParser(description="Extract 'Compensation Discussion and Analysis' section from DEF14A HTML file")
    parser.add_argument('file_path', help="Path to the DEF14A HTML file")
    args = parser.parse_args()
    parser = DEF14AParser(args.file_path)
    result = parser.get_compensation_discussion_and_analysis()
    print(result)

if __name__ == "__main__":
    main()
