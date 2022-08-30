#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Test job methods."""

import job
import unittest


class JobTests(unittest.TestCase):

    job_object = job.Job()

    def test_get_jobs(self):
        # Arrange
        COMPARISON_LIST = ["This line should not be in the list\n"]
        file = open("jobs.csv", "w")
        file.write("This line should not be in the list\n")
        for i in range(5):
            file.write(f"This is line {i}\n")
        file.close()

        # Act
        self.job_object.get_jobs()
        file = open("jobs.csv", "w")
        file.close()

        # Assert
        self.assertEqual(5, len(self.job_object.jobs_list))
        self.assertNotIn(COMPARISON_LIST, self.job_object.jobs_list)
        self.job_object.jobs_list.clear()

    def test_clear_jobs_list(self):
        # Arrange
        for i in range(10):
            self.job_object.jobs_list.append(i)

        # Act
        self.job_object.clear_jobs_list()

        # Assert
        self.assertEqual(0, len(self.job_object.jobs_list))

    def test_count_jobs(self):
        # Arrange
        self.job_object.jobs_list = ["1", "2", "3", "4"]
        # Act
        length_of_jobs_list = self.job_object.count_jobs
        # Assert
        self.assertEqual(4, length_of_jobs_list)
        self.job_object.jobs_list.clear()
