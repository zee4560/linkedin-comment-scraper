thonimport re

def parse_comment_text(comment_html):
    return comment_html.get_text(strip=True)

def parse_comment_author(author_html):
    return author_html.get_text(strip=True)

def parse_comment_likes(likes_html):
    return int(likes_html.get_text(strip=True))

def parse_comment_replies(replies_html):
    return int(replies_html.get_text(strip=True))

def parse_comment_time(time_html):
    return time_html['datetime']