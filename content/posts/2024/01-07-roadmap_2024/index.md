---
title: "Roadmap 2024"
date: "2024-01-07"
slug: "roadmap_2024"
categories:
  - "Development"
---

A lot of the podcasts I listen to, and quite a few of the blogs I read, encourage you to pick a touchstone word for the year. I've never done that before, but I'm going to try it this year. My word for 2024 is "Simplicity". I'm going to try to use this word to guide my decisions and actions for the year, both in my personal life and in my professional life.

My decision to choose **simplicity** was reinforced by a recent blog post by Matt Mullenweg, the CEO of Automattic, the company behind WordPress. And a second by Terry Sutton, a front end developer. In [Terry's post](https://terrysutton.dev/blog/open-source-state-of-mind) he says:

> Good open source software is / does / can (roughly in order):
>
> 1.  easy to install and setup, for free, both locally and on my own server
> 2.  powerful, capable
> 3.  make easy things easy
> 4.  make hard things possible
> 5.  opinionated, and so you get:
> 6.  a lot out of the box, so you don't have to:
> 7.  constantly reinvent the wheel to do simple or common things
> 8.  interoperable, flexible, extensible
> 9.  Has a core user story in mind (ie: it appeals extremely well to a couple of use cases, while enabling many others)
> 10. continuously improved and updated

I think that's a great list, and I think that the Runestone software ticks a lot of those boxes, but not the first one, and I've heard from many of you, not not the third one. It certainly is the fifth one, and I think sixth through tenth follow. The good news is that principles 1 and 3 are closely related to my touchstone word for the year.

Runestone has been around since 2011, and it has grown organically over the years. Myself, students, other contributors added features as I've needed them, and as others have asked for them. I've tried to keep the code clean, and the architecture flexible, but I think it's time to take a step back and look at the big picture. I think it's time to simplify.

Moving to the monorepo was a first step in that direction. I think it's time to take a second step. I'm going to try to simplify the user experience, particularly for instructors. I'm going to try to make it easier to install and setup, and I'm going to try to make it easier to use. I'm going to try to make it easier to contribute to, and I'm going to try to make it easier to extend.

Here are some some of the things I'm targeting especially for the first half of 2024:

- Create a quick programming project interface to serve as a replacement for instructors who used repl.it.
- Simplify the experience for creating and grading assignments
- Simplify the installation process
- Simplify the configuration process
- Make the developer experience better for contributors
- We are going to have to bite the bullet on LTI 1.3 support soon! People are deprecating 1.1 as we speak.

Please note, these are **Goals** not *guarantees.* I had many features I wanted to implement in the Fall of 2023, but most of my time was eaten up answering questions from users, and dealing with growth and scaling issues. I'm hoping that by setting these goals, and by sharing them with you, I'll be able to stay focused on them.

I'm not going to go into details here, but I'll post about progress periodically. If you want to get into the details, it is all on [Github](https://github.com/RunestoneInteractive/rs/projects?query=is%3Aopen) in the form of six projects (Sort them by name). Under the hood the main goal is to get all of the instructor facing pages ported to the same underlying technology we use for the assignment and book serving pages. This will make it easier to maintain, and easier to extend. It will also make it easier to add new features, and to make the user experience more consistent.
