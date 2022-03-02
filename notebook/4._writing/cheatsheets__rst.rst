.. _gakwao0Xn4:

=======================================
reStructuredText
=======================================

.. code-block:: text

    # Lists
    * This is a bulleted list.
    * It has two items, the second
      item uses two lines.

    1. This is a numbered list.
    2. It has two items too.

    #. This is a numbered list.
    #. It has two items too.

    # Nested Lists
    * this is
    * a list

      * with a nested list
      * and some subitems

    * and here the parent list continues

    # external link
     `Link text <https://domain.invalid/>`_

    # code block
    .. code-block:: console|html|python|text

        def myfunction():
            return 42

    # list table
        .. list-table::
        :header-rows: 1

        * - Cheat Sheets
          - Check Lists
          - Documents
        * - :ref:`Tickler File <gtd_tickler_file_cheat_sheet>`
          -
          - :ref:`Introduction <gtd-introduction>`


References
=======================================

#. `Docutils <http://docutils.sourceforge.net/rst.html>`_
#. `Quick reStructuredText <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_
#. `Sphinx reStructuredText Primer <https://www.sphinx-doc.org/es/master/usage/restructuredtext/basics.html>`_
