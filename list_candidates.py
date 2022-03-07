import argparse
import string
import textwrap


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--hits", type=str,
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
    parser.add_argument(
        "-i", action="store_true",
        help="Run this tool in interactive mode"
    )
    args = parser.parse_args()
    return args.hits, args.b, args.m, args.i


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

    words = []
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
                words.append(word)
    return words


def print_n_col(items, cols=10):
    for i, item in enumerate(items):
        print(item, " ", end="")
        if i % cols == cols-1:
            print()
    print()


def prompt_word_length(default_value=5) -> int:
    while True:
        try:
            num_letters = int(
                input(f"Enter number of letters [{default_value}]: ") or default_value)
            return num_letters
        except:
            print("Value must be a integer")


def run_interactive():
    num_letters = prompt_word_length()

    hits = ["."] * num_letters
    blows = set()
    misses = set()

    print(textwrap.dedent("""\

        Input Example:
          Enter your 1st guess      : abcde
          Enter the response (h/b/m): hmbmm

        'h/b/m' stands for:
          hit:  the letter is in correct position,
          blow: the letter is in the word but in wrong position, and
          miss: the letter is not in the word.

        Enter empty string to quit.
    """))

    for i in range(6):

        while True:
            guess = input(f"Enter your {i+1}th guess      : ")
            if not guess:
                return
            if len(guess) != num_letters:
                print(f"Must be {num_letters} letters long")
                continue
            guess = guess.strip().lower()
            break
        while True:
            response = input(f"Enter the response (h/b/m): ")
            if not response:
                return
            if len(response) != num_letters:
                print(f"Must be {num_letters} letters long")
                continue
            response = response.strip().lower()
            break

        for i, (g, r) in enumerate(zip(guess, response)):
            if r == "h":
                hits[i] = g
            elif r == "b":
                blows.add(g)
            else:
                misses.add(g)
        c = list_candidates("".join(hits), blows, misses)
        print_n_col(c)


if __name__ == "__main__":
    hits, blows, misses, interactive = parse_args()
    if interactive:
        run_interactive()
    else:
        candidates = list_candidates(hits, blows, misses)
        print("\n".join(candidates))
