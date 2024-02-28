# pyvecc

## Elliptic curve FIPS 186-3

Cloned from the ecc project

Pure Python implementation of an elliptic curve cryptosystem based on FIPS 186-3
Cloned from the ecc project

This is an adaptation from the original to Python Version 3.
Also added test suite.

### Timings / Performance:

    Key generation

    192 bits     0.15692 seconds   637.26951/sec
    224 bits     0.19632 seconds   509.36798/sec
    256 bits     0.25150 seconds   397.61599/sec
    384 bits     0.53108 seconds   188.29529/sec
    521 bits     1.10281 seconds    90.67742/sec

    Signing

    192 bits     0.16258 seconds   615.06642/sec
    224 bits     0.21078 seconds   474.42906/sec
    256 bits     0.26684 seconds   374.75208/sec
    384 bits     0.54190 seconds   184.53698/sec
    521 bits     1.08671 seconds    92.02118/sec

    Verifying

    192 bits     0.20362 seconds   491.11330/sec
    224 bits     0.26438 seconds   378.24961/sec
    256 bits     0.31328 seconds   319.20826/sec
    384 bits     0.68741 seconds   145.47447/sec
    521 bits     1.39412 seconds    71.72986/sec

    Encrypting

    192 bits     0.00326 seconds  30689.28075/sec
    224 bits     0.00410 seconds  24365.65586/sec
    256 bits     0.00512 seconds  19532.92041/sec
    384 bits     0.01096 seconds  9122.01827/sec
    521 bits     0.02173 seconds  4601.03554/sec

    Decrypting

    192 bits     0.00178 seconds  56306.94053/sec
    224 bits     0.00220 seconds  45407.64317/sec
    256 bits     0.00268 seconds  37302.59694/sec
    384 bits     0.00549 seconds  18230.55592/sec
    521 bits     0.01075 seconds  9300.21508/sec

### Getting Started

    org2 = Random.new().read(80)
    org = base64.b64encode(org2)

        ttt = time.time()
        k = Key.generate(256)
        print("key gen time %.3fms" % ((time.time() - ttt) * 1000) )

        print("org:")
        print(org2)
        ttt = time.time()
        sss = k.encrypt(org)
        print("encrypt time %.3fms" % ((time.time() - ttt) * 1000) )

        ttt = time.time()
        ddd = k.decrypt(sss)
        print("decypt time %.3fms" % ((time.time() - ttt) * 1000) )

        ddd2 = base64.b64decode(ddd)
        print("dec:")
        print(ddd2)

### The above command will print:

    key gen time 2.669ms
    org:
    b'\xdb\xef\xcf\xdc\xc3\x03\x0e\xfd\x05\x9c\x8b\xba\xa8\x05\x0e\xd7\x9d(1\xb2\x80\x80t\xd05\xed\x8f\xa4\x81\xa7'
    encrypt time 5.411ms
    decypt time 2.803ms
    dec:
    b'\xdb\xef\xcf\xdc\xc3\x03\x0e\xfd\x05\x9c\x8b\xba\xa8\x05\x0e\xd7\x9d(1\xb2\x80\x80t\xd05\xed\x8f\xa4\x81\xa7'

#### PyTest results
    ============================= test session starts ==============================
    platform linux -- Python 3.10.12, pytest-7.4.3, pluggy-1.0.0
    rootdir: /home/peterglen/pgpygtk/pyvecc
    collected 2 items

    test_encdec.py .                                                         [ 50%]
    test_gen.py .                                                            [100%]


### Revisions:

    rev 0.0.2  Tue 27.Feb.2024     Initial

## Errata:

  Ported from Python 2 ... Not all is carried over. This port is not 8 bit clean
but can be used with a help of hexify utils like base64.

// EOF
