#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Test file handling methods."""

import file_handling
import unittest


class FileHandlingTests(unittest.TestCase):

    file_handling_object = file_handling.FileHandling()

    def test_open_jobs_file_readable(self):
        # Act
        self.file_handling_object.open_file("jobs", "r")

        # Assert
        self.assertTrue(self.file_handling_object.jobs_file.readable())
        self.file_handling_object.jobs_file.close()

    def test_open_jobs_file_writable(self):
        # Act
        self.file_handling_object.open_file("jobs", "a")

        # Assert
        self.assertTrue(self.file_handling_object.jobs_file.writable())
        self.file_handling_object.jobs_file.close()

    def test_open_stats_file_readable(self):
        # Act
        self.file_handling_object.open_file("stats", "r")

        # Assert
        self.assertTrue(self.file_handling_object.stats_file.readable())
        self.file_handling_object.stats_file.close()

    def test_open_stats_file_writable(self):
        # Act
        self.file_handling_object.open_file("stats", "a")

        # Assert
        self.assertTrue(self.file_handling_object.stats_file.writable())
        self.file_handling_object.stats_file.close()

    def test_wipe_jobs_file(self):
        # Arrange
        file = open("jobs.csv", "w")
        file.write("Add this to the file")
        file.close()
        contents = []

        # Act
        self.file_handling_object.wipe_file("jobs")
        file = open("jobs.csv", "r")
        for item in file:
            contents.append(item)
        file.close()

        # Assert
        self.assertEqual(0, len(contents))

    def test_wipe_stats_file(self):
        # Arrange
        file = open("stats.csv", "w")
        file.write("Add this to the file")
        file.close()
        contents = []

        # Act
        self.file_handling_object.wipe_file("stats")
        file = open("stats.csv", "r")
        for item in file:
            contents.append(item)
        file.close()

        # Assert
        self.assertEqual(0, len(contents))

    def test_write_jobs_header(self):
        # Arrange
        file = open("jobs.csv", "w")
        file.close()
        COMPARISON_STRING = (
            "ID,JOBID,NAME,PROJECTID,QUEUEDDURATION,DURATION,STATUS\n"
        )

        # Act
        self.file_handling_object.write_header_to_file("jobs")

        file = open("jobs.csv", "r")
        line = file.readline()
        file.close()

        # Assert
        self.assertEqual(COMPARISON_STRING, line)
        file = open("jobs.csv", "w")
        file.close()

    def test_write_stats_header(self):
        # Arrange
        file = open("stats.csv", "w")
        file.close()
        COMPARISON_STRING = "ID,NAME,INSTANCES,AVERAGEQUEUEDDURATION,AVERAGEDURATION,PASSES,FAILS,SKIPS,CANCELLATIONS\n"

        # Act
        self.file_handling_object.write_header_to_file("stats")

        file = open("stats.csv", "r")
        line = file.readline()
        file.close()

        # Assert
        self.assertEqual(COMPARISON_STRING, line)
        file = open("stats.csv", "w")
        file.close()
