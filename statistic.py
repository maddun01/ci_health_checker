#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Module for creating statistic objects."""

import csv
import file_handling


class Statistic:

    file_handling_object = file_handling.FileHandling()

    stats_list = []

    def get_stats(self):
        """Get data from the statistics file."""
        self.file_handling_object.open_file("stats", "r")
        csv_reader = csv.DictReader(self.file_handling_object.stats_file)
        for stat in csv_reader:
            self.stats_list.append(stat)
        self.file_handling_object.close_file("stats")

    def clear_stats_list(self):
        self.stats_list.clear()

    @property
    def count_stats(self):
        return len(self.stats_list)
