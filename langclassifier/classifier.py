# -*- coding: utf-8 -*-


class classifier:
    """ Classifier class for classifying input of strings, by matching
        with predefined lists of words characteristic of specified languages.

        Languages structure is specifically set NOT as a class variable, so we
        can have multiple classes loaded with different language settings.
    """

    config_file = 'config_classifier'  # configuration file

    def __init__(self):
        """ Initialises class.

            Needs to initialise:
                languages structure used for matching.
        """
        languages = {}  # dictionary holding the words we define as "key" for each language
        pass

    def classify(string_to_classify=None):
        """ Attempts to match
        """
        # structure of returned object
        answer = {'classified_string': '', 'language_detected': ''}
        # detect function being called without parameter
        if string_to_classify is not None:
            pass
        return answer
