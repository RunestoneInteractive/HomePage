Summer 2022
===========

Summer time is often when instructors of all kinds can help out with Runestone Development.  Since June marks the beginning of summer I thought I would highlight what is on my list for development list for the next few months.  If something sounds interesting to you then please get in touch!


PreTeXt 
-------

PreTeXt is now the official authoring language for Runestone.  There are a host of reasons why this makes sense, and I've written about them before.  It has taken some time but we have finally arrived in a place where it is a reality.  I have converted our first Runestone book ever How to Think Like a Computer Scientist to PreTeXt and Rob Beezer has added markup to support our interactive elements.  This is a huge step forward and we now begin a process of converting our current books.  Like any conversion process it is not 100% so each book is going to take some manual work to perfect the conversion.

* select questions
* toggle questions + A/B testing 
	* I think the correct way to do this moving forward is to make toggles tasks and have Runestone show the tasks as dropdown

* Convert select books to PreTeXt for Fall 2022
* Build APEX Calculus for Runestone
* Build ORCCA for Runestone
* Build Yoshiwara's Algebra book for Runestone
* Finish up the SAGE Cell integration
* Jaas - Jing as a service - Jing is a validator for PreTeXt
* Make a PR to store traces with a hash of the input.

  
Peer + Grant Work
-----------------

This work is funded by an NSF Grant for Barb Ericson at the University of Michigan.

* Grading - 2 interaction Qs plus chat (maybe) - update autograder 
* Add async peer instruction page
* Get tags working with question bank searching - what we really want is prereqs and reqs - add to web UI and make use of some taxonomy - someone please give me a taxonomy!

Automatically Create Parsons problems
-------------------------------------

This work is also funded by an NSF Grant for Barb Ericson!

* Get Overcode working in python3 - this may also be a good task for Celery
* Generate parson's problems from the selected

Github Integration for Custom books
-----------------------------------

This work is funded by a grant from Elliot Houser and UT Austin.

* Add simple interface to connect a Repository 
* Add simple interface to publish draft/published
* Integrate the web hooks to auto build when pushed - this may be a separate server


Runestone Internal Projects
---------------------------

* Updates to student progress page - replacing d3 stuff with pandas
* Allow instructors to download LARGE classes on their own - using a celery task with an email followup - maybe create a special role for trusted teachers / researchers to allow them access
	* celery could also be used to do build on demand of Runestone / PreTeXt books

* Finish redoing the login process
* prototype an author/researcher dashboard
* Convert other books
* Does PreTeXt support hidden pages?  Somehow we will need a workaround for how barb has been adding problems to the database but not on a page that is linked to a TOC
* Create a bibtex file with references and generate a web page of references from that.


.. author:: default
.. categories:: Developement
.. tags:: none
.. comments::
