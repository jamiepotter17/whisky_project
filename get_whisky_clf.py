from all_whisk_clf import get_all_whisk_clf

import numpy as np
import pandas as pd
import joblib
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet, stopwords

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import FunctionTransformer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def drop_unpopular_brands(name, df, lower_limit=0):
    print("Dataframe {} had {} rows. After dropping rows with {} or fewer reviews, ".format(
        name, df.shape[0], lower_limit), end="")
    dfbrandcounts = df['brand'].value_counts()
    limited_list = dfbrandcounts[dfbrandcounts>lower_limit].index
    df = df[df['brand'].isin(limited_list)]
    print("it now has {} rows.".format(df.shape[0]))
    return df

def tokenise_and_stem_text(text):
    '''
    INPUTS:
    text (string) - what you want to be lemmatised
    OUTPUTS:
    lemmas (list) - list of lemmatised next
    '''
    # Import stopword list and update with a few of my own
    stopword_list = stopwords.words("english")
    [stopword_list.append(i) for i in ['nose', 'palate', 'taste', 'finish']]

    # Normalise text - remove numbers too as we don't need them
    text = re.sub(r"[^a-zA-Z]", " ", text.lower())

    # tokenise
    words = text.split()

    # Checks it's a word and removes stop words
    words = [word for word in words if word not in stopword_list]

    # Create stemmer object
    stemmer = PorterStemmer()

    # Add lemmas
    lemmas = []
    for word in words:
        lemmas.append(stemmer.stem(word))

    return lemmas

def getnose(array):
    return array[:,0]

def getpalate(array):
    return array[:,1]

def getfinish(array):
    return array[:,2]

print('Running get_all_whisk_clf...')
get_all_whisk_clf()
