#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Test crop names methods."""

import unittest
import data_ui


class DataUITests(unittest.TestCase):

    data_ui_object = data_ui.DataUI()

    def test_name_crop_short_name(self):
        # Arrange
        short_name = "The hand that mocked them, and the heart that fed; And on the pedestal, these words appear:"

        # Act
        short_name = self.data_ui_object.crop_names(short_name)

        # Assert
        self.assertEqual(
            "The hand that mocked them, and the heart that fed; And on the pedestal, these words appear:",
            short_name,
        )

    def test_name_crop_long_name(self):
        # Arrange
        long_name = "My name is Ozymandias, King of Kings; Look on my Works, ye Mighty, and despair! Nothing beside remains."

        # Act
        long_name = self.data_ui_object.crop_names(long_name)

        # Assert
        self.assertEqual(
            "My name is Ozymandias, King of Kings; Look on my Works, ye Mighty, and despair! Nothing beside r...",
            long_name,
        )
