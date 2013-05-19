# -*- coding: utf-8 -*-

# Copyright 2013 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of InteractiveCommandLine. http://jacquev6.github.com/InteractiveCommandLine

# InteractiveCommandLine is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# InteractiveCommandLine is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with InteractiveCommandLine.  If not, see <http://www.gnu.org/licenses/>.

import unittest

import MockMockMock

from InteractiveCommandLine import StoringOption

class DeactivateableStoringOption(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        class Container:
            def __init__(self):
                self.attribute = None

        self.__container = Container()
        self.__activationValue = (42,)
        self.__deactivationValue = (56,)
        self.__option = StoringOption("name", self.__container, "attribute", self.__activationValue, self.__deactivationValue)

    def testCOnstructionDoesNotTouchContainer(self):
        self.assertIsNone(self.__container.attribute)

    def testActivateReturnsArguments(self):
        self.assertEqual(self.__option.activate("xx", "yy"), ("xx", "yy"))

    def testDeactivateReturnsArguments(self):
        self.assertEqual(self.__option.deactivate("xx", "yy"), ("xx", "yy"))

    def testActivateActivates(self):
        self.__option.activate()
        self.assertIs(self.__container.attribute, self.__activationValue)

    def testDeactivate(self):
        self.__option.deactivate()
        self.assertIs(self.__container.attribute, self.__deactivationValue)

class NonDeactivateableStoringOption(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        class Container:
            def __init__(self):
                self.attribute = None

        self.__container = Container()
        self.__activationValue = (42,)
        self.__option = StoringOption("name", self.__container, "attribute", self.__activationValue)

    def testActivateActivates(self):
        self.__option.activate()
        self.assertIs(self.__container.attribute, self.__activationValue)

    def testDeactivateRaises(self):
        with self.assertRaises(Exception) as cm:
            self.__option.deactivate()
        self.assertEqual(cm.exception.message, "Option 'name' cannot be deactivated")
