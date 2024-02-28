#!/usr/bin/python
# coding=utf-8

import pytest, os, sys, base64
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

cypher = b'AEAyZWdqwrJ4wrddw6RScMOhwqQ8C8OKUMKrw5x5wq0bCsOTS2obL0hCWQnCpsKZPsOgw7LDhTLDvMKIAV8dfTjCncKIXjBFw7EqwqNRd1cMQTIcKVPDhwAAABhKV8OIwrrCrjRtLkB9w6TDtC3Dt8KeBcO6Y8O6wrgww5LDp8OQ'


org2 = b"1234567890abcdef"
org = base64.b64encode(org2)

def test_func(capsys):

    kk = Key.import_priv(priv)
    assert kk.validate() == True
    assert kk.fingerprint() == fp
    assert kk.private() == True

    kkk = Key.import_pub(pub)
    assert kkk.validate() == True
    assert kkk.fingerprint() == fp
    assert kkk.private() == False

    eee = kkk.encrypt(org)
    assert cypher, base64.b64encode(eee.encode())
    ddd = kk.decrypt(eee)
    assert org2, ddd

    #print(ddd)
    #assert 0
