Academy Update
==============

Thanks to everyone for your patience over the last three weeks!  As a recap here is what has transpired.

1. I took Runestone Academy offline on Christmas day and started up my script to migrate the database to a new machine dedicated to running Postgresql.  That script took just over 25 hours to complete.  It modernizes the database and adds many new constraints to make sure that when we store something in the database it is good and consistent and valid.
2. On January 27 I brought up two "worker bee" servers and our load balancer.  This allows me to add as many "worker bees" as we may need to serve the traffic going to runestone.  I changed our DNS entry to point "runestone.academy" at the new load balancer.  Unfortunately I did not delete a previous DNS entry so now some people were getting the old address and some the new.  Chaos ensued for a few days.
3. By Monday January 3rd I was patting myself on the back and thinking "this is going better than I thought" LOL -- Many problems -- to numerous to count ensued as soon as classes actually started again.
4. LTI - or what I call the "community supported feature" was just supposed to work.  But did not.  Thankfully I think that as of yesterday it is now working great!

Today was **the first day** since December 27 that I have not had a **new** bug report.  I know there are still problems out there, but at this point they are outliers not the norm.  That does not mean I don't care, I do, but it does mean that I need a lot of detailed information to try to figure out what is wrong.  Major widespread problems are easy to figure out because I hear from hundreds of people.  I'm not hearing from 100's anymore!! So details are important.

If your students are having trouble
-----------------------------------

1. Logout - clear browsing history, and log in.
2. Try incogito mode
3. Open up the Javascript console on their browser and send me everything!  No detail is too small. And **Its not your fault!** at this point I am trying my best to debug the odd cases. I am even willing to do a zoom with you and your students to debug the problem.

I cannot emphasize how useful it is to do #3!  So much of what happens in Runestone is delegated to the browser.  If we did not delegate this work to the browser we could never scale to as many students as we have!

Thanks for sticking with us through this transition.  Major shifts like this are always painful, and I know we are not through yet.  But this new architecture sets us up for a very bright future!


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
