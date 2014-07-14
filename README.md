langclassifier
==============

A rough language classification of a continuous stream of documents, using keyword matching.

Can be instantiated with language structure per instance.

Can be instantiated with either parameter 'languages_file' or parameter 'languages_to_use'. 'languages_file' takes precedence.
No parameter attempts to load default languages file.


Tests:

cd langclassifier

python classifier_test.py


Usage:

cd langclassifier

cl = classifier.classifier()

cl.feed_from_source(source) where source is a file or a url, classifying each line.
