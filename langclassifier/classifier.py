# -*- coding: utf-8 -*-


class classifier:
    """ Classifier class for classifying input of strings, by matching
        with predefined lists of words characteristic of specified languages.

        Languages structure is specifically set NOT as a class variable, so we
        can have multiple classes loaded with different language settings.

        To optimise matching, the intersection of sets is used.
    """

    config_file = 'config_classifier'  # configuration file

    def __init__(self, languages_to_use=None):
        """ Initialises class.

            Needs to initialise:
                languages structure used for matching.

            Args:
                languages_to_use: a list containing dictionaries defining language/words pairs.
        """
        self.languages = []  # list holding the words we define as "key" for each language

        # if class was called with languages_to_use param
        if isinstance(languages_to_use, list):
            self.set_language_sets(languages_to_use)

    def set_language_sets(self, languages_to_set):
        """ Sets class instance language/words pairs, later used for the classification process.

            languages class instance variable is a list of dictionaries, each dictionary containing:
                lang_name: name of language.
                words: a frozenset derived from a list provided, containing strings.

            Args:
                languages_to_set: a list of dictionaries.
        """
        if isinstance(languages_to_set, list):  # if param is list
            for lang in languages_to_set:  # for each element in list
                if isinstance(lang, dict):  # if element is dict
                    if 'lang_name'in lang and 'words' in lang:  # if dict contains required attributes
                        word_set = frozenset(lang['words'])  # create frozenset of words
                        l = {'lang_name': lang['lang_name'], 'words': word_set}
                        self.languages.append(l)  # append to instance language object

    def classify(self, string_to_classify=None):
        """ Attempts to match words contained within passed string with
            words defined in

            Args:
                string_to_classify: string to be classified.

            Returns:
                dictionary containing the passed string and the language name it was classified under.
                If string is not classified under any language, "could not classify" is returned.
        """
        # structure of returned object
        answer = {'classified_string': '', 'language_detected': ''}
        # detect function being called without parameter
        if string_to_classify is not None:
            pass
        return answer
