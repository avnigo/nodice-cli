from nodice.diceware import Diceware
from nodice.cli import parser


def main():
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
        generate_keys=args.make_custom,
    )

    if args.verbose:
        print(passphrase)


if __name__ == "__main__":
    main()
