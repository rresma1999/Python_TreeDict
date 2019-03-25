# -*- coding: utf-8 -*-
"""Tests for CS109 Python Assignment 5.

This does not test for all the requirements of the assignment! So make
sure you test it yourself.

Run this script using:
  python3.5 assignment5_tests.py
It should work if you are in the same directory as your assignment5.py
file. If this does not work you may want to try:
  PYTHONPATH=[directory containing assignment2.py] python3.5 assignment5_tests.py

"""

# DO NOT CHANGE THIS FILE. Grading will be done with an official
# version, so make sure your code works with this exact version.

import unittest
import itertools
import functools
from contextlib import contextmanager
import sys


import assignment5

_shuffled_list = [39, 83, 31, 8, 66, 19, 45, 61, 86, 65, 28, 89, 95,
                 82, 40, 50, 88, 25, 47, 24, 51, 87, 93, 2, 67, 73, 7,
                 79, 98, 9, 34, 5, 72, 91, 64, 48, 30, 20, 37, 22, 43,
                 54, 46, 17, 55, 74, 49, 76, 35, 97, 14, 26, 10, 52,
                 78, 75, 13, 6, 4, 36, 77, 84, 59, 68, 11, 60, 71, 63,
                 100,90, 57, 41, 70, 96, 15, 92, 21, 56, 38, 27, 53,
                 23, 18, 12, 16, 33, 85, 44, 69, 42, 1, 99, 32, 29,
                 81, 3, 80, 58, 94, 62]

    
_strings_list = ['¬UlV=ic',
     'q´wBox´{¥!^Yu',
     'ªC°§ª/¬W',
     'q}QYX',
     ')B',
     'ݶ𤒪⺒鶴',
     '𩾔긽締𠔍𫀳杶𩝪𫃲𠝼떴咃ᛂ',
     '뉇',
     '¶°GGm',
     '쮛𦏖鱗𠂱𨤂𪖺',
     'Un',
     '𧸜',
     '꽔䈋瞁嚁䱄娳𩦼吝絘玕塸𑀤𧐤',
     '𧖔侏⽊ᾬ𩛧壝𤹀烶◠𑂐魾ᓪ𤕙𪵱',
     '𥐚',
     '𢹐𤇔𝚲𖣅诅𓃦𦑻픇踵ど錩𪊺㲰',
     '𥗻',
     'bd:hrTWo·By®c',
     '卼𥚿𣙊𩰄𣥉泰𡈹栐⍦阈🍂',
     '𣒳𨀰薷䐹娻𣓘',
     'V)Hz%Q°¥}jp',
     'u}n;§G',
     '뢲𡖟ꈰ𩧎𝁪𥮣',
     'W+»?¬',
     ';TGeG«>hE',
     '[º©S',
     '[%L«',
     '𨿣ꝓṊ쑓鹛悈牴𥨅挟𨁼',
     '醾㵐𡁵蚊Ⴢ𨗟𠿈𨰣出𩎜😑𦴆朢',
     '勂橭妁𤝡˻못',
     '£U:[F©i»nB_',
     '℈𤏖𠘁훾𝘫𨍿퇨𩘠亻똠秈',
     'X{-J¶Ni¥±AeSQ°',
     '𧚪𠆸𠌲勲',
     'GWPj»«}',
     '𩅾',
     'gzAbF|jF)[¦',
     'VǟDđoBQⱼ/ǪŪFT«Ĵ',
     '嘩堽𦮠𝗸├袈𧊃𤉆',
     '嚥쇚ﲣ𢢭ぐ',
     'M',
     '¥',
     'Y@¢$°JaTsr°±->',
     '芓𤣆ꚰ봥𡪼𧜊𧔄뜢慣𤨛𡭷',
     'b',
     'pweo',
     '𢽦秷𨺁𢲍謃䴧喟쪳',
     '𧟍𨘮𥨮𢱍櫁𩲀',
     '煖夿杁ও𩀎𩬢촦𣋁𒁚㇓',
     'slk',
     '®Av§p¥¦P*?J~¡',
     'Ⴅ𪃝𪨗ઘ쨸𣬒猺',
     '邆𪖷Ꝫ𡼇𤲠岙𧪦∜﹘𫅋𥴜澝',
     '𤤛𨩝欕遼𩖦𤑔𠰇岿𤐡丹',
     'N?HW.qzL¸cQ',
     'RXIoMU|q¶«J',
     '_eXDiMs&´%µ¦',
     '𪌼礣薕嚲',
     '(~º}jH¤¤',
     'ﻄ貕𓆙🅡',
     '𦷊㎡릏𤴥𣵴귛㟎',
     'ᖺ곘𣡅韜낼',
     '⦓ﵜ㖮⊫ꯎ櫬𪩁诞𥝀捂䂦槻',
     '㝚𠛠𡖠𢒫𪑦𪈳𤓱䪢ꙃ㢑밦',
     't',
     '®.a.°x~x`}k@w£',
     '𫜡𤖗뱯𥲳𣌋𥒜𥷃앸狴ː䯂頁𒊱',
     'B',
     'l¨¦',
     '®',
     '^@¯nyB»',
     '𩚙',
     '𩐶镋㯼𦦗𥬐𨻋⤽ᛂ𣴟홠',
     '쎹笙𣐑昳𪲕',
     'MRu-=mU#JZ',
     'iR-}¥uU/N´¬(b}',
     '𐡐힒𪡠珊篩捠慜𢿋𪭅蚊𣹡',
     '즙𩻓槎㰅𤬄',
     '/¤qG&#¡o]',
     '$}°yC¨/',
     '§OP',
     '㓣𨸦🃃癒𥭔쩘',
     '⢛켴𥕢𓋒𢑙姺𠓂',
     '>',
     '脪𪜝뫨ὣ𪍸昝𠿇𫅸𠘭',
     '¤iDtU¤(t¢Fn',
     'xȶɃᛟŠǷ',
     '𨮤𝞄𩭍쀱𨞻煫묶',
     '¡ScM};(¯',
     '+IGn.JRB',
     '#g',
     'woqt*%lxY@']

