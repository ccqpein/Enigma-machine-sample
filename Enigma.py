#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Hardware import Rotors, Reflector


def buildEnigma():
    rotor1 = Rotors(1)
    rotor2 = Rotors(2)
    rotor3 = Rotors(3)
    # todo: make the rotor making function
    rotorChain = [rotor1, rotor2, rotor3]
    reflector = Reflector("R")  # reflector can be thought a rotor
    return(rotorChain, reflector)

rotorChain, reflector = buildEnigma()


def encryptProcess(string):
    global rotorChain, reflector
    for rotor in rotorChain:
        string = rotor.encrypt(string)

    string = reflector.encrypt(string)

    for rotor in reversed(rotorChain):
        string = rotor.encrypt(string)

    print(string)
    return string
