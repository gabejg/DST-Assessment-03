A major observation we made, especially in comparison to other examples of topic modelling, was the structure of the SSH logs that we used. In a more general topic modelling environment (such as the news headline analysis in the workshop, or analysis of emails that we found examples of as part of our extended research) there are generally a lot more variety of words present in the data. SSH logs are fundamentally only written in a certain way: The computer detects the SSH and writes it's assessment of the situation, generally an acceptance or denial of service with a variety of messages for different situations. While this still produces a large number of different looking logs, in comparison to the sheer breadth of sentences found in emails or news headlines as part of the English language, the SSH logs tend towards certain patterns. We notice in our final topics that several words appear with exactly the same frequency, obviously they always appear in the same type of log message, something that would not happen in other situations generally due to individual preference on how something is written.

Leading on from the above, due to the nature of SSH logs, most of the words in the model are of quite a similar nature: to do with authentication, denial of service, and connecting to other devices on a network. This means that the topics are not particularly varied which almost certainly had a negative impact on our model. As previously mentioned, the amount of "junk" words which are hard to filter out without manual observation and removal in the logs is also a potential reason for less diverse and obvious topics.

## References

[SSH Dataset from here](https://www.simpleweb.org/wiki/index.php/SSH_datasets)

[Specifically this dataset](http://traces.simpleweb.org/ssh_datasets/dataset2_log_files.tgz)

[SSH Topic Modelling](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7117015)

[Topic Modelling tutorial - ft. data preparation](https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/)

[Workshop 7 was also very helpful - introduced to pickles](https://dsbristol.github.io/dst/coursebook/07.html)

[Loading pickles from URL](https://stackoverflow.com/questions/53107052/can-we-load-pkl-files-from-an-external-url)

[Catching HTTP errors](https://stackoverflow.com/questions/3193060/catch-specific-http-error-in-python)

[Regex stripping non-alphanumeric](https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python)

[Gzip Pickle](https://wiki.python.org/moin/How%20to%20I%20use%20gzip%20module%20with%20pickle%3F)