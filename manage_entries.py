#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Script for adding, editing and deleting entries from the data store."""

import data_ui
import file_handling
import input_validation
import job
import job_handling


class AddEntries:
    def __init__(self):
        self.new_jobs_entry = {}
        self.to_return = False
        self.data_ui_object = data_ui.DataUI()
        self.input_validation_object = input_validation.InputValidation()
        self.job_object = job.Job()
        self.job_handling_object = job_handling.JobHandling()

    def add_data(self):
        """Get user inputs."""
        fields = [
            (
                "Enter the job's ID: ",
                "JOBID",
                lambda user_input: self.input_validation_object.validate_int(
                    user_input, "Error: Please enter a number"
                ),
            ),
            (
                "Enter the job's name: ",
                "NAME",
                lambda user_input: self.input_validation_object.validate_string(
                    user_input
                ),
            ),
            (
                "Enter the job's project ID: ",
                "PROJECTID",
                lambda user_input: self.input_validation_object.validate_int(
                    user_input, "Error: Please enter a number"
                ),
            ),
            (
                "Enter the job's queued duration: ",
                "QUEUEDDURATION",
                lambda user_input: self.input_validation_object.validate_float(
                    user_input
                ),
            ),
            (
                "Enter the job's duration: ",
                "DURATION",
                lambda user_input: self.input_validation_object.validate_float(
                    user_input
                ),
            ),
            (
                "Enter the job's status (success, failed, skipped or canceled): ",
                "STATUS",
                lambda user_input: self.input_validation_object.validate_status(
                    user_input
                ),
            ),
        ]
        while self.to_return is not True:
            self.new_jobs_entry = {}
            self.new_jobs_entry["ID"] = self.job_object.count_jobs + 1
            print(self.display_return_to_menu_header)
            for user_prompt, field, validation_type in fields:
                user_input = " "
                while user_input == " ":
                    user_input = input(user_prompt)
                    if user_input.upper() == "Q":
                        return
                    else:
                        user_input = validation_type(user_input)
                        self.new_jobs_entry[field] = user_input
            self.data_ui_object.display_temp_data(self.new_jobs_entry)
            self.save_jobs_data()

    def save_jobs_data(self):
        """Save new entry to file."""
        choice = input("Are you sure you want to save? (Y/N/Q) ")
        if choice.upper() == "Y":
            self.job_object.jobs_list.append(self.new_jobs_entry)
            self.job_handling_object.save_to_jobs_file()
            print("\nNew entry saved")
            self.job_handling_object.recalculate_statistics()
            self.to_return = True
            return
        elif choice.upper() == "Q":
            self.to_return = True
            return
        self.reset_to_return_variable()

    def reset_to_return_variable(self):
        self.to_return = False

    @property
    def display_return_to_menu_header(self):
        return "Press Q at any time to return to the main menu\n"


