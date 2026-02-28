FROM jekyll/jekyll:3.5.2

LABEL maintainer OBOFoundry<obo-discuss@googlegroups.com>

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
COPY requirements.txt requirements.txt
RUN apk add python3-dev
RUN pip3 install --no-cache -r requirements.txt
#RUN pip3 install --no-cache --upgrade pip setuptools frontmatter

RUN mkdir -p /tools/
ENV PATH "/tools/apache-jena/bin:/tools/sparqlprog/bin:$PATH"
# Install Jena.
RUN wget -nv http://archive.apache.org/dist/jena/binaries/apache-jena-3.12.0.tar.gz -O- | tar xzC /tools && \
    mv /tools/apache-jena-3.12.0 /tools/apache-jena

RUN apk --no-cache add openjdk11 --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community


CMD make all && jekyll serve