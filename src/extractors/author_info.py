thonimport re

def extract_author_name(author_html):
    return author_html.get_text(strip=True)

def extract_author_profile_url(profile_url_html):
    return profile_url_html['href']