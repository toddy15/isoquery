# Copyright © 2016 Dr. Tobias Quathamer

SUBDIRS = tests

AM_CPPFLAGS = $(GLIB_CFLAGS) $(GIO_CFLAGS) $(JSON_CFLAGS)
LDADD = $(GLIB_LIBS) $(GIO_LIBS) $(JSON_LIBS)

bin_PROGRAMS = isoquery

isoquery_SOURCES = iso.c number.c number.h
