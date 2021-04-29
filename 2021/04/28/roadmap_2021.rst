Runestone Roadmap 2021
======================

There is a lot going on in the Runestone world right now and I wanted to
let you in on the current roadmap for Runestone development. I’m doing
it now as summer is on the horizon and I know for many of you summer is
the one time of the year that you may be able to help with development!
More on that later. Here is what is on the Horizon for Runestone.

Roadmap Overview
----------------

.. contents:: 
    :depth: 3
    :backlinks: none

BookServer
----------

Although the web2py framework has served us well since 2011, I have
wanted for a long time to rewrite the core book server in Runestone
using modern web frameworks and technologies. This will allow us to
scale Runestone more elegantly and save us money as well! The Instructor
interface, which gets 10% of the traffic that the book server does will
stay on web2py until I or someone else finds the time to port it as
well. They will continue to work together just fine as they will share a
common database. The `BookServer
project <https://github.com/bnmnetp/BookServer>`__ is using a fully
async framework called FastAPI as well as SQLAlchemy for the database
work. It will be tightly integrated with the Runestone Components so
that you can easily spin up a server to serve a Runestone book on your
own infrastructure, With access to all your data in a sqlite database.
Production on Runestone Academy or another large installation will still
use Postgresql. This is the highest priority for me at the moment as I
don’t want to do any further student facing development on the old
server.

Funded Projects
---------------

There are several high priority projects that are being funded by NSF
money through colleagues like Barbara Ericson at the University of
Michigan, or the `SPLICE <https://cssplice.github.io>`__ project. Others
may be on the way… 

Support for Peer Instruction 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The peer instruction project is part of Barbara Ericson’s research at the University of
Michigan and has a two year timeline. 

1. Allow Runestone to ingest question banks from various projects so that we increase the number and
quality of questions available for instructors to assign. 

2. Integrate a discussion system into Runestone and the assignment system to allow
students to first answer questions and then discuss them with each other
synchronously or asynchronously before they answer the question again.
This is the heart of the Peer instruction model. 

3. Analytics for
selecting questions suitable for peer instruction. 

4. An instructor interface to allow an instructor to see and share aggregate information about how students are answering a particular question. 

5. Support for automatically pairing students for peer instruction. 

Publishing Anonymous Runestone Data 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is an ongoing project funded by the SPLICE
project. If you are interested in analytics or machine learning and how
we might improve the learning experience by applying machine learning to
Runestone books I have made available several datasets using the
`DataShop <https://pslcdatashop.web.cmu.edu>`__ system at Carnegie
Mellon University. Contact me for access to the data. 

Support for Large Online Courses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a project that is adding support for courses on
Coursera using Runestone as the underlying textbook and backend. And
includes a number of miscellaneous tasks. 

* Supporting the new toggle question. Given a particular coding problem allow a student to answer a series of hint problems (maybe even a parsons problem) to guide students that are struggling to a solution. Conversely many students would rather write code than drag parsons blocks around so in that case allow the student to simply write the code. 

* Improve the performance of the autograder and the student progress dashboard for large classes.

* Modify the assignment page interface to allow for a group of students to work together on an assignment. 

Smaller Projects
----------------

Change the Runestone Onboarding (Registration) Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Separate registration from adding a course. The flow should look more
like the following: 

1. Register for Runestone Academy. 
2. Are you an instructor? 

   #. Provide a bit more information so that we can verify that you are. 
   #. Here is an overview of the books we offer. Select one to create your course. 
   #. Guide you through the course creation process and give you some resources to make the most of Runestone. 

3. Are you a student? 

   1. If you are an independent learner here are some open courses you can join.
   2. If you are part of a course here is a nice interface to find the course by name and register for it.

Support for Custom Textbooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a feature than lots of people ask for, but I’ve never found a
scalable way to implement it... Until one day as I was registering Runestone on “Read the Docs”  it occurred to me that the readthedocs.org model would work perfectly well for Runestone!

This development effort would add webhooks for git and Runestone to
allow an instructor to Fork any of the Runestone textbooks (or create
their own) and link it to Runestone.Academy for hosting. When changes
are pushed to the forked textbook Runestone will automatically rebuild
and publish the book as a draft. The instructor can then choose when to
upgrade the draft to published using the instructor interface.

Even for instructors that do not want to get deeply into
restructuredText or python programming this would allow a book to be
customized using github’s web based editor. With rebuilds run
automatically it would allow authoring a book with no setup.

A somewhat related part of this project is to update our library page to
make it database driven. Right now we simply walk the directory of books
and rely on the presence of a ``conf.py`` file that we import. This is
error prone and does not allow us to distinguish books that should
remain private versus books that are available to create classes from,
etc. This part of the project would make the library page as well as the
course creation page database driven.

**Real time UPDATE** I just found out this project will be funded through a grant from Elliott Hauser at University of Texas at Austin !!  Elliott is the founder of `Trinket <https://trinket.io>`_ and a long time collaborator on the `Skulpt Project <https://skulpt.org>`_ used to power Python in the browser.

Editorial Interface for Editing and Updating Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As Runestone has grown and as more instructors gain experience and
confidence in using Runestone the size of our question bank has grown.
However my ability to manage all of these questions is far less than
what is needed. This project would build out an interface for volunteer
editors to clean up and remove bad questions as well as make slight
editorial updates to typos or unclear instructions.

