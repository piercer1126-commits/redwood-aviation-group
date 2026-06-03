# Redwood Aviation Group — Website

A simple, single-page marketing site for **Redwood Aviation Group**, an
owner-first aircraft leaseback business based at Charles M. Schulz – Sonoma
County Airport (KSTS). The page establishes a web presence and captures inbound
leads from flight schools and operators interested in leasing an aircraft.

## Contents

| File         | Purpose                                            |
| ------------ | -------------------------------------------------- |
| `index.html` | The landing page markup and content                |
| `styles.css` | Styling (brand palette, layout, responsive design) |
| `script.js`  | Footer year + contact form handling                |

No build step, framework, or dependencies — it's plain HTML/CSS/JS.

## Run locally

Open `index.html` directly in a browser, or serve the folder:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Contact form

The form lives in the **Contact Us** section. By default the site has no
backend, so submitting the form opens the visitor's email client with a
prefilled message to `redwoodav8@gmail.com` (works on any static host).

To capture leads automatically instead:

1. Create a form endpoint (e.g. a free [Formspree](https://formspree.io) form).
2. In `script.js`, set `FORM_ENDPOINT` to your endpoint URL.

Submissions will then be POSTed to that endpoint and the page shows an inline
success message.

## Deploy

The site is static and can be hosted anywhere. For **GitHub Pages**: enable
Pages for this repository and serve from the branch root — no configuration
needed.
