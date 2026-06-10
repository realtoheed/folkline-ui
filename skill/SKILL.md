# Folkline UI Skill — Build Beautiful UIs with Zero CSS

A complete skill for **Folkline UI v3.0.0** — the utility-first CSS framework with 2,734 utility classes and 30+ accessible components.

## Overview

Folkline UI is a modern CSS framework that combines the flexibility of utility classes with the convenience of pre-built components. Drop one CDN link and start building immediately — no build step required.

### Key Stats
| Metric | Value |
|--------|-------|
| Utility classes | 2,734 |
| Components | 30+ |
| Gzipped | ~3.5 KB |
| License | MIT |
| CDN | `https://cdn.jsdelivr.net/npm/@realtoheed/folkline-ui@3/dist/folkline.min.css` |
| npm | `@realtoheed/folkline-ui` |
| Repository | https://github.com/realtoheed/folkline-ui |

### Design Principles
1. **Utility-first** — Compose UIs from small, single-purpose classes
2. **Accessibility first** — Every component meets WCAG 2.1 AA
3. **Zero configuration** — One CDN link, everything works
4. **Framework agnostic** — Works with React, Vue, Alpine, or plain HTML
5. **Lightweight** — ~3.5 KB gzipped for the entire framework
6. **Consistent** — OKLCH-based color system, harmonious scales

## Usage

