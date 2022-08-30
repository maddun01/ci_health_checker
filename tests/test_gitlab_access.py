#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Test connection to GitLab and usage of REST API."""

import csv
import gitlab_access
import unittest


class GitlabAccessTests(unittest.TestCase):

    gitlab_access_object = gitlab_access.GitlabAccess(
        "<group_number>", "<private_token>", "<private_url"
    )

    def test_connect_to_gitlab(self):
        # Act
        token = "<private-token>"
        gl = self.gitlab_access_object.connect_to_gitlab(token)
        project = gl.projects.get(420)
        pipeline = project.pipelines.get(52344)

        # Assert
        self.assertTrue(52344, pipeline.id)
        self.assertTrue(1, pipeline.iid)
        self.assertTrue(420, pipeline.project_id)
        self.assertTrue("failed", pipeline.status)

    def test_fetch_projects(self):
        # Act
        self.gitlab_access_object.fetch_projects()
        PROJECT_LIST = [
            505, 502, 479, 477, 442, 434, 433, 427, 421,
            420, 408, 406, 365, 314, 301, 295, 294, 282,
            258, 247, 154, 153, 129, 128, 125, 123
        ]

        # Assert
        self.assertEqual(26, len(self.gitlab_access_object.project_id_list))
        self.assertEqual(PROJECT_LIST, self.gitlab_access_object.project_id_list)

    def test_store_jobs(self):
        # Arrange
        self.gitlab_access_object.project_id_list = ["434"]
        jobs_list = []
        file = open("jobs.csv", "w")
        file.close()
        HEADER = [
            "ID", "JOBID", "NAME", "PROJECTID",
            "QUEUEDDURATION", "DURATION", "STATUS"
        ]

        # Act
        self.gitlab_access_object.store_jobs()
        file = open("jobs.csv", "r")
        csv_reader = csv.reader(file)
        for job in csv_reader:
            jobs_list.append(job)
        file.close()

        # Assert
        self.assertIn(HEADER, jobs_list)
        self.assertEqual("504188", jobs_list[1][1])
        self.assertEqual("skipped", jobs_list[2][6])
        self.assertEqual("434", jobs_list[4][3])
        file = open("jobs.csv", "w")
        file.close()
