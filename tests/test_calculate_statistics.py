#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Test calculation of statistics."""

import calculate_statistics
import unittest


class CalculateStatisticsTests(unittest.TestCase):

    calculate_statistics_object = calculate_statistics.CalculateStatistics()

    def test_collect_average_queued_durations(self):
        # Arrange
        EXAMPLE_QUEUED_DURATIONS_LIST = ["3.423", "4.732", "2.408"]

        # Act
        for item in EXAMPLE_QUEUED_DURATIONS_LIST:
            self.calculate_statistics_object.collect_average_durations(item, "queued")

        # Assert
        self.assertEqual(
            [3.423, 4.732, 2.408],
            self.calculate_statistics_object.average_queued_duration_list,
        )

    def test_collect_average_durations(self):
        # Arrange
        EXAMPLE_DURATIONS_LIST = ["3.243", "2.374", "4.802"]

        # Act
        for item in EXAMPLE_DURATIONS_LIST:
            self.calculate_statistics_object.collect_average_durations(
                item, "duration"
            )

        # Assert
        self.assertEqual(
            [3.243, 2.374, 4.802],
            self.calculate_statistics_object.average_duration_list,
        )

    def test_calculate_average_queued_duration(self):
        # Arrange
        self.calculate_statistics_object.average_queued_duration_list = [
            3.423,
            4.732,
            2.408,
        ]

        # Act
        self.calculate_statistics_object.calculate_average_durations()

        # Assert
        self.assertEqual(
            3.521, self.calculate_statistics_object.average_queued_duration
        )

    def test_calculate_average_queued_duration_no_durations(self):
        # Arrange
        self.calculate_statistics_object.average_queued_duration_list = []

        # Act
        self.calculate_statistics_object.calculate_average_durations()

        # Assert
        self.assertEqual(
            "None", self.calculate_statistics_object.average_queued_duration
        )

    def test_calculate_average_duration(self):
        # Arrange
        self.calculate_statistics_object.average_duration_list = [3.243, 2.374, 4.802]

        # Act
        self.calculate_statistics_object.calculate_average_durations()

        # Assert
        self.assertEqual(3.473, self.calculate_statistics_object.average_duration)

    def test_calculate_average_duration_no_durations(self):
        # Arrange
        self.calculate_statistics_object.average_duration_list = []

        # Act
        self.calculate_statistics_object.calculate_average_durations()

        # Assert
        self.assertEqual("None", self.calculate_statistics_object.average_duration)

    def test_reset_statistics(self):
        # Arrange
        self.calculate_statistics_object.number_of_passes = 6
        self.calculate_statistics_object.number_of_fails = 3
        self.calculate_statistics_object.number_of_skips = 2
        self.calculate_statistics_object.number_of_cancellations = 1
        self.calculate_statistics_object.average_queued_duration_list = [
            3.234,
            3.246,
            3.433,
        ]
        self.calculate_statistics_object.average_duration_list = [2.432, 4.217, 1.965]

        # Act
        self.calculate_statistics_object.reset_statistics()

        # Assert
        self.assertEqual(0, self.calculate_statistics_object.number_of_passes)
        self.assertEqual(0, self.calculate_statistics_object.number_of_fails)
        self.assertEqual(0, self.calculate_statistics_object.number_of_skips)
        self.assertEqual(0, self.calculate_statistics_object.number_of_cancellations)
        self.assertEqual(
            0, len(self.calculate_statistics_object.average_queued_duration_list)
        )
        self.assertEqual(
            0, len(self.calculate_statistics_object.average_duration_list)
        )
