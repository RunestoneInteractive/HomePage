On Data Privacy Agreements
==========================

An Open Letter
--------------

.. admonition:: Rant Alert

    Before I get into the heart of this I will apologize in advance if this sounds a little like a rant. I started this post on a day when I got three different reqeusts to sign contracts! I am trying to clarify my position, open a dialog, and provide you some alternatives for using Runestone without needing a long contract.

Dear School Districts,

I run Runestone Academy as a "labor of love."  For me it is a great way of paying back all those who have helped me be successful over the years.  The mission of Runestone is to democratize textbooks for the 21st century.  One implication of that mission is that everyone who wants to learn computer science should have access to free, high quality materials.

I'm not trying to turn Runestone into a major corporation or even make a profit.  If I can run it as a small business that keeps me from becoming a greeter at Wal-Mart that is even better! I'm perfectly transparent about the finances, please take the time to read about that in our `Annual Report <https://blog.runestone.academy/2021/01/27/annual_report_2020.html>`_  It also does a nice job of clarifying our mission.

Districts, you are driving me crazy with your student data privacy agreements!  Do you even understand what you are asking for?  I understand that you must follow laws that have been thrust upon you by your well meaning state legislators, I understand that student data privacy is a good thing.  I understand that you don't want some corporation making money by selling your students PII for fun and profit.  I agree! Read my `Privacy Policy <https://runestone.academy/runestone/default/privacy>`_ and our `Terms of Service <https://runestone.academy/runestone/default/privacy>`_  We are on the same side.

But here is the problem:

1. As a free and open source project we don't have lawyers, nor do we have the budget to pay for them as needed.  I am definitely not a lawyer, and frankly Its very risky for me to spend my time pretending to be one to read your agreements.
2. As a free and open source project I work on this because I love to write educational materials that help students learn and I love to code systems like Runestone that help you and your students teach and learn more effectively.  This does not include spending my time filling out attachements A, B, C and H of yet another data privacy agreement.
3. As a free and open source project we don't have any money to promise to reimburse you for anything if something goes wrong.
4. Approximately every district in every state has a different agreement!

As a professor of 15 years I am very aware of FERPA and all that it entails.  But seriously here is what I am asked to agree to on a regular basis.  This is taken directly from contract sent to me by a school district like yours.

    The Contractor warrants that the service it will provide to District is fully compliant with the following regulations:

    * Children's Online Privacy and Protection Act (COPPA)
    * Family Educational Rights and Privacy Act (FERPA)
    * Health Insurance Portability and Accountability Act (HIPAA)
    * Payment Card Industry Data Security Standards (PCI-DSS)
    * Student Data Privacy Pledge

    And any changes to the preceding that may occur from time to time.

    The vendor hosting data center meets the following standards (proof must be provided if PII is stored at rest in the vendor's data center):

    * ISO27001:2005
    * SOC2
    * SSAE 18

Sometimes I swear you and your lawyers just Google everything related to privacy and add it to a laundry list for us to figure out.  Honestly what does HIPPA have to do with computer science?  I asked a lawyer friend about HIPPA compliance and he laughed and said that only a handful of people in the country even know what that means.

As a non-lawyer computer scientist I have learned some heuristics that help me weed through these agreements in record time.  All I need to do is search for the words "indemnify" and "reimburse" as in:

    * If requested by the District, Provider shall reimburse District for costs incurred to notify parents/families of a breach not originating from District's use of the Service.

    * The Provider shall indemnify and hold harmless the District from and against any loss, claim, cost (including attorneys' fees) or damage of any nature arising from or in connection with the breach by the Provider or any of its officers, directors, employees, agents or representatives of the obligations of the Provider’s or its Authorized Representatives under this provision or under a Confidentiality Agreement, as the case may be.

Really!?  If Equifax, major banks, and pipeline companies cannot always prevent hacks! How are we supposed to be any better?  We do our best, try to follow good practices and take all reasonable precautions, but you now want me to promise to pay you back for a service that you are using for FREE.  If I find a clause like that I will ask you to remove it.  I simply cannot enter into a contract that obligates Runestone to pay you back.

Trying to guilt me into signing something will not work. "If you don't sign this then our students will not be able to use your materials." Yes I want your students to use the materials, its why I do this, but I don't make anything from your students, Its not like a for profit corporation where if I don't sign you don't pay me. In fact every district that uses Runestone just adds to the costs of running Runestone. More students means more servers means more money we have to pay to keep running the service.  I am not going to put the project at risk just to make your lawyers happy.

Every minute I spend trying to deal with your red tape is a minute a don't get to spend making Runestone better or writing new materials to help your students learn.

Solutions
---------

First, **everything** on Runestone is open source and free for you to use however you see fit.  This includes every book and the Runestone server that supports it! This allows for several solutions.

1.  You can run your own Runestone Server and serve any of the books you want on your very own server.  This totally eliminates the need for you to use Runestone Academy and keeps you 100% in control of your students data.  This was actually the model I envisioned for Runestone in the beginning, but I quickly learned that many people do not have the time or the skill to maintain their own server, and so to help those people Runestone Academy was born.  No good deed goes unpunished as they say.

2.  You and your students can read and use **any and all** of the books on `Runestone Academy <https://runestone.academy>`_ **without creating an account.**  Ok, yes this makes life a lot harder for teachers to gather their students homework and grade it, but it is 100% an option.  I am not trying to force anyone to create an account so I can gather PII to sell!

3. You could agree to send Runestone some money so that I can have your agreement properly reviewed by a lawyer at around $350 / hour.  Lets call it $1200.  In that case I would be happy to agree to refund that entire $1200 as reimbursement for a data breach.  I'm happy to put that in writing and send you an invoice.

4.  You, as a teacher, can register all of your students anonymously with NO PII. `See this post for instructions <https://blog.runestone.academy/2019/10/25/privaterunestone.html>`_ on how to do this.  I would be happy if everyone who sent me contract would just do this instead.  I have no interest in knowing anything about your students, the only reason I collect names and email addresses is to deal with password resets and to make life easier for instructors when they are grading assignments.  This solution makes it a bit less convenient, but does so without any PII.

In the back of my head I have an addition to Runestone that would allow everyone to use option 4, but allow instructors to keep a mapping in their browser (NOT on Runestone) that would let them see who the anonymous students really are.  That is just a gleam in my eye at this point, no code has been written, so please don't ask when it will be ready.

We Are in this Together
-----------------------

I firmly believe that our goals are aligned!  I want to provide great free resources to help students learn, and you as school districts with limited budgets want to use great free resources to help your students learn.  I am not the enemy!  I have signed the student data privacy pledge, I have published a privacy policy.  I sincerely care about student privacy!

But, I believe these laws put projects like Runestone at a real disadvantage. We do not have the resources to hire lawyers to review and negotiate all of these contracts.  We are not big enough to make you sign our own.  So we need to work together and treat each other with respect and maybe engage in a little give an take.  It is a win win!  If you don't use Runestone are you going to pay a big publisher $100 per student every semester?

If you have other suggestions for how we can make this work please feel free to reach out to me, I am open to hearing ideas and working on alternatives that do not create more legal hassle for any of us!

Thanks for reading!

Sincerely,

Brad Miller

Professor Emeritus, Luther College

Founder, Runestone Interactive


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
