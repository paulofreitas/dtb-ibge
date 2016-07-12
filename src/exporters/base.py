#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Brazilian territorial distribution data exporter

The MIT License (MIT)

Copyright (c) 2013-2016 Paulo Freitas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

# -- Imports ------------------------------------------------------------------

# Built-in modules

import collections

# -- Implementation -----------------------------------------------------------


class BaseExporter(object):
    '''Base exporter class.'''
    def __init__(self, data, minified=False):
        if type(self) == BaseExporter:
            raise Exception('<BaseExporter> must be subclassed.')

        self._data = data
        self._minified = minified

    def __str__(self):
        raise NotImplementedError

    def __toDict__(self, strKeys=False, unicode=False):
        dict_obj = collections.OrderedDict()

        for table_name in self._data._tables:
            if not self._data._dict[table_name]:
                continue

            dict_obj[table_name] = collections.OrderedDict()

            for item in self._data._dict[table_name]:
                item_obj = collections.OrderedDict()

                for key in self._data._fields[table_name]:
                    item_obj[key] = item[key].decode('utf-8') \
                        if unicode and (type(item[key]) == str) else item[key]

                item_id = str(item_obj['id']) if strKeys else item_obj['id']
                del item_obj['id']
                dict_obj[table_name][item_id] = item_obj

        return dict_obj