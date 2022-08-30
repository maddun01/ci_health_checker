#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Module for creating job objects."""

import csv
import file_handling


class Job:
    def __init__(self):
        self.file_handling_object = file_handling.FileHandling()

    jobs_list = []

    def get_jobs(self):
        """Get data from the jobs file."""
        self.file_handling_object.open_file("jobs", "r")
        csv_reader = csv.DictReader(self.file_handling_object.jobs_file)
        for job in csv_reader:
            self.jobs_list.append(job)
        self.file_handling_object.close_file("jobs")

    def clear_jobs_list(self):
        self.jobs_list.clear()

    @property
    def count_jobs(self):
        return len(self.jobs_list)
