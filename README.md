langclassifier
==============

A rough language classification of a continuous stream of documents, using keyword matching.

Can be instantiated with language structure per instance.

Can be instantiated with either parameter 'languages_file' or parameter 'languages_to_use'. 'languages_file' takes precedence.
No parameter attempts to load default languages file.


Tests:

python langclassifier/classifier_test.py


Simple Usage:

from langclassifier import classifier

cl = classifier.classifier()

cl.feed_from_source(source) where source is a file or a url, classifying each line.
