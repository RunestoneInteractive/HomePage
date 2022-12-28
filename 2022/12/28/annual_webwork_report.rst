Annual WeBWorK report
=====================

Last year we posted a `report <https://blog.runestone.academy/2021/12/13/annual_webwork_report.html>`_ on Runestone's WeBWorK hosting project over the year 2021. Now as 2022 comes to a close, we post a similar report.


Facts and Figures
-----------------

Over the terms and semesters of 2022, Runestone's WeBWorK hosting service has supported:

- 65 institutions in 6 countries (59 higher ed and 6 secondary)
- 242 individual sections

Our revenue from this service was $22,660. We spent it as follows:
- $8140 for Alex and backup admin
- $3260 for WeBWorK code developer
- $2844 operational expenses
- $2379 taxes
- $3018 transferred to The WeBWorK Project
- $3018 retained by Runestone

In last year's report I hoped these last numbers would raise to $4000 for 2022, but we fell short of that. We made no real effort to advertise this service this year, and that is evident in the low growth from 62 institutions to 65. In the coming year, we will make more of an effort to advertise the service. New features in new versions of WeBWorK (currently 2.17, and 2.18 by summer) shouls also help attract new users.


New Server and Versions
-----------------------

Starting with courses for 2023, Runestone WeBWorK hosting is on a new server at webwork-hosting.runestone.academy. This server is currently runninig WeBWorK 2.17, and it will be upgraded to 2.18 over the summer. Keeping this service using the latest version of WeBWorK is important to us. WeBWorK developers work hard to improve the experience of faculty and students with each new version, and it is a shame when users don't have access to those latest improvements.

The old server at webwork.runestone.academy will then have the sole function of supporting Runestone's primary service, hosting interactive textbooks. Those textbooks with embedded WeBWorK exercises will be relying on this server.


Pricing
-------

Secondary school pricing continues to cost a simple $100 per course. And for secondary schools, it will not matter how many students are enrolled in a course. All we ask is that separate courses be separate courses. For example, please do not manage a calculus course and an algebra course from the same WeBWorK course.

For higher ed, beginning Fall 2022 we changed pricing to be $120 per course, with every 6th course free. For schools with many WeBWorK courses, it is still an average of $100 per course. This pricing will remain in effect until at least Fall 2024. However, we have identified a need to redefine what constitutes a "course" more carefully.

When we started this service, we had in mind that each "course" would correspond to a section of up to around 30 students. But not all schools operate that way. A school may have hundreds of students enrolled in the same section, especially if it is an asynchronous online course, a lecture hall course, or an emporium model course. These latter two (especially the emporium model) are problematic for us because they lead to a large number of students accessing our server simultaneously. This causes spikes in server resource utilization that impact WeBWorK's responsiveness for all users at certain times of day. WeBWorK is not yet designed to scale well (although changes are in the works) and this can be a real problem for users. Until an expansive coding overhaul is complete, the only way to deal with this is to spend more on cloud computing resources, or prevent that kind of usage in the first place. But we don't want to deny anyone the service if we don't have to. Only a handful of our higher ed institutions have large section enrollments, and we decided to pass the added expenses for additional server resources on to those particualar institutions.

So our plan is that beginning Fall 2023, a "course" only covers up to 60 students (double our original assumption of 30 students). Invoicing will include an additional course for every mutliple of 60 students. For example, a WeBWorK shell serving 70 students will be invoiced as two courses for $240. And a shell serving 500 students will count as 9 courses invoiced for $960 (where the 6th course is free). We know this may be a steep increase for schools with hundreds of students in one course, but it still approaches only $2 per student for the term/semester. If it breaks your budget, we can provide no-cost consulting for setting up your own institutional WeBWorK server.


Thank you
---------

Thank you again to all of our subscribers. You support the development of two significant open-source apps for higher ed. May these projects continue to grow and serve you better.

Alex Jordan

.. author:: default
.. categories:: none
.. tags:: none
.. comments::
