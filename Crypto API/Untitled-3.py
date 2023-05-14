#!/usr/bin/env python
#
# Copyright (c) 2005-2007 Niels Provos <provos@citi.umich.edu>
# Copyright (c) 2007-2012 Niels Provos and Nick Mathewson
# All rights reserved.
#
# Generates marshaling code based on libevent.

# pylint: disable=too-many-lines
# pylint: disable=too-many-branches
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-statements
# pylint: disable=global-statement

# TODO:
# 1) propagate the arguments/options parsed by argparse down to the
#    instantiated factory objects.
# 2) move the globals into a class that manages execution, including the
#    progress outputs that go to stderr at the moment.
# 3) emit other languages.

import argparse
import re
import sys

_NAME = "event_rpcgen.py"
_VERSION = "0.1"

# Globals
LINE_COUNT = 0

CPPCOMMENT_RE = re.compile(r"\/\/.*$")
NONIDENT_RE = re.compile(r"\W")
PREPROCESSOR_DEF_RE = re.compile(r"^#define")
STRUCT_REF_RE = re.compile(r"^struct\[(?P<name>[a-zA-Z_][a-zA-Z0-9_]*)\]$")
STRUCT_DEF_RE = re.compile(r"^struct +[a-zA-Z_][a-zA-Z0-9_]* *{$")
WHITESPACE_RE = re.compile(r"\s+")

HEADER_DIRECT = []
CPP_DIRECT = []

QUIETLY = False


def declare(s):
    if not QUIETLY:
        print(s)


def TranslateList(mylist, mydict):
    return [x % mydict for x in mylist]


class RpcGenError(Exception):
    """An Exception class for parse errors."""

    def __init__(self, why): # pylint: disable=super-init-not-called
        self.why = why

    def __str__(self):
        return str(self.why)


# Holds everything that makes a struct
class Struct(object):
    def __init__(self, name):
        self._name = name
        self._entries = []
        self._tags = {}
        declare("  Created struct: %s" % name)

    def AddEntry(self, entry):
        if entry.Tag() in self._tags:
            raise RpcGenError(
                'Entry "%s" duplicates tag number %d from "%s" '
                "around line %d"
                % (entry.Name(), entry.Tag(), self._tags[entry.Tag()], LINE_COUNT)
            )
        self._entries.append(entry)
        self._tags[entry.Tag()] = entry.Name()
        declare("    Added entry: %s" % entry.Name())

    def Name(self):
        return self._name

    def EntryTagName(self, entry):
        """Creates the name inside an enumeration for distinguishing data
        types."""
        name = "%s_%s" % (self._name, entry.Name())
        return name.upper()

    @staticmethod
    def PrintIndented(filep, ident, code):
        """Takes an array, add indentation to each entry and prints it."""
        for entry in code:
            filep.write("%s%s\n" % (ident, entry))


