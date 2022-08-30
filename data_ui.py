#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Methods for displaying data."""

import job
import statistic


class DataUI:
    def __init__(self):
        self.job_object = job.Job()
        self.statistic_object = statistic.Statistic()

    stats_format = "{:<5}: {:<101} {:<10} {:<24} {:<17} {:<7} {:<6} {:<6} {}"
    jobs_format = "{:<5}: {:<7} {:<101} {:<11} {:<16} {:<12} {}"

    def display(self, display_type):
        """Display all the jobs or all the statistics."""
        if display_type == "jobs":
            self.jobs_header
            for item in self.job_object.jobs_list:
                name = self.crop_names(item["NAME"])
                print(
                    self.jobs_format.format(
                        item["ID"],
                        item["JOBID"],
                        name,
                        item["PROJECTID"],
                        item["QUEUEDDURATION"],
                        item["DURATION"],
                        item["STATUS"].capitalize(),
                    )
                )
        elif display_type == "stats":
            self.stats_header
            for item in self.statistic_object.stats_list:
                name = self.crop_names(item["NAME"])
                print(
                    self.stats_format.format(
                        item["ID"],
                        name,
                        item["INSTANCES"],
                        item["AVERAGEQUEUEDDURATION"],
                        item["AVERAGEDURATION"],
                        item["PASSES"],
                        item["FAILS"],
                        item["SKIPS"],
                        item["CANCELLATIONS"],
                    )
                )

    def display_by_id(self, display_type, choice):
        """Display a specific job or statistic."""
        if display_type == "jobs":
            self.jobs_header
            for item in self.job_object.jobs_list:
                if int(item["ID"]) == choice:
                    name = self.crop_names(item["NAME"])
                    print(
                        self.jobs_format.format(
                            item["ID"],
                            item["JOBID"],
                            name,
                            item["PROJECTID"],
                            item["QUEUEDDURATION"],
                            item["DURATION"],
                            item["STATUS"].capitalize(),
                        )
                    )
        elif display_type == "stats":
            self.stats_header
            for item in self.statistic_object.stats_list:
                if int(item["ID"]) == choice:
                    name = self.crop_names(item["NAME"])
                    print(
                        self.stats_format.format(
                            item["ID"],
                            name,
                            item["INSTANCES"],
                            item["AVERAGEQUEUEDDURATION"],
                            item["AVERAGEDURATION"],
                            item["PASSES"],
                            item["FAILS"],
                            item["SKIPS"],
                            item["CANCELLATIONS"],
                        )
                    )

    def search_records(self, display_type, phrase):
        """Display all jobs or statistics containing the search phrase."""
        if display_type == "jobs":
            found_jobs = []
            for item in self.job_object.jobs_list:
                name = item["NAME"]
                if phrase.upper() in name.upper():
                    found_jobs.append(item)
            if len(found_jobs) == 0:
                print("\nPhrase not found")
            else:
                self.count_search_results(found_jobs)
                self.jobs_header
                for job_i in found_jobs:
                    name = self.crop_names(job_i["NAME"])
                    print(
                        self.jobs_format.format(
                            job_i["ID"],
                            job_i["JOBID"],
                            name,
                            job_i["PROJECTID"],
                            job_i["QUEUEDDURATION"],
                            job_i["DURATION"],
                            job_i["STATUS"].capitalize(),
                        )
                    )
        elif display_type == "stats":
            found_stats = []
            for item in self.statistic_object.stats_list:
                name = item["NAME"]
                if phrase.upper() in name.upper():
                    found_stats.append(item)
            if len(found_stats) == 0:
                print("\nPhrase not found")
            else:
                self.count_search_results(found_stats)
                self.stats_header
                for stat_i in found_stats:
                    name = self.crop_names(stat_i["NAME"])
                    print(
                        self.stats_format.format(
                            item["ID"],
                            name,
                            item["INSTANCES"],
                            item["AVERAGEQUEUEDDURATION"],
                            item["AVERAGEDURATION"],
                            item["PASSES"],
                            item["FAILS"],
                            item["SKIPS"],
                            item["CANCELLATIONS"],
                        )
                    )

    def count_search_results(self, results_list):
        """Count and display the number of results."""
        if len(results_list) == 1:
            print(f"\nFound 1 result\n")
        else:
            print(f"\nFound {len(results_list)} results\n")

    def display_temp_data(self, entry):
        """Display data from the user that hasn't been saved."""
        self.jobs_header
        print(
            self.jobs_format.format(
                entry["ID"],
                entry["JOBID"],
                entry["NAME"],
                entry["PROJECTID"],
                entry["QUEUEDDURATION"],
                entry["DURATION"],
                entry["STATUS"].capitalize(),
            )
        )

    def crop_names(self, name):
        """Crop long names."""
        if len(name) >= 97:
            name = name[:96]
            name += "..."
        return name

    # Headers
    @property
    def jobs_header(self):
        """Header displayed before jobs."""
        print(
            self.jobs_format.format(
                "ID",
                "JOB ID",
                "NAME",
                "PROJECT ID",
                "QUEUED DURATION",
                "DURATION",
                "STATUS",
            )
        )

    @property
    def stats_header(self):
        """Header displayed before jobs."""
        print(
            self.stats_format.format(
                "ID",
                "NAME",
                "INSTANCES",
                "AVERAGE QUEUED DURATION",
                "AVERAGE DURATION",
                "PASSES",
                "FAILS",
                "SKIPS",
                "CANCELLATIONS",
            )
        )
