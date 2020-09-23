import os

import fire

import requests
from bs4 import BeautifulSoup

from src.extract import ignoreTag, process_dump


def get_wikidump_file(wikidump_link):
    # get wikidump html as text
    wikidump_html = requests.get(wikidump_link).text
    # parse the html with BeautifulSoup
    soup_dump = BeautifulSoup(wikidump_html, 'html.parser')
    # Search through all files
    for link in soup_dump.findAll('a'):
        link_str = link.get('href')
        if "pages-articles-multistream.xml.bz2" in link_str:
            return link_str


def download_file(url, dest_folder):
    file_path = os.path.join(dest_folder, url.split('/')[-1])

    r = requests.get(url, stream=True)
    if r.ok:
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
        return file_path
    return None


def main(wikidump_language, wikidump_folder="./wikidump",
         keep_links=False, processes=1,
         ignored_tags="abbr,b,big,blockquote,center,cite,em,font,h1,h2,h3,h4,hiero,i,kbd,p,plaintext,s,span,strike,strong,tt,u,var"):
    # create folder, if exist no error
    os.makedirs(wikidump_folder, exist_ok=True)

    # Download Wikipedia dump
    wikidump_link = "https://dumps.wikimedia.org/{}wiki/latest/".format(wikidump_language)
    wikidump_file = get_wikidump_file(wikidump_link)
    file_url = os.path.join(wikidump_link, wikidump_file)
    wikidump_file_path = os.path.join(wikidump_folder, wikidump_file)
    if not os.path.isfile(wikidump_file_path):
        print("Downloading {}".format(file_url))
        downloaded = download_file(file_url, wikidump_folder)
        if not downloaded:
            print("Failed to download {}".format(file_url))
            return 0

    # parse options
    ignoredTags = set(ignored_tags.split(','))
    for tag in ignoredTags:
        ignoreTag(tag)
    if not keep_links:
        ignoreTag('a')
    print("Start parsing {}".format(wikidump_file_path))
    process_dump(wikidump_file_path, False, wikidump_folder, 1000 * 1024,
                 False, processes)


if __name__ == '__main__':
    fire.Fire(main)
