Docker Images for Macs and Linux
================================

One of my hoped for quality of life improvements for the Runestone platform is to make it easier for everyone to run a Runestone server own their own computer.  This is especially important for authors who want to test their books locally before pushing them to the Runestone server.  We made great progress on this front a couple years ago when I created a container registry on github to hold our docker images for all of our servers.  The problem was that the images were built for x86_64 architecture, and so they would not run on ARM based machines like the new Apple Silicon Macs.  I didn't know how to build multi-architecture docker images, and I didn't have the time to learn how to do it.

Like many things in life, solving the problem is not that hard if you take the time to learn how to do it.  I finally carved some time out of my routine of fixing bugs and adding features to learn how to build multi-architecture docker images.  I am pleased to announce that we now have images for the Runestone servers that will run on both ``x86_64`` and ``ARM`` architectures.  This means that you can now run a Runestone server on your Mac or Linux machine without having to build the images yourself!  These images are the same images we use in production, so you can be sure that they are stable and reliable.

.. attention:: Details on how to get configured and running are here: `Runestone Server Setup <https://runestone-monorepo.readthedocs.io/en/latest/running.html>`_.  In my experience the vast majority of the problems that people have when trying to run a Runestone server on their own machine are related to the configuration of the server.  The sample env file should work for most people, but you may need to tweak it a bit to get it to work on your machine.  If you run into problems, please feel free to create an issue on our GitHub repository, and we will do our best to help you get it working.

The next step would be to create a script that will automatically get the server up and running with minimal user intervention.  If anyone is interested in helping with that, please let me know.  I would be happy to work with you to get it set up.



.. author:: default
.. categories:: none
.. tags:: none
.. comments::
