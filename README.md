# NYTimes-Web-Scraper
An easier way to search New York Times articles by keyword formatted in an excel format

Heavily inspired by this: https://medium.com/codex/web-scraping-the-new-york-times-articles-with-python-part-i-e2d6fc02d4e0

Sign up for an API key from this link: https://developer.nytimes.com/. You do not need a NYT subscription to get a key, but much recommended to read the actual articles! 

See this for more usage and modifying code https://developer.nytimes.com/docs/articlesearch-product/1/overview. 

Example of output. Output is saved into an excel file as well
![image](https://github.com/ajcheng1/SavedArticlesWebScraping/assets/85465417/a682debc-35f1-44d8-8710-18ae53827423)

To save multiple open tabs into an excel sheet, (1) right click next to the rightmost tab on chrome, (2) bookmark all tabs, (3) saved the bookmark as an html file -- convert to an html file if it is in a different format, (4) copy file path to bookmarks_file into linkScraper.py, (5) python program will save the file's name and URL

Example of excel file: 

![image](https://github.com/ajcheng1/SavedArticlesWebScraping/assets/85465417/922be75e-b585-47e0-91f1-98d9b55e62c0)
