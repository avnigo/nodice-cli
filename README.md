# simple-diceware

Yet another diceware passphrase generator.

# Usage

```console
$ python diceware.py --help
usage: diceware.py [-h] [--file FILE] [--words WORDS] [--delimiter DELIMITER] [--spacer SPACER] [--entropy ENTROPY] [--dice DICE] [--show-rolls] [--verbose]

Generate diceware passphrases from wordlists.

options:
  -h, --help                            show this help message and exit
  --file FILE, -f FILE                  diceware dictionary file (default: `wordlists/eff_large_wordlist.txt`)
  --words WORDS, -w WORDS               number of words (default: `5`)
  --delimiter DELIMITER, -t DELIMITER   dictionary delimiter (default: $'\t')
  --spacer SPACER, -s SPACER            separate words with a spacer (default: ` `)
  --entropy ENTROPY, -e ENTROPY         set minimum bits of entropy
  --dice DICE, -d DICE                  number of dice per word; ignores --file and --entropy options
  --show-rolls, -r                      show dice rolls only
  --verbose, -v                         show entropy information
```

# Examples

- Running `diceware.py` without any options falls back to defaults: **5 random words** from `eff_large_wordlist.txt`.

```console
$ python diceware.py
anybody desecrate battalion agility skid
```

- Choosing the **number of words** to generate:

```console
$ python diceware.py --verbose --words 8
citric trimming whole unlivable drivable percent suitor clump

> 8 random words from a 7776-word list yield 103.4 bits of entropy.
```

- Setting the **minimum bits of entropy** for the passphrase will generate the appropriate amount of words:

```console
$ python diceware.py -v --entropy 120 --s"-"
glade-unmoved-pacemaker-gallon-jogging-sculpture-gentleman-disburse-unsaddle-surprise

> 10 random words from a 7776-word list yield 129.2 bits of entropy.
```

- Only **show dice rolls** generated based on the provided wordlist:

```console
$ python diceware.py -w 10 --show-rolls --file my_printed_wordlist.txt
21162 54422 55235 46233 61313 62442 21411 23555 54232 55436
```

- Use a **custom delimiter** to parse wordlist:

```console
$ python diceware.py -w 7 --show-rolls --file my_wordlist.csv --delimiter ","
23611 62433 55136 12534 55642 51415 13611
```

- Set the **number of dice** to roll for each word:

```console
$ python diceware.py -d6 -w 10 -s $'\n'
464645
664516
111426
133531
416231
613133
541445
156546
325161
566625
```

- Use an alternative EFF wordlist:

```console
$ python diceware.py -v -f wordlists/eff_short_wordlist_2_0.txt -w 8
goldfish depot unwrinkled tiger caviar rustproof urgent urethane

> 8 random words from a 1296-word list yield 82.7 bits of entropy.
```

# Attribution

- Wordlists available from the [EFF](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases).
