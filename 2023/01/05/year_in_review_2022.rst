Year in Review 2022
===================

With the year 2022 in the rear view mirror I wanted to take some time to update you all on what we have accomplished in the last year, give you some fun facts, a financial update, and talk about the community in general.  So lets get to it!

Fun Facts
---------

During 2022 we welcomed 74,000 registered students and instructors to the community!  That is a lot of new people and a lot of money saved on textbooks!  During an average school day we have around 1000 students active during a given five minute period.  I think that is something we can leverage moving forward.  The traffic on Runestone clearly shows that we have a "homework bump" that is once the traffic slows down at the end of the school day across North America, we have an evening spike that lasts three to four hours.   We have no such spike on Friday nights.  Also, students do not do homework on Saturdays.  In 2022 we had 115,100,000 page views!  That is nearly double the number of page views from 2021.  About 60% of the page views are from registered users while the other 40% come from searches through Google, Bing, and others.

What makes Runestone Academy Tick?
----------------------------------

People, 100's of people who donate their time in many ways.

* **Authors** -- between PreTeXt and Runestone we probably have around 60 different authors represented on Runestone Academy.
* **Developers** -- Over the years around 100 developers have contributed at least one line of code to Runestone, and around 50 developers have contributed at least one line of code to PreTeXt.  Over the years this job has become more difficult as the complexity of the whole system increases.  I am aware of this and actively trying to find ways to make it easier for anyone to help with development.
* **Dev Ops** - Monitoring the servers, building, testing and deploying updates, to our servers, building, updating and deploying updates to the textbooks, are all things that happen weekly.  It takes time, although a lot of that time is just keeping an eye on things while they run in the background.  For example it takes about 4 hours to rebuild and deploy all of the books on Runestone Academy.  Its mostly automated but you have to keep an eye on it for those few times when something goes wrong.  It takes another 30 minutes or so to rebuild and deploy all of our servers.
* **Bug Finders** - Reporting problems to us is equally as important as writing code!  I am always surprised by the number of people who just live with a bug instead of reporting it to us on github.   PreTeXt is tracking 1242 issues while Runestone is tracking 2216.  Of course those numbers are obsolete the moment I type them.  Issues come in all forms and we welcome reports of typos as well as serious bugs in the Runestone servers.
* **Exercise Creators** - Over the years the question bank for Runestone has grown by leaps and bounds - over 14,000 questions not including those that are part of a book.  This is a great way to learn a little about restructuredText or soon PreTeXt and contribute to the whole.  If you have a good exercise please feel free to add it through the web interface.  You can keep it private if you wish or you can share it with all the other instructors out there looking for new homework problems.
* **Exercise Editors** - With the huge growth in the size of the question bank, we have created quite a problem for ourselves.  Many of these questions are just dummy questions that instructors use to learn and should be weeded out.  Anyone can help with this problem by flagging a bad question.  This puts it in the queue for an editor to take a look at and either delete or update.  We need loads more exercise editors!
* **Community Builders** - Do you know what makes for the most successful textbooks on Runestone?  It is an active and supportive community of teachers using that book.  The best case in point for that is CSAwesome.  It truly is awesome the way teachers help and support each other on the mailing list.  But that takes some effort and leadership to nurture Beryl Hoffman and the people at the Center for Computer Science Education do a wonderful job. We need more of that for all of our books!
* **Documentation Writers and Trainers** - Have you gotten pretty good at some aspect of Runestone?  How about taking a look at the documentation and bringing it up to date, or making it easier to understand?  By now I've lost all perspective of what it is like to be a newcomer to Runestone, but many of you have not.  Would you like to host a workshop to train people how to use Runestone?  We would be happy to support that!
* **Word Spreaders** - If you like Runestone or any of its books please help us spread the word.  We would love to have everyone recommend Runestone and PreTeXt  to two colleagues.  We would love to have everyone mention Runestone and PreTeXt on social media.  Do you  Write a blog?  Toot on Mastadon?    Post on Facebook?  Tweet on twitter?  How about a shout out?  I have left both Facebook and Twitter but if someone would like to take over the FB page or the iRunestone account on twitter let me know!  Anybody can help with this and the more we grow our community the more good ideas we get.

