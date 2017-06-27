#!/usr/bin/python2.7

# given an english phrase, how many valid english phrases can be generated
# by changing n number of letters?
#
# This does not scale well. Can you do better?

# another way to get the english dictionary:
# aspell -d en dump master |
# aspell -l en expand |
# sed "s/[^[:alpha:]\s]//g"

# DICTIONARY_PATH = '/usr/share/dict/cracklib-small'
DICTIONARY_PATH = '~/words.txt'

class CompoundLofts:
  chars = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

  def __init__(self, dict_path):
    self.lang_dict = self.read_dict_file(dict_path)

    self.swap_limit = None
    self.phrase = None
    self.orig_phrase = None

  def read_dict_file(self, dict_path):
    lang_dict = {}

    with open(dict_path, 'r') as dict_fp:
      for line in dict_fp.read().splitlines():
        lang_dict[line.strip().lower()] = True

    return lang_dict

  # probably faster to write over the same string repeatedly,
  # rather then hammering the gc with copies
  def restore_phrase(self, index):
    for i in range(index, len(self.phrase)):
      self.phrase[i] = self.orig_phrase[i]

  def test_phrase(self):
    phrase_str = ''.join(self.phrase)
    words = phrase_str.split(' ')

    for word in words:
      if word not in self.lang_dict:
        return

    print phrase_str

  def test_recursive(self, index, swapped):
    if index >= len(self.phrase) or swapped == self.swap_limit:
      return

    start_char = self.phrase[index]

    for c in self.chars:
      self.phrase[index] = c

      if c == start_char:
        # no need to test phrase if unchanged
        self.test_recursive(index + 1, swapped)
      else:
        self.test_phrase()
        self.test_recursive(index + 1, swapped + 1)

      self.restore_phrase(index + 1)

  def test(self, phrase, swap_limit):
    self.swap_limit = swap_limit
    self.phrase = list(phrase)
    self.orig_phrase = list(phrase)

    return self.test_recursive(0, 0)

c = CompoundLofts('/usr/share/dict/cracklib-small')
c.test('compound lifts', 2)
