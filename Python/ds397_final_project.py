# -*- coding: utf-8 -*-
"""DS397_Final_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1knuYAwoz-EIhcxMDrRaG60Vu36TDmun4

# **DS 397 Final Project**

**Application Domain: Recommender Systems**

For my project, the application domain that I will be looking at is the recommender system domain.

**Problem**

The problem I will be addressing is whether or not there exists a bias of some sort in recommender system algorithms.

**Problem Formulation**

To solve the aforementioned problem, I have decided to use content-based recommender system to judge if there is a bias or not.

**Algorithm**

Below is the algorithm for a content-based recommender system that uses data from a dataset of popular movies.

First, we need to mount the drive with the dataset in order to begin.
"""

from google.colab import drive
drive.mount('/content/drive')

"""The drive is now mounted, and now we need to import several libraries needed for our recommender system."""

import pandas as pd
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

"""The necessary libraries and tools have been imported


"""

mdata = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/movies_metadata.csv', low_memory=False)
tfidf = TfidfVectorizer(stop_words='english')
mdata['overview'] = mdata['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(mdata['overview'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(mdata.index, index=mdata['title']).drop_duplicates()

"""Using pandas, the movie data (from https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) csv file is read and prepared for creation of the recommender system. Variables for TFIDF and cosine similarity scores are also created.

Note: Due to Google Colab's limited RAM, the cosine_sim variable cannot be created to create the necessary cosine similarity values for the next part.
"""

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return mdata['title'].iloc[movie_indices]

"""The function to get recommendations has been created and will be used to return a list of recommended movies."""

get_recommendations('Braveheart')

"""Due to the problem in a previous step, the output cannot be retrieved. Running this line of code will output a list of movies that are similar to the movie "Braveheart".

**Conclusion**

There is no bias in a recommender system as the algorithm mainly uses mathematical functions to produce an output.

**Alternatives**

Other alternatives include other types of recommender systems. One common alternative to a content-based system is a collaborative system. Collaborative systems can provide better individualized results due to their nature. However, they require more data than a content-based system to generate the results.
"""