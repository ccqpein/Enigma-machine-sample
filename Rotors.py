#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

originalKey = ("a", "b", "c", "d", "e", "f", "g",
               "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z")


class Rotors(object):

    def __init__(self):
        self.originalDict = [i for i in originalKey]
        random.shuffle(self.originalDict)

        self.originalKey = originalKey
        # print(self.originalKey)
        # print(self.originalDict)

    def encrypt(self, string):
        string = string.lower()
        encryptDict = dict(zip(self.originalKey, self.originalDict))

        encryptString = ""
        for i in string:
            try:
                encryptString += encryptDict[i]
            except KeyError:
                encryptString += i
        # print(encryptDict)
        return encryptString
