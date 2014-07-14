# -*- coding: utf-8 -*-
import unittest

import classifier


class ClassifierTests(unittest.TestCase):

    def test_loads_settings(self):
        # to be implemented later
        #self.assertTrue(False)
        pass

    def test_accepts_list_as_language_input(self):
        lang_list = [{'lang_name': 'test', 'words': ['ping', 'pong']}]
        try:
            cl = classifier.classifier(languages_to_use=lang_list)
        except:
            pass
        self.assertTrue(isinstance(cl, classifier.classifier))

    def test_loads_language_lists_to_instance(self):
        lang_list = [{'lang_name': 'test', 'words': ['ping', 'pong']}]
        cl = classifier.classifier(languages_to_use=lang_list)
        expected_internal_lang_structure = []
        for lang in lang_list:
            language_name_set_pair = {
                'lang_name': lang['lang_name'],
                'words': frozenset(lang['words'])
                }
            expected_internal_lang_structure.append(language_name_set_pair)
        self.assertTrue(cl.languages == expected_internal_lang_structure)

    def test_does_not_load_invalid_language_list_dicts(self):
        lang_list = [
            {'lang_name': 'valid', 'words': ['ping', 'pong']},
            {'lang_name': 'invalid1', 'not_words': ['ping', 'pong']},
            {'not_lang_name': 'invalid2', 'words': ['ping', 'pong']}
            ]

        expected_internal_lang_structure = [
            {'lang_name': 'valid', 'words': frozenset(['ping', 'pong'])}
            ]

        cl = classifier.classifier(languages_to_use=lang_list)
        self.assertTrue(cl.languages == expected_internal_lang_structure)

    def test_loads_languages_from_file(self):
        cl = classifier.classifier(languages_file='config_languages')
        # test at least on elanguage is loaded. If test fails, check file actually contains a valid language.
        self.assertTrue(len(cl.languages) > 0)

    def test_classify_returns_dictionary(self):
        cl = classifier.classifier()
        output = cl.classify()
        self.assertTrue(isinstance(output, dict))

    def test_classify_returns_dictionary_containing_expected_elements(self):
        cl = classifier.classifier()
        output = cl.classify()
        self.assertTrue('classified_string' in output and 'language_detected' in output)

    def test_classify_returns_empty_dict_for_none_input(self):
        expected_answer = {'classified_string': '', 'language_detected': ''}
        cl = classifier.classifier()
        output = cl.classify()
        self.assertTrue(output == expected_answer)

    def test_split_returns_empty_list_for_empty_input_string(self):
        cl = classifier.classifier()
        output = cl.split_and_cleanse_string("")
        self.assertTrue(isinstance(output, list) and len(output) == 0)

    def test_split_returns_list_of_strings(self):
        test_string = "This is a test string."
        cl = classifier.classifier()
        output = cl.split_and_cleanse_string(test_string)
        #test each element in output list is of typre string
        result = True
        for element in output:
            result = result and isinstance(element, str)
        self.assertTrue(result)

    def test_split_returns_list_for_words_in_provided_string(self):
        test_string = "This is a test string."
        expected_output = ['This', 'is', 'a', 'test', 'string']
        cl = classifier.classifier()
        output = cl.split_and_cleanse_string(test_string)
        self.assertTrue(output == expected_output)


    def test_split_returns_none_of_the_words_we_wish_cleansed(self):
        # to be implemented later
        #self.assertTrue(False)
        pass


def main():
    unittest.main()

if __name__ == '__main__':
    main()