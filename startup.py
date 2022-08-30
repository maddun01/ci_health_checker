#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Script for ensuring the data store is correctly prepared."""

import file_handling
import gitlab_access
import job
import job_handling
import os
import statistic


JOBS_HEADER = "ID,JOBID,NAME,PROJECTID,QUEUEDDURATION,DURATION,STATUS"


class StartUp:
    def __init__(self, group_number, token, url):
        self.file_handling_object = file_handling.FileHandling()
        self.job_handling_object = job_handling.JobHandling()
        self.statistic_object = statistic.Statistic()
        self.gitlab_access_object = gitlab_access.GitlabAccess(group_number, token, url)
        self.job_object = job.Job()

    def start_up(self):
        self.check_for_empty_file()
        self.check_for_corrupted_file()
        if self.job_object.count_jobs == 0:
            self.job_object.get_jobs()

        print("Calculating statistics")
        self.file_handling_object.wipe_file("stats")
        self.job_handling_object.call_statistics()

        if self.statistic_object.count_stats == 0:
            self.statistic_object.get_stats()

    def check_for_corrupted_file(self):
        """Check the jobs header is correct."""
        self.file_handling_object.open_file("jobs", "r")
        first_line = self.file_handling_object.jobs_file.readline()
        if first_line.strip("\n") != JOBS_HEADER:
            print("Corrupted jobs file detected - wiping file")
            self.file_handling_object.wipe_file("jobs")
        self.file_handling_object.close_file("jobs")
        self.check_for_empty_file()

    def check_for_empty_file(self):
        job_filesize = os.path.getsize(self.file_handling_object.jobs_filename)
        if job_filesize == 0:
            print("Empty jobs file detected - fetching from GitLab")
            self.file_handling_object.wipe_file("jobs")
            self.gitlab_access_object.store_jobs()
            self.job_object.get_jobs()
