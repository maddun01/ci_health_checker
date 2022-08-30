# Continuous Integration Health Checker

This repository contains code written for Module 3: Software Development Fundamentals.

The application is a Continuous Integration Health Checker, written to help users monitor automated tests running on a GitLab server.

It connects to a private GitLab instance and fetches job information from a specific group. This is used to populate the jobs csv file.

## Requirements

This application requires the `python-gitlab` module - find the docs here: https://python-gitlab.readthedocs.io/en/stable/index.html.

## Usage

Navigate to the project directory.

Run the command: `python ci_health_checker.py -g <group_number> -t <private_token> -u <url>`.

Run `python ci_health_checker.py -h` for more information.
