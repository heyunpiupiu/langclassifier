# -*- coding: utf-8 -*-

import re


class classifier:
    """ Classifier class for classifying input of strings, by matching
        with predefined lists of words characteristic of specified languages.

        Languages structure is specifically set NOT as a class variable, so we
        can have multiple classes loaded with different language settings.

        To optimise matching, the intersection of sets is used.
    """

    config_file_langs_default = 'config_languages'  # language configuration file

    def __init__(self, languages_file=None, languages_to_use=None):
        """ Initialises class.

            Needs to initialise:
                languages structure used for matching.

            Args:
                languages_file: a file containing a language structure of
                                    a list containing dictionaries defining language/words pairs.
                languages_to_use: a list containing dictionaries defining language/words pairs.

            If languages_file is passed, languages_to_use is ignored.
            If neither parameter is passed, it will try to load languages from default language file.
        """
        self.languages = []  # list holding the words we define as "key" for each language

        if languages_file:  # if class was called with a languages config file
            self.load_language_sets_from_config(languages_file)
        elif languages_to_use:  # if class was called with languages_to_use param
            if isinstance(languages_to_use, list):
                self.set_language_sets(languages_to_use)
        else:  # if no parameters were passed, try to load languages from default language file
            self.load_language_sets_from_config(self.config_file_langs_default)

    def load_language_sets_from_config(self, config_file=config_file_langs_default):
        """ Loads language sets from configuration file.
        """
        if __import__(config_file):  # if config file for languages can be imported
            config_langs = __import__(config_file)
            self.set_language_sets(config_langs.languages)

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
        answer = {'classified_string': '', 'language_detected': 'could not classify'}
        # detect function being called without parameter
        if string_to_classify is not None:
            answer['classified_string'] = string_to_classify
            word_list = self.split_and_cleanse_string(string_to_classify)  # parse string into a wordlist
            word_list_set = frozenset(word_list)  # create a frozenset of the word list
            for lang in self.languages:
                intersection_of_sets = lang['words'].intersection(word_list_set)  # intersection of sets
                if len(intersection_of_sets) > 0:  # if there is an intersection
                    answer['language_detected'] = lang['lang_name']  # language found
                    break

        return answer

    def split_and_cleanse_string(self, string):
        """ Splits string into words. If we wish to cleanse any characters or words, should be done within.

            Args:
                string we wish to split and cleanse.

            Returns:
                list containing the words found in provided string as string elements.
        """
        resulting_list = []

        if isinstance(string, str):
            rx = re.compile('\W+')  # create a new regular expression
            cleansed_string = rx.sub(' ', string).strip()  # strip everything apart from single whitespace
            resulting_list = cleansed_string.split()  # split cleansed string
            # additional cleansing can occur before or after the splitting

        return resulting_list
