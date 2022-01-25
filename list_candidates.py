import argparse
import string


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "hits", type=str,
        help="Letters in correct positions. Denote unknown with '.'.  ex. '..ol.'"
    )
    parser.add_argument(
        "-b", type=str, default="", metavar="BLOWS",
        help="Letters included but in wrong positions. ex. 'n'"
    )
    parser.add_argument(
        "-m", type=str, default="", metavar="MISSES",
        help="Letters not included. ex. 'whetsqueryidac'"
    )
    args = parser.parse_args()
    return args.hits, args.b, args.m


def list_candidates(hits, blows, misses):
    """List candidates according to the clues given.

    1.  skip words with different length
    2.  skip if blows are missing
    3.  skip if hits don't hit
    4.  skip if misses are included
    5.  what's left are the candidates
    """
    length = len(hits)

    misses = set(misses)
    alphabets = set(string.ascii_lowercase)
    candidates = alphabets - misses

    blows = set(blows)

    with open("words.txt") as f:
        for word in f:
            word = word.strip().lower()
            # skip words with different length
            if len(word) != length:
                continue
            # skip if blows are missing
            if blows - set(word):
                continue
            for char, hit in zip(word, hits):
                # skip if hits don't hit
                if hit != '.':
                    if char != hit:
                        break
                # skip if misses are included
                else:
                    if char not in candidates:
                        break
            else:
                # print a candidate
                print(word)


if __name__ == "__main__":
    list_candidates(*parse_args())
