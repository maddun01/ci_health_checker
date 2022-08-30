#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Test statistic methods."""

import unittest
import statistic


class StatisticTests(unittest.TestCase):

    statistic_object = statistic.Statistic()

    def test_get_stats(self):
        # Arrange
        file = open("stats.csv", "w")
        file.write("This line should not be in the list\n")
        for i in range(5):
            file.write(f"This is line {i}\n")
        file.close()
        COMPARISON_LIST = ["This line should not be in the list"]

        # Act
        self.statistic_object.get_stats()
        file = open("stats.csv", "w")
        file.close()

        # Assert
        self.assertEqual(5, len(self.statistic_object.stats_list))
        self.assertNotIn(COMPARISON_LIST, self.statistic_object.stats_list)
        self.statistic_object.stats_list.clear()

    def test_clear_stats_list(self):
        # Arrange
        for i in range(10):
            self.statistic_object.stats_list.append(i)

        # Act
        self.statistic_object.clear_stats_list()

        # Assert
        self.assertEqual(0, len(self.statistic_object.stats_list))

    def test_count_stats(self):
        # Arrange
        self.statistic_object.stats_list = ["1", "2", "3", "4"]
        # Act
        length_of_stats_list = self.statistic_object.count_stats
        # Assert
        self.assertEqual(4, length_of_stats_list)
        self.statistic_object.stats_list.clear()
