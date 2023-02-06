import requests
import base64
from urllib.parse import parse_qs
from urllib.parse import urlparse

from bs4 import BeautifulSoup

def b64decode(str):
    str = str.replace('_','/')
    str += "=" * ((4 - len(str) % 4) % 4)
    return base64.b64decode(str)

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
}

twitterDomains = (
    'https://twitter.com', 
)

def getToken(url):
    try:
        response = requests.post('https://twittermate.com/', headers=headers)
       
        cookies = response.cookies
        soup = BeautifulSoup(response.content, 'html.parser').find_all('input')
        data = {
            soup[0].get('name'):url,
        }
        
        return True, cookies, data
    
    except Exception:
        return None, None, None

def getVideo(url):
    if not url.startswith('http'):
        url = 'https://' + url

    if url.lower().startswith(twitterDomains):
        url = url.split('?')[0]
        
        status, cookies, data = getToken(url)
       
        if status:
            headers = {
                # 'Cookie': f"session_data={cookies['session_data']}",
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': '96',
                'Origin': 'https://twittermate.com/',
                'Referer': 'https://twittermate.com/en/',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Te': 'trailers'
            }

            try:
                response = requests.post('https://twittermate.com/download.php', data=data, headers=headers, allow_redirects=False)                      
                soup = BeautifulSoup(response.content, 'html.parser')                  
                link = soup.findAll('a',attrs={'class':'btn waves-effect waves-light light-blue darken-4'})[1]['href']
                return link

            except Exception as e:
                return {
                    'success': False,
                    'error': e
                }
        
        else:
            return {
                        'success': False,
                        'error': 'exception'
                    }

    else:
        return {
                    'success': False,
                    'error': 'invalidUrl'
                }
