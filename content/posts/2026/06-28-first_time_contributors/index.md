---
title: "First Time Contributors Accelerate Progress"
date: "2026-06-28"
slug: "first_time_contributors"
---

I hope your summer is off to a good start! June has been a busy month with changes big and small. I'm thrilled so say that we have **five first time contributors** to the project this month. Not to mention significant contributions from returning contributors as well. I've been taking advantage of the quieter days to do a lot of behind-the-scenes work -- some of it the kind of cleanup that has been on my list for a very long time. Most of it falls into three buckets: tightening up security, modernizing the plumbing that runs both runestone.academy and the self-hosted installations, and continuing to retire the old code. I could not have done it without the help of the community and my trusty sidekick Claude. Here are the highlights from the last couple of weeks:

- Security fixes across the book, assignment, and admin servers
- More progress retiring the original 2011 web framework -- the old Peer Instruction pages and most of the old instructor admin pages are gone
- A switch to [uv](https://docs.astral.sh/uv/) for all of our Python services, which makes installs and builds much faster
- [Caddy](https://caddyserver.com/) as an option for serving Runestone with automatic HTTPS
- A new user menu and a consistent set of icons across the interface
- A/B testing and a new reflection step for Peer Instruction
- A lighter-weight translation system for the interactive components

## A word about security

We completed a focused security pass across the servers and fixed a handful of issues -- among them a server-side request forgery hole in the image proxy, a peer-chat channel that did not require an authenticated user, and several instructor actions that did not check that you actually owned the course you were acting on. None of these require anything from you other than running a current release, but I wanted to be transparent that the work happened. If you self-host, updating to the latest version picks all of it up.

## Retiring more of the old code

Longtime readers know I have been chipping away at retiring the code based on the web framework the project was built on back in 2011. This stretch took several more bites out of it. The old Peer Instruction controller and views are gone, fully replaced by the new versions. I also retired the bulk of the old instructor admin pages -- course and student management, the old assignment builder, exam resets, and the logs -- all of which now live in the new services. A few pages (grading, Manage Practice, and the editorial page) are staying on the old stack a little longer until their replacements have had more time to soak. The student progress report and a couple of small activecode endpoints moved over as well. We are getting close to the clean slate I have been hoping to reach by the end of the summer.

## Faster installs and easier HTTPS

A couple of the changes are mostly for those of you who run your own Runestone server or like to dig into the code. We moved the whole project from Poetry to uv for managing dependencies and building. In practice this means installs and builds are dramatically faster, and I think it makes the project a little friendlier to contribute to. We also added Caddy as an alternative to nginx for the front door. The big draw there is automatic HTTPS -- Caddy can obtain and renew certificates for you with almost no configuration -- which makes standing up a secure instance much easier. You can keep using nginx if you prefer; Caddy is simply there as an option now.

## A more consistent interface

On the interface side, PreTeXt books get a new user menu, and I replaced the old icons with a single consistent set throughout the site. This is part of the larger effort I have mentioned before to make the experience feel like one cohesive system rather than a collection of separate ones. The navigation bar is now shared between the book pages and the login and account pages. I would love feedback on how it looks and feels.

## New tools for Peer Instruction

For those of you using Peer Instruction, there are two additions worth trying. You can now run a small A/B test comparing different discussion modes, with each student's group remembered across sessions, and we fixed a bug where the instructor's own vote was sneaking into the chart. Asynchronous Peer Instruction can also include an optional Likert-scale reflection step that you can turn on per course. If you use peer instruction in your classes, I would really like to hear whether these are useful. Much of this work is done as part of a PhD research project! Its important example of how **pedagogy drives progress!**

## Lighter, more flexible interactives

Finally, a quieter but satisfying piece of work in the interactive components: we replaced the old jQuery-based translation library with a small, dependency-free one of our own and moved ActiveCode, fill-in-the-blank, multiple choice, Parsons, and drag-and-drop over to it. Drag-and-drop questions can now also be authored in JSON and XML, which is part of a longer effort to make question authoring more uniform across component types. The Cardsort question behavior was also modified based on feedback from teachers, students and researchers at the PROTEUS (Pretext Runestone Open Textbooks for Engaging Undergraduates in STEM) workshop held in Ann Arbor the week of June 14th. Its great to have this kind of community involvement and feedback!

## Thanks, as always

This is a community effort, and I am grateful for everyone who reports issues, sends pull requests, and is patient with a project that does not have a full-time support staff. Version 8.8.1 is out, so self-hosters can pick up everything above by updating. If you run into trouble, please open an [issue on GitHub](https://github.com/RunestoneInteractive/rs/issues) with as much detail as you can, and if you just want to share feedback or ask a question, the [public forums](https://runestone.academy/ns/books/published/PTXSB/rune.html) are the best place. Thanks, and happy summer!
