#!/usr/bin/env python3
import argparse, sys, os
ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)
from phone import lookup_phone
from ip import lookup_ip
from instagram import lookup_instagram
from utils import load_config

def main():
    parser = argparse.ArgumentParser(prog="Faruk-OSINT", description="Faruk-OSINT CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    p_phone = sub.add_parser("phone", help="Lookup phone number")
    p_phone.add_argument("number", help="+905xxxxxxxxx")
    p_ip = sub.add_parser("ip", help="Lookup IP")
    p_ip.add_argument("ip", help="8.8.8.8 or domain")
    p_insta = sub.add_parser("insta", help="Lookup Instagram public profile")
    p_insta.add_argument("username", help="instagram username")
    args = parser.parse_args()
    config = load_config()
    if args.command == "phone":
        print(lookup_phone(args.number, config))
    elif args.command == "ip":
        print(lookup_ip(args.ip, config))
    elif args.command == "insta":
        print(lookup_instagram(args.username, config))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
