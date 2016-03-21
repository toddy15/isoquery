# Copyright © 2016 Dr. Tobias Quathamer

include $(top_srcdir)/build/glib-tap.mk

AM_CPPFLAGS = -I$(top_srcdir)/src $(GLIB_CFLAGS) $(GIO_CFLAGS) $(JSON_CFLAGS)
LDADD = $(GLIB_LIBS) $(GIO_LIBS) $(JSON_LIBS) \
	$(top_srcdir)/src/number.o

# test binaries
test_programs = getnumber
