A Farewell to RST
=================

The end of the semester is approaching, and with it comes the beginning of Summer development time! 

In a few days I will release Runestone 7.13.6, this marks the last release of Runestone that will support RST as an authoring language. That is probably not true, the 7.13 line will continue for key bug fixes, but it will be the last release that will include new features for RST.

What does this mean for Runestone?  Well, just over six years ago we formed a partnership with the PreTeXt project to use their XML-based authoring language as the basis for Runestone.  We have been very happy with that decision, and it has allowed us to add a lot of features to Runestone where I can focus on the interactive features and not worry about the authoring language.  PreTeXt is a very powerful author language, and it is being used by a growing number of projects. It has a great focus on accessibility and is designed to be easily converted to a variety of output formats.  When two open source projects can work together to create a better product, that is a win for everyone.

If you are an author and have not converted your book to PreTeXt, I encourage you to do so.  The conversion process is not difficult, and there are a number of resources available to help you.  The PreTeXt project has a number of people willing to help with the conversion process, and there are a number of tools availble to help with the conversion, not to mention LLM-based tools like Copilot Claude Code and ChatGPT.  If you have questions about the conversion process, please reach out to me or the PreTeXt community for help.

We will continue to develop and support the interactive elements of Runestone like activecode, parsons problems, and the various interactive widgets that we have developed over the years.  Future updates to the componenents will be released in the 8.x line, although I don't see a reason to push them to pypi, the ``runestone build`` command will not build anything in the 8.x line.

If you absolutely must have a new feature in RST, you are welcome to add it to the ``legacy_support`` branch of the Runestone repository, but I will only support critical bug fixes on that branch, so if you want a feature merged you will need to provide the ongoing support for it.

I'll have more to say about our summer development goals in the next few weeks, but I wanted to get this news out as soon as possible so that authors have plenty of time to make the transition to PreTeXt, current users of RST will not be surprised by this transition.  Nobody should be surprised as I've been talking about it for years.


.. author:: default
.. categories:: none
.. tags:: none
.. comments::
