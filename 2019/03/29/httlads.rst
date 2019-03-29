Book Spotlight: How to Think like a Data Scientist
==================================================

.. author:: default
.. categories:: Books
.. tags:: none
.. comments::

It is said that the most important characteristic of a data scientist is curiosity.  So how do you structure a class that encourages students to be curious and ask questions of the data?  When I first taught DS-320 at Luther in 2017 I had to make it up as I went.  Luckily I had some great, and very patient students that were willing to go with it.  My main goal was to "let the data drive the learning!" My vision for the course was to pick some data sets, do exploratory data analysis on them, generate a bunch of questions as a class, and then figure out what we needed to know in order to answer our questions.  As a course, I thought this was an amazing and really fun way to structure the learning.  It doesn't lend itself to a structured day by day syllabus since you can't necessarily predict everything you are going to learn when you start!  But we learned a LOT in that class, and we had a lot of fun doing it.

Finding textbooks for undergraduate data science courses is really hard.  There is little agreement on curriculum at the undergrad level and definitely not much with a more liberal arts emphasis.  So, I was thrilled when the `Applied Computing Series <https://edu.google.com/computer-science/applied-computing-series/intensive.html>`_ team at Google asked me to take the lead on creating a book for their AC201 course.

This book is an attempt to build some structure around the approach described above, without totally killing the spontaneity of encouraging students to ask good questions of the data.  You are never going to find a data set to make everyone happy, but if you pick several data sets hopefully enough of them will interest enough students to keep everyone engaged.  In this text (so far) we look at World Happiness data, Movie Reviews, the CIA world factbook, United Nations speeches, Bike Rental data from Washington DC and shopping cart data from Instacart.

The learning objectives of the course are as follows:

* Articulate the data science processing pipeline
* Extract data using SQL
* Gather data from the Internet using web API's and screen scraping
* combine data from different sources
* Clean the data
* Handle missing data/finding outliers/fixing data
* Normalizing and rescaling data
* Visualize the data
* Translate questions to analysis and analysis to interesting stories
* Analyze data

  * Single variable regression, logistic regression
  * Market basket analysis
  * Cohort analysis
  * Sentiment analysis, exposure to Bayes Theorem
  * Time series
  * Geographic analysis
  * Simulations, Monte Carlo

* Understand statistical significance and how to test for it using practical simulation techniques.

You can see how the individual skills learned map onto different data sets and chapters by taking a look at `the preface <https://runestone.academy/runestone/static/httlads/index.html>`_

One of the big challenges of this was how to make the book interactive even while wanting students to install and run their own copy of a Jupyter notebook server.  The approach is to have the book lead the students through some analysis while asking them to do work in the notebook and bring answers back into the textbook.  For example use the notebook to find the busiest bike rental pickup point, and then paste the id of that station into a multiple choice question in the text.

Maybe at some point we'll have a way to embed Jupyter notebook cells into a Runestone text, but that will require a LOT more computing power.

In the meantime please take a look.  The book, as is, has been classroom tested in four schools this spring, but I think there is a lot more content that could be added, and the existing content still needs work to clean up.  So feel free to let us know about any issues on github.
