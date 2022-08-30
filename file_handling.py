#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Script for opening, closing and wiping files."""


class FileHandling:
    def __init__(self):
        self.jobs_filename = "jobs.csv"
        self.stats_filename = "stats.csv"

    def open_file(self, filename, mode):
        """Open given file in given mode."""
        if filename == "jobs":
            if mode == "a":
                self.jobs_file = open(self.jobs_filename, "a")
            elif mode == "r":
                self.jobs_file = open(self.jobs_filename, "r")
            elif mode == "n":
                self.jobs_file = open(self.jobs_filename, "a", newline="")
        elif filename == "stats":
            if mode == "a":
                self.stats_file = open(self.stats_filename, "a")
            elif mode == "r":
                self.stats_file = open(self.stats_filename, "r")

    def close_file(self, filename):
        """Close given file."""
        if filename == "jobs":
            self.jobs_file.close()
        elif filename == "stats":
            self.stats_file.close()

    def wipe_file(self, filename):
        """Clear given file."""
        if filename == "jobs":
            self.jobs_file = open(self.jobs_filename, "w")
            self.close_file("jobs")
        elif filename == "stats":
            self.stats_file = open(self.stats_filename, "w")
            self.close_file("stats")

    def write_header_to_file(self, filename):
        """Write given header to file."""
        if filename == "jobs":
            self.open_file("jobs", "a")
            self.jobs_file.write(
                "ID,JOBID,NAME,PROJECTID,QUEUEDDURATION,DURATION,STATUS\n"
            )
            self.close_file("jobs")
        elif filename == "stats":
            self.open_file("stats", "a")
            self.stats_file.write(
                f"ID,NAME,INSTANCES,AVERAGEQUEUEDDURATION,"
                f"AVERAGEDURATION,PASSES,FAILS,SKIPS,CANCELLATIONS\n"
            )
            self.close_file("stats")
