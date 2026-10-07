---
title: "Fall Semester Updates"
date: "2026-10-07"
slug: "fall_updates"
categories: ["Announce"]   # optional
# author: ["Guest Name"]     # optional; defaults to the site author
---

The fall semester is well underway, and I hope your classes are off to a great start! Back in August I said we were going to slow down and focus on polish and squashing bugs. We did a lot of that, and somehow we also managed to ship a few new things. About a dozen contributors have made more than 250 commits since the end of the summer. Here is a tour of the highlights.

## For Instructors

**The gradebook and grader** got a lot of attention. The gradebook is now part of the same React app as the grader, so moving between them feels seamless. Students with late work are highlighted in the grader, so you can find them without hunting. The manual grading view does a better job of displaying questions, and it has a new filter and toolbar so you can get to the work that still needs a grade. You can also see a student's work on a selectquestion, the grader remembers your page and how many rows per page you like, and the gradebook CSV export has the username column back. Rows are now labeled "Last, First" so the sort order makes sense.

**Grading got more trustworthy.** A few of these were bugs that could really bite you:

* The autograder will no longer overwrite a grade you entered by hand.
* Autograded scores are capped at the points the question is worth in the assignment. Before, a score earned somewhere the question was worth more could carry over. Grades you enter by hand are left alone, so extra credit still works.
* Deadline exceptions you give for "all assignments" now apply when you grade a single assignment.
* The accommodation form no longer loses extra days or time limits.
* Readings can now be scored when you regrade.

**LMS integration (LTI)** now pushes grades to your LMS when you release an assignment. If your LMS somehow gets out of sync you can now force a repush of grades even when they haven't changed. Grades you have not released yet stay private while you recompute.

**Assignments** have bulk edit actions on the assignment list, so you can change a bunch of assignments at once. The assignment builder shows chapter and subchapter numbers, and sorts exercises more sensibly when you add them while browsing the book. Assignment links will also no longer open in the wrong course if you teach more than one.

**Peer instruction** had a round of fixes, especially for async peer instruction. Visible/hidden dates are honored, the first vote stays visible after students vote a second time, and the chat no longer gets stuck trying to reconnect after a session expires.

**A new question editor.** You can now edit questions through a structured editing view, and the rendered question stays in sync as you make changes.

**Visualizations (new!)** We are starting a new set of instructor reports under `/dash/`. The first two show, for each question on a page of the book, how many students got it right on the first try, got it right after retrying, never got it right, or never tried it, along with an assignment progress view. This is the start of what I talked about in the spring: helping you see where your students are struggling. I would love to hear what you think, and what you would like to see next.

## For Students

**Accessibility** was the biggest area of work this fall. We worked toward the WCAG AA standard on all of our pages, fixing color contrast, focus indicators, and page structure. Then we went through the interactive components one by one: drag and drop, matching, multiple choice, Parsons problems (both kinds), clickable areas, fill in the blank, short answer, and activecode. Each one works better with a keyboard and a screen reader now. Math is read aloud properly, feedback is announced, and keyboard hints show up where you need them. Our VPAT has been updated to reflect all of this work.

Some smaller student-facing changes:

* Students get a friendly warning if they are in the book before the term starts, and the progress box at the bottom of each page has been rewritten.
* Your course name appears in the user menu, so it's easy to tell which course you are in.
* If a student types a course name when registering, that wins over a book they also picked, so they land in the right course.
* Icons that were showing up as words (like "menu") are fixed.
* CodeTailor's personalized Parsons problems handle indentation, comparison operators, and cloned courses correctly.

## Under the Hood

**Speed.** Early in the semester we had some slowdowns when lots of people were using Runestone at once. We fixed how the servers share database connections, and we sped up the assignment pages, the assessment results, and instructor pages. Things should feel snappier, especially at the start of class when everyone logs in at once.

**Security.** We did a security review of our servers and fixed several issues. We also strengthened password requirements.

**Problem reports** now include your email, and if you have a GitHub account you can file the report as yourself. Please keep sending them! The information they collect from your browser makes bugs much easier to track down.

## Thank You

Thanks again to everyone who contributed code, reported bugs, and tested new features this fall. A special thanks to the folks who worked on accessibility. That work makes Runestone better for every student. As always, if something isn't working, use the **Problem Report** option in the user menu and let us know.