Accomplishments in 2022
-----------------------

New Server Architecture
~~~~~~~~~~~~~~~~~~~~~~~

Looking back at it now, I have to agree that 2022 started off a little bit rocky.  We moved to a brand new server architecture, and a brand new server to handle the majority of the book serving traffic.  After a month or so of headaches things calmed down, and I'm super pleased with the new architecture.  It allows us to scale horizontally as our traffic ebbs and flows over the course of the year.  There is much more to be done in this area, but we will do our best to make it as seamless as possible.

The PreTeXt Partnership
~~~~~~~~~~~~~~~~~~~~~~~

During the Summer of 2022 a lot of work that has been going on since just before the global pandemic took hold really began to pay off.  The partnership with the PreTeXt project allows me to focus more on the server and interactive widgets for learning, while freeing me from maintaining and improving an authoring language.  We converted our first books from restructuredText to PreTeXt and in the words of Billy Crystal  "they look mahhhhhvelous!"  My hope is that we can transition the rest of the books during 2023.  As we master the conversion process we will also be able to make PDF, Braille, ePub and other formats of our interactive books available.  Though of course they will not be interactive.

I'm also really excited to see that a number of the Mathematics authors have embraced the interactive elements that Runestone brings to the table in writing their textbooks.   Parson's problems for doing proofs or derivations anyone?

The Launch of Peer Instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

During the winter of 2022 we piloted our new peer instruction system, this was followed by a workshop attended by about 20 instructors who used peer instruction in their classroom during the Fall of 2022.  This is a very exciting new feature that you can use to replace clickers in your classroom and which also works well in the virtual classroom.  This work was funded by the NSF and led by Dr. Barbara Ericson at the University of Michigan.

The Launch of the Author Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every year I hear from a handful or more of instructors that want to customize one of our books for the classroom.  While making that easy for everyone is still a ways off we took our first steps in enabling that by creating a server just for authors.  The server allows you to start with a brand new book, or with the fork of an existing book on github and gives you control over when the book is updated and published either publicly or privately.  A few brave authors have been using it for the 2022 fall term and it has worked quite well.  This server also has the beginnings of what I am calling an **impact report**, that is, as an author you will be able to track the usage of your book, and understand what parts of your book are used the most.  We look forward to working with authors to see how we can expand this out to provide much finer grained information on individual questions and other features.

Micro-Parsons
~~~~~~~~~~~~~

Formerly known as horizontal parsons, this new interactive question type allows you to create a parsons problem for an individual expression or statement.  This is great for teaching SQL or regular expressions, or even helping students work through some trickier kinds of expressions that you might write in Java or Python.  The new Micro parsons are also leading the way in terms of allowing parsons problems to be graded by unit tests in addition to simple block order.

Joint Runestone - PreTeXt Workshop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In June of 2022 we held our first joint workshop, where we brought together about 20 authors and developers from the PreTeXt and Runestone projects.  The workshop was held in Ann Arbor on the University of Michigan campus and it was an amazing week of learning together, sharing research, and brainstorming ideas for the future.  I'm so excited about where this could all lead.

NSF POSE Grant
~~~~~~~~~~~~~~

We were honored to receive a grant for the project we call `**PROSE** <https://prose.runestone.academy>`_ - PreTeXt Runestone Open Ecosystem.  This NSF grant is designed to help projects like our become a sustainable ecosystem.  For us that means many things:  recruiting community managers, developers, authors, editors, question bank maintainers, and more.  It also means reaching out other projects to see how we can work together more effectively and efficiently.  There are so many projects that are part of the "Ed Tech" world and there is so much needless duplication of effort.  The marriage of PreTeXt and Runestone demonstrates that two projects can come together and be more efficient and stronger when we work together, we want to spread that message and find other projects who share our vision and are willing to join us.  Another big part of this grant is to help us figure out how to organize and maintain all that we do going forward.  In a world where anything can happen, we need procedures and people in place if something horrible were to happen.

Finances
--------

