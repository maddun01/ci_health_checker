#!/usr/bin/env python
# Copyright (c) 2022 Madeleine Dunn. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

"""Test validation methods."""

import input_validation
import unittest

class InputValidationTests(unittest.TestCase):

    input_validation_object = input_validation.InputValidation()

    def test_validate_float(self):
        # Arrange
        var_to_validate = 3.456

        # Act
        var_to_validate = self.input_validation_object.validate_float(var_to_validate)

        # Assert
        self.assertEqual(3.456, var_to_validate)

    def test_validate_float_int(self):
        # Arrange
        var_to_validate = 3

        # Act
        var_to_validate = self.input_validation_object.validate_float(var_to_validate)

        # Assert
        self.assertEqual(3.0, var_to_validate)

    def test_validate_float_str(self):
        # Arrange
        var_to_validate = "hello"

        # Act
        var_to_validate = self.input_validation_object.validate_float(var_to_validate)

        # Assert
        self.assertEqual(" ", var_to_validate)

    def test_validate_float_none(self):
        # Arrange
        var_to_validate = "None"

        # Act
        var_to_validate = self.input_validation_object.validate_float(var_to_validate)

        # Assert
        self.assertEqual("None", var_to_validate)

    def test_validate_int(self):
        # Arrange
        var_to_validate = 2
        ERROR_MESSAGE = "Error"

        # Act
        var_to_validate = self.input_validation_object.validate_int(
            var_to_validate, ERROR_MESSAGE
        )

        # Assert
        self.assertEqual(2, var_to_validate)

    def test_validate_int_str(self):
        # Arrange
        var_to_validate = "hello"
        ERROR_MESSAGE = "Error"

        # Act
        var_to_validate = self.input_validation_object.validate_int(
            var_to_validate, ERROR_MESSAGE
        )

        # Assert
        self.assertEqual(" ", var_to_validate)

    def test_validate_status_success(self):
        # Arrange
        var_to_validate = "success"

        # Act
        var_to_validate = self.input_validation_object.validate_status(
            var_to_validate
        )

        # Assert
        self.assertEqual("success", var_to_validate)

    def test_validate_status_failed(self):
        # Arrange
        var_to_validate = "failed"

        # Act
        var_to_validate = self.input_validation_object.validate_status(
            var_to_validate
        )

        # Assert
        self.assertEqual("failed", var_to_validate)

    def test_validate_status_skipped(self):
        # Arrange
        var_to_validate = "skipped"

        # Act
        var_to_validate = self.input_validation_object.validate_status(
            var_to_validate
        )

        # Assert
        self.assertEqual("skipped", var_to_validate)

    def test_validate_status_canceled(self):
        # Arrange
        var_to_validate = "canceled"

        # Act
        var_to_validate = self.input_validation_object.validate_status(
            var_to_validate
        )

        # Assert
        self.assertEqual("canceled", var_to_validate)

    def test_validate_status_wrong_status(self):
        # Arrange
        var_to_validate = "hello"

        # Act
        var_to_validate = self.input_validation_object.validate_status(
            var_to_validate
        )

        # Assert
        self.assertEqual(" ", var_to_validate)

    def test_validate_string(self):
        # Arrange
        var_to_validate = "String"

        # Act
        var_to_validate = self.input_validation_object.validate_string(
            var_to_validate
        )

        # Assert
        self.assertEqual("String", var_to_validate)

    def test_validate_string_invalid_string(self):
        # Arrange
        var_to_validate = ""

        # Act
        var_to_validate = self.input_validation_object.validate_string(
            var_to_validate
        )

        # Assert
        self.assertEqual(" ", var_to_validate)
