#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Script for connecting to GitLab."""

import file_handling
import gitlab


class GitlabAccess:
    def __init__(self, group_number, token, url):
        self.group_number = group_number
        self.token = token
        self.url = url
        self.file_handling_object = file_handling.FileHandling()

    project_id_list = []

    def connect_to_gitlab(self, token):
        return gitlab.Gitlab(url=self.url, private_token=token)

    def fetch_projects(self):
        """Fetch projects from given group."""
        self.gl = self.connect_to_gitlab(self.token)
        group = self.gl.groups.get(self.group_number)
        projects = group.projects.list(all=True, include_subgroups=True)
        for project in projects:
            self.project_id_list.append(project.id)

    def store_jobs(self):
        """Fetch each job from each pipeline from each project."""
        self.gl = self.connect_to_gitlab(self.token)
        if len(self.project_id_list) == 0:
            self.fetch_projects()
        self.file_handling_object.write_header_to_file("jobs")
        added_id = 1
        for i in self.project_id_list:
            project = self.gl.projects.get(int(i))
            self.file_handling_object.open_file("jobs", "a")
            jobs = project.jobs.list(all=True)
            for job in jobs:
                if job.queued_duration is None:
                    queued_duration = None
                else:
                    queued_duration = round(job.queued_duration, 3)
                if job.duration is None:
                    duration = None
                else:
                    duration = round(job.duration, 3)

                self.file_handling_object.jobs_file.write(
                    f'{added_id},{job.id},"{job.name}",{job.project_id},'
                    f"{queued_duration},{duration},{job.status}\n"
                )
                added_id += 1
            print(f"Jobs from Project {i} fetched and stored")
        self.file_handling_object.close_file("jobs")
        print("Completed")
