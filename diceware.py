import argparse
import math
import random

from dataclasses import dataclass
from pathlib import Path

CRLF = "\n"


@dataclass
class Diceware:
    file: Path
    entropy: int | None
    num_dice: int
    num_sides: int
    num_words: int = 5
    delimiter: str = "\t"
    spacer: str = " "
    no_words: bool = False

    def __post_init__(self):
        self.wordlist = self.build_dict(self.file, self.delimiter)

        if self.wordlist:
            self.num_dice = len(next(iter(self.wordlist.keys())))
            self.wordlist_length = len(self.wordlist)
            self.numwords_for_entropy(self.wordlist_length, self.entropy)

        self.rolls = self.roll_dice(self.num_words, self.num_dice, self.num_sides)
        self.print_rolled_words(self.rolls, self.wordlist, self.spacer)
        del self.rolls

    def build_dict(self, file: Path, delimiter: str) -> dict[str, str] | None:
        return (
            {
                roll: word
                for roll, word in (
                    line.split(delimiter)
                    for line in file.read_text().split(CRLF)
                    if self.delimiter in line
                )
            }
            if not self.num_dice or not self.num_sides
            else None
        )

    def roll_dice(self, num_words: int, num_dice: int, num_sides: int) -> list[str]:
        return [
            "".join(
                f"{random.SystemRandom().randint(1, num_sides)}"
                for _ in range(num_dice)
            )
            for _ in range(num_words)
        ]

    def print_rolled_words(self, rolls, wordlist, spacer):
        for index, roll in enumerate(rolls):
            print(
                wordlist.get(roll, "NULL")
                if (self.wordlist and not self.no_words) or not self.num_dice
                else roll,
                end=CRLF if index + 1 == self.num_words else spacer,
                # flush=True,
            )

    def numwords_for_entropy(self, wordlist_length: int, min_entropy: int | None):
        if min_entropy:
            self.num_words = int(math.ceil(min_entropy / math.log(wordlist_length, 2)))

    def calc_entropy(self) -> float:
        return math.log(self.wordlist_length, 2) * self.num_words

    def __repr__(self):
        return (
            (
                f"{CRLF}> {self.num_words} random words from a {self.wordlist_length}-word list "
                f"yield {self.calc_entropy():.1f} bits of entropy."
            )
            if self.wordlist
            else "No words found."
        )


def parser():
    parser = argparse.ArgumentParser(
        description="Generate diceware passphrases from wordlists.",
    )
    parser.add_argument(
        "--words",
        "-w",
        help="number of words (default: `%(default)s`)",
        default=5,
        type=int,
    )
    parser.add_argument(
        "--entropy", "-e", help="set minimum bits of entropy", default=0, type=int
    )
    parser.add_argument(
        "--spacer",
        "-s",
        help="separate words with a spacer (default: `%(default)s`)",
        type=str,
        default=" ",
    )
    parser.add_argument(
        "--dice",
        "-d",
        help="number of dice per word; ignores --file and --entropy options (default based on wordlist)",
        default=0,
        type=int,
    )
    parser.add_argument(
        "--sides",
        "-D",
        help="number of sides per die (default: `%(default)s`)",
        default=6,
        type=int,
    )
    parser.add_argument(
        "--show-rolls",
        "-r",
        help="show dice rolls only",
        action="store_true",
    )
    parser.add_argument(
        "--file",
        "-f",
        help="diceware dictionary file (default: `%(default)s`)",
        default=Path("./wordlists/eff_large_wordlist.txt"),
        type=Path,
    )
    parser.add_argument(
        "--delimiter",
        "-t",
        help="dictionary delimiter (default: $'\\t')",
        type=str,
        default="\t",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        help="show entropy information",
        action="store_true",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parser()

    passphrase = Diceware(
        file=args.file,
        entropy=args.entropy,
        delimiter=args.delimiter,
        spacer=args.spacer,
        num_dice=args.dice,
        num_sides=args.sides,
        num_words=args.words,
        no_words=args.show_rolls,
    )

    if args.verbose:
        print(passphrase)
