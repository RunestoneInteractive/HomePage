A Practical Introduction to Databases
=====================================

I am pleased to announce the availability of the new textbook `A Practical Introduction to Databases <https://runestone.academy/ns/books/published/practical_db/index.html>`_ on Runestone Academy (book id: **practical_db**).  The purpose of this book is to provide a free, open textbook on material of practical interest for students going into computing professions.  The text at present is suitable as the core of an introductory course on databases, and may also find use as a gentle introduction to the topic in more advanced courses on databases, web applications, or software engineering.

In this first release, the book covers three core topics: SQL, data modeling, and relational database theory.

SQL
---

The chapters on SQL (part 1 of the book) take full advantage of the Runestone platform to provide live, interactive examples with a real database.  Students can see the examples in action, test themselves on the challenge questions, and experiment with querying the provided tables.  As the database is an in-memory copy that is replaced whenever the browser page refreshes, students can freely try out data modification and DDL statements.

For students or instructors who wish to use something other than the SQLite engine built into Runestone (perhaps wanting more persistence), scripts are provided to create the book's database in PostgreSQL, MySQL, Oracle, and SQL Server.  The text also gives appropriate guidance for these systems where they differ from the SQL used in the book's examples; an appendix provides a SQL reference that similarly supports these systems.

SQL coverage includes: basic SELECT, INSERT, UPDATE, DELETE; joins (both explicit and implicit); data types and DDL (CREATE TABLE); keys & constraints; subqueries; grouping and aggregation; and set operations.  The chapter on joins includes coverage of one-to-one, one-to-many, and many-to-many relationships and their typical implementations (e.g., cross-reference tables).  There is also a very brief explanation of views, CTEs, and window functions.

Data modeling and theory
------------------------

Part 2 of the book covers ERD (Chen notation) and translation of the ERD into a relational database, with a complete worked example.  Crow's foot notation and other alternatives are also covered.

The third part of the book covers the relational model, relational algebra, and normalization (through 4NF), and has a short chapter on the differences between the relational model in theory and as implemented in SQL.

Future work
-----------

Future releases are planned, covering software programming with databases, NoSQL, and other topics of practical interest, and some expansion of existing topics.  The book is licensed under a Creative Commons (CC BY-SA 4.0) license.  The github repo is public (https://github.com/cpainterwakefield/practical_db_textbook), please feel free to fork and adapt as per the license terms.  Suggestions, corrections, and pull requests are all welcome!

Christopher Painter-Wakefield, Colorado School of Mines
``cpainter@mines.edu``

.. author:: Christopher Painter-Wakefield
.. categories:: Announce, Book
.. tags:: none
.. comments::
