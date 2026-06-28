{{- $base := replaceRE "^[0-9]{2}-[0-9]{2}-" "" .File.ContentBaseName -}}
---
title: "{{ $base | replaceRE "[_-]" " " | title }}"
date: "{{ dateFormat "2006-01-02" .Date }}"
slug: "{{ $base }}"
# categories: ["Announce"]   # optional
# author: ["Guest Name"]     # optional; defaults to the site author
---

Write the post here. Put images in this folder and reference them with an
absolute bundle path, e.g. `![alt](/YYYY/MM/DD/{{ $base }}/image.png)`.
