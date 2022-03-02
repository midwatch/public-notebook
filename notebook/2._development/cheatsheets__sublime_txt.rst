.. _GGedzC6TsD:

=======================================
Sublime Text
=======================================

Standard Configuration and Packages
=======================================

Omni Markup Previewer
---------------------------------------

.. code-block:: console

    # Linux & Windows
    $ Ctrl+Alt+O:       Preview Markup in Browser.
    $ Ctrl+Alt+X:       Export Markup as HTML.
    $ Ctrl+Alt+C:       Copy Markup as HTML.

    # OSX
    $ ⌘+⌥+O:            Preview Markup in Browser.
    $ ⌘+⌥+X:            Export Markup as HTML.
    $ Ctrl+Alt+C:       Copy Markup as HTML.

**Suported Formats:**

- Markdown
- reStrcuturedText
- WikiCreole
- Textile
- Pod
- RDoc
- Org Mode
- mediaWiki
- AsciiDoc
- Literate Haskell


Standard Config File
---------------------------------------

.. code-block:: json

    {
        "ensure_newline_at_eof_on_save": true,
        "font_size": 10,
        "tab_size": 4,
        "rulers": [100],
        "translate_tabs_to_spaces": true,
        "trim_trailing_white_space_on_save": true
    }

**Notes:**

#. Preferences -> Settings
#. Location (Linux): $HOME/.config/sublime-text-3/Packages/User/Preferences.sublime-settings


Manage Packages
=======================================

Install package contol by following instructions in [1]

Preferences -> Package Control


References
=======================================

#. `Sublime Text Package Manager <https://packagecontrol.io/>`_
#. `OmniMarkupPreviewer <https://github.com/timonwong/OmniMarkupPreviewer>`_
