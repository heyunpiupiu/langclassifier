# -*- coding: utf-8 -*-
import unittest

import classifier


class ClassifierTests(unittest.TestCase):

    def test_loads_settings(self):
        self.assertTrue(False)

    def test_accepts_lists_as_input(self):
        self.assertTrue(False)

    def test_does_not_load_invalid_language_list_dicts(self):
        self.assertTrue(False)

    def test_loads_language_lists_to_instance(self):
        self.assertTrue(False)

    def test_classify_returns_dictionary(self):
        self.assertTrue(False)

    def test_classify_returns_dictionary_containing_expected_elements(self):
        self.assertTrue(False)

    def test_classify_returns_empty_dict_for_none_input(self):
        cl = classifier.classifier()
        output = cl.classify()
        self.assertTrue('classified_string' in output and 'language_detected' in output)


def main():
    unittest.main()

if __name__ == '__main__':
    main()