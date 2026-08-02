---
title: "Done with the big Changes for a while"
date: "2026-08-02"
slug: "july_updates"
# categories: ["Announce"]   # optional
# author: ["Guest Name"]     # optional; defaults to the site author
---

The school year int he northern hemisphere will be starting again before we know it!  So its a good time to celebrate our summer wins, and slow down the changes and focus on polish and squashing bugs!

I'm happy to say that after 15 years of working on Runestone we are now independent of our original web framework called web2py!  The web2py codebase has served us well, but it was also a bit of an anchor around our ankle.  From an instructors perspective everything is new.  Everything is hopefully a bit faster, and it is certainly easier to maintain the code we have now.  We have learned a lot about web development in this time!

The **gradebook** has been improved. You can now click on a score and get the student details. The **assignment builder** and **grading interface** have all had another great update.  

**Authentication** should be better than ever, since we don't have the web2py server around anymore we have a single authentication system and token.

Students will see some really nice improvments as well.  The course home page and the assignment pages now look like they are part of the textbook. Input for Python programs got a lot better, and a long standing bug for mixing input and output was squashed!  We have made a bunch of **accessibility** updates to the interactive widgets so we are better than ever in the a11y department.

## We left a few things behind

With progress sometimes you realize that there are things that you have added that are not used very much, or are out of date.  For us those things are:

* The **practice** feature. Although quite effective at improving grades people still didn't use it. (MOST people) I know there will be a few of you that are dissappointed.  We are looking at new opportunities to replace this.
* The **student progress dashboard** with the donut charts is gone.  There is a new assignment summary report that replaces this along with the chapter progress reports.  We will look for new ways to help instructors understand where their students are struggling.
* Books built with the old restructuredText authoring system are deprecated.  Most of our popular books have been moved to PreTeXt!  Please please use the new PreTeXt books.  Here's a quick guide for a few of the most widely used books.  You can see others in the library.

  * csawesome -> csawesome2
  * thinkcspy -> httlacs
  * py4e-int -> py4eint
  * pythonds -> pswadsup
  * fopp -> foppff

We'll be removing access to the old books probably over winter break.


## We need your help

Now, with all of these changes, we need your help to make sure everything is tip top so we can make a good impression on all the new students.  Please test and experiment with the new features.  If you find that something is broken please report the bug.  If you have a github account it would be great to use that.  But if you don't Please use the **Problem Report** menu option from the user menu.  Most of the bugs in Runestone need information from the browser and this new problem report form, includes all of that information, so even if you do have a github account it would be great if you selected that menu and then copied and pasted the info into the issue.

