A Lab in Three Easy Steps
=========================

.. author:: default
.. categories:: How-To
.. tags:: none
.. comments::


This weeks post is an update of a post that has been continually one of the most popular on my `Personal Blog <http://reputablejournal.com>`_ So I thought it would be good to update it a bit and publish it here.  These instructions can be used to create a lab or any kind of in-class activity that you want to use with your students.  Its a good "Getting Started with Runestone" tutorial.


Getting Started
---------------

The major steps in getting started are

* Installing Python
* Installing the Runestone Components
* Building your first lab

Install Python
~~~~~~~~~~~~~~

1.  If you are on a Mac you are already done with this step.
2.  If you are on Windows you will need to go to `Python.org <http://python.org>`_

If you are an advanced Python user you may want to may want to create a `virtualenvironment` for this project but it is not a requirement.

If you are on Windows you may want to edit your PATH environment variable following the instructions `here <https://docs.python.org/3.7/using/windows.html>`_.  Again, Mac users can ignore this.

Installing the Runestone Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You are going to need to use the command line for the rest of this tutorial, so start up a `terminal <http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line>`_   (/Applications/Utilities/Terminal) on macOS  or run `Powershell <http://www.tomshardware.co.uk/faq/id-1656450/windows-powershell-feature.html>`_ or cmd.exe on Windows)  I will repeat myself here.  These commands need to be run from the command line, **not** from the Python shell.

Run the ``pip`` command

.. code-block:: bash

    $ pip install runestone

Or on Windows if you have not modified  your PATH try:

    C:\\Python34\Scripts\pip.exe install runestone

From now on I'm only going to give the Mac way of running the commands.  If you are on windows you will need to add `C:\\Python34\Scripts` to the beginning of the command and add `.exe` to the end.

You can watch as a lot of text goes scrolling by.  But as long as you don't get any errors you should be good to go.  You only need to do these first two steps once.  Once you have installed Python and Runestone you will not have to do it again.

Starting your first Runestone Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is a session of me on my computer creating a simple project.

.. code-block:: bash

    $ mkdir mynewproject
    $ cd mynewproject
    $ runestone init

    This will create a new Runestone project in your current directory.
    Do you want to proceed?  [Y/n]: y
    Next we need to gather a few pieces of information to create your configuration files
    Project name: (one word, no spaces): MyLab
    Path to build dir  [./build]:
    Path to deploy built site  [../../static]:
    Use Runestone Web Services  (true, false) [false]:
    Your Name  [bradleymiller]:
    Title for this project  [Runestone Default]: My First Lab
    Use Simple Python3 Semantics  [false]: true
    Default ActiveCode language [python]:
    Enable inline Activecode downloads by default (single activecode downloads may be enabled with the :enabledownload: flag) [false]:
    Done. Type runestone build to build your project

You should answer no to using the Runestone services as at this point you are just making a static page with no ability to capture and store data about your students.  You can write Runestone labs for lots of languages, including C++ and Java but Python, Javascript, and HTML are the only languages supported directly in the browser.

At this point you will have the following files and folders:

.. code-block:: bash

    mynewproject/
            _static/
            _sources
            _templates
            build
            conf.py
            pavement.py

* The ``_static`` folder is for things like images or Javascript files.
* The ``_sources`` folder is where you will put your own writing.  To start with there are a couple of example files for you.
* The ``_templates`` folder is for styling.  There is a default set of templates that match the Runestone interactive look and feel.  That is a good thing to start with.  Once you become more familiar with the system you may want to customize the templates or even make your own.
* The ``conf.py`` file is used by Sphinx, and contains information from some of the questions you answered when you initialized your project.
* The ``pavement.py`` file is used for building and setting build parameters.

All of these files are important, and you should not delete any of them.

Next run ``runestone build``  This command will create a build/mynewproject folder with an index.html file in it.  If you want you can now run ``runestone serve`` and then go to your browser and open up the following URL  ``http://localhost:8000/index.html``   Yay!  You have a webpage.  Feel free to explore a bit to get an idea about some of the components you can use in your lab.

Writing your Own Lab
~~~~~~~~~~~~~~~~~~~~

OK, lets edit  `_sources/index.rst`   Initially it looks like this:

.. code-block:: rst

    =====================
    This Is A New Project
    =====================


    SECTION 1: Introduction
    :::::::::::::::::::::::

    Congratulations!   If you can see this file you have probably successfully run the ``runestone init`` command.  If you are looking at this as a source file you should now run ``runestone build``  to generate html files.   Once you have run the build command you can run ``runestone serve`` and then view this in your browser at ``http://localhost:8000``

    This is just a sample of what you can do.  The index.rst file is the table of contents for your entire project.  You can put all of your writing in the index, or as you will see in the following section you can include additional rst files.  those files may even be in subdirectories that you can reference using a relative path.

    The overview section, which follows is an ideal section to look at both online and at the source.  It is pretty easy to see how to write using any of the interactive features just by looking at the examples in ``overview.rst``


    SECTION 2: An Overview of the extensions
    ::::::::::::::::::::::::::::::::::::::::

    .. toctree::
       :maxdepth: 2

       overview.rst


    SECTION 2: Add more stuff here
    ::::::::::::::::::::::::::::::

    You can add more stuff here.


