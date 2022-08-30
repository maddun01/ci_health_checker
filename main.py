#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Script for navigation and selecting menu options."""

import menu_ui
import startup


ERROR_MESSAGE_MAIN_MENU = "Error: Please enter a number (0-5)"
ERROR_MESSAGE_JOBS_STATS = "Error: Please enter a number (1 or 2)"


def check_ci_health(group_number, token, url):
    """Checks the health of the CI.

    Args:
        group_number (int): the group to fetch projects from.
        token (str): the token to allow access to the GitLab instance.
        url (str): the URL of the GitLab instance.

    """
    menu_UI_object = menu_ui.MenuUI()
    start_up_object = startup.StartUp(group_number, token, url)

    start_up_object.start_up()

    while True:
        menu_UI_object.display_menu()
        menu_UI_object.process_user_menu_choice(input("\nSelect an option: "))
        if menu_UI_object.to_return:
            break
