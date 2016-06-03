FROM debian:sid

ENV DEBIAN_FRONTEND noninteractive

# Get the latest versions
RUN apt-get update -y

# Install all locales to enable UTF-8 for testing
RUN apt-get install -y locales-all
ENV LANG en_US.UTF-8
ENV LANGUAGE en
ENV LC_ALL en_US.UTF-8

# Install packages for building isoquery
RUN apt-get install -y build-essential libglib2.0-dev libjson-glib-dev python3-docutils po4a iso-codes

# Clean up
RUN apt-get clean
