import numpy as np
from txtai.embeddings import Embeddings
import pandas as pd
import requests

embeddings = Embeddings({"method": "transformers", "path": "sentence-transformers/bert-base-nli-mean-tokens"})

c= pd.read_csv('f1.csv')
print(c.head())

# today = c.loc[c['date'] == '2020-09-01']
# today_list=today['title'].tolist()
# today_arr=today['title'].to_numpy()


# def sim (query):
#     x=embeddings.similarity(query, today_list)
#     uid = np.argsort(x)
#     # print(uid)
#     largest_indices = uid[::-1][:5]
#     for i in largest_indices:
#         print(today_list[i])

# sim('jobs, workers and employment')