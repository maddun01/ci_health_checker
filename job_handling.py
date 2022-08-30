#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Script for manipulating data."""

import calculate_statistics
import file_handling
import job
import statistic


class JobHandling:
    def __init__(self):
        self.calculate_statistics_object = calculate_statistics.CalculateStatistics()
        self.file_handling_object = file_handling.FileHandling()
        self.job_object = job.Job()
        self.statistic_object = statistic.Statistic()
        self.jobs_field_names = [
            "ID", "JOBID", "NAME", "PROJECTID",
            "QUEUEDDURATION", "DURATION", "STATUS"
        ]

    unique_jobs_list = []
    number_of_instances = 0

    def unique_jobs(self):
        """Collect the unique job names."""
        if self.job_object.count_jobs == 0:
            self.job_object.get_jobs()
        for item in self.job_object.jobs_list:
            name = item["NAME"]
            if name not in self.unique_jobs_list:
                self.unique_jobs_list.append(name)

    def call_statistics(self):
        """Calculate and form the statistics data."""
        if len(self.unique_jobs_list) == 0:
            self.unique_jobs()

        self.file_handling_object.write_header_to_file("stats")
        self.file_handling_object.open_file("stats", "a")
        id_number = 1
        for unique_job in self.unique_jobs_list:
            for item in self.job_object.jobs_list:
                job_name = item["NAME"]
                if job_name == unique_job:
                    self.number_of_instances += 1
                    self.calculate_statistics_object.collect_average_durations(
                        item["QUEUEDDURATION"], "queued"
                    )
                    self.calculate_statistics_object.collect_average_durations(
                        item["DURATION"], "duration"
                    )
                    self.calculate_statistics_object.calculate_status(
                        item["STATUS"].strip("\n")
                    )
            self.calculate_statistics_object.calculate_average_durations()
            self.file_handling_object.stats_file.write(
                f'{id_number},"{unique_job}",{self.number_of_instances},'
                f"{self.calculate_statistics_object.average_queued_duration},"
                f"{self.calculate_statistics_object.average_duration},"
                f"{self.calculate_statistics_object.number_of_passes},"
                f"{self.calculate_statistics_object.number_of_fails},"
                f"{self.calculate_statistics_object.number_of_skips},"
                f"{self.calculate_statistics_object.number_of_cancellations}\n"
            )

            self.calculate_statistics_object.reset_statistics()
            self.number_of_instances = 0
            id_number += 1
        self.file_handling_object.close_file("stats")
        self.statistic_object.clear_stats_list()
        self.statistic_object.get_stats()

    def recalculate_statistics(self):
        print("Changes to jobs file detected - recalculating statistics")
        self.file_handling_object.wipe_file("stats")
        self.unique_jobs_list.clear()
        self.call_statistics()

    def save_to_jobs_file(self):
        """Save changes to data store."""
        self.file_handling_object.wipe_file("jobs")
        self.file_handling_object.write_header_to_file("jobs")
        self.file_handling_object.open_file("jobs", "n")
        for item in self.job_object.jobs_list:
            self.file_handling_object.jobs_file.write(
                f'{item["ID"]},{item["JOBID"]},"{item["NAME"]}",'
                f'{item["PROJECTID"]},{item["QUEUEDDURATION"]},'
                f'{item["DURATION"]},{item["STATUS"]}\n'
            )
        self.file_handling_object.close_file("jobs")
