# Folkline UI

⚡ Utility-First CSS Framework — 2,500+ Classes for Rapid UI Development

A comprehensive utility-first CSS framework designed for both **human developers** and **AI code generation**. Build complete websites without writing custom CSS — just compose classes in HTML.

## Features

- **2,500+ Utility Classes** — Spacing, typography, colors, flexbox, grid, transforms, filters, animations
- **Component Classes** — Buttons, cards, forms, alerts, navbar
- **10 CSS Animations** — Fade, slide, scale, spin, pulse, bounce, shake with delay/duration controls
- **67+ Color Shades** — 10-shade palettes for primary, secondary, success, danger, warning, info
- **Responsive** — sm/md/lg/xl/2xl breakpoints
- **Zero Dependencies** — Pure CSS, no JavaScript
- **108KB Minified** — Gzip-friendly
- **MIT License** — Free for commercial use

## Installation

```bash
npm install @realtoheed/folkline-ui
```

## Quick Start

```html
<link rel="stylesheet" href="/node_modules/@realtoheed/folkline-ui/dist/folkline.min.css" />

<!-- Components -->
<button class="btn btn-primary">Click Me</button>
<div class="card p-6 shadow-lg rounded-xl">Card content</div>

<!-- Utilities -->
<div class="d-flex items-center justify-between gap-4 p-4 bg-gray-100 rounded-lg">
  <h2 class="text-xl font-bold text-primary-700">Title</h2>
  <span class="text-sm text-gray-500">Subtitle</span>
</div>

<!-- Animations -->
<div class="animate-fade-in-up animate-slow animate-delay-2">Hello</div>
```

## Class Reference

### Spacing (margin/padding)
`m|mt|mr|mb|ml|mx|my|p|pt|pr|pb|pl|px|py-{0|px|1|2|3|4|5|6|7|8|9|10|12|14|16|20|24|28|32|36|40|44|48|52|56|60|64|72|80|96}`

Negative margins: `-m-{1..96}`

### Typography
- **Sizes:** `text-xs|sm|base|lg|xl|2xl|3xl|4xl|5xl|6xl|7xl|8xl|9xl`
- **Weights:** `font-thin|extralight|light|normal|medium|semibold|bold|extrabold|black`
- **Line Height:** `leading-none|tight|snug|normal|relaxed|loose|3|4|5|6|7|8|9|10`
- **Letter Spacing:** `tracking-tighter|tight|normal|wide|wider|widest`

### Colors (text, bg, border)
`.text|bg|border-{primary|secondary|success|danger|warning|info|light|dark}-{50|100|200|300|400|500|600|700|800|900}`

### Flexbox
`d-flex|d-inline-flex`, `flex-row|col|wrap|nowrap`, `flex-1|auto|initial|none`, `flex-grow|shrink`
`justify-start|end|center|between|around|evenly`
`items-start|end|center|baseline|stretch`
`gap-{size}`, `gap-x|y-{size}`

### Grid
`d-grid`, `grid-cols-{1..12}`, `grid-rows-{1..6}`, `col-span-{1..12}`, `row-span-{1..6}`, `gap-{size}`

### Sizing
`w|h-{0..96|full|screen|auto|min|max|fit|1/2|1/3|2/3|1/4|3/4}`
`min-w|max-w|min-h|max-h-{0..96|full|screen}`

### Borders
`border`, `border-{0..8}`, `border-t|r|b|l`, `border-{solid|dashed|dotted|double}`
`rounded-{none|sm|md|lg|xl|2xl|3xl|full}`

### Shadows
`shadow-{sm|base|md|lg|xl|2xl|inner|none}`

### Animations
`animate-{fade-in|fade-in-up|fade-in-down|fade-in-left|fade-in-right|scale-in|spin|pulse|bounce|shake}`
Controls: `animate-fast|normal|slow`, `animate-delay-{1..5}`, `animate-once|twice|infinite`

### Transforms
`scale-{0|50|75|90|95|100|105|110|125|150}`, `scale-x|y-{same}`
`rotate-{0|1|2|3|6|12|45|90|180}`
`translate-x|y-{size}`, `-translate-x|y-{size}`
`origin-{center|top|right|bottom|left|...}`

### Filters
`blur-{none|sm|base|md|lg|xl|2xl|3xl}`
`brightness-{0|50|75|90|95|100|105|110|125|150|200}`
`contrast-{0|50|75|100|125|150|200}`
`grayscale|invert|sepia|saturate-{0|50|100|150|200}`

### Position
`static|fixed|absolute|relative|sticky`
`inset|inset-x|inset-y|top|right|bottom|left-{0|auto|full|size}`
`z-{0|10|20|30|40|50|auto}`

### Display & Overflow
`d-{block|inline|inline-block|flex|inline-flex|grid|inline-grid|table|none}`
`overflow-{auto|hidden|visible|scroll|clip}`, `overflow-x|y-{...}`

### Cursor
`cursor-{auto|default|pointer|wait|text|move|not-allowed|grab|grabbing|crosshair|zoom-in|zoom-out|...}`

### Transitions
`transition|transition-all|transition-colors|transition-opacity|transition-shadow|transition-transform`
`duration-{75|100|150|200|300|500|700|1000}`
`delay-{0|75|100|150|200|300|500|700|1000}`
`ease-linear|in|out|in-out`

### AI Usage

Feed folkline-ui to any AI coding assistant for automatic UI generation:

```
Build a landing page for a SaaS product using folkline-ui classes
```

The AI will use the utility classes directly in HTML to create professional layouts.

## License

MIT — see [LICENSE](LICENSE).
