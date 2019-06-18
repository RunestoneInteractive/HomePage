SQL
===

Today, I built something I've been wanting to add to Runestone for several years.  I added support for the SQL language.  I've been holding off on adding support for it, because I thought I was going to have to support SQL as a server side language rather than in the browser.  This means a lot of thinking about security, and making sure that one student can't wipe out the data in a test database for all students, and setting up accounts, etc.  Every time I've taught introduction to SQL we get to that point in the semester where I know I have to keep a close eye on the server as students begin to write bad cartesian products and create result sets with millions of rows!  This effectively slows down or stops the database engine for the entire class.

However, last week, as I was thinking about it again I stumbled across the `SQL.js project <https://github.com/kripken/sql.js>`_  This project takes the `SQLite <https://www.sqlite.org/index.html>`_ C code, and compiles it to `Webassembly <https://webassembly.org>`_.  Thus making it possible to run an authentic version of SQLite in the browser!  SQLite is a good tool for teaching as it is lightweight, comes with Python, and runs small databases directly in memory.

From a teaching perspective this really simplifies things a lot! Now each student has their own copy of a database that I can distribute to them over the Internet. Students can't mess upanyone else's results or hang the server. If they really do mess up a query they just need to reload the page.  In addition, this also means that I can add autograding of SQL queries.  As I begin to work on my Web Development course for next fall, and we begin to revise our intro to data science course, having SQL in the browser is going to be a game changer!

Its available today in the github version of Runestone.

Stay tuned.


.. author:: default
.. categories:: Announce, Development
.. tags:: none
.. comments::
