#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Script for getting command line arguments to pass to the Health Checker."""

import argparse
import main


def parse_args():
    """Parse the command line args."""
    parser = argparse.ArgumentParser(
        description="CI Health Checker",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-g",
        "--group_number",
        type=int,
        required=True,
        help=("the group to fetch projects from."),
    )

    parser.add_argument(
        "-t",
        "--token",
        type=str,
        required=True,
        help=("the token to allow access to the GitLab instance."),
    )

    parser.add_argument(
        "-u",
        "--url",
        type=str,
        required=True,
        help=("the URL of the GitLab instance."),
    )

    return parser.parse_args()


if __name__ == "__main__":
    """Run CI Health Checker."""
    args = parse_args()
    main.check_ci_health(args.group_number, args.token, args.url)
