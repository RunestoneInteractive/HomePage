DDoS Update
===========

.. image:: ManyHats.png
    :alt: Many Hats
    :width: 100%

The Distributed Denial of Service (DDoS) attack is ongoing.  Even after I moved our load balancer to new hardware and a new IP address.  This means that the attackers are not just targeting the IP address of the load balancer, but they are targeting "runestone.academy" by name.  This is a much more serious attack and it is taking a lot of time to mitigate.

I've learned a lot about how to mitigate these attacks and I'm implementing the solutions as quickly as I can without causing a lot of downtime.  I'm sorry for the inconvenience this is causing you. I think are to the point where we have minimized it.  When a new wave of attacks hits it just takes a minute or so to block the attackers.  So, just keep that in mind, take a breath, wait a minute and refresh your page.   I'm also sorry that I have to spend so much time on this instead of working on new features for Runestone.

These kinds of sustained attacks do not come for free.  There are literally thousands of IP addresses involved over a period of days.  This is not just a kid in a basement with a botnet.  This is a reasonably well-funded and well-organized attack.  I'm not sure what the motive is, but it is clear that they are not going to give up easily.  Could it be an evil publisher trying to squash free textbook distribution?  Could it be one of our "competitors" trying to take us down?  Could it be a foreign government trying to disrupt education in the US?  I don't know.  I do know that I'm not going to give up easily either.

The cartoon at the top was generated yesterday by DALL-E.  It is a cartoon of me wearing many hats.  I thought it was appropriate for the situation.  GitHub co-pilot suggested that I should be wearing a tinfoil hat.  I'm not sure that would help.  It also suggested that I should write that I am working with the NSA, CIA, and Department of Homeland Security to track down the attackers.  That is certainly not true.  I'm just a guy trying to keep the Runestone servers up and running.

I also want to assure you that, so far, the attack has been limited to, and stopped by the load balancer, our application servers and database are secured behind the load balancer and an additional firewall. So, even if the load balancer were to go down, the application servers would still be up and running. Yes, timeouts of API calls to save data to the database might happen, but you should get a dialog if that happens, so that you can reclick the button and have it save the latest answer again.

Again, please remember to check the `Runestone Status Page <https://status.runestone.academy>`_ if you are having trouble accessing the Runestone books.  It updates every 5 minutes and is served from a completely different server, so is unaffected by the DDoS attacks.



.. author:: default
.. categories:: none
.. tags:: none
.. comments::
