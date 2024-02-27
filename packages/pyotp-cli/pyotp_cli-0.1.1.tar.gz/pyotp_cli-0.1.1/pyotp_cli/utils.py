def get_hotp(secret, count, digits: int = 6) -> str:
    import pyotp

    hotp = pyotp.HOTP(secret, digits=digits)
    return hotp.at(count)
