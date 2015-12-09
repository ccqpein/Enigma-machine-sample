#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Rotors import Rotors


def main():
    rotor1 = Rotors()
    rotor2 = Rotors()
    rotor3 = Rotors()
    print(rotor1.encrypt("LOL"))
