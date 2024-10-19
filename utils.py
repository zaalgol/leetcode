import os
import requests
import wget
import bz2
import mwparserfromhell
from tqdm import tqdm
from datasets import load_dataset
# # Define the URL of the latest Wikipedia dump
# url = 'https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2'

# # Define the output path for the downloaded file
# output_path = 'enwiki-latest-pages-articles.xml.bz2'

# # Download the file using requests
# if not os.path.exists(output_path):
#     print(f"Downloading {url} to {output_path}...")
#     response = requests.get(url, stream=True)
#     if response.status_code == 200:
#         with open(output_path, 'wb') as f:
#             for chunk in response.iter_content(chunk_size=1024):
#                 if chunk:
#                     f.write(chunk)
#         print("\nDownload complete.")
#     else:
#         print(f"Failed to download file. Status code: {response.status_code}")
# else:
#     print(f"{output_path} already exists. Skipping download.")
def extract_text_from_wiki_dump(dump_path, output_path):
    with bz2.open(dump_path, 'r') as file, open(output_path, 'w', encoding='utf-8') as out_file:
        for line in tqdm(file):
            try:
                line = line.decode('utf-8')
                if '<text' in line:
                    text_start = line.find('>', line.find('<text')) + 1
                    text_end = line.find('</text')
                    text = line[text_start:text_end]
                    wikicode = mwparserfromhell.parse(text)
                    plain_text = wikicode.strip_code()
                    out_file.write(plain_text + '\n')
            except Exception as e:
                print(f"Error processing line: {e}")
                continue

output_path = 'wikipedia_text.txt'
extract_text_from_wiki_dump('enwiki-latest-pages-articles.xml.bz2', output_path)
