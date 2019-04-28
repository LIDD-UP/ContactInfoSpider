import pandas as pd
from TruthFinderSpider.settings import URLS_FILE

TRUTH_SEARCH_URLS = list(pd.read_csv(URLS_FILE).values)
for index, info in enumerate(TRUTH_SEARCH_URLS):
    if index == len(TRUTH_SEARCH_URLS) - 1:
        print("last url",info[0])
    print(info[0])