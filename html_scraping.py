from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

raw_html = simple_get('http://shakespeare.mit.edu/lll/full.html')

html = BeautifulSoup(raw_html, 'html.parser')
for body in html.select('body'):
    word_list = body.text.strip()
    word_list = word_list.replace(';',' ').replace(',',' ').replace(']',' ').replace(':',' ').replace('.',' ').replace('!',' ').replace('?',' ').replace('[',' ').split()
