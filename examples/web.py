from panthon import WebsiteExtractor

url = "https://abibinator.blogspot.com/"  # Change this URL to the website you want to extract
extractor = WebsiteExtractor(url)
assets_content = extractor.get_html()
print (assets_content)
#for asset_url, content in assets_content.items():
 #   print(f"Content of {asset_url}: {content}..." if content else f"Failed to download {asset_url}")
  #  break
