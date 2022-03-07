# wordle-candidates-viewer

## Warning

Use this **ONLY AFTER** solving it by yourself.  
Using this tool to solve a Wordle game is **NOT ALLOWED**.

## Description

Outputs list of candidates for a Wordle game based on the given clues.

It's useful when:

1. you want to know where you could have done better, or
1. you want to expand your vocabulary.

## Usage

1. Get a word list of your choice, name it 'words.txt',
    and place it in the root directory.

    The list should be a '\\n' separated list of words.
    I got mine from [here](https://svnweb.freebsd.org/csrg/share/dict/).

1. Run `python list_candidates.py`.
    The arguments are listed below.

    ```
    usage: list_candidates.py [-h] [-b BLOWS] [-m MISSES] hits

    positional arguments:
    hits        Letters in correct positions. Denote unknown with '.'. ex. '..ol.'

    optional arguments:
    -h, --help   show this help message and exit
    --hits HITS  Letters in correct positions. Denote unknown with '.'. ex. '..ol.'
    -b BLOWS     Letters included but in wrong positions. ex. 'n'
    -m MISSES    Letters not included. ex. 'whetsqueryidac'
    -i           Run this tool in interactive mode
    ```

## Example

https://www.reddit.com/r/wordlegame/comments/sbaahp/i_gave_up_on_this_one_what_would_you_guess/

```
> python list_candidates.py --hits ..... -b u -m adie
bluff
blunt
blurb
...
# this gives you a lot of candidates...

> python list_candidates.py --hits ....y -b u -m adiecomf
buggy
bulky
bully
...
# still a lot...
# but if you look closely at the list,
# most candidates have 'u' on the second letter.
# therefore, guessing a word with second letter 'u' might be a good move.
# if it hits, you know that 'u' does go there.
# if it does not hit, you are left with only two candidates.

> python list_candidates.py --hits ...py -b u -m adiecomftras
puppy
# now you are left with only one.
# you know that this guy could have won the game in just 4 tries.
```