# Redwood Aviation Group — Website

A single-page marketing site for **Redwood Aviation Group LLC**, an owner-first
aircraft leaseback business based at Charles M. Schulz – Sonoma County Airport
(KSTS). The page establishes a web presence and captures inbound leads from
flight schools, clubs, and operators looking to lease an aircraft.

## Contents

| File         | Purpose                                            |
| ------------ | -------------------------------------------------- |
| `index.html`     | The landing page markup and content                |
| `styles.css`     | Styling (brand palette, layout, responsive design) |
| `script.js`      | Footer year + contact form handling                |
| `assets/logo.png`| The Redwood Aviation Group pine-cluster logo       |

No build step, framework, or dependencies — it's plain HTML/CSS/JS. These three
files together fully define the site; with all three you can restore it exactly.

## Design / brand

- **Theme:** black background, **bright gold** (`#f0c040`) as the primary accent,
  **bright emerald** (`#00d97e`) as the secondary accent.
- **Type:** Playfair Display (headings) + Inter (body).
- **Logo:** the official Redwood Aviation Group pine-cluster mark — emerald
  pines with a gold center tree and roots, on a transparent background —
  lives at `assets/logo.png` and is shown in the nav alongside the wordmark.

## Sections

Nav → Hero → Our Approach (3 cards) → For Flight Schools & Operators → Contact
form → Footer. Positioning is aimed at schools/clubs/operators who want to lease
an aircraft from Redwood.

## Run locally

Open `index.html` directly in a browser, or serve the folder:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Contact form

The form is in the **Contact** section. With no backend, submitting opens the
visitor's email client with a prefilled message to `rob@redwoodaviationgroup.com`
(works on any static host).

To capture leads automatically instead:

1. Create a form endpoint (e.g. a free [Formspree](https://formspree.io) form).
2. In `script.js`, set `FORM_ENDPOINT` to your endpoint URL.

Submissions are then POSTed to that endpoint and the page shows an inline
success message.

## Deploy

The site is static and can be hosted anywhere. For **GitHub Pages**: enable
Pages for this repository and serve from the branch root — no configuration
needed.
