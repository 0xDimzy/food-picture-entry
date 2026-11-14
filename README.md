# Food Picture — Photorealistic Smash Burger

A photorealistic photograph of a gourmet smash burger as the single hero
dish, shot for the make.fun food-picture-01 bounty.

## The shot

A smashed, charred beef patty crowned with melted cheddar dripping down
the sides, stacked with tomato, pickles and crisp lettuce inside a glossy
toasted brioche bun. The burger sits on dark slate with steam rising off
it, lit by dramatic warm side light that catches the sheen of the cheese
and the char on the patty edge.

## Files

- `entry.png` — the entry image, a square 1024x1024 JPEG.
- `main.py` — the entry script. It copies `entry.png` unchanged into
  `$MAKEFUN_OUTPUT_DIR/entry.png`.

## Running it

```sh
python3 main.py
```

The script uses only the Python standard library. It does no image
editing: the output is a byte-for-byte copy of the bundled image, so
two runs produce identical bytes.
