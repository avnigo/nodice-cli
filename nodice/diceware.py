import math
import random
from dataclasses import dataclass
from itertools import product
from os import linesep
from pathlib import Path


@dataclass
class Diceware:
    file: Path
    entropy: int
    num_dice: int
    num_sides: int
    num_words: int
    delimiter: str
    spacer: str
    custom_rolls: tuple = ()
    no_words: bool = False
    generate_keys: bool = False

    def __post_init__(self):
        self.wordlist = self.build_dict(self.file, self.delimiter)

        if self.generate_keys and self.wordlist:
            self.print_custom_rolls(self.wordlist)

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
                    if self.delimiter in line
                    else self.get_roll_pair(index, line)
                    for index, line in enumerate(file.read_text().splitlines())
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

    def numwords_for_entropy(self, wordlist_length: int, min_entropy: int) -> None:
        if min_entropy != 0:
            self.num_words = int(math.ceil(min_entropy / math.log(wordlist_length, 2)))

    def calc_entropy(self) -> float:
        return math.log(self.wordlist_length, 2) * self.num_words

    @staticmethod
    def find_factor_pairs(num_words: int) -> tuple:
        # TODO: Fix case where num_words is not a perfect power (clip to nearest lowest)
        # TODO: Fix case where num_words has sides > 9 (e.g. 2500) because concatenation
        return min(
            (sides, dice)
            for sides, dice in product(range(2, math.isqrt(num_words) + 1), repeat=2)
            if sides**dice == num_words
        )

    def create_custom_rolls(self) -> tuple:
        self.num_sides, self.num_dice = self.find_factor_pairs(
            len(self.file.read_text().splitlines())
        )
        return tuple(product(range(1, self.num_sides + 1), repeat=self.num_dice))

    def print_custom_rolls(self, wordlist: dict) -> None:
        for rolls, word in wordlist.items():
            print(f"{rolls}{self.delimiter}{word}")
        raise SystemExit

    def get_roll_pair(self, index: int, word: str) -> tuple:
        if not self.custom_rolls:
            self.custom_rolls = self.create_custom_rolls()
        return ("".join(map(str, self.custom_rolls[index])), word)

    def print_rolled_words(self, rolls, wordlist, spacer) -> None:
        for index, roll in enumerate(rolls):
            print(
                wordlist.get(roll, "NULL")
                if (self.wordlist and not self.no_words) or not self.num_dice
                else roll,
                end=linesep if index + 1 == self.num_words else spacer,
                flush=True,
            )

    def __repr__(self):
        return (
            (
                f"{linesep}> {self.num_words} random words from a "
                f"{self.wordlist_length}-word list yield {self.calc_entropy():.1f} "
                f"bits of entropy."
            )
            if self.wordlist
            else "No words found."
        )
