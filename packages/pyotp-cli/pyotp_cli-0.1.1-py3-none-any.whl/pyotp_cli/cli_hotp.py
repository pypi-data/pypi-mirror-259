#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2024-02-26
Purpose: Get OTP Using HOTP
"""

import argparse
from pathlib import Path


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Get OTP Using HOTP",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("secret", metavar="SECRET", help="Secret")
    parser.add_argument("count", metavar="COUNT", type=int, help="Counter value")
    parser.add_argument(
        "-d",
        "--digits",
        metavar="DIGITS",
        type=int,
        default=6,
        help="Number of digits",
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    from utils import get_hotp

    otp = get_hotp(args.secret, args.count, args.digits)
    print(otp, end="")


if __name__ == "__main__":
    main()
