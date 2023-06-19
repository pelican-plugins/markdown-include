# -*- coding: utf-8 -*-
"""Unit testing suite for the Markdown-Include Plugin"""

# Copyright (C) 2015, 2021, 2022  Rafael Laboissière <rafael@laboissiere.net>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Affero Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.

import os
import re
from shutil import rmtree
from tempfile import mkdtemp
import unittest

from pelican import Pelican
from pelican.settings import read_settings

from . import md_include

TEST_FILE_STEM = "test"
TEST_DIR_PREFIX = "pelicantests."
INCLUDE_FILENAME = "include"
INCLUDED_CONTENT = "naïve"


class TestMarkdownInclude(unittest.TestCase):
    """Class for testing the URL output of the Markdown-Include plugin"""

    def setUp(
        self,
        encoding=None,
        base_path=None,
        inherit_heading_depth=None,
        heading_offset=None,
    ):
        self.output_path = mkdtemp(prefix=TEST_DIR_PREFIX)
        self.content_path = mkdtemp(prefix=TEST_DIR_PREFIX)

        settings = {
            "PATH": self.content_path,
            "OUTPUT_PATH": self.output_path,
            "PLUGINS": [md_include],
            "CACHE_CONTENT": False,
        }

        if base_path:
            include_dir = os.path.join(self.content_path, base_path)
            os.makedirs(include_dir)
        else:
            include_dir = self.content_path
        settings["MD_INCLUDE_BASE_PATH"] = include_dir

        if encoding:
            settings["MD_INCLUDE_ENCODING"] = encoding

        if inherit_heading_depth:
            settings["MD_INCLUDE_INHERIT_HEADING_DEPTH"] = inherit_heading_depth

        if heading_offset:
            settings["MD_INCLUDE_HEADING_OFFSET"] = heading_offset

        # Create the article file
        fid = open(
            os.path.join(self.content_path, f"{TEST_FILE_STEM}.md"),
            "w",
        )
        fid.write(
            f"""Title: Test
Date: 1970-01-01

{{!{INCLUDE_FILENAME}!}}
"""
        )
        fid.close()

        # Create the included file
        if encoding:
            encoded_content = INCLUDED_CONTENT.encode(encoding)
            fid = open(os.path.join(include_dir, INCLUDE_FILENAME), "wb")
        else:
            encoded_content = INCLUDED_CONTENT
            fid = open(os.path.join(include_dir, INCLUDE_FILENAME), "w")
        fid.write(encoded_content)
        fid.close()

        # Run the Pelican instance
        self.settings = read_settings(override=settings)
        pelican = Pelican(settings=self.settings)
        pelican.run()

    def tearDown(self):
        rmtree(self.output_path)
        rmtree(self.content_path)

    def test_inclusion(self):
        """Test for default values"""
        fid = open(
            os.path.join(self.output_path, f"{TEST_FILE_STEM}.html"),
            "r",
        )
        found = False
        for line in fid.readlines():
            if re.search(INCLUDED_CONTENT, line):
                found = True
                break
        assert found


class TestMarkdownIncludeEncoding(TestMarkdownInclude):
    """Class for exercising the configuration variable MD_INCLUDE_ENCODING"""

    def setUp(self, override=None):
        """Initialize the configurations"""
        TestMarkdownInclude.setUp(self, encoding="iso-8859-1")

    def test_inclusion(self):
        """Test for MD_INCLUDE_ENCODING setting"""
        TestMarkdownInclude.test_inclusion(self)


class TestMarkdownIncludeBasePath(TestMarkdownInclude):
    """Class for exercising configuration variable MD_INCLUDE_BASE_PATH"""

    def setUp(self, override=None):
        """Initialize the configurations"""
        TestMarkdownInclude.setUp(self, base_path="subdir")

    def test_inclusion(self):
        """Test for MD_INCLUDE_BASE_PATH setting"""
        TestMarkdownInclude.test_inclusion(self)


class TestMarkdownInheritHeadingDepth(TestMarkdownInclude):
    """Class for exercising configuration variable MD_INCLUDE_INHERIT_HEADING_DEPTH"""

    def setUp(self, override=None):
        """Initialize the configurations"""
        TestMarkdownInclude.setUp(self, inherit_heading_depth=True)

    def test_inclusion(self):
        """Test for MD_INCLUDE_INHERIT_HEADING_DEPTH setting"""
        TestMarkdownInclude.test_inclusion(self)


class TestMarkdownHeadingOffset(TestMarkdownInclude):
    """Class for exercising configuration variable MD_INCLUDE_HEADING_OFFSET"""

    def setUp(self, override=None):
        """Initialize the configurations"""
        TestMarkdownInclude.setUp(self, heading_offset=1)

    def test_inclusion(self):
        """Test for MD_INCLUDE_HEADING_OFFSET setting"""
        TestMarkdownInclude.test_inclusion(self)
