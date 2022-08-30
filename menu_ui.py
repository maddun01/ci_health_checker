#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Module for displaying information to the user."""

import data_ui
import input_validation
import manage_entries


ERROR_MESSAGE_MAIN_MENU = "Error: Please enter a number (0-5)"
ERROR_MESSAGE_JOBS_CHOICE = "Error: Please enter a number (1 or 2)"


class MenuUI:
    def __init__(self):
        self.add_entries = manage_entries.AddEntries()
        self.data_ui_object = data_ui.DataUI()
        self.delete_entries = manage_entries.DeleteEntries()
        self.edit_entries = manage_entries.EditEntries()
        self.input_validation_object = input_validation.InputValidation()
        self.to_return = False

    def display_menu(self):
        print(
            f"\nMenu"
            f"\n1. Display jobs or statistics"
            f"\n2. Display a specific job or statistic"
            f"\n3. Search jobs or statistics"
            f"\n4. Add a new job record"
            f"\n5. Edit a job record"
            f"\n6. Delete a job record"
            f"\n0. Quit"
        )

    def jobs_or_stats(self, header_type):
        if header_type == "D":
            print("1. Display jobs\n2. Display statistics\n")
        elif header_type == "S":
            print("1. Search jobs\n2. Search statistics\n")

    def process_user_menu_choice(self, user_choice):
        user_choice = self.input_validation_object.validate_int(
            user_choice, ERROR_MESSAGE_MAIN_MENU
        )
        if user_choice == 1:
            print("\nDisplay all jobs or all statistics\n")
            print(self.add_entries.display_return_to_menu_header)
            self.jobs_or_stats("D")
            choice = input("Select an option: ")
            if choice.upper() != "Q":
                choice = self.input_validation_object.validate_int(
                    choice, ERROR_MESSAGE_JOBS_CHOICE
                )
                if choice == 1:
                    print("Display jobs\n")
                    self.data_ui_object.display("jobs")
                elif choice == 2:
                    print("Display statistics\n")
                    self.data_ui_object.display("stats")
        elif user_choice == 2:
            print("\nDisplay a specific job or statistic\n")
            print(self.add_entries.display_return_to_menu_header)
            self.jobs_or_stats("D")
            choice = input("Select an option: ")
            if choice.upper() != "Q":
                choice = self.input_validation_object.validate_int(
                    choice, ERROR_MESSAGE_JOBS_CHOICE
                )
                if choice == 1:
                    print("Display a specific job\n")
                    entry_choice = input("Enter job ID: ")
                    if entry_choice.upper() != "Q":
                        entry_choice = self.input_validation_object.validate_ID(
                            entry_choice, "jobs"
                        )
                        if entry_choice:
                            self.data_ui_object.display_by_id("jobs", entry_choice)
                elif choice == 2:
                    print("Display a specific statistic\n")
                    entry_choice = input("Enter statistic ID: ")
                    if entry_choice.upper() != "Q":
                        entry_choice = self.input_validation_object.validate_ID(
                            entry_choice, "stats"
                        )
                        if entry_choice:
                            self.data_ui_object.display_by_id("stats", entry_choice)
        elif user_choice == 3:
            print("\nSearch jobs or statistics\n")
            print(self.add_entries.display_return_to_menu_header)
            self.jobs_or_stats("S")
            choice = input("Select an option: ")
            if choice.upper() != "Q":
                choice = self.input_validation_object.validate_int(
                    choice, ERROR_MESSAGE_JOBS_CHOICE
                )
                if choice == 1:
                    print("Search jobs data\n")
                    search_phrase = input("Enter a search phrase to use: ")
                    if search_phrase.upper() != "Q":
                        self.data_ui_object.search_records("jobs", search_phrase)
                elif choice == 2:
                    print("Search statistics data\n")
                    search_phrase = input("Enter a search phrase to use: ")
                    if search_phrase.upper() != "Q":
                        self.data_ui_object.search_records("stats", search_phrase)
        elif user_choice == 4:
            print("\nAdd a record\n")
            self.add_entries.reset_to_return_variable()
            self.add_entries.add_data()
        elif user_choice == 5:
            print("\nEdit a record\n")
            self.edit_entries.reset_variables()
            self.edit_entries.choose_data_to_edit()
        elif user_choice == 6:
            print("\nDelete a record\n")
            self.delete_entries.choose_data_to_remove()
        elif user_choice == 0:
            quit_choice = input("0: Quit. Are you sure (Y/N)? ")
            if quit_choice.upper() == "Y":
                self.to_return = True
                return self.to_return
