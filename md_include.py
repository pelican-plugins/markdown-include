"""Pelican Plugin for using the Markdown include extension"""

## Copyright (C) 2015  Rafael Laboissiere
##
## This program is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Affero Public License as published by
## the Free Software Foundation, either version 3 of the License, or (at
## your option) any later version.
##
## This program is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## Affero General Public License for more details.
##
## You should have received a copy of the GNU Affero General Public License
## along with this program.  If not, see http://www.gnu.org/licenses/.

import os
from pelican import signals

import logging
logger = logging.getLogger (__name__)

try:
    from markdown_include.include import MarkdownInclude
except ImportError:
    MarkdownInclude = None


def initialize (pelicanobj):
    """Initialize the Libravatar plugin"""
    pelicanobj.settings.setdefault ('MD_INCLUDE_BASE_PATH', None)
    pelicanobj.settings.setdefault ('MD_INCLUDE_ENCODING', None)

    config = {}

    base_path = pelicanobj.settings.get ('MD_INCLUDE_BASE_PATH')
    if base_path:
        config ['base_path'] = base_path

    encoding = pelicanobj.settings.get ('MD_INCLUDE_ENCODING')
    if encoding:
        config ['encoding'] = encoding

    pelicanobj.settings ['MD_EXTENSIONS'].append (MarkdownInclude (config))


def register ():
    """Register the Graphviz plugin with Pelican"""
    if MarkdownInclude:
        signals.initialized.connect (initialize)
    else:
        logger.warning ('Failed to load the markdown_include module. '
                        'The md_include plugin is deactivated.')
