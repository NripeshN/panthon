import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {self.base_url}: {e}")
            return None

    def extract_assets(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for script in soup.find_all("script"):
            src = script.get('src')
            if src:
                full_url = urljoin(self.base_url, src)
                self.assets['scripts'].append(full_url)
        
        for link in soup.find_all("link", rel="stylesheet"):
            href = link.get('href')
            if href:
                full_url = urljoin(self.base_url, href)
                self.assets['stylesheets'].append(full_url)
        
        for img in soup.find_all("img"):
            src = img.get('src')
            if src:
                full_url = urljoin(self.base_url, src)
                self.assets['images'].append(full_url)

        return self.assets

    def download_asset(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.content  # returns bytes
        except requests.RequestException as e:
            print(f"Error downloading {url}: {e}")
            return None

    def fetch_website_assets(self):
        html = self.get_html()
        if html is not None:
            assets = self.extract_assets(html)
            asset_contents = {}
            for category in assets:
                for asset_url in assets[category]:
                    content = self.download_asset(asset_url)
                    asset_contents[asset_url] = content
            return asset_contents
        else:
            return {}

# Example usage:
if __name__ == "__main__":
    url = "https://www.wolframalpha.com"  # Change this URL to the website you want to extract
    extractor = WebsiteExtractor(url)
    assets_content = extractor.fetch_website_assets()
    for asset_url, content in assets_content.items():
        print(f"Content of {asset_url}: {content[:100]}..." if content else f"Failed to download {asset_url}")
