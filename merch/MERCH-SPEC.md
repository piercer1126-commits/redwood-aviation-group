# Redwood Aviation Group — Merch Spec

Print-ready artwork and specs for branded apparel.
First run: **sweatshirts, black/charcoal, stacked lockup, full-front print.**

## Print files — `merch/print/`

| File | Size (px) | Use |
| ---- | --------- | --- |
| `lockup-8in-300dpi.png` | 2400 × 2566 | **Send this to the printer.** Full lockup, transparent, sized for an 8 in wide print at 300 DPI. |
| `lockup-native.png` | 1343 × 1435 | Same lockup with the mark at its true native resolution, never upscaled. For a printer who prefers to scale it themselves. |
| `mark-only.png` | 1343 × 1134 | Trees alone, transparent. For hats, sleeves, favicons, stickers. |
| `lockup-leftchest-3.5in.png` | 1050 × 1123 | Stacked lockup for a **left-chest** print at 3.5 × 3.74 in, 300 DPI. |
| `lockup-horizontal.png` | 2686 × 1134 | Horizontal lockup (mark left, wordmark right), 2.37 : 1. Master file — scale down as needed. |
| `lockup-horizontal-cap-4.5in.png` | 1350 × 570 | Horizontal lockup sized for a **cap front**: 4.5 × 1.9 in, 300 DPI. |
| `proof-black.png` | — | Visual proof on black. Not for printing. |
| `proof-charcoal.png` | — | Visual proof on charcoal. Not for printing. |

### Placement guide

| Product | File | Size |
| ------- | ---- | ---- |
| Sweatshirt, full front | `lockup-8in-300dpi.png` | 7–8 in wide, 3–4 in below collar |
| Sweatshirt, left chest | `lockup-leftchest-3.5in.png` | 3.5 in wide |
| Cap front | `lockup-horizontal-cap-4.5in.png` | 4.5 in wide |
| Sleeve / small accents | `mark-only.png` | 2–3 in wide |

**Caps and embroidery:** the horizontal lockup is correct for a printed or
DTF-patch cap. For *stitched* embroidery, the fine root system won't reproduce —
roots thinner than about 1 mm cannot be stitched cleanly. For embroidered caps,
either use `mark-only.png` and let the digitizer simplify the roots, or choose a
DTF/woven/leather patch instead, which reproduces the artwork as drawn.

All three artwork files have **true transparency** — correct for DTF/DTG on dark
garments. The tree trunks are intentional open gaps, so the garment color shows
through them.

## The lockup

Stacked and centered:

```
      [ pine cluster mark ]
           REDWOOD
       AVIATION  GROUP
```

- **Typeface: Playfair Display Bold (weight 700)** — the same serif as the website.
- All caps. `REDWOOD` set to ~88% of the mark's width; `AVIATION GROUP` to ~86%
  with wider letterspacing, so both lines read as one justified block.
- Overall lockup aspect ≈ **0.94 : 1** (slightly taller than wide).

## Colors

| Role | Hex | Notes |
| ---- | --- | ----- |
| Wordmark gold | `#f0c040` | Solid. Matches the website's primary accent. |
| Mark gold, average | `#db9b05` | Center tree mid-tone |
| Mark gold, gradient | `#976900` → `#ffc452` | |
| Mark green, average | `#06944d` | Surrounding pines |
| Mark green, gradient | `#025e1f` → `#73d469` | |

The mark is **gradient-filled, not flat** (~12,000 distinct shades). This drives
the print-method choice below.

## Print size

The mark's true resolution is **1343 px wide**. That is the real constraint — the
wordmark is rendered as type and stays sharp at any size.

| Print width | Mark effective DPI | Verdict |
| ----------- | ------------------ | ------- |
| 6 in | 224 | Excellent |
| 7 in | 192 | **Recommended** |
| 8 in | 168 | Very good — supplied file is built for this |
| 9 in | 149 | Acceptable; about the practical floor |
| 10 in | 134 | Not advised |

**Recommended: 7–8 in wide**, centered, top edge about 3–4 in below the collar seam.
On knit fabric, 170–190 DPI is visually indistinguishable from 300 DPI — the weave
is coarser than the ink detail.

For a **left chest** print, use `mark-only.png` at 3.5–4 in wide (335–384 DPI).

## Print method

