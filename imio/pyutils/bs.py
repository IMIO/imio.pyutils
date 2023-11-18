#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# bs4 utility methods
# IMIO <support@imio.be>
#
from bs4 import BeautifulSoup
from bs4.element import Comment

import re


def remove_attributes(element, attributes=[], recursive=True):
    """ Removes attributes on given element or recursively """
    elements = [element]
    if recursive:
        elements += element.find_all()
    for tag in elements:
        for attr in attributes:
            try:
                del tag[attr]
            except KeyError:
                pass


def remove_childrens_by_pattern(parent, child_text_pat, name=None, recursive=False, keep=()):
    """Remove children with matched text

    :param parent: parent to consider
    :param child_text_pat: pattern to search
    :param name: optional children's tag
    :param recursive: recursive children
    :param keep: keep children at this position (starting at 1)
    :return:
    """
    childrens = list(parent.find_all(name=name, recursive=recursive))
    if isinstance(parent, BeautifulSoup):
        childrens.pop(0)
    removed = []
    change = False
    count = 0
    for ch_t in childrens:
        if found := re.search(child_text_pat, ch_t.text, re.I):
            count += 1
            if count not in keep:
                change = True
                removed.append(str(ch_t))
                ch_t.decompose()
    return change, removed


def remove_comments(element):
    """ Removes html comments """
    for comment in element.find_all(text=lambda text: isinstance(text, Comment)):
        comment.extract()


def remove_elements(element, to_remove=[]):
    """ Removes sub tags and all their content """
    for tagtr in to_remove:
        for tag in element.find_all(tagtr):
            tag.decompose()


def replace_entire_strings(element, replace=u'\n', by=u''):
    """ Replaces an entire string by another value. With default params, removes newlines """
    # reversed needed to avoid internal strings error
    strings = reversed([s for s in element.strings])
    for string in strings:
        if string == replace:
            string.replace_with(by)


def replace_strings_by_pattern(element, find_pat, replace_pat):
    """Replace element strings

    :param element: element to ocnsider
    :param find_pat: pattern to find
    :param replace_pat: replacement pattern
    :return: replaced strings
    """
    replaced = []
    # reversed needed to avoid internal strings error
    strings = list(reversed([s for s in element.strings]))
    for string in strings:
        if found := re.search(find_pat, string, re.I):
            new_val = re.sub(find_pat, replace_pat, string, re.I)
            replaced.append("'{}' => '{}'".format(string, new_val))
            string.replace_with(new_val)
    return replaced


def unwrap_tags(element, tags=[]):
    """ unwrap tags on content (<a ...>lien</a> => lien) """
    for tagtu in tags:
        for tag in element.find_all(tagtu):
            tag.unwrap()
