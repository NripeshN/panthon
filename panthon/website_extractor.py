import requests
from bs4 import BeautifulSoup, Tag
from urllib.parse import urljoin
from lxml import html, etree

class WebsiteExtractor:
    def __init__(self, url):
        self.base_url = url
        self.assets = {
            'scripts': [],
            'stylesheets': [],
            'images': [],
            'others': []
        }

    def get_html(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {self.base_url}: {e}")
            return None

    def extract_assets(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for script in soup.find_all("script"):
            src = script.get('src')
            if src:
                self.assets['scripts'].append(urljoin(self.base_url, src))
        
        for link in soup.find_all("link", rel="stylesheet"):
            href = link.get('href')
            if href:
                self.assets['stylesheets'].append(urljoin(self.base_url, href))
        
        for img in soup.find_all("img"):
            src = img.get('src')
            if src:
                self.assets['images'].append(urljoin(self.base_url, src))

        return self.assets

    def download_asset(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            print(f"Error downloading {url}: {e}")
            return None

    def fetch_website_assets(self):
        html = self.get_html()
        if html:
            assets = self.extract_assets(html)
            asset_contents = {}
            for category in assets:
                for asset_url in assets[category]:
                    content = self.download_asset(asset_url)
                    asset_contents[asset_url] = content
            return asset_contents
        else:
            return {}

    def get_input_xpaths(self):
        html_content = self.get_html()
        if html_content:
            tree = html.fromstring(html_content)
            # Convert the HtmlElement to an ElementTree object
            etree_obj = etree.ElementTree(tree)
            input_elements = tree.xpath('//input | //textarea | //select')
            xpaths = [etree_obj.getpath(element) for element in input_elements]
            return xpaths
        else:
            return []

# Example usage:
if __name__ == "__main__":
    url = "https://abibinator.blogspot.com"
    extractor = WebsiteExtractor(url)
    input_xpaths = extractor.get_input_xpaths()
    print("XPaths of input elements:", input_xpaths)
