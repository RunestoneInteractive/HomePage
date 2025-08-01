Mid-July Update
===============

Today is July 19, 2025, and we are excited to share the latest updates with you. We have been hard at work on several projects, and we are pleased to announce that we have made significant progress on the following:

**LTI 1.3**: We are continuing to roll out LTI 1.3 support across more Learning Management Systems (LMS). This integration will enhance the usability of Runestone in various educational environments, making it easier for instructors to incorporate our resources into their courses. We are happy to report that we have successfully tested it with Desire2Learn, Moodle, and Canvas.  If you want to get LTI 1.3 set up for your course please `create an issue <https://github.com/RunestoneInteractive/rs/issues>`_ on our GitHub repository, and we will assist you in the setup process.  Note there is a special category for LTI Support issues.  Please refer to the LTI documentation in `The Instructor Guide <https://guide.runestone.Academy>`_ for more information.  If you have questions please ask them on the ``#lti_community_support`` channel in the Runestone discord.

**New Assignment Builder**: The new assignment builder has been well received, and we are continuing to refine it based on user feedback. We have added several new features, and fixed many bugs. The assignment builder now supports a wider range of question types, including fill-in-the-blank and matching questions. We encourage all instructors to try it out and share their experiences with us.

**Quality of Life Improvements**: We have made several quality of life improvements to the platform, including:
- Improved Course Selection Page
- Improved Instructor Dashboard
- Better support for MathJax and LaTeX rendering in several areas
- Support for attaching pdfs, and image files to short answer questions
- many more small improvements to the user interface

**Internals** : We have made significant internal improvements to our platform, including updates our logging system, optimizing our database queries, and improving the overall performance of the site. These changes will help us provide a more reliable and efficient system.

The internal updates also make it easier for anyone to contribute to Runestone.  If you are interested in helping out with a feature or a bug fix I would welcome your help!  The documentation is available at `Runestone Development Docs <https://runestone-monorepo.readthedocs.io/en/latest/index.html>`_. If you have any questions or need assistance, please feel free to reach out to us.  We have especially simplified the process by creating database API's to do most everything you need to do with the database.  No need to know or use SQL.

Book Updates
------------

As we continue the transition to writing books in PreTeXt there are several books that are no longer being updated in their original format.  In particular the following books have been replaced by new versions:

-  *How to Think Like a Computer Scientist* (``thinkcspy``)  switch to ``httlacs``
-  *CSAwesome* now has a new edition and a new look, You should switch to ``csawesome2`` which follows the latest college board standards for APCSA.
-  *Problem Solving with Algorithms and Data Structures using Python* ``pythonds`` has been replaced by ``pswadsup``.
-  *Problem Solving with Algorithms and Data Structures using C++* ``cppds`` has been replaced by ``cppds2``.
- *C++ for Python Programmers* ``cpp4python`` has been replaced by ``cpp4py-v2``.
- *Java for Python Programmers* ``java4python`` has been replaced by ``java4py2``.
- *How to Think Like a Computer Scientist C++ edition* (``thinkcpp``) has been replaced by ``thinkcpp2``.

We'll mark these and other books as deprecated in the library in the next few weeks to make it easier to find the latest version.

Retiring restructuredText
----------------------------

This is a good time to remind everyone that the markup extensions to restructuredText will no longer be developed.  In fact there are quite a few features that are supported in PreTeXt that are not supported in restructuredText.  If you are writing a new book, or updating an existing book, we encourage you to use PreTeXt.  Beginning with the 8.0 release of the runestone components, we will not include the python code for the markup.  Beginning with that release we will just provide the javascript for the interactive components.  We look forward to continuing to develop new and innovative interactive components that support student learning with Markdown in PreTeXt.

.. author:: default
.. categories:: none
.. tags:: none
.. comments::
