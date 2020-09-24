# Wikidump
Wikidump is a fork from the repository [wikiextractor](https://github.com/attardi/wikiextractor), maintained by attardi. The current master branch of wikiextractor is not working, which is why I needed to make a fork from a old commit. I refactored the code a bit, added the automatical download of the wikidump files and changed the CLI. It is much more simpler to use

## Getting Started
Clone our repository and install the needed Python libraries. You may want to use a virtual enviroment:
```https://github.com/NewsPipe/wikidump.git
cd wikidump
pip install -r requirements.txt```

Afterward you can start the script by calling it. Show script usage:
```python3 wikidump.py --help```
Get german wikipedia articles:
```python3 wikidump.py de```
Get english wikipedia articles:
```python3 wikidump.py en```

The articles are stored as JSON format. 
