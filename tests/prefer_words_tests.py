#!/usr/bin/env python2.7
# coding=utf-8

from __future__ import print_function, unicode_literals

import unittest

import sickbeard
from sickbeard.show_name_helpers import hasPreferedWords


class PreferWordFilterTest(unittest.TestCase):
    def setUp(self):
        sickbeard.PREFER_WORDS = 'atmos,7.1,5.1,ddp,dd'

        # prefer words only works on names, so we don't need complete shows
        self.results_names_only_source = [
            'Archer.2009.S01E10.1080p.WEB.x264-MEMENTO',
            'Archer.2009.S01E10.1080p.WEB.dd2.0.x264-MEMENTO',
            'Archer.2009.S10E08.1080p.AMZN.WEB-DL.DDP5.1.H.264-NT',
            'Archer.2009.S10E08.1080p.AMZN.WEB-DL.Atmos.DDP5.1.H.264-NT',
            'Archer.2009.S10E08.1080p.AMZN.WEB-DL.Atmos.DDP7.1.H.264-NT',
            'Archer.2009.S10E08.1080p.AMZN.WEB-DL.True-HD.DDP7.1.H.264-NT',
            'Archer.2009.S10E08.1080p.AMZN.WEB-DL.DDP.H.264-NT',
        ]

    def test_prefer_words_determine_weight(self):
        self.assertTrue(hasPreferedWords(self.results_names_only_source[0]) == 0)
        self.assertTrue(hasPreferedWords(self.results_names_only_source[1]) == 1)
        self.assertTrue(hasPreferedWords(self.results_names_only_source[2]) == 3)
        self.assertTrue(hasPreferedWords(self.results_names_only_source[3]) == 5)
        self.assertTrue(hasPreferedWords(self.results_names_only_source[4]) == 5)
        self.assertTrue(hasPreferedWords(self.results_names_only_source[5]) == 4)
        self.assertTrue(hasPreferedWords(self.results_names_only_source[6]) == 2)

if __name__ == '__main__':
    SUITE = unittest.TestLoader().loadTestsFromTestCase(PreferWordFilterTest)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
