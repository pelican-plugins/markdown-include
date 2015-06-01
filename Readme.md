# Pelican plugin for using the Markdown-Include extension

## Description

This plugin allows the use of the
[Markdown-Include extension](https://github.com/cmacmackin/markdown-include)
in Pelican articles.


## Installation

The Markdown-Include module must be installed in the system, otherwise this
plugin will be deactivated.  The module can be installed with pip:

    pip install markdown-include

You might install this plugin directly from Github along with your website
sources.  At the top-level directory, do, for instance:

    mkdir plugins-extra
    git clone https://github.com/rlaboiss/pelican_md_include.git plugins-extra/md_include

In `pelicanconf.py`, add `'plugins-extra'` to `PLUGIN_PATHS` and
`md_include'` to `PLUGINS` (see the Pelican
[documentation](http://docs.getpelican.com/en/3.5.0/plugins.html#how-to-use-plugins)
for details about configuring your plugins).


## Usage

The syntax for use within Pelican articles is `{!filename!}`. According to
the documentation of the Markdown-Include extension, this statement will be
replaced by the contents of `filename` and will work recursively. The
replacement is done prior to any other Markdown processing, so any Markdown
syntax that is wanted can be used within the included files.


## Configuration

The following variables control the behavior of the plugin and can be set
in the Pelican settings file:

- `MD_INCLUDE_BASE_PATH`: By default, the file name is given relative to
the directory from where Pelican is run.  This can be changed with this
variable.

- `MD_INCLUDE_ENCODING`: The encoding of the included files (defaults to
  `'utf-8'`).


## Alternative to this plugin

Pelican allows the use of extra Markdown extensions by declaring them in
the `MD_EXTENSIONS` configuration variable.  However, as
[explained](http://docs.getpelican.com/en/latest/settings.html) in the
Pelican documentation, adding new extensions via MD_EXTENSIONS is awkward,
because all the extensions loaded by default must also be listed.  Besides
avoiding this problem, this plugin provides a "pelicanish" way of setting
the configuration values of the Markdown-Include extension (`base_path` and
`encoding`).  Furthermore, Markdown-Include extension must be installed in
a place where Pelican can find it, what may be tricky.


## Author

Copyright (C) 2015  Rafael Laboissiere (<rafael@laboissiere.net>)

Released under the GNU Affero Public License, version 3 or later.  No warranties.
