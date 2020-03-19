import random
import string
import argparse as agp

parser = agp.ArgumentParser()
parser.add_argument("--size", "-S", default="8", help="size of the password", type=int)
args = parser.parse_args()

charset = string.ascii_letters + string.digits + string.punctuation
print(''.join(random.choice(charset) for _ in range(int(args.size))))