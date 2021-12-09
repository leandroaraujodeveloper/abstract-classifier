# Article Research Abstract classifier
This project is a proof of concept of an automated tool to classify scientific research by field and autotagging. I've used a machine learning model to classify articles crawled on arxiv.org repository.
## Web Crawler
 The crawler has developed with scrapy framework a powerful web scraping tool that permit mount the dataset to do the predictions needed on this project. The folder of the source code is `arxiv_crawler` and the fields scraped on the site are of computational inteligence area this fields can be founded on file `keywords_crawler.py`, the file is the starter of the crawler and can be executed by the command `python keywords_crawler.py`(after install the dependences on your enviroment).

## Model classifier
 The model choosed to the task of classification was a RandomForestClassifier that is a decision tree based model with improved accuracy and overfit control. The details of the implementation can be founded on the file `tagging-training.ipynb`.

## Running the project
Install the dependences with the folowing command.
```
pip install requirements.txt
```
To running the notebook you install [Jupyter Notebook](https://jupyter.org/install.html)
