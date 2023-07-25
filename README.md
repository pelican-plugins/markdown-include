Markdown Include: A Plugin for Pelican
======================================

[![Build Status](https://img.shields.io/github/actions/workflow/status/pelican-plugins/markdown-include/main.yml?branch=main)](https://github.com/pelican-plugins/markdown-include/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-markdown-include)](https://pypi.org/project/pelican-markdown-include/)
![License](https://img.shields.io/pypi/l/pelican-markdown-include?color=blue)

This plugin allows the use of the [Markdown-Include extension][] in Pelican articles.

[Markdown-Include extension]: https://github.com/cmacmackin/markdown-include

Installation
------------

This plugin can be installed via:

    python -m pip install pelican-markdown-include

As long as you have not explicitly added a `PLUGINS` setting to your Pelican settings file, then the newly-installed plugin should be automatically detected and enabled. Otherwise, you must add `md_include` to your existing `PLUGINS` list. For more information, please see the [How to Use Plugins](https://docs.getpelican.com/en/latest/plugins.html#how-to-use-plugins) documentation.

Usage
-----

The syntax for use within Pelican articles is `{!filename!}`. According to the documentation of the [Markdown-Include extension][], this statement will be replaced by the contents of `filename` and will work recursively. The replacement is done prior to any other Markdown processing, so any Markdown syntax that is wanted can be used within the included files. For more details, see the [Markdown-Include extension documentation][].

[Markdown-Include extension documentation]: https://github.com/cmacmackin/markdown-include/#readme


Configuration
-------------

The following variables control the behavior of the plugin and can be set in the Pelican settings file:

- `MD_INCLUDE_BASE_PATH`: By default, the file name is given relative to the directory from where Pelican is run. This can be changed via this variable.

- `MD_INCLUDE_ENCODING`: The encoding of the included files. Default: `"utf-8"`

- `MD_INCLUDE_INHERIT_HEADING_DEPTH`: If `True`, increases headings on included file by amount of previous heading. Combines with `MD_HEADING_OFFSET` option below. Default: `False`

- `MD_HEADING_OFFSET`: Increases heading depth by a specific amount, in addition to the `MD_INCLUDE_INHERIT_HEADING_DEPTH` option. Default: `0`


Alternatives to this Plugin
---------------------------

Pelican allows the use of extra Markdown extensions by declaring them in the `MARKDOWN` configuration variable.  However, as [explained][] in the Pelican documentation, adding new extensions via the `MARKDOWN` setting is awkward, because all the extensions loaded by default must also be explicitly listed. In addition to avoiding this problem, this plugin provides a “Pelican-ish” way of setting the configuration values of the Markdown-Include extension (`base_path`, `encoding`, `inherit_heading_depth`, and `heading_offset`).  Furthermore, the [Markdown-Include extension][] must be installed in a place where Pelican can find it, which may be tricky.

[explained]: https://docs.getpelican.com/en/latest/settings.html

Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/pelican-plugins/markdown-include/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

Acknowledgments
---------------

Thanks to [Justin Mayer][] for helping with migration of this plugin under the Pelican Plugins organization.

[Justin Mayer]: https://justinmayer.com

Author
------

Copyright © 2015, 2021-2023 Rafael Laboissière (<rafael@laboissiere.net>)

License
-------

This project is licensed under the terms of the the AGPL-3.0 license.