If you are not familiar with markup languages, this file should still be quite readable to you, and you can probably easily guess what most things do.  Runestone uses a markup language called restructuredText.  There is a very nice, short tutorial `here <http://getnikola.com/quickstart.html>`_.  But maybe the most important reminder is that restructuredText is like Python, **indentation matters**. 😀

To give you an idea of what you see in the example above,  the section that starts with `.. toctree::` is called a directive and it creates a table of contents for you.  the `maxdepth` part sets the table of contents to show sections and subsections.  And the line with `overview.rst` indicates that it is a file that should be included in the overall  web page.  More on all of this later. Our first task is simply going to be to wipe everything out, and start over.   Using a plain text editor change index.rst to look like this:

.. code-block:: rst

    =============
    My Sample Lab
    =============

    Part 1: Turtle Graphics
    =======================

    In this section we will do the following:

    * Create a turtle
    * Make the turtle draw a box

    .. activecode:: turtle1

       import turtle

       timmy = turtle.Turtle()
       for i in range(4):
           timmy.forward(100)
           timmy.right(90)


    Now it is your turn.  Can you modify the program to make timmy draw an octagon instead of a square?

Now save the file and rerun the ``runestone build`` command.  Everything should build without a problem and you can now run ``runestone serve`` and open up ``http://localhost:8000`` from your browser.  Notice that you can change the program and rerun it right from your browser.

It is probably obvious that you can create headings and subheadings.  Unordered lists are created using ``*`` and the runnable code examples are created by the ``.. activecode::``  directive. The name turtle1 must be unique on the webpage, other than that it is not used for too much at this point.  The rest of the activecode directive contains plain old python code, but it must be indented to line up with the ``a`` in ``activecode.``  All indented lines are included as the body of the activecode directive, regular text processing starts at the first unindented line.

There you have it.  You have created a very nice little lesson without a lot of hassle.  The Runestone and Sphinx tools take care of all of the formatting for you!

Documentation
~~~~~~~~~~~~~

There are lots of resources to help you with writing resources with Runestone.

* `Runestone Overview <https://runestone.academy/runestone/static/overview/overview.html>`_
* `The Authors Guide <https://runestone.academy/runestone/static/authorguide/index.html>`_
* Using the ``runestone doc`` command.  Runestone has some basic documentation built right into the command. ``runestone doc --list`` gives you a list of all of the various components.  You can guess what they do from the name pretty well.

.. code-block:: bash

    $ runestone doc --list
    Runestone Directives List
        activecode
        clickablearea
        codelens
        datafile
        disqus
        dragndrop
        fillintheblank
        mchoice
        parsonsprob
        poll
        qnum
        reveal
        shortanswer
        showeval
        tab
        tabbed
        timed
        usageassignment
        video
        vimeo
        youtube

To get the detailed Syntax and options for any of the components you can run ``runestone doc <componentname>``

.. code-block:: console

    runestone doc fillintheblank

        .. fillintheblank:: some_unique_id_here

            Complete the sentence: |blank| had a |blank| lamb. One plus one is: (note that if there aren't enough blanks for the feedback given, they're added to the end of the problem. So, we don't **need** to specify a blank here.)

            -   :Mary: Is the correct answer.
                :Sue: Is wrong.
                :x: Try again. (Note: the last item of feedback matches anything, regardless of the string it's given.)
            -   :little: That's right.
                :.*: Nope.
            -   :2: Right on! Numbers can be given in decimal, hex (0x10 == 16), octal (0o10 == 8), binary (0b10 == 2), or using scientific notation (1e1 == 10), both here and by the user when answering the question.
                :2 1: Close.... (The second number is a tolerance, so this matches 1 or 3.)
                :x: Nope. (As earlier, this matches anything.)

        config values (conf.py):

        - fitb_div_class - custom CSS class of the component's outermost div


Giving Students Browser Access to the Lab
-----------------------------------------

At this point the build folder has a static webpage that you can upload to any web server.  If you have your own webpage hosted on a school server that you normally use for class you can make your Lab available to the students by simply taking the folder `mynewproject` inside the `build` folder and putting that on your website.  The folder is self contained and can be hosted on any web server.

If you know the IP Address of your own computer and you simply want to give let students bring up the webpage from your computer you can do that too.  For example, lets suppose you know that your IP address is `10.0.0.23`  Your students can get everything they need from `http://10.0.0.23:8000/index.html`

In another post, I'll cover how to host your lab using Github pages.

If you have questions or comments on getting going, please leave them below, or join our community on Slack or our Google Group.  You'll find links to these resources on our `Support Page </pages/support.html>`_
