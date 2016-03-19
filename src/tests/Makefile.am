include $(top_srcdir)/build/glib-tap.mk

AM_CPPFLAGS = $(GLIB_CFLAGS) $(GIO_CFLAGS) $(JSON_CFLAGS)
LDADD = $(GLIB_LIBS) $(GIO_LIBS) $(JSON_LIBS)

# test binaries
test_programs = number

number_SOURCES = number.c ../number.c ../number.h
