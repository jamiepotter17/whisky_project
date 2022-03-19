# Whisky Project

## Summary

This is a natural language, machine learning project that classifies whiskies based on tasting notes provided by the user. It was trained on data harvested from Reddit's whisky community through Reddit's API.

This repository contains the bulk of the background work and code for Whisky Project. The code for the web application hosted on Heroku is to be found on another GitHub repository - [whiskyapp](https://github.com/jamiepotter17/whiskyapp).

## Instructions:

The completed app is hosted on Heroku at [https://whiskyproject.herokuapp.com](https://whiskyproject.herokuapp.com). Please go there to view the app.

To use, simply enter your tasting notes for the nose, palate, and finish of your whisky, and click 'Guess Whisky Brand'. For example, my review of a typical Laphroaig (my favourite whisky!) would be:

* Nose - medicinal, peat, smoky
* Palate - sweet, mint, liquorice, peat
* Finish - sweet, salty, long

## Background

This is the Capstone Project for Udacity's [Become a Data Scientist](https://www.udacity.com/course/data-scientist-nanodegree--nd025) Nanodegree Program. It was commenced on 2012-02-28. Here the brief was fairly open, but the essential idea was to follow the Data Science Process from start to finish on a project of my own design. That is, to:

1. **Define** the problem you want to solve and investigate potential solutions.
2. **Analyse** the problem through visualisations and data exploration.
3. **Implement** algorithms and metrics, documenting any preprocessing, refinement, and post-processing steps along the way.
4. **Collect results**, and draw conclusions about whether your implementation adequately addresses the problem.

The final project could be in the form of either a blog post documenting all of the steps from start to finish of your project, or a deployment of a web application (or something that can be run on a local machine).

In my case, I decided that I was most interested in developing a web application that would allow users to enter tasting notes on a whisky, and it would predict what whisky it was. Other potential functionality I thought I might include was generating word clouds for particular brands of whisky and suggest similar whiskies.

## Data

The data I have gathered was taken from [Reddit's API](https://www.reddit.com/dev/api) using [PRAW](https://praw.readthedocs.io/en/stable/), a Python package that provides a useful wrapper when working with the API. A link to a list of reviews called the '[Whisky Review Archive](https://docs.google.com/spreadsheets/d/1X1HTxkI6SqsdpNSkSSivMzpxNT-oeTbjFFDdEkXD30o/edit#gid=695409533&fvid=484110565)' [Google Docs link] is made available on the [/r/whisky](https://www.reddit.com/r/whisky/) subreddit. I downloaded this spreadsheet file as a csv, and then augmented it as best I could so that the each row has the original review text included under the 'review' column.

## Ethics

In order to address any ethical concerns about the use of data, I note the following:

* All data were gathered via use of Reddit's API, using PRAW's standard downloading rate. No scraping was used.
* Reddit usernames are included in the spreadsheet, and Reddit users understand that their usernames are public-facing avatars. Thus, it is not disclosing private information to include this information. Nonetheless, seeing as it is not an important part of my project, I have removed username data from my dataset once I move beyond the data gathering stage.
* I will make users of /r/whisky aware of the existence of the app in the hopes that they will gain value from it.
* The app is for personal use and learning purposes only. It is not intended for commercial purposes. People are licenced to use it as they see fit (see licence.md)

## File list:

* README.MD - this file.
* .gitignore - tells GitHub which files it doesn't need to monitor.
* '1. Data Gathering.ipynb' - Jupyter Notebook file in which I use PRAW to gather the raw data for analysis from Reddit's whisky community.
* '2. Data Exploration and Cleaning.ipynb' - Jupyter Notebook file in which I'm mainly extracting the correct review from multi-review comments/submissions, and then the nose, palate and taste comments from the review. Some other issues as well.
* '3. Model Building.ipynb' - Jupyter Notebook file in which I develop the pipeline.
* '4. Creating Visualisations & Evaluation.ipynb' - Jupyter Notebook file in which I try out visualisations for the app and offer some evaluative thoughts.
* 'all_whisk_clf.py' - python module containing get_all_whisk_clf(), which is the function you need to run to get whisky_classifer.pkl, the pickle file the app requires. DO NOT RUN THIS FILE.
* 'get_whisky_clf.py' - this is file you have to actually run to get whisky_classifier.pkl. Simply use 'python get_whisky_clf.py' and it will generate the file in the models folder. It takes a few hours to run.
* ./data/branded.csv - csv file ready to be fed into ML algorithm.
* ./data/distances.csv  - csv file with Euclidean distances between the whiskies. Use index_col = ['brand','distance_type'] to open as it has a multi-index.
* ./data/gathering_complete.csv - this is the raw data I got from Reddit. 
* ./data/tasting_notes.txt - vocabulary list used by my countvectoriser in my pipeline.
* ./data/Whisky_Review_Archive.csv - original spreadsheet downloaded from Reddit, known as the '[Whisky Review Archive](https://docs.google.com/spreadsheets/d/1X1HTxkI6SqsdpNSkSSivMzpxNT-oeTbjFFDdEkXD30o/edit#gid=695409533&fvid=484110565)' [Google Docs link].
