#!/usr/bin/env sh
docker run -v $PWD/:/srv/jekyll/ -p 4000:4000 --rm -it obolibrary/site
