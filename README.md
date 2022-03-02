# Whisky Classifier

## Summary

## Instructions:

1. Run the following commands in the project's root directory to set up your
database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python ./process_data.py data/disaster_messages.csv
        data/disaster_categories.csv Disaster_Response.db`
    - To run ML pipeline that trains classifier and saves
        `python ./train_classifier.py data/Disaster_Response.db
        classifier.pkl`

2. Run the web app: `python run.py`

3. Copy the URL into your browser - e.g. http://192.168.1.117:3000/ from
the line 'Running on http://192.168.1.117:3000/ (Press CTRL+C to quit)'.

## Background

This is the Capstone Project for Udacity's [Become a Data Scientist](https://www.udacity.com/course/data-scientist-nanodegree--nd025) Nanodegree Program. It was commenced on 2012-02-28. Here the brief was fairly open, but the essential idea was to follow the Data Science Process from start to finish on a project of my own design. That is, to:

1. **Define** the problem you want to solve and investigate potential solutions.
2. **Analyse** the problem through visualisations and data exploration.
3. **Implement** algorithms and metrics, documenting any preprocessing, refinement, and post-processing steps along the way.
4. **Collect results**, and draw conclusions about whether your implementation adequately addresses the problem.

The final project could be in the form of either a blog post documenting all of the steps from start to finish of your project, or a deployment of a web application (or something that can be run on a local machine).

In my case, I decided that I was most interested in developing a web application that would allow users to enter tasting notes on a whisky, and it would predict what whisky it was. Other potential functionality I might include would be generating word clouds for particular brands of whisky and suggest similar whiskies.

## Data

The data I have gathered was taken from [Reddit's API](https://www.reddit.com/dev/api) using [PRAW](https://praw.readthedocs.io/en/stable/), a Python package that provides a useful wrapper when working with the API. A link to a list of reviews called the '[Whisky Review Archive](https://docs.google.com/spreadsheets/d/1X1HTxkI6SqsdpNSkSSivMzpxNT-oeTbjFFDdEkXD30o/edit#gid=695409533&fvid=484110565)' [Google Docs link] is made available on the [/r/whisky](https://www.reddit.com/r/whisky/) subreddit. I downloaded this spreadsheet file as a csv, and then augmented it as best I could so that the each row has the original review text included under the 'review' column.

## Ethics

In order to address any ethical concerns about the use of data, I note the following:

* All data were gathered via use of Reddit's API, using PRAW's standard downloading rate. No scraping was used.
* Reddit usernames are included in the spreadsheet, and Reddit users understand that their usernames are public-facing avatars. Thus, it is not disclosing private information to include this information. Nonetheless, seeing as it is not an important part of my project, I have removed username data from my dataset.
* I will make users of /r/whisky aware of the existence of the app in the hopes that they will gain value from it.
* The app is for personal use and learning purposes only. It is not intended for commercial purposes. People are licenced to use it as they see fit (see licence.md)




## File list:

* .gitignore - tells GitHub which files it doesn't need to monitor.
* 'ETL Pipeline Preparation.ipynb' - Jupyter Notebook file used to develop the
code for process_data.py.
* 'ML Pipeline Preparation.ipynb' - Jupyter Notebook file used to develop the
code for train_classifier.py.
* README.MD - this file.
* graphs.py - python module that contains get_graphs(), a function that returns
the graphs that ultimately get displayed on master.html.
* process_data.py - python script that runs an ETL pipeline, loading data into
an SQLite database, specifically a table titled 'messages'.
* requirements.txt - things should work fine in a standard Anaconda
environment, but here is a list of all the packages used in my Anaconda
environment in case you have compatibility issues.  Use
'pip install requirements.txt' to install the packages.
* run.py - python script that runs the Flash app that routes traffic to the
right places.
* train_classifier.py - python script that runs a ML pipeline, transforming
data from an SQLite database into a pickle file.
