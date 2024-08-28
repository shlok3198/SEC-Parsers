import re
import argparse
from bs4 import BeautifulSoup

class DEF14AParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.soup = self._load_html()

    def _load_html(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return BeautifulSoup(file, 'html.parser')

    def get_compensation_discussion_and_analysis(self):
        section_heading = self.soup.find(lambda tag: tag.name in ['h1', 'h2', 'h3', 'h4', 'h5'] and
                                                      'compensation discussion and analysis' in tag.get_text().strip().lower())
        if not section_heading:
            return "Section not found."

        content = []
        for sibling in section_heading.find_next_siblings():
            if sibling.name in ['h1', 'h2', 'h3', 'h4', 'h5'] and re.search(r'item\s+\d+|signatures', sibling.get_text().strip(), re.IGNORECASE):
                break
            content.append(sibling.get_text().strip())

        section_text = '\n'.join(content).strip()

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
