import argparse

parser = argparse.ArgumentParser(description='Short sampleapp')

parser.add_argument('-a', action="store_true", default=False)

parser.add_argument('-b', action="store", dest="b")

parser.add_argument('-c', action="store", dest="c", type=int)

args = parser.parse_args(['-a', '-bval', '-c', '3'])
print(args)
print(args.a)
