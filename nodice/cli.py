import argparse
from pathlib import Path


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
        help=(
            "number of dice per word; ignores --file and --entropy options"
            "(default based on wordlist)"
        ),
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
        "--make-custom",
        "-m",
        help="generate keys (dice rolls) for custom wordlist",
        action="store_true",
    )
    parser.add_argument(
        "--file",
        "-f",
        help="diceware dictionary file (default: `%(default)s`)",
        default=Path(__file__).parent / "wordlists/eff_large_wordlist.txt",
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
