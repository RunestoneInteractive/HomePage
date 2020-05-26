Runestone 5.0
=============

Today I am extremely pleased to announce Runestone 5.0!  This is a combined new release of both the server as well as the components. Not a lot of this release is highly visible but there is a lot going on behind the scenes.

Perhaps the biggest change for everyone is that pages should load faster.  We have moved to using the webpack system to bundle all of our javascript files into a single `runestone.js` file.  Pages used to grab more than 100 javascript and css files, but that has been reduced to just a few now.  This makes Runestone MUCH more interoperable with things like Markdown or vanilla html.  It was also a really good chance to clean up, refactor and modularize a lot of ugly javascript that had accumulated in the last 9 years!

For Authors
-----------

1. jUnit is now support for writing auto grade-able Java questions
2. catch.hpp is now supported for writing auto grade-able C++ questions
3. The python tutor support is upgraded to the latest version and supports writing embedded visualizations for Python, C, C++ and Java
4. Skulpt -- our in-browser version of Python supports all Python 3 syntax and lot more of Python3!  f-strings are even supported now! This will provide students with a much more consistent experience when moving
5. `.. datafile::` -- if you need data for your program or auxiliary cpp or java files for your programs you should use the datafile directive to provide them.  This will ensure that these files are available anywhere in the book, including assignments and the grading interface.
6. There is a video now that walks you through the process of getting runestone installed and ready to go if you want to write your own content.

For Instructors
---------------

1. The Runestone instructor interface has accumulated a lot of great changes in the last 9 months.  I attribute many of these changes to wonderful discussions I have had with teachers on the CSAwesome mailing list.
2. I have set up Google Groups for each book, with the goal of using these groups to develop communities of practice around each book.  There is a lot we can all learn from each other and share with each other.  These groups will also serve as the gatekeeper for access to instructor-only materials.  In particular both FOPP and HTTLADS have very highly developed instructor manuals now.


Summer is a great time to get involved
--------------------------------------

We have a lot of projects in the pipeline for this summer!  Including lots of great new content for you to use this Fall.  Here are some links to help you get started.

* Installing the `Runestone Components and building starter book <https://youtu.be/Fy0S4bGRPNE>`_
* Installing the `Runestone Server with Docker <https://youtu.be/y3oeBmRQVf0>`_
* A quick intro to a `Docker/Runestone Workflow <https://youtu.be/UtAj1lQLt5U>`_

We can use help writing unit tests for exercises, editing exercises, adding new features, whatever your interest there is sure to be a project for the common good that you can get involved with.  You don't need to be an expert, none of us were when we started, and we are happy to help get you up and running.

.. author:: default
.. categories:: none
.. tags:: none
.. comments::
