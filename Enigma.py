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


def encryptProcess(string, position):
    global rotorChain, reflector
    for rotor in rotorChain:
        string = rotor.doEncrypt(string, position)

    string = reflector.encrypt(string)

    for rotor in reversed(rotorChain):
        string = rotor.doEncrypt(string, position)

    print(string)
#    return string


def encryptInput():
    code = raw_input("put string want to code \n")
    return code


if __name__ == '__main__':
    encryptProcess(encryptInput(), position=0)