| Method | Fit | Notes |
| ------ | --- | ----- |
| **DTF transfer** | **Best for a first run** | Reproduces the gradients exactly. No minimums, no color separations. Excellent on dark garments. |
| **DTG** | Also good | Handles gradients well. On black it needs a white underbase — factor into cost. |
| **Screen print** | Best at 24+ units | Each color is a separate screen; gradients need halftones, which costs more. Ask for a flattened 3-color version (gold, mid green, dark green) if going this route. |
| **Embroidery** | Needs rework | Premium look, but the fine root system and gradients can't be stitched as drawn. Requires a simplified mark. |

**Recommendation:** DTF or DTG for the first run. Both print the artwork as
designed with no rework and no minimums.

## Source & provenance

- Origin: Canva design *"Copy of Copy of Untitled"* — worth renaming to
  **"Redwood Aviation Group — Logo"** so it's findable.
- Exported at 2000 × 2000; the artwork itself occupies 1343 × 1134 of that canvas
  (the rest was white padding, since removed).
- The Canva source is a **flat raster image**, not vector shapes. There is no way
  to export it larger with more real detail, and **Canva Pro would not change
  this** — the ceiling is in the artwork, not the export plan. Don't upgrade for this.
- White background removed locally with per-pixel alpha estimation and
  white-unpremultiply, so edges carry no light fringe on dark garments.
- Minor caveat: the file transited as lossy WebP, so there is slight compression
  in flat areas. Measured impact is ~0.2% of pixels and is irrelevant at print
  scale on fabric.

### If you ever want true unlimited scaling

The mark would need to be redrawn as vector (SVG). Worth doing only if you later
want large-format use — banners, vehicle graphics, a trade-show booth. It is not
needed for apparel.

## Pre-flight checklist

- [ ] Send `lockup-8in-300dpi.png`
- [ ] Confirm transparent background preserved (no white box behind the trees)
- [ ] Print width specified: 7–8 in
- [ ] Placement specified: centered, 3–4 in below collar
- [ ] Garment confirmed: black or charcoal
- [ ] Method confirmed: DTF or DTG
- [ ] Physical proof approved before the full run

---

# Business Cards

Files in `merch/cards/`.

| File | For |
| ---- | --- |
| `card-front-robert-pierce.png` | Robert Pierce — CEO / Co-Founder |
| `card-front-mario-rosso.png` | Mario Rosso — CFO / Co-Founder |
| `card-back.png` | Shared back — same for both |
| `build-cards.py` | Regenerates all of the above |

## Specs

| | |
| --- | --- |
| Trim size | 3.5 × 2.0 in (US standard) |
| File size | 3.75 × 2.25 in — includes 0.125 in bleed on all sides |
| Pixels | 2250 × 1350 |
| Resolution | 600 DPI |
| Orientation | Landscape |
| Color | Background `#0a0a0c`, gold `#f0c040`, body text `#e8e4dd` |
| Type | Playfair Display Bold (names) · Inter (titles, contact) |

The extra 0.125 in around every edge is **bleed** — it gets trimmed off. It
exists so that a slight cutting misalignment shows more black rather than a
white sliver. All text sits inside the safe area, at least 0.25 in from the
file edge, so nothing can be clipped.

## Layout

**Front:** name in Playfair Display Bold (white), title in letterspaced Inter
caps (gold), short gold rule, then phone / email / website. Pine mark on the
right, vertically centered.

**Back:** horizontal lockup centered, with `AIRCRAFT LEASEBACK PARTNERSHIPS`
letterspaced in gold beneath it.

## Ordering

Upload the front and back as a two-sided job. Both files already include bleed,
so choose "my file includes bleed" if asked.

- **Moo** — best quality for small runs; strong on dark stock
- **Jukebox** — specialty stocks; soft-touch black with gold looks genuinely premium
- **Canva Print** — convenient, decent quality
- **Vistaprint** — cheapest acceptable option

**Get soft-touch or matte laminate.** Bare dark stock shows fingerprints
immediately; laminate also deepens the black and makes the gold read richer.

Avoid glossy UV coating — it makes dark cards look cheap and reflects badly
under hangar and FBO lighting.

## To change details later

```bash
curl -sSL -o /tmp/PlayfairDisplay.ttf \
  "https://raw.githubusercontent.com/google/fonts/main/ofl/playfairdisplay/PlayfairDisplay%5Bwght%5D.ttf"
curl -sSL -o /tmp/Inter.ttf \
  "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz,wght%5D.ttf"

python3 merch/cards/build-cards.py '[{"slug":"name","name":"Full Name",
  "title":"Title","phone":"(707) 555-0000","email":"you@redwoodaviationgroup.com"}]'
```