Tag all Questions within a Taxonomy of Competencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the addition of the exam generator to Runestone we have a real need
to create a way of tagging questions with the various competencies that
they exercise or test for. This could be related to the editorial
interface, but another great suggestion is to crowd source this and have
students participate. This project would enhance the question interface
to allow students to tag/categorize key concepts for each question.
Ultimately editors may have to make the final decision, but it would be
a rich dataset to see what students think.

Enhance the Web Interface to allow Instructors to Publish Projects or Labs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although it is already possible to create coding exercises a number of
books are more project oriented. It would be great to allow instructors
to publish units of work that are larger than a single exercise but
smaller than an entire book. More like a project size unit that may
consist of text plus a number of exercises.

Convert Runestone output to XML (PreTeXt)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

My work with the `PreTeXt <https://pretextbook.org>`__ project has
brought several math books to Runestone. PreTeXt is an authoring system
that is primarily used for math books but also some others. It has the
advantage of allowing you to write once and choose several output
formats. Including PDFs, this is something that I get asked about all
the time. My usual answer is why would you want a pdf of an interactive
book? That just eliminates the interactivity! But the truth is there are
lots of situations where people want or need a pdf version **in addition
to** the interactive version. This is work that I’ll be at least
starting on at a workshop in late June hosted by the PreText Project.

Improve the Navigation of Runestone Books
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Make the main table of contents have collapsible headings
-  provide an omnipresent outline in a sidebar to allow for faster
   navigation to different parts of the book.

Upgrade LTI to Version 1.3
~~~~~~~~~~~~~~~~~~~~~~~~~~

Currently Runestone supports LTI 1.1, the future is 1.3. Anyone who
would like to take ownership of Runestone’s LTI integration is more than
welcome to do so. Since I do not use an LMS as part of my daily work
anymore I have little motivation to work on this.  More work is also needed to
verify and document how to use LTI with other LMS systems (besides Canvas and Moodle)

Template Questions
~~~~~~~~~~~~~~~~~~

We have a prototype of a fill in the blank questions that would allow you to 
write a question where every student would get the question but it would be
slightly different.  For example you might want to write a question like What is X + Y? where each student would get a different X and Y chosen from a range of integers.  The question would be smart enough to use a computed answer based on the X and Y given to each student.  We would also like to expand this concept to multiple choice questions.  Not only is this great for exams and keeping students from cheating but it also gives the students more practice as they could see a different version of the same problem each time they refresh the page.

Blockly on Runestone
--------------------

Thanks to the authors of the amazing Mobile CSP curriculum and book (coming to Runestone for Fall 2021) and the hard work of Ralph Morelli we will have a great addition to the runestone library, and the ability to use blockly in your textbooks.  I think this is awesome for beginners and I've always wanted to update The How to Think Like a Computer Scientist (HTTLACS) book to illustrate each new programming construct in Blockly first.  I think this is a really cool way to give students a visual understanding of loops and conditionals before they see the syntax.

As is usually the case with all things Runestone we start small, and then iterate, so if you are into blockly and would like to help evolve this new component (which goes by quizly in the source) we would love to have your help.

Fixing Bugs and Even Smaller Projects
-------------------------------------

Many small coding projects are available on Runestone and are identified
as issues. These issues are all typically tagged with the “Good First
Issue” and or “Help Wanted” tags. I try to identify these projects this
way because they are good starter projects that can get you into the
Runestone system. See 

* Runestone Server Projects - `Good First Issue <https://github.com/RunestoneInteractive/RunestoneServer/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22>`__
* Runestone Component Projects - `Good First Issue <https://github.com/RunestoneInteractive/RunestoneComponents/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22>`__

Video Production Anyone?
------------------------

The YouTube videos that accompany the HTTLACS book are very popular on YouTube, but I consistently get complaints about their resolution.  Unfortunately the original recordings are 8 years old at least, and have been lost through many migrations of computers.  They also feature version 0.1 of Runestone so that pages don't match at all anymore.  My new years resolution for 2021 was to work on one of these a week.  So far we are at week 17 of 2021 and I have redone exactly 0 videos.  If you would like to try your hand at re-recording any of these I would love it!  You can just take the transcript of an existing video and work your way through it.

How You Can Help
----------------

Runestone is an Open Source project. Everything on Runestone is freely
available as part of our `Github Organization <https://github.com/RunestoneInteractive>`__. Summer may be
a good time for you to help hack on something, test something, or write
something!  I would be happy to have help on any and all projects.  Funded or not it does not matter to me.  I only point out the funded projects to show how awesome it is that some big partners have put their faith and money behind Runestone to keep it sustainable.

You do not have to be an expert coder to help out. We welcome people of
all abilities to our community and would be grateful for your help.

Another way you can provide coding help to Runestone is to consider us
as an option for a student capstone project. We have had great success
in working with students at Berea college and other colleges that have
adopted Runestone for their capstone course. Many of the projects
identified above would be great as capstone projects for a group of
students. The students really love, especially if they have benefitted
from using a Runestone book as part of their education. This is a
pathway for them to give back to a project that has helped them.

Another way you can help is to talk to encourage your department to budget 
some money to help support Runestone.  I've heard from a number of instructors 
this spring asking about this, and I'm very grateful.  We are happy to send 
an invoice for whatever amount you decide.  Other departments have decided
to charge a lab fee of $10.00 for the course, and have designated part or all 
of the per student lab fee to go to Runestone.  We are happy to work with you
on billing and payment!

.. author:: default
.. categories:: Development
.. tags:: none
.. comments::
