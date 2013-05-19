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
import textwrap

import MockMockMock

from InteractiveCommandLine import Program, Command, Option


class AutoHelp(unittest.TestCase):
    def setUp(self):
        self.mocks = MockMockMock.Engine()
        self.input = self.mocks.create("input")
        self.output = self.mocks.create("output")

        self.commandOption = Option("command-option")

        self.programOption = Option("program-option")

        self.command = Command("test")
        self.command.addOption(self.commandOption)

        self.program = Program(self.input.object, self.output.object)
        self.program.addAutoHelp("example")
        self.program.addCommand(self.command)
        self.program.addOption(self.programOption)

    def tearDown(self):
        self.mocks.tearDown()

    def testCommandLineHelp(self):
        self.output.expect.write(textwrap.dedent("""\
        Usage:
          Command-line mode: example [global-options] command [options]
          Interactive mode: example [global-options]

        Global options:
          --program-option  xx

        Commands:
          help  xx
          test  xx
        """))
        self.program._execute("help")