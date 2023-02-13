import re
import requests
from urllib.parse import urlparse, urljoin


# requesting url
def request (url):
    try:
            get_response = requests.get("https://" + url)
            return get_response

    except requests.exceptions.ConnectionError:
       pass
    except requests.exceptions.InvalidURL:
        print("Invalid url")
    except requests.exceptions:
        pass


# subdomain test :

# required format for this tool :
#print("Enter domain name and top-level domain only :\n ->  example.com")
def subdomain_test (url, path = "", short=False , long=False) :

    if short:
        path = "sub.txt"
    if long:
        path = "subdomains.txt"

    found = False
    with open(path, 'r') as file:
        for line in file:
            word = line.strip()
            test_url = word + '.' + url
            response = request(test_url)
            if response:
                found = True
                print("[*] : Subdomain {} exist  ".format(test_url))
    if (not found):
        print("no subdomains found in the wordlist ")

#subdomain_test(target_url)

# Directory Crawler:

def crawl(url):
    href_link = extract_link("http://" + url)
    print("Found links in {} : \n".format(url))
    for link in href_link:
        link = urljoin(url, link)
        print("[*] : "+link)

# to find all links in php page
def extract_link (url):
    response = requests.get(url)
    # to parse the content of the response and take only the urls
    return re.findall('(?:href=")(.*?)"',response.content.decode('utf-8'))

