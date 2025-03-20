import requests

def visit_web_page(url: str):
    '''
    This tool can be used to visit page on web by the url. It returns text of the page.
    
    Args:
        url: url to the website.
    '''
    try:
        page = requests.get(url)
        page.raise_for_status()
        return page.text
    except requests.exceptions.RequestException as e:
        return f"error, cannot access URL: {url}, exception {e}"
    
if __name__ == '__main__':
    res = visit_web_page('https://www.restack.io/p/autogpt-answer-duckduckgo-rate-limit-cat-ai')
    print(res)

    