class EditEntries:
    def __init__(self):
        self.add_entries = AddEntries()
        self.data_ui_object = data_ui.DataUI()
        self.delete_entries = DeleteEntries()
        self.input_validation_object = input_validation.InputValidation()
        self.job_object = job.Job()
        self.to_validate = False
        self.id_to_edit = False
        self.to_return = False
        self.edited_entry = {}

    def choose_data_to_edit(self):
        """Get the ID of the entry."""
        while not self.id_to_edit:
            if self.to_return:
                self.to_return = False
                return
            else:
                print(self.add_entries.display_return_to_menu_header)
                self.id_to_edit = input("Enter the ID of the job to edit: ")
                if self.id_to_edit.upper() == "Q":
                    self.to_return = True
                    return
                else:
                    self.id_to_edit = self.input_validation_object.validate_ID(
                        self.id_to_edit, "jobs"
                    )
                    if not self.id_to_edit:
                        pass
                    else:
                        self.data_ui_object.display_by_id("jobs", self.id_to_edit)
                        choice = input(
                            "Are you sure you want to edit this? (Y/N/Q): "
                        )
                        if choice.upper() == "Y":
                            self.edit_data(self.id_to_edit)
                        elif choice.upper() == "N":
                            self.id_to_edit = False
                        elif choice.upper() == "Q":
                            self.reset_variables()
                            self.to_return = False
                            return

    def edit_data(self, id_to_edit):
        """Get user inputs."""
        fields = [
            (
                "Enter the job's new ID: ",
                "JOBID",
                lambda user_input: self.input_validation_object.validate_int(
                    user_input, "Error: Please enter a number"
                ),
            ),
            (
                "Enter the job's new name: ",
                "NAME",
                lambda user_input: self.input_validation_object.validate_string(
                    user_input
                ),
            ),
            (
                "Enter the job's new project ID: ",
                "PROJECTID",
                lambda user_input: self.input_validation_object.validate_int(
                    user_input, "Error: Please enter a number"
                ),
            ),
            (
                "Enter the job's new queued duration: ",
                "QUEUEDDURATION",
                lambda user_input: self.input_validation_object.validate_float(
                    user_input
                ),
            ),
            (
                "Enter the job's new duration: ",
                "DURATION",
                lambda user_input: self.input_validation_object.validate_float(
                    user_input
                ),
            ),
            (
                "Enter the job's new status (success, failed, skipped or canceled): ",
                "STATUS",
                lambda user_input: self.input_validation_object.validate_status(
                    user_input
                ),
            ),
        ]
        while not self.to_return:
            if not self.id_to_edit:
                return
            print("Enter the new values, or leave blank to leave unchanged\n")
            self.item = self.job_object.jobs_list[id_to_edit - 1]
            self.edited_entry = {}
            self.edited_entry["ID"] = id_to_edit

            for user_prompt, field, validation_type in fields:
                user_input = " "
                while user_input == " ":
                    user_input = input(user_prompt)
                    if user_input.upper() == "Q":
                        return
                    else:
                        user_input = self.is_null(user_input, field)
                        if self.to_validate:
                            user_input = validation_type(user_input)
                        self.edited_entry[field] = user_input
            self.data_ui_object.display_temp_data(self.edited_entry)
            self.save_changes()

    def is_null(self, var_to_check, key):
        """Determine if the entry is unchanged."""
        if var_to_check == "":
            self.to_validate = False
            return self.item[key]
        else:
            self.to_validate = True
            return var_to_check

    def save_changes(self):
        """Update the data store."""
        choice = input("Are you sure you want to save? (Y/N/Q) ")
        if choice.upper() == "Y":
            self.job_object.jobs_list[self.id_to_edit - 1] = self.edited_entry
            self.delete_entries.update_file()
            self.to_return = True
            return
        elif choice.upper() == "N":
            self.id_to_edit = False
            return
        elif choice.upper() == "Q":
            self.to_return = True
            return
        self.reset_variables()

    def reset_variables(self):
        self.to_validate = False
        self.id_to_edit = False
        self.to_return = False


class DeleteEntries:
    def __init__(self):
        self.add_entries = AddEntries()
        self.data_ui_object = data_ui.DataUI()
        self.file_handling_object = file_handling.FileHandling()
        self.input_validation_object = input_validation.InputValidation()
        self.job_object = job.Job()
        self.job_handling_object = job_handling.JobHandling()

    to_return = False

    def choose_data_to_remove(self):
        """Get the ID of the entry."""
        while not self.to_return:
            print(self.add_entries.display_return_to_menu_header)
            id_to_remove = input("Enter the ID of the job to delete: ")
            if id_to_remove.upper() == "Q":
                return
            else:
                id_to_remove = self.input_validation_object.validate_ID(
                    id_to_remove, "jobs"
                )
                if not id_to_remove:
                    pass
                else:
                    self.data_ui_object.display_by_id("jobs", id_to_remove)
                    choice = input(
                        "Are you sure you want to delete this? (Y/N/Q): "
                    )
                    if choice.upper() == "Y":
                        self.remove_data(id_to_remove)
                        return
                    elif choice.upper() == "N":
                        pass
                    elif choice.upper() == "Q":
                        return

    def remove_data(self, id_to_remove):
        """Remove the entry from the list."""
        self.job_object.jobs_list.pop(id_to_remove - 1)
        for i in range(id_to_remove - 1, self.job_object.count_jobs):
            line = self.job_object.jobs_list[i]
            line["ID"] = int(line["ID"]) - 1
        self.update_file()

    def update_file(self):
        """Remove the entry from the list."""
        self.file_handling_object.wipe_file("jobs")
        self.file_handling_object.write_header_to_file("jobs")
        self.job_handling_object.save_to_jobs_file()
        print("Jobs file updated\n")
        self.job_handling_object.recalculate_statistics()
