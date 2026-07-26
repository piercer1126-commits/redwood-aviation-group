# Redwood Aviation Group — Merch Spec

Reference for producing branded apparel. First run: **sweatshirts, black/charcoal,
stacked lockup, full-front print.**

## Files in this folder

| File | What it is |
| ---- | ---------- |
| `lockup-stacked.png` | Layout proof of the stacked lockup (transparent background) |
| `proof-black.png` | Same lockup shown on black |
| `proof-charcoal.png` | Same lockup shown on charcoal |
| `resolution-check.png` | Why the current file can't be printed as-is |

> **These are layout proofs, not print files.** They define composition,
> proportion, and color. The final print file must be exported fresh from Canva
> at the sizes below. See "Getting a print-ready file."

## The lockup

Stacked, centered:

```
      [ pine cluster mark ]
           REDWOOD
      AVIATION GROUP
```

- Wordmark sits directly under the mark, optically centered on the gold center tree.
- `REDWOOD` is the dominant line; `AVIATION GROUP` is roughly half its cap height
  and more widely letterspaced so both lines end up near the same visual width.
- Wordmark total width stays slightly narrower than the tree cluster.
- Overall lockup aspect is about **0.9 : 1** (slightly taller than wide).

### Typography

- **Typeface:** Playfair Display Bold — the same serif used on the website.
- All caps, generous letterspacing on both lines.
- The proofs in this folder were built with a substitute serif because Playfair
  wasn't available locally. **Rebuild the final in Canva using Playfair Display**
  so the merch matches the site.

## Colors

Sampled from the logo artwork itself:

| Role | Hex | Notes |
| ---- | --- | ----- |
| Brand gold (wordmark) | `#f0c040` | Matches the website's primary accent |
| Logo gold, average | `#db9b05` | The center tree's mid-tone |
| Logo gold, gradient | `#976900` → `#ffc452` | Dark to light across the tree |
| Logo green, average | `#06944d` | The surrounding pines |
| Logo green, gradient | `#025e1f` → `#73d469` | Dark to light across the pines |

The mark is **not flat color** — it contains roughly 12,000 distinct shades
because every tree is gradient-filled. This drives the print-method decision below.

The tree trunks are transparent gaps, not white. On a dark garment they read as
intentional negative space, which is why the mark works on black without a knockout.

## Print sizes

Lockup aspect is ~0.9:1, so height is the limiting dimension on a chest print.

| Placement | Width | Height | Pixels needed @300 DPI |
| --------- | ----- | ------ | ---------------------- |
| Full front (recommended) | 10 in | ~11.1 in | **3000 × 3345 px** |
| Full front, conservative | 9 in | ~10 in | 2700 × 3010 px |
| Left chest | 4 in | ~4.5 in | 1200 × 1338 px |

Position a full-front print about 3–4 in below the collar seam.

## Getting a print-ready file

The current `assets/logo.png` is **350 × 298 px** — sized for the website. Print
needs about 300 DPI, so a 10 in wide print needs ~3000 px. Enlarging the existing
file cannot add detail that was never there; edges go soft and stair-stepped
(see `resolution-check.png`).

Re-export from the Canva original instead:

1. **Best — vector.** In Canva, Share → Download → **SVG** or **PDF Print**
   (both require Canva Pro). Vector scales to any size with zero quality loss.
   Give this to the printer and any size becomes possible.
2. **Good — large PNG.** If you're on the free plan: set the Canva canvas to the
   print size in inches (e.g. 10 × 11.1 in) *before* exporting, then
   Download → PNG with the size slider at maximum, and tick **Transparent background**.
3. Either way, build the full stacked lockup in Canva — mark plus both lines of
   Playfair Display — so it exports as one correctly-proportioned file.

**One caveat:** this only works if the trees in your Canva file are vector
elements (Canva graphics/shapes). If the logo was placed into Canva as an
imported image, exporting larger won't help and the mark would need to be
redrawn as vector.

## Print method

The gradients are the deciding factor.

| Method | Fit | Notes |
| ------ | --- | ----- |
| **DTF transfer** | Best for a first run | Handles gradients exactly. No minimums, no color separations. Strong on dark garments. |
| **DTG** | Also good | Prints gradients well. On black it needs a white underbase — factor that into cost. Best for low quantities. |
| **Screen print** | Best at volume (24+) | Each color is its own screen; gradients need halftones, which costs extra. For this route, ask for a flattened 3-color version (gold, mid green, dark green). |
| **Embroidery** | Needs rework | Very premium on sweatshirts, but the fine root system and gradients cannot be stitched as drawn. Would require a simplified mark. |

**Recommendation for a first small run on black:** DTF or DTG. Both reproduce the
gradient artwork as designed with no minimums and no artwork rework.

## Checklist before sending to a printer

- [ ] Vector (SVG/PDF) or ≥3000 px wide PNG exported from Canva
- [ ] Transparent background
- [ ] Built with Playfair Display Bold
- [ ] Gold set to `#f0c040`
- [ ] Print size and placement specified (10 in wide, 3–4 in below collar)
- [ ] Garment color confirmed (black or charcoal)
- [ ] Physical proof or press sample approved before the full run
