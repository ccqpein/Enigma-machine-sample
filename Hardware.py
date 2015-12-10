#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

originalKey = ["a", "b", "c", "d", "e", "f", "g",
               "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]


class Rotors(object):

    def __init__(self, *args):
        self.originalDict = [i for i in originalKey]
        random.shuffle(self.originalDict)
        self.originalKey = []

        for i in reversed(self.originalDict):
            self.originalKey.append(i)

        self.__rotorId__ = args[0]
        self.__position__ = 0
        # print(self.originalKey)
        # print(self.originalDict)

    def encrypting(self):  # can make a doEncrypt function, and use encrypt methon to change rotors
        unoriginalDict = self.originalDict[self.__position__:]
        unoriginalDict = unoriginalDict + self.originalDict[:self.__position__]
        self.__position__ += 1
#        print(unoriginalDict, self.__position__)
        encryptDict = dict(zip(self.originalKey, unoriginalDict))
        print(self. originalDict, unoriginalDict)
        return encryptDict

    def doEncrypt(self, string):
        string = string.lower()
        encryptString = ""

        encrypting(self)
        for i in string:
            try:
                encryptString += encryptDict[i]
            except KeyError:
                encryptString += i
        print(encryptDict)
        return encryptString


class Reflector(object):

    def __init__(self, *args):
        self.originalDict = [i for i in originalKey]
        self.__RefId__ = args[0]

        random.shuffle(self.originalDict)
        self.originalKey = []

        for i in reversed(self.originalDict):
            self.originalKey.append(i)

    def encrypt(self, string):
        encryptDict = dict(zip(self.originalKey, self.originalDict))

        encryptString = ""
        for i in string:
            try:
                encryptString += encryptDict[i]
            except KeyError:
                encryptString += i
        print(encryptDict)
        return encryptString
