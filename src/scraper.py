thonimport requests
from bs4 import BeautifulSoup
import json

class LinkedInCommentScraper:
    def __init__(self, post_url):
        self.post_url = post_url

    def fetch_page(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        response = requests.get(self.post_url, headers=headers)
        if response.status_code != 200:
            raise Exception("Failed to fetch page")
        return response.text

    def parse_comments(self, page_html):
        soup = BeautifulSoup(page_html, 'html.parser')
        comments = []
        comment_elements = soup.find_all('div', class_='comments__comment')
        for comment_element in comment_elements:
            comment = {}
            comment['text'] = comment_element.find('span', class_='comment__text').get_text(strip=True)
            comment['author_name'] = comment_element.find('span', class_='comment__author').get_text(strip=True)
            comment['author_profile_url'] = comment_element.find('a', class_='comment__author-link')['href']
            comment['likes'] = int(comment_element.find('span', class_='comment__likes').get_text(strip=True))
            comment['replies'] = int(comment_element.find('span', class_='comment__replies').get_text(strip=True))
            comment['time'] = comment_element.find('time')['datetime']
            comments.append(comment)
        return comments

    def scrape(self):
        page_html = self.fetch_page()
        comments = self.parse_comments(page_html)
        return comments

def save_comments_to_json(comments, output_file):
    with open(output_file, 'w') as f:
        json.dump(comments, f, indent=4)

if __name__ == "__main__":
    url = "https://www.linkedin.com/feed/update/urn:li:activity:7019294467031543808"
    scraper = LinkedInCommentScraper(url)
    comments = scraper.scrape()
    save_comments_to_json(comments, 'comments.json')