Fall 2025 Transitions
=====================

Welcome back!  Registrations have begun to soar for the Fall 2025 semester, and we are excited to see many new faces joining our community. As we prepare for the upcoming semester, here are some important updates and transitions to keep in mind.  We realize that transitions like this can be challenging and confusing, we appreciate your patience and understanding as we work through these changes.

New Instructor Dashboard
------------------------

You will notice a revamped instructor dashboard.  It has a new look, and uses a modern web framework on the backend.  `Please let us know if you encounter any issues <https://github.com/RunestoneInteractive/rs/issues>`_ as the backend code is new. Please check existing issues before you make a new one. This new dashboard should replicate the old functionality, but we may have missed some edge cases in our rewrite.  The old dashboard will remain available, probably for the entire 2024/2025 year, but I won't be fixing any bugs or doing any enhancements to the old interface.  Think of it as a faithful backup in case something critical goes wrong with the new dashboard.

New Assignment Builder
-----------------------

The story for the new assignment builder is similar.  It has been completely rewritten using a modern web framework on the backend.  Notably, the database for the two builders is identical and shared.  You can see the assignments in both.  **Really Important** The old assignment builder used the authoring language restructuredText plus our extensions for you to write questions.  The new assignment builder uses a different approach, rather than saving the RST for you to edit, the new assignment builder saves the questions in a JSON format. I have tried to write a converter and have converted old ``activecode``, ``shortanswer``, and ``multiple choice`` questions to the new json format so you can edit those old question in the new assignment builder.  That was a **one time conversion**.  If you write new questions in the old assignment builder you **will not** be able to edit them in the new assignment builder.  Please use the new assignment builder - we think it is much more user friendly and easier to use.  The old questions had a myriad of options ``:option:`` in the RST.  Many of them were experimental, or implemented for a particular project and many of them are not that useful.  So far we have only added the most used options to the new assignment builder.  If you find that you need an option that is not available, please let us know.

As with the instructor dashboard, please report any issues you encounter.  The old assignment builder will also remain available for the 2024/2025 year, but it will not be receiving any enhancements or bug fixes.

LTI 1.3 Support
----------------

Many schools have told us they are moving to LTI 1.3 for their LMS integration and will no longer support LTI 1.1.  We have added support for LTI 1.3 in addition to the existing LTI 1.1 support. LTI 1.1 support is *only available through the old instructor dashboard*, and I won't be moving any support to the new dashboard since most schools will no longer support 1.1.

Unfortunately LTI 1.3 will need to be configured by your LMS administrator. We have been testing it out in production with Canvas, Moodle, and D2L.  If you want to use LTI 1.3 you will need to create an `issue on github <https://github.com/RunestoneInteractive/rs/issues/new/choose>`_` to have us enable your domain.  As you will read on the issue template, if your school is going to require us to fill out forms and provide things like HECVATs and VPATs and then LTI 1.3 support is a paid feature.  As an open source project we do not have the resources to fill out forms for every school that wants to use our software.  If you are a small school or a school in a developing country please let us know and we will work with you to get LTI 1.3 enabled.

On the positive side, if you are using 1.3 and you have pre-released your assignment (on the grading page), then grades will be automatically sent back to your LMS.  This is a big improvement over LTI 1.1 where you had to remember to push the grades back.

More to Come
------------

We are continuously working on improving the platform.  There are only a few more things to migrate away from our old web framework. These include:

* Grading
* Peer Instruction
* Practice

As we migrate each of these components we will keep the old in place so they can be used in parallel.  I hope that all of the above can be completed by the end of the school year so that we have a fully modernized code base for fall 2026.  As with any system that has been around for a long time, there are lots of features that have been added over the years.  We will be evaluating each feature to see if it is still useful and if it is worth migrating to the new framework.  We have a lot of usage data to help us make these decisions, but if you find that a feature you use has not been migrated, please let us know.

| Brad Miller
| Professor Emeritus, Luther College
| Founder, President, Chief Developer, Runestone Academy

.. author:: default
.. categories:: none
.. tags:: none
.. comments::
