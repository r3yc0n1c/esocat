#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import json

__author__  = 'Raja Majumdar'
__version__ = '0.1.0'
__email__   = '0xsr1337@gmail.com'
__github__  = 'https://github.com/r3yc0n1c/esocat'


IN = json.load(open('interpreters.json'))
BANNER = open('banner.txt').read()

# class Detect

def malbolge(payload):
    charset = base64.b64decode(
        "OW08LlRWYWNgdVkqTUsnWH54RGx9UkVva046Iz9HImlANXpdJmdxdHlmciQod2U0e1dQKUgtWm4sWyVcM2RMK1E7PlUhcEpTNzJGaE9BMUNCNnZePUlfMC84fGpzYg=="
        ).decode()

    if check(payload, charset):
        return IN["malbolge"]

def moo(payload):
    charset = ['moo', 'mOo', 'moO', 'mOO', 'Moo', 'MOo', 'MoO', 'MOO', 'OOO', 'MMM', 'OOM', 'oom']
    if check(payload.split(), charset):
        return IN["cow"]

def pikalang(payload):
    charset = ["pi", "ka", "pipi", "pichu", "pika", "chu", "pikachu", "pikapi"]
    if check(payload.split(), charset):
        return IN["pikalang"]

def brainfuck(payload):
    charset = "><+-.,[]"
    if check(payload, charset) and payload.count('[')==payload.count(']'):
        return IN['brainfuck']

def jsfuck(payload):
    charset = "[]()!+"
    if check(payload, charset):
        return IN["jsfuck"]

def binaryfuck(payload):
    charset = "01"
    if check(payload, charset):
        return IN['binaryfuck']

def ook(payload):
    charset = "Ook!.? "
    try:
        payload = payload.replace('Ook', '')
        if check(payload, charset[3:]):
            return IN["ook"]
    except:
        return None

def alphuck(payload):
    charset = "aceijops"
    if check(payload, charset):
        return IN["alphuck"]

def deadfish(payload):
    charset = "idso"
    c = {x:payload.count(x) for x in charset}
    if check(payload, charset) and c['i']+c['d'] >= c['o']+c['s']:
        return IN["deadfish"]

def check(payload, charset):
    for character in payload:
        if character not in charset:
            return False
    return True


def detect(payload):
    print(BANNER)

    payload = payload.strip() # sanitize

    esolangs = [
            brainfuck, jsfuck, binaryfuck, alphuck, deadfish, ook,
            pikalang, moo, malbolge
            ]

    print("\n[+] Possible Esolangs:\n")

    flag = 0
    for checkEso in esolangs:
        res = checkEso(payload)
        if res:
            flag = 1
            print('[+]', res)
    
    if not flag:
        print('[x] Result: None! New Esolang?')
