#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Script for validating user inputs."""

import job
import statistic


class InputValidation:
    def __init__(self):
        self.job_object = job.Job()
        self.statistic_object = statistic.Statistic()

    def validate_float(self, var_to_validate):
        if var_to_validate == "None":
            return "None"
        else:
            try:
                var_to_validate = float(var_to_validate)
            except:
                print(
                    "Error: Please enter a decimal (can be an integer) or None"
                )
                return " "
            else:
                return float(round(var_to_validate, 3))

    def validate_int(self, var_to_validate, error_message):
        try:
            var_to_validate = int(var_to_validate)
        except:
            print(error_message)
            return " "
        else:
            return int(var_to_validate)

    def validate_ID(self, var_to_validate, ID_type):
        """Check given IDs are valid numbers and in range of the list."""
        var_to_validate = self.validate_int(
            var_to_validate, "Error: Please enter a number"
        )
        if var_to_validate == " ":
            return False
        else:
            if ID_type == "jobs":
                if (
                    0 < var_to_validate
                    and var_to_validate < self.job_object.count_jobs + 1
                ):
                    return int(var_to_validate)
                else:
                    print("Error: Given ID does not exist")
                    return False
            elif ID_type == "stats":
                if (
                    0 < var_to_validate
                    and var_to_validate < len(self.statistic_object.stats_list) + 1
                ):
                    print("This is a valid ID")
                    return int(var_to_validate)
                else:
                    print("Error: Given ID does not exist")
                    return False

    def validate_status(self, var_to_validate):
        if (
            var_to_validate.upper() == "SUCCESS"
            or var_to_validate.upper() == "FAILED"
            or var_to_validate.upper() == "SKIPPED"
            or var_to_validate.upper() == "CANCELED"
        ):
            return var_to_validate
        else:
            print("Error: Invalid entry for this field")
            return " "

    def validate_string(self, var_to_validate):
        if var_to_validate == "" or var_to_validate == " ":
            print("Error: Please enter a phrase")
            return " "
        else:
            return var_to_validate
