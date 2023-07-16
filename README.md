# 🎲 nodice

A simple [diceware](https://en.wikipedia.org/wiki/Diceware) generator with no dependencies.

## 📦 Setup

#### From source:
##### - Clone the repository:

```
git clone https://github.com/avnigo/nodice-cli.git && cd nodice-cli
```

##### - [*Optional*] Install `nodice` to path:

```pwsh
python -m pip install .
```

##### - Otherwise, use as follows inside the `nodice-cli` directory:

```pwsh
python nodice
```
#### Install from package using `pip` or [`pipx`](https://github.com/pypa/pipx):

```pwsh
pip install nodice-cli
```

## 📖 Usage

```console
$ nodice --help
usage: nodice [-h] [--words WORDS] [--entropy ENTROPY] [--spacer SPACER] [--dice DICE] [--sides SIDES] [--show-rolls] [--file FILE] [--delimiter DELIMITER] [--verbose]

Generate diceware passphrases from wordlists.

options:
  -h, --help                            show this help message and exit
  --words WORDS, -w WORDS               number of words (default: `5`)
  --entropy ENTROPY, -e ENTROPY         set minimum bits of entropy
  --spacer SPACER, -s SPACER            separate words with a spacer (default: ` `)
  --dice DICE, -d DICE                  number of dice per word; ignores --file and --entropy options
  --sides SIDES, -D SIDES               number of sides per die (default: `6`)
  --show-rolls, -r                      show dice rolls only
  --make-custom, -m                     generate keys (dice rolls) for custom wordlist
  --file FILE, -f FILE                  diceware dictionary file (default: `wordlists/eff_large_wordlist.txt`)
  --delimiter DELIMITER, -t DELIMITER   dictionary delimiter (default: $'\t')
  --verbose, -v                         show entropy information
```

## 🗒️ Examples

- Running `nodice` or `python -m nodice` without any options falls back to defaults: **5 random words** from `eff_large_wordlist.txt`.

```console
$ nodice
anybody desecrate battalion agility skid
```

- Choosing the **number of words** to generate:

```console
$ nodice --verbose --words 8
citric trimming whole unlivable drivable percent suitor clump

> 8 random words from a 7776-word list yield 103.4 bits of entropy.
```

- Setting the **minimum bits of entropy** for the passphrase will generate the appropriate amount of words:

```console
$ nodice -v --entropy 120 -s"-"
glade-unmoved-pacemaker-gallon-jogging-sculpture-gentleman-disburse-unsaddle-surprise

> 10 random words from a 7776-word list yield 129.2 bits of entropy.
```

- Only **show dice rolls** generated based on the provided wordlist:

```console
$ nodice -w 10 --show-rolls --file my_printed_wordlist.txt
21162 54422 55235 46233 61313 62442 21411 23555 54232 55436
```

- Use a **custom delimiter** to parse wordlist:

```console
$ nodice -w 7 --show-rolls --file my_wordlist.csv --delimiter ","
23611 62433 55136 12534 55642 51415 13611
```

- Set the **number of dice** to roll for each word:

```console
$ nodice -d6 -w 10 -s $'\n'
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
$ nodice -v -f nodice/wordlists/eff_short_wordlist_2_0.txt -w 8
goldfish depot unwrinkled tiger caviar rustproof urgent urethane

> 8 random words from a 1296-word list yield 82.7 bits of entropy.
```

- Set the **number of sides** of the dice used (e.g. two-sided coin):

```console
$ nodice -v -f nodice/wordlists/bip_0039.txt -w 12 -D2
mountain noble arctic joke hero fruit novel palace quarter genuine rather price

> 12 random words from a 2048-word list yield 132.0 bits of entropy.
```

## 🛠️ Custom wordlists

It is possible to use custom wordlists, either delimited alongside their corresponding dice rolls, or simply a bare list of words, as in the examples below respectively.

- For *delimited wordlists*, the defaults apply (i.e., delimiter and number of sides), otherwise they would need to be passed in as arguments.

```
11111	abacus
11112	abdomen
11113	abdominal
11114	abide
11115	abiding
11116	ability
...
```

- In the case of a *bare wordlist* like the one below, dice roll keys for a [perfect-power-length wordlist](https://en.wikipedia.org/wiki/Perfect_power) will be generated when possible using smaller than 10-sided dice, whereas other length wordlists are unhandled for now.

```
abacus
abdomen
abdominal
abide
abiding
ability
...
```

Using the `--make-custom` flag with a bare wordlist creates the wordlist alongside the corresponding keys (dice rolls):

```console
$ nodice --make-custom -t, -f bare_wordlist.txt | tail
66656,zombie
66661,zone
66662,zoning
66663,zookeeper
66664,zoologist
66665,zoology
66666,zoom
```

## 🔗 Attribution

- [EFF wordlists](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases)
- [BIP-0039 wordlist](https://github.com/bitcoin/bips/blob/master/bip-0039/bip-0039-wordlists.md)