### CDN (Recommended)
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@realtoheed/folkline-ui@3/dist/folkline.min.css" />
```

### npm
```bash
npm install @realtoheed/folkline-ui
```
```javascript
import "@realtoheed/folkline-ui/dist/folkline.min.css";
```

## Utility Classes

### Spacing
| Pattern | Example | Description |
|---------|---------|-------------|
| `p-{size}` | `p-4` | Padding all sides |
| `pt-{size}`, `pr-{size}`, `pb-{size}`, `pl-{size}` | `pt-2` | Individual padding sides |
| `px-{size}`, `py-{size}` | `px-4` | Horizontal / vertical padding |
| `m-{size}` | `m-3` | Margin all sides |
| `mx-auto` | — | Auto horizontal margin (centering) |
| `gap-{size}` | `gap-2` | Grid/flex gap |
| `gap-x-{size}`, `gap-y-{size}` | `gap-x-3` | Row/column gap |

Sizes: `0`, `0.25`, `0.5`, `1`, `1.5`, `2`, `2.5`, `3`, `4`, `5`, `6`, `8`, `10` (in rem)

### Typography
| Pattern | Example | Description |
|---------|---------|-------------|
| `text-{size}` | `text-lg` | Font size (xs through 9xl) |
| `font-{weight}` | `font-bold` | Font weight (100-900) |
| `leading-{height}` | `leading-tight` | Line height |
| `tracking-{spacing}` | `tracking-wide` | Letter spacing |
| `text-left/center/right` | `text-center` | Text alignment |
| `uppercase/lowercase/capitalize` | `uppercase` | Text transform |
| `underline/line-through/no-underline` | `underline` | Text decoration |
| `italic/not-italic` | `italic` | Font style |
| `truncate` | — | Single-line truncate with ellipsis |

### Colors (OKLCH)
| Pattern | Example | Description |
|---------|---------|-------------|
| `text-{color}-{shade}` | `text-primary-600` | Text color |
| `bg-{color}-{shade}` | `bg-blue-500` | Background color |
| `border-{color}-{shade}` | `border-red-300` | Border color |

Colors: `primary`, `secondary`, `success`, `danger`, `warning`, `info`, `light`, `dark` (each with 50-900 shades)

### Flexbox
| Pattern | Example | Description |
|---------|---------|-------------|
| `flex` | — | Display flex |
| `flex-{direction}` | `flex-col` | Flex direction |
| `flex-{wrap}` | `flex-wrap` | Flex wrap |
| `flex-{grow}` | `flex-1` | Flex grow/shrink |
| `justify-{alignment}` | `justify-between` | Justify content |
| `items-{alignment}` | `items-center` | Align items |
| `order-{n}` | `order-1` | Flex order |

### Grid
| Pattern | Example | Description |
|---------|---------|-------------|
| `grid` | — | Display grid |
| `grid-cols-{n}` | `grid-cols-3` | Grid columns (1-12) |
| `col-span-{n}` | `col-span-2` | Column span |
| `grid-rows-{n}` | `grid-rows-2` | Grid rows (1-6) |
| `row-span-{n}` | `row-span-2` | Row span |
| `grid-flow-{dir}` | `grid-flow-col` | Grid auto flow |

### Sizing
| Pattern | Example | Description |
|---------|---------|-------------|
| `w-{size}` | `w-48` | Fixed width |
| `w-{fraction}` | `w-1/2` | Fractional width |
| `w-full/screen/auto` | `w-full` | Full/screen/auto width |
| `h-{size}` | `h-12` | Fixed height |
| `h-full/screen/auto` | `h-screen` | Full/screen/auto height |
| `max-w-{size}` | `max-w-lg` | Max width (xs-7xl, full) |
| `min-h-screen` | — | Min height screen |

### Borders
| Pattern | Example | Description |
|---------|---------|-------------|
| `border` | — | Default border (1px) |
| `border-{n}` | `border-2` | Border width (0-8) |
| `border-{side}` | `border-t` | Side-specific border |
| `rounded-{size}` | `rounded-lg` | Border radius |
| `rounded-{side}` | `rounded-t` | Side-specific radius |
| `rounded-full` | — | Full rounded (circle/pill) |

### Shadows
| Pattern | Example | Description |
|---------|---------|-------------|
| `shadow-{size}` | `shadow-lg` | Box shadow (sm through 2xl, inner, none) |

### Transforms
| Pattern | Example | Description |
|---------|---------|-------------|
| `scale-{n}` | `scale-105` | Scale transform (0-150) |
| `rotate-{deg}` | `rotate-45` | Rotation |
| `translate-{axis}-{size}` | `translate-y-2` | Translation |
| `skew-{axis}-{deg}` | `skew-x-6` | Skew |

### Filters
| Pattern | Example | Description |
|---------|---------|-------------|
| `blur-{size}` | `blur-sm` | Blur (none through 3xl) |
| `brightness-{n}` | `brightness-125` | Brightness |
| `contrast-{n}` | `contrast-150` | Contrast |
| `grayscale` | — | Grayscale filter |

### Transitions
| Pattern | Example | Description |
|---------|---------|-------------|
| `transition-{property}` | `transition-colors` | Transition (none, all, colors, opacity, shadow, transform) |
| `duration-{ms}` | `duration-300` | Transition duration |
| `ease-{type}` | `ease-in-out` | Timing function |

### Position & Z-Index
| Pattern | Example | Description |
|---------|---------|-------------|
| `static/fixed/absolute/relative/sticky` | `absolute` | Position |
| `inset-{size}` | `inset-0` | All sides inset |
| `top/right/bottom/left-{size}` | `top-4` | Individual sides |
| `z-{n}` | `z-50` | Z-index (0-50, auto) |

### Display & Overflow
| Pattern | Example | Description |
|---------|---------|-------------|
| `d-{value}` | `d-none` | Display (block, inline, flex, grid, none, etc.) |
| `overflow-{value}` | `overflow-hidden` | Overflow (auto, hidden, visible, scroll, clip) |

### Cursor & Opacity
| Pattern | Example | Description |
|---------|---------|-------------|
| `cursor-{type}` | `cursor-pointer` | Cursor (pointer, not-allowed, grab, etc.) |
| `opacity-{n}` | `opacity-50` | Opacity (0-100) |

### Animations
| Pattern | Example | Description |
|---------|---------|-------------|
| `animate-{name}` | `animate-fade-in` | Animation (fade-in, fade-in-up, scale-in, spin, pulse, bounce, shake) |
| `animate-fast/slow` | `animate-slow` | Speed modifier |
| `animate-delay-{n}` | `animate-delay-2` | Delay modifier |
| `animate-once/twice/infinite` | `animate-once` | Iteration control |

## Components

| Component | Selectors | Description |
|-----------|-----------|-------------|
| **Badge** | `.badge`, `.badge-{variant}`, `.badge-sm/lg/pill`, `.badge-dot` | Inline labels for status, counts, or categories |
| **Breadcrumb** | `.breadcrumb`, `.breadcrumb-item` | Navigation breadcrumb trail |
| **Spinner** | `.spinner`, `.spinner-{sm/lg/xl}`, `.spinner-{color}` | Loading spinner indicator |
| **Skeleton** | `.skeleton`, `.skeleton-{text/title/avatar/circle/thumbnail}` | Content placeholder loading animation |
| **Progress** | `.progress`, `.progress-bar`, `.progress-bar-{color}`, `.progress-{sm/lg}`, `.progress-striped/animated` | Progress bar indicator |
| **Avatar** | `.avatar`, `.avatar-{xs/sm/lg/xl/2xl}`, `.avatar-group`, `.avatar-status` | User profile images and initials |
| **Tooltip** | `[data-tooltip]`, `[data-tooltip-{top/bottom/left/right}]` | Hover tooltips for additional information |
| **Modal** | `.modal`, `.modal-overlay`, `.modal-content`, `.modal-header/body/footer` | Dialog overlay for focused content |
| **Tabs** | `.tabs-container`, `.tab-label`, `.tab-panel` | Tabbed content navigation (CSS-only) |
| **Accordion** | `.accordion`, `.accordion-content` | Collapsible content sections |
| **Dropdown** | `.dropdown`, `.dropdown-trigger`, `.dropdown-menu`, `.dropdown-item` | Revealable menu from a trigger element |
| **Toast** | `.toast`, `.toast-container`, `.toast-element`, `.toast-{color}` | Brief notification messages |
| **Switch** | `.switch`, `.switch-{sm/lg}` | iOS-style toggle switch (CSS-only) |
| **Pagination** | `.pagination`, `.pagination-item`, `.pagination-{sm/lg}` | Page navigation for lists and tables |
| **List Group** | `.list-group`, `.list-group-item`, `.list-group-flush` | Styled list groups |
| **Stat** | `.stat`, `.stat-label/value/desc`, `.stat-card` | Statistics and metrics display |
| **Kbd** | `.kbd` | Keyboard shortcut display |
| **Separator** | `.separator`, `.separator-vertical`, `.separator-label` | Horizontal and vertical separators |
| **Stepper** | `.stepper`, `.stepper-vertical`, `.stepper-item`, `.stepper-number/label/desc` | Multi-step progress indicator |
| **Code** | `.code`, `.code-block` | Inline code and code blocks |
| **Hero Section** | `.hero-section` | Full-width hero section component |
| **Table** | `.table`, `.table-striped/bordered`, `.table-{sm/lg}`, `.sortable` | Styled table with responsive options |
| **Menu** | `.menu`, `.menu-item`, `.menu-title`, `.menu-divider` | Vertical navigation menu |
| **Timeline** | `.timeline`, `.timeline-item`, `.timeline-dot/content/time` | Vertical timeline for chronological content |
| **Rating** | `.rating`, `.rating-star`, `.rating-{sm/lg}` | Star rating display |
| **Carousel** | `.carousel`, `.carousel-item` | Slideshow component for images and content |
| **Upload Zone** | `.upload-zone`, `.upload-zone-icon/text/hint` | Drag-and-drop file upload area |
| **FAQ** | `.faq-item`, `.faq-question`, `.faq-answer` | Frequently asked questions accordion |
| **Feature Compare** | `.compare`, `.compare-col`, `.compare-title/item` | Side-by-side comparison component |
| **Button** | `.btn`, `.btn-{color}`, `.btn-outline-{color}`, `.btn-{sm/lg}`, `.btn-block` | Buttons with multiple style and size variants |
| **Card** | `.card`, `.card-header/body/footer`, `.card-text/title`, `.card-hover`, `.card-divider` | Content containers |
| **Form** | `.form-group`, `.form-label`, `.input-group`, `.input-error`, `.form-text` | Form layout and styling |
| **Navbar** | `.navbar`, `.navbar-brand`, `.navbar-nav`, `.navbar-toggle` | Navigation bar |
| **Grid System** | `.container`, `.row`, `.col`, `.col-{1-12}`, `.col-auto`, `.col-md-{1-12}` | Responsive 12-column grid |
| **Alert** | `.alert`, `.alert-{color}`, `.alert-heading` | Contextual alert messages |

## Accessibility

Folkline UI is built with accessibility as a core principle. All components follow WCAG 2.1 AA guidelines:

- **ARIA**: All interactive components include appropriate roles, states, and properties
- **Keyboard**: All interactive elements receive visible focus indicators; components manage focus trapping, arrow key navigation, and Escape key handling
- **Semantic HTML**: Components use semantic elements and proper heading hierarchy
- **Reduced Motion**: All animations respect `prefers-reduced-motion`
- **High Contrast**: All color combinations meet WCAG AA contrast requirements; components work in forced-colors mode

## Responsive Design

Folkline UI uses breakpoints: `sm` (640px), `md` (768px), `lg` (1024px), `xl` (1280px), `2xl` (1536px).

Responsive utilities follow the pattern: `{breakpoint}:d-{value}` (e.g. `md:d-block`).

## Design Tokens

The design system is powered by CSS custom properties. Override them in your stylesheet:

```css
:root {
  --primary: #3b82f6;
  --secondary: #8b5cf6;
  --radius: 0.5rem;
  --font-family: 'Inter', sans-serif;
}
```

Token categories: Colors, spacing, fonts, radii, shadows, transitions, breakpoints.

## Framework Integration

Folkline UI works with any framework:
- **React/Vue/Svelte/Alpine**: Add the CDN link and use classes in your templates
- **Build tools**: Import via npm for tree-shaking and optimization
- **Plain HTML**: Add the CDN link and style directly with classes

## Generating Content

When generating UI designs with Folkline UI:
1. Use the utility classes for layout, spacing, and styling
2. Use components for complex UI patterns
3. Follow accessibility patterns (proper ARIA, focus-visible, semantic HTML)
4. Use the CDN link for quick prototyping
5. Combine utility classes creatively for custom designs

## Resources

- **CDN**: `https://cdn.jsdelivr.net/npm/@realtoheed/folkline-ui@3/dist/folkline.min.css`
- **npm**: `@realtoheed/folkline-ui`
- **Source**: https://github.com/realtoheed/folkline-ui
- **Templates**: 66 pre-built templates available in the skill data
- **Documentation**: https://realtoheed.github.io/folkline-ui-site/

## Examples

### Buttons
```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-outline-primary">Outline</button>
<button class="btn btn-sm">Small</button>
<button class="btn btn-lg btn-block">Full Width</button>
```

### Card
```html
<div class="card">
  <div class="card-header">Header</div>
  <div class="card-body">
    <h5 class="card-title">Card Title</h5>
    <p class="card-text">Some quick example text.</p>
  </div>
</div>
```

### Alert
```html
<div class="alert alert-primary">
  <strong class="alert-heading">Info:</strong> This is an alert message.
</div>
```
