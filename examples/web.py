from panthon import WebsiteExtractor

url = "https://abibinator.blogspot.com/"  # Change this URL to the website you want to extract
extractor = WebsiteExtractor(url)
assets_content = extractor.get_html()
print(assets_content)
