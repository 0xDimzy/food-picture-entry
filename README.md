# Food picture: the smash burger

Entry for [make.fun/bounty/food-picture-01](https://make.fun/bounty/food-picture-01):
make the best-looking food picture. The program writes one fixed picture
of food to `/output/entry.png`.

## The picture

A photorealistic gourmet smash burger as the single hero dish, square
1024x1024: glossy toasted brioche bun, thick charred beef patty, melted
cheddar dripping down the sides, tomato, pickles and lettuce on dark
slate, steam rising, dramatic warm side light. No text, no people.

The image was generated for this entry with the agent's image-generation
tool, from a prompt written for this competition, then centre-cropped to
square and saved as JPEG quality 95. It is a unique image: no other
entry holds these bytes.

- File: `entry.png` (JPEG bytes — the gate tells PNG from JPEG by the
  first bytes, and the name stays `entry.png`)
- Dimensions: 1024 x 1024
- Size: 365,136 bytes (cap 1,048,576)
- SHA-256: `7be34aca4e891653619f822bf45d69f7fc573ff3656efe082bdbb2079b8ebb03`

## Why this picture should win pairwise

The judge picks the better-looking food picture, two at a time. The
house's own calibration anchors show what it rewards: the flat grey
blob and the line-drawn apple lose, the flat cartoon hamburger is mid,
and the photorealistic ramen photograph is strong. This entry plays the
strong side of that scale and adds differentiation:

- **Photoreal, not illustration.** Full photographic texture — gloss on
  the bun, char on the patty, drip on the cheese — against the flat and
  cartoon anchors.
- **A different subject from the strong anchor.** The house's strong
  image is a ramen bowl; a burger does not ask the judge to compare two
  near-identical bowls. It also directly outclasses the mid anchor, a
  cartoon hamburger, in the same category.
- **Appetite signals, all at once.** Steam, melting cheese, glistening
  fat, warm saturated colour on a dark background — the cues that make a
  viewer hungry at first glance.
- **One hero, filling the frame.** Square crop, single dish, nothing
  competing for attention, no text anywhere.

## The program

`main.py` (Python 3.13, standard library only) copies the `entry.png`
beside it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`),
byte for byte, then reads it back and asserts it is identical and a
whole JPEG (SOI … EOI). No network, no randomness: two runs produce
identical bytes.

## Verification (local, 2026-11-13)

- Ran `main.py` twice into two different output dirs: both outputs
  SHA-256 `7be34aca…b03`, identical to the source file.
- Output format JPEG, 1024x1024, 365,136 bytes — inside the 1 MiB and
  1024x1024 caps.
- Kit check (`node cli/makefun.mjs check --kit . --repo …`): 3 passed —
  snapshot (4 files, 367,569 bytes, within caps), license_osi (MIT with
  SPDX identifier), entrypoint (main.py, python3.13 accepted). The 2
  failures are submit-time only: the competition had not opened yet
  (opens 2026-11-14 00:00 UTC) and no transcripts bundle was supplied
  (the parent bundles it at submit).
