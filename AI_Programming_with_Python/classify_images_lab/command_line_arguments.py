"""
Create by Killer at 2019-04-25 15:19
"""

import argparse

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--dir", type=str, default="my_folder/", help="path to the folder my_folder")

    parser.add_argument("--num", type=int, default=1, help="Number (integer) input")

    in_args = parser.parse_args()

    print("Argument 1:", in_args.dir, " Argument 2:", in_args.num)


if __name__ == "__main__":
    main()