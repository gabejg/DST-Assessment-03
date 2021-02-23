# Data Science Toolbox - Assessment 03

*This project is the 3rd assessment for the Data Science Toolbox from the MSc Mathematics of Cybersecurity course at the University of Bristol (2020/21). There are 3 contributors to the project. While it is preferrable to be able to test models and draw solid conclusions, the most important parts of these assessments is to explore options available for good Data Science in the industry and learn new skills throughout the project.*

## Introduction

In this project we were challenged, as a group, to apply topic-modelling in a cybersecurity context. The actual brief is this project was rather short compared to our previous projects, leaving much of what we did in this project open to interpretation. It was acknowledged that *"public domain cyber-security data in this space is sparse and you may have to work with other sources"*, which presented one of the larger challenges we've experienced thus far in this module as we had to find and select our own data to work on.

It was also specified that this project had to be worked on in Python, which provided unexpected challenges for some less familiar with the language. However, we understand that Python was the best language for the task, as not only does it have a wide variety of packages available for topic modelling, but the string manipulation (particularly in the form of regular expressions) in Python is considerably better than that of R.

We spent a good amount of time researching into what data we were going to apply our model to, checking several different sources as well as the resources we had available from the course notes to make sure that the data set we were working on would be suitable for our purpose. Our first pass of research highlighted all to well the problem phrased above in that it was quite hard to find "wordy" public cybersecurity data that could be use to apply topic modelling to. This led us to believe that we might have to go a different route and use "Meta-Data" surrounding cyber-security; using data that talks about types of attack rather than specific data.

Upon further research however we found the following [data](https://www.simpleweb.org/wiki/index.php/SSH_datasets). Upon inspection of the data we found that it had a selection of SSH logs, which contained plenty of text detailing what was going on at each connection, and could be processed well for use with our models. More details on the data will be mentioned in the [next part] of the report.

Now that we had found the data we needed we needed to decide on a suitable focus for our project; what did we want to achieve? We boiled it down to two main points:
* To apply different topic models and test the efficiency of each, as well as comparing the results to draw conclusions about how good each model is.
* To see what conclusions about the data we can draw from these models, as it would be a shame if we were to apply these models for no reason other than to just see if they work.

The two models we decided to use were an TFIDF model, and standard LDA model, with explorations into other areas. While these models have elegant solutions and packages to implement in Python, adapting each for use in our area with our data is always a challenge and was in this project too.

The reader is asked to look at each item in the [Report](https://github.com/Galeforse/DST-Assessment-03/tree/master/Report) folder chronologically in order to follow a similar sequence of events to how we conducted our code.

## Contributors

Additional annotated and unannotated work can be find in our individual folders, but not all of this made it into the final report:

[Gabriel Grant](https://github.com/Galeforse/DST-Assessment-03/tree/master/Gabriel%20Grant)
    
[Luke Hawley](https://github.com/Galeforse/DST-Assessment-03/tree/master/Luke%20Hawley)

[Wenqi Fang](https://github.com/Galeforse/DST-Assessment-03/tree/master/Wenqi%20Fang)