In late 2021 Runestone Academy LTD was formed as a new corporation to supplant Runestone Interactive.  We are operating Runestone Academy as a non-profit.    Although the conversion process took a lot longer than expected Runestone Academy has also filed our paperwork to get IRS approval as a 501(c)(3) which will give us official non-profit status for tax purposes.  We have also named a board of directors to help us think strategically about how we ensure a strong future for Runestone.  I am honored to have this group of forward thinking people help guide the way:  Paul Resnick, Assoc. Dean of the University of Michigan School of Information, David Farmer of the American Institute of Mathematics, Susan Rodger, former President of SIGCSE and of Duke University, Danny Fenjves former founder and CEO of Upperline code  now leads the LEARN team at Giant Machines and Jane Miller our CFO and Secretary/Treasurer who has been a partner in my crazy endeavors for the majority of my life.

The financial details of any transition year can be confusing, especially when trying to compare to a past year, so lets just focus on 2022 and mostly not try to compare to last year.

These are unofficial numbers but they should be pretty accurate.  We have several different sources of income including students, schools, ads, partner support from people who use Runestone for their own purposes but want to support our work, Grant money, and consulting work on grants.  Here is how that all breaks down.

.. csv-table:: **Income**
    :header: Source, Amount

    Direct support from students, "$10,000"
    "Support from institutions (departments, colleges, schools)",  "$17,000"
    Advertising Income, "$16,500"
    Support from Grants,  "$11,250"
    Support from partners,  "$2,400"
    Webwork income, "$23,300"
    Other, "$3,000"

    **Total**,   "$83,450"

.. csv-table:: **Expenses**
    :header: Expense, Amount

    Hosting and server costs,  "$8,800"
    Webwork expenses, "$15,500"
    Legal fees, "$9,725"
    Credit card and Paypal fees, "$900.00"
    Travel,  "$1,800"
    "People costs (healthcare, salary, etc)",  "$44,600"
    **Total**,  "$81,325"

So, you might think that we have a net profit of about $2,000 which would be great for a non-profit, everything balances. But let me point out a few problems with that conclusion.

1. People costs -- $44,607 includes 1 full time person and 1 part time person. Thats not a very good salary.
2. Support from institutions is what we have **Invoiced** for $17,195 Unfortunately we have been paid only $12,165 of that.  People will often ask for an invoice and then completely ignore the invoice and our followup emails.  This makes it hard for us to plan and count on that money.

In 2023 we have and will institute a couple of changes.

1. If you school wants Runestone Academy to sign a contract or data privacy agreement we will invoice the school for $100.
2. During the first part of the year we will be working on determining a small set of features will will require payment.  None of the paid for features would prevent you from using Runestone for free.  These are all features that are nice to have, but provide good backup for why you could pay to support Runestone.  I know that many public schools have policies that don't allow you to "donate" so by providing a few features that you can only use if you pay turns that donation into a fee for service.

Runestone Academy is not a big corporation.  The two employees mentioned are myself and my wife.  As I made clear above, Runestone is powered by volunteers.  The Runestone community has accomplished a LOT on very little over the last 10 years.  The challenge is to sustain that progress and spirit in an ever changing world.

Conclusions
-----------

This past fall I ran a survey for the instructors who use Runestone Academy, I learned a lot from the survey that will help us set a course to smooth out some of the rough edges of the Runestone platform.  But even more than that was the outpouring of support for the mission.  So many people have come to rely on using Runestone Academy in their classrooms every day, and so many people said that love it!  That kind of feedback is really energizing and makes me want to work hard to keep building and improving things.

Our mission is expanding, Democratizing textbooks for the 21st century is only part of what we do now.  An updated mission statement might read as follows:

>To enable authors and researchers to maximize the accessibility of open educational resources for learners, and advance the teaching of STEM fields.

As with any mission statement it needs a bit of unpacking.  *Accessibility* is the practice of making information, activities, and/or environments sensible, meaningful, and usable for as many people as possible.  And the goal is to create a virtuous circle of feedback that drives progress for our four major stakeholders:  learners, researchers, authors, and teachers.

It is worth repeating... we can use your help!  If you or your school can join the project by supporting us financially that would be awesome.  But beyond that we want YOU to become an active participant in our community in any of the ways I mentioned above.

.. author:: default
.. categories:: none
.. tags:: none
.. comments::