@functools.total_ordering
class OrderedThing(object):
    allow_hashing = False

    def __init__(self, data):
        self.data = data

    @property
    def _sum(self):
        return sum(ord(c) for c in self.data)

    def __eq__(self, other):
        if not isinstance(other, OrderedThing):
            return NotImplemented
        return self._sum == other._sum

    def __lt__(self, other):
        if not isinstance(other, OrderedThing):
            return NotImplemented
        return self._sum < other._sum

    def __hash__(self):
        if self.allow_hashing:
            return hash(self._sum)
        else:
            raise TypeError("OrderedThing is not hashable")

    def __repr__(self):
        return "<{} {}>".format(self.__class__.__name__, self._sum)
    def __str__(self):
        return "{}([{}])".format(self.__class__.__name__, self._sum)

@contextmanager
def hashable_OrderedThing():
    OrderedThing.allow_hashing = True 
    try:
        yield None
    finally:
        OrderedThing.allow_hashing = False 

def get_attrs(obj, attrs):
    return tuple(getattr(obj, a) for a in attrs if hasattr(obj, a))


class Assignment5Tests(unittest.TestCase):
    shuffled_list = _shuffled_list
    strings_list = _strings_list
    
    def setUp(self):
        super().setUp()
        sys.stdout.flush()
        sys.stderr.flush()

    def float_key_td(self):
        return self.make_treedict((float(i/19), chr(i)) for i in self.shuffled_list)
    def large_str_key_td(self):
        return self.make_treedict((s, s and ord(s[0])) for s in self.strings_list)
    def custom_key_td(self):
        with hashable_OrderedThing():
            d = dict((OrderedThing(s), s and ord(s[0])) for s in self.strings_list)
        return self.make_treedict(d.items())

    def make_treedict(self, iterable):
        # Test two different ways of making the TreeDict each time.
        iterable = list(iterable)
        assignment5.TreeDict(iter(iterable))
        return assignment5.TreeDict(iterable)

    def treedict_get(self, td, key):
        return td.get(key)

    def int_key_td(self):
        return self.make_treedict((i, str(i)) for i in self.shuffled_list)
    def str_key_td(self):
        return self.make_treedict(({"zero": 0, "one": 1, "two": 2}).items())

    def call_methods(self, td, key, value=None):
        try:
            td[key]
        except Exception:
            self.fail("The key '{}' should exist in TreeDict".format(key))
        if value is not None:
            self.assertEqual(td[key], value)
        td[key] = 1
        td[key]
        td.get(key)
    
    def test_construct_empty(self):
        td = assignment5.TreeDict()
        td["1"] = 1
        td["1"]
        td.get("1")        
        
    def test_construct_unordered_pairs(self):
        self.call_methods(assignment5.TreeDict((i, str(i)) for i in self.shuffled_list), 1, "1")
        
    def test_construct_ordered_pairs(self):
        self.call_methods(assignment5.TreeDict((i, str(i)) for i in range(1, 101)), 2, "2")
        
    def test_construct_dict(self):
        self.call_methods(assignment5.TreeDict({1: "1", 2: "2"}), 2, "2")
        self.call_methods(assignment5.TreeDict({"1": "1", "2": "2"}), "1", "1")

    def test_construct_td(self):
        self.call_methods(assignment5.TreeDict(self.int_key_td()), 2, "2")
        self.call_methods(assignment5.TreeDict(self.str_key_td()), "one", 1)

    def test_construct_order_unimportant(self):
        td1 = assignment5.TreeDict((i, str(i)) for i in self.shuffled_list)
        td2 = assignment5.TreeDict((i, str(i)) for i in range(1, 101))
        self.assertEqual(self.treedict_get(td1, 2), "2")
        self.assertEqual(self.treedict_get(td2, 2), "2")
        self.assertTrue(all(self.treedict_get(td1, i) == self.treedict_get(td2, i)
                            for i in range(110)))

    def test_index1(self):
        self.assertEqual(self.int_key_td()[50], "50")
    def test_index2(self):
        self.assertEqual(self.str_key_td()["zero"], 0)

    def test_set_add(self):
        td = self.int_key_td()
        td[1000] = 5
        self.assertEqual(self.treedict_get(td, 1000), 5)
    def test_set_overwrite(self):
        td = self.int_key_td()
        td[30] = 3
        self.assertEqual(self.treedict_get(td, 30), 3)

    def test_in1(self):
        self.assertIn(10, self.int_key_td())
        self.assertNotIn(110, self.int_key_td())
        self.assertTrue(hasattr(self.int_key_td(), "__contains__"))
        
    def test_in2(self):
        self.assertIn("two", self.str_key_td())
        self.assertNotIn("Two", self.str_key_td())
        self.assertTrue(hasattr(self.str_key_td(), "__contains__"))

    def test_get_exists(self):
        self.assertEqual(self.int_key_td().get(50), "50")
        self.assertEqual(self.int_key_td().get(50, "Not this"), "50")
    def test_get_nonexists(self):
        self.assertEqual(self.int_key_td().get(500), None)
    def test_get_default(self):
        td = self.int_key_td()
        self.assertEqual(td.get(500, 400), 400)
        self.assertEqual(td.get(500), None)
        self.assertEqual(td.get(77, 400), "77")
        self.assertEqual(td.get(77), "77")
        td = self.str_key_td()
        self.assertEqual(td.get("Three", 400), 400)
        self.assertEqual(td.get("three"), None)
        self.assertEqual(td.get("two", 400), 2)
        self.assertEqual(td.get("two"), 2)
    def test_get_str_key(self):
        self.assertEqual(self.str_key_td().get("one"), 1)
        self.assertEqual(self.str_key_td().get("zero"), 0)

    def test_update1(self):
        td = self.int_key_td()
        td.update([(10, "ten"), (11, "eleven")])
        self.assertEqual(self.treedict_get(td, 10), "ten")
        self.assertEqual(self.treedict_get(td, 11), "eleven")
        self.assertEqual(self.treedict_get(td, 12), "12")

    def test_len1(self):
        self.assertEqual(len(self.int_key_td()), 100)
        td = self.int_key_td()
        td.update({6: 7, 10000: 100})
        self.assertEqual(len(td), 101)
        self.assertEqual(len(td), 101)
        
    def test_len2(self):
        self.assertEqual(len(self.str_key_td()), 3)
        td = self.str_key_td()
        td["one"] = 3
        self.assertEqual(len(td), 3)
        self.assertEqual(len(td), 3)
        
    def test_len3(self):
        td = assignment5.TreeDict()
        self.assertEqual(len(td), 0)
        td["2"] = 2
        self.assertEqual(len(td), 1)
        self.assertEqual(len(td), 1)

    def test_iterate(self):
        self.assertEqual(list(self.int_key_td()), list(range(1, 101)))
        self.assertEqual(list(self.make_treedict([])), list())
        self.assertTrue(all(x == y
                            for x, y in itertools.zip_longest(self.int_key_td(), range(1, 101))))

    def test_parallel_iterate(self):
        td = self.int_key_td()
        
        for x, y in zip(td, td):
            self.assertEqual(x, y)

        td = self.str_key_td()
        
        i1 = iter(td.items())
        i2 = iter(td.items())
        prev = next(i1)
        for x, y in zip(i1, i2):
            self.assertEqual(prev, y)
            prev = x
            

    def test_items(self):
        self.assertEqual(list(self.int_key_td().items()), [(y, str(y)) for y in range(1, 101)])
        self.assertEqual(list(self.make_treedict([]).items()), list())
        self.assertTrue(all(x == (y, str(y)) 
                            for x, y in itertools.zip_longest(self.int_key_td().items(), range(1, 101))))

    def test_iterate2(self):
        self.assertEqual(list(self.str_key_td()), ["one", "two", "zero"])
        self.assertEqual(list(self.str_key_td().items()), [("one", 1), ("two", 2), ("zero", 0)])

    def test_raises_KeyError(self):
        td = self.str_key_td()
        with self.assertRaisesRegex(KeyError, ".*aaaa.*"):
            td["aaaa"]
        td = self.int_key_td()
        with self.assertRaisesRegex(KeyError, ".*5000.*"):
            td[5000]

    def test_raises_KeyError_understand_regex(self):
        td = self.int_key_td()
        with self.assertRaises(KeyError) as cm:
            td[5000]
        self.assertNotIn(".*", str(cm.exception),
                         "'.*' should not be in your exception message. It's a regular expression. You shouldn't just copy what you see in the "+
                         "tests. Instead you should look up how KeyError is supposed to be used and how other code uses it.")

    def test_raises_on_None_in_get(self):
        def check(td):
            with self.assertRaises((ValueError, TypeError, KeyError)):
                td.get(None)
            with self.assertRaises((ValueError, TypeError, KeyError)):
                td[None]
        check(self.str_key_td())
        check(self.int_key_td())

    def test_raises_on_None_in_update(self):
        with self.assertRaises((ValueError, TypeError, KeyError)):
            assignment5.TreeDict([("sss", 3), (None, 4)])
        def check(td):
            with self.assertRaises((ValueError, TypeError, KeyError)):
                td.update([(None, 4)])
            with self.assertRaises((ValueError, TypeError, KeyError)):
                td[None] = 1
        check(self.str_key_td())
        check(self.int_key_td())

    def test_update_dict(self):
        td = self.float_key_td()
        td.update({10.0: "ten", 11.2: "eleven"})
        self.assertEqual(self.treedict_get(td, 10.0), "ten")
        self.assertEqual(self.treedict_get(td, 11.2), "eleven")

    def test_update_td(self):
        td = self.int_key_td()
        td.update(self.make_treedict({10: "ten", 0: "eleven"}.items()))
        self.assertEqual(self.treedict_get(td, 9), "9")
        self.assertEqual(self.treedict_get(td, 10), "ten")
        self.assertEqual(self.treedict_get(td, 0), "eleven")

    def test_update_bad_argument(self):
        td = self.int_key_td()
        with self.assertRaises(Exception, msg="Update should not accept random values and ignore them. Values that will not work should cause some error."):
            td.update(5)
        with self.assertRaises(Exception, msg="Update should not accept random values and ignore them. You shouldn't just pass a default None value to update. Use () or similar instead."):
            td.update(None)

    def test_str_keys_iterate(self):
        td = self.large_str_key_td()
        pairs = [(s, s and ord(s[0])) for s in self.strings_list]
        self.assertEqual(list(td.items()), sorted(pairs))
        
    def test_str_keys_get(self):
        td = self.large_str_key_td()
        pairs = [(s, s and ord(s[0])) for s in self.strings_list]
        self.assertTrue(all(self.treedict_get(td, k) == v 
                            for k, v in pairs))
        
    def test_custom_keys_iterate(self):
        td = self.custom_key_td()
        with hashable_OrderedThing():
            d = dict((OrderedThing(s), s and ord(s[0])) for s in self.strings_list)
        self.assertEqual(list(td.items()), sorted(d.items()))

    def test_custom_keys_get(self):
        td = self.custom_key_td()
        with hashable_OrderedThing():
            d = dict((OrderedThing(s), s and ord(s[0])) for s in self.strings_list)
        self.assertTrue(all(self.treedict_get(td, k) == v 
                            for k, v in d.items()))
        
    def test_in3(self):
        self.assertIn('즙𩻓槎㰅𤬄', self.large_str_key_td())

    def test_in4(self):
        self.assertIn(78/19, self.float_key_td())

    def test_in_boolean(self):
        self.assertIsInstance(78/19 in self.float_key_td(), bool)
        self.assertIsInstance(10 in self.int_key_td(), bool)
        self.assertIsInstance(110 in self.int_key_td(), bool)

    def test_0_key(self):
        td = self.int_key_td()
        td[0] = 102
        self.assertEqual(self.treedict_get(td, 0), 102)

    def test_0_value(self):
        td = self.int_key_td()
        td[102] = 0
        self.assertEqual(self.treedict_get(td, 102), 0)
        self.assertIn(102, td)

        td = self.int_key_td()
        td[102] = None
        self.assertEqual(self.treedict_get(td, 102), None)
        self.assertIn(102, td)

    def test_none_value(self):
        td = self.int_key_td()
        td[0] = None
        self.assertEqual(self.treedict_get(td, 0), None)
        self.assertEqual(td[0], None)

if __name__ == "__main__":
    unittest.main()
