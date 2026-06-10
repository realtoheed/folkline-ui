# Folkline UI

⚡ Modern CSS Framework — Simple, Fast, Beautiful

A lightweight, production-ready CSS framework with pre-built components and utility classes.

## Features

- **Pre-built Components** — Buttons, cards, forms, alerts, navbar
- **Utility Classes** — Flexbox, spacing, colors, responsive design
- **Responsive Design** — Mobile-first approach
- **Zero Dependencies** — Pure CSS
- **Tiny Bundle** — ~15KB minified
- **MIT License** — Free for commercial use

## Installation

```bash
npm install @realtoheedsyed/folkline-ui
```

## Quick Start

```html
<link rel="stylesheet" href="/node_modules/@realtoheedsyed/folkline-ui/dist/folkline.min.css" />

<button class="btn btn-primary">Click Me</button>

<div class="card">
  <div class="card-header"><h3>Title</h3></div>
  <div class="card-body"><p>Content</p></div>
</div>
```

## Components

| Component | Classes |
|---|---|
| Buttons | `.btn .btn-primary .btn-secondary .btn-success .btn-danger .btn-warning .btn-info` |
| Cards | `.card .card-header .card-body .card-footer` |
| Forms | `.form-group .form-label .input-group` |
| Navbar | `.navbar .navbar-brand .navbar-nav` |
| Grid | `.container .row .col-*` (12-column) |
| Alerts | `.alert .alert-primary .alert-success .alert-danger .alert-warning .alert-info` |

## Utilities

- **Spacing** — `m-1`, `mt-2`, `mb-3`, `p-1`, `pt-2`, `pb-1`, `mx-auto`
- **Colors** — `text-primary`, `bg-primary`, etc.
- **Flexbox** — `d-flex`, `flex-center`, `flex-between`, `gap-*`
- **Display** — `d-block`, `d-inline`, `d-none`, `d-grid`
- **Sizing** — `w-100`, `h-100`, `min-h-100vh`
- **Responsive** — `d-md-none`, `d-md-block`, `w-md-100`

## Auto-Publishing

Every push to `main` triggers GitHub Actions to build and publish to npm automatically.

## License

MIT — see [LICENSE](LICENSE).
