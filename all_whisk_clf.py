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

def get_all_whisk_clf():

    # Read in data and tasting_note_list
    df = pd.read_csv('./data/branded.csv', index_col = 'Unnamed: 0')
    with open('./data/tasting_notes.txt', 'r') as f:
        wordlist = [item[:-1] for item in f.readlines()]

    # dropping brands that only have a frequency of lower_limit or fewer because it screws
    # up cross-validation.
    df = drop_unpopular_brands('df', df, 10)

    # Pipeline to use
    pipeline = Pipeline([

            ('union', FeatureUnion([

                ('pipe_nose', Pipeline([
                    ('get_nose', FunctionTransformer(getnose)),
                    ('countvec_nose', CountVectorizer(
                        tokenizer=tokenise_and_stem_text, vocabulary=wordlist) )
                ]) ),
                ('pipe_palate', Pipeline([
                    ('get_palate', FunctionTransformer(getpalate)),
                    ('countvec_palate', CountVectorizer(
                        tokenizer=tokenise_and_stem_text, vocabulary=wordlist) )
                ]) ),
                ('pipe_finish', Pipeline([
                    ('get_finish', FunctionTransformer(getfinish)),
                    ('countvec_finish', CountVectorizer(
                        tokenizer=tokenise_and_stem_text, vocabulary=wordlist) )
                ]) ),
            ]) ),

            ('tfidf_transform', TfidfTransformer()),

            ('clf', RandomForestClassifier(n_jobs=-1))
            ])

    param_grid = [
        {'clf' : [LogisticRegression()],
         'clf__penalty' : ['l2'],
        'clf__C' : [1, 2, 4, 8],
        'clf__solver' : ['liblinear']},
        {'clf' : [RandomForestClassifier(n_jobs=-1)],
        'clf__bootstrap': [False],
        'clf__max_depth': [200, 500],
        'clf__max_features': ['sqrt'],
        'clf__n_estimators': [1000, 2000]},
        {'clf' : [SVC()],
         'clf__degree' : [1, 2],
         'clf__C' : [2, 2.5, 3, 3.5, 4]}
    ]

    X_train, X_test, y_train, y_test = train_test_split(
        df[['nose', 'palate', 'finish']], df['brand'])
    X_train, X_test = X_train.to_numpy(), X_test.to_numpy()

    print('Performing grid search now...')
    grid_search_all_whiskies = GridSearchCV(estimator = pipeline, cv=3,
                        param_grid = param_grid, scoring='accuracy', verbose=3)

    grid_search_all_whiskies.fit(X_train, y_train)

    # Save to pickle file
    with open('./models/whisky_classifier.pkl', "wb") as f:
        joblib.dump(grid_search_all_whiskies, f, compress='zlib')
