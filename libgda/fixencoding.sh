#!/bin/sh

# https://github.com/voidlinux/void-packages/commit/f16a2d557e84f5d7f5ece8b2022aab4fd17aa0ce
for f in $(find . -type f -exec file "{}" \; | grep "C source" | cut -d ':' -f1); do
  echo "${f}"
  recode ISO-8859-1..UTF-8 "${f}"
done
