Runestone Home Page
===================


This repository contains the source for the homepage at `blog.runestone.academy <https://blog.runestone.academy>`_ (`runestoneinteractive.com <https://runestoneinteractive.com>`_)

If you are interested in authoring a blog post about how you use Runestone in your course, we would welcome your contribution!  You can do it as a PR against this repository or submit the rst as an issue.  And I'll take care of it.


To Build this Site
------------------

This site is built using `tinker` which is an open source static site generator written in Python.  You can install tinker with pip::

    pip install -r requirements.txt

Then to build the site::

    tinker --build

To view the site locally::

    python -m http.server

Then open your browser to http://localhost:8000

