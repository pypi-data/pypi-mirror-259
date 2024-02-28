#!/usr/bin/python
# coding=utf-8

import pytest, os, sys
from mytest import *

from Crypto import Random

priv = '''\
-----BEGIN PRIVATE ECC-----
w4Yow4fDpsOSwqvDk3wBAABAw7wpSQNOKsOqLwjDilTDglTCv8OfDBhCw6JTBkUxw4HDscKcw53CqTImX3vDhsOUMVnCrAjClcK8wqzDt8O4O8KFb2IKPi1bfMK0wqfCqsKzW8KEXsOSw5HDrcKdLAAgM8Oye8OWWcKXOSjDjSXCucKrGsOww7DDncKYw7cxRMOFwrsiwp3Cn8KuwrM3dcKkwpMj
-----END PRVATE ECC-----'''
pub = '''\
-----BEGIN PUBLIC ECC-----
w4Yow4fDpsOSwqvDk3wBAABAw7wpSQNOKsOqLwjDilTDglTCv8OfDBhCw6JTBkUxw4HDscKcw53CqTImX3vDhsOUMVnCrAjClcK8wqzDt8O4O8KFb2IKPi1bfMK0wqfCqsKzW8KEXsOSw5HDrcKdLAAA
-----END PUBLIC ECC-----'''

fp = b'\xc6(\xc7\xe6\xd2\xab\xd3|\x9f\xda\x8cj0\xc7\x98\xa14\xa6\x86\xce'

def test_func(capsys):

    k = Key.generate(256)

    assert k.validate() == True

    kk = Key.import_priv(priv)
    assert kk.validate() == True
    assert kk.fingerprint() == fp
    assert kk.private() == True

    #print (kk.export_pub())
    kkk = Key.import_pub(pub)
    assert kkk.validate() == True
    assert kkk.fingerprint() == fp
    assert kkk.private() == False

    pub2 = kkk.export_pub()
    #print(pub); print(pub2)
    assert pub == pub2

    priv2 = kk.export_priv()
    #print(priv); print(priv2)
    assert priv == priv2

    #assert 0
