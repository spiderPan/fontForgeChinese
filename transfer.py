#! /usr/bin/env python
import fontforge
import argparse
import codecs

# return the character set from the given file
# file should be utf-8 encoded
def get_character_set(fname):
    with codecs.open(fname, encoding='utf-8') as f:
        return f.read()

def build_ttf(source_ttf_fname, dest_ttf_fname, char_set_fname):
    char_set = get_character_set(char_set_fname)
    source_font = fontforge.open(source_ttf_fname)
    # select characters
    for c in char_set:
        source_font.selection.select(("more", None), ord(c))
    source_font.selection.invert()
    # remove all characters we're not interested in
    for glyph in source_font.selection:
        try:
            source_font.removeGlyph(glyph)
        except ValueError:
            pass
    source_font.generate(dest_ttf_fname)
    source_font.close()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_ttf', help='source ttf')
    parser.add_argument('dest_ttf', help='lite ttf')
    parser.add_argument('char_set', help='lite character set')
    return parser.parse_args()

if __name__ == '__main__':
    namespace = parse_args()
    build_ttf(namespace.source_ttf, namespace.dest_ttf, namespace.char_set)
