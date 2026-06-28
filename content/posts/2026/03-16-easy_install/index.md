---
title: "Easy Install"
date: "2026-03-16"
slug: "easy_install"
---

I know that running your own server is not for everyone, but we want to make it was easy as possible for Runestone to support the students who need us. But sometimes Government regulations or institutional policies make it difficult to use a third party hosting service. For those of you who want to run your own server, we have created an easy install script that will set up a Runestone server on your machine. This script will install all the necessary dependencies and configure the server for you.

To use the easy install script, copy and paste the following command into your terminal:

``` bash
bash <(curl -fsSL https://raw.githubusercontent.com/RunestoneInteractive/rs/main/init_runestone.sh)
```

This will download and run the easy install script. The script will ask you a few questions about your setup, It will then install all the necessary dependencies and configure the server for you. You will need to have Docker installed on your machine for this to work. If you do not have Docker installed, there are some great tutorials online that can help you get started such as [Docker for Beginners](https://docker-curriculum.com/).

## Why Run your own Server?

There are a few reasons why you might want to run your own server:

- You may have legal or institutional requirements that we as a small non-profit, open-source organization cannot meet. We are committed to the **National Data Privacy Agreement** But we understand that some institutions may have additional requirements that we cannot meet. If this is the case, running your own server may be the best option for you.
- You want to have more control over your data and how it is stored.
- You want to be able to customize the server to fit your specific needs.
- You want to be able to run the server on your own hardware.
- You want to be able to run the server in an environment that does not allow third party hosting services.

All of these are valid reasons, and we understand that running your own server is not for everyone. We are here to support you regardless of how you choose to use our software. If you have any questions about running your own server, please feel free to reach out to us on our [public forums](https://discord.gg/f3Qmbk9P3U) or [GitHub](https://github.com/RunestoneInteractive/rs/issues). We are happy to help you get set up and answer any questions you may have. We also welcome contributions to the easy install script, if you have any improvements or suggestions please let us know!

I would also like to acknowledge Tyler Conzet for his work on the easy install script. Tyler was a former student of mine and has been a great contributor to the Runestone project. He has done a lot of work on the easy install script and has made it much easier for people to run their own servers. Thank you Tyler!

## Keeping up to date

If you choose to run your own server, it is important to keep it up to date. We are constantly making improvements and adding new features to the software, and it is important to keep your server up to date in order to take advantage of these improvements. We recommend that you check for updates regularly and apply them as soon as possible. You can check for updates by running the following command in your terminal:

``` bash
cd /wherever/you/installed/runestone
docker compose pull
docker compose stop && docker compose up -d
```

Occasionally it may be necessary to run a database migration when we make changes to the database schema. If this is the case, we will provide instructions on how to run the migration. We will also provide instructions on how to roll back the migration if something goes wrong. We recommend that you back up your database before applying any updates, just in case something goes wrong. Most updates should be seamless, but occasionally we add more data to the database in the form of new columns or new tables. These migrations will not result in the loss of any data, but it is always a good idea to have a backup just in case something goes wrong.

## Feedback

As this is a new feature, we would love to hear your feedback on the easy install script. If you have any suggestions for improvements or if you encounter any issues, please let us know on our [public forums](https://discord.gg/f3Qmbk9P3U) or [GitHub](https://github.com/RunestoneInteractive/rs/issues). Your feedback is invaluable to us and helps us improve the software for everyone. We are committed to making the easy install script as user-friendly and reliable as possible, and we appreciate any feedback you can provide.

Join our Community -----------------

As always, our mission is to provide free and open educational resources to everyone! We are committed to supporting our students and instructors regardless of how they choose to use our software. If you have any questions or need help with anything, please don't hesitate to reach out to us on our [public forums](https://discord.gg/f3Qmbk9P3U) or hang out with us on zoom! Our weekly zoom schedule is [available here](https://mathtech.org/events/). And you can always drop in on our zoom [during one of the scheduled times here](https://mathtech.org/dropin). We are always happy to help and we welcome your feedback and suggestions and just being a part of our community. It is amazing what can happen when people come together face to face and share their ideas and experiences. We are grateful for everyone who has contributed to the project and we look forward to continuing to work together to make education more accessible and engaging for everyone. Thank you for being a part of our community!

Brad
