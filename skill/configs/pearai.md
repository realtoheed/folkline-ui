# Folkline UI — PearAI Rules
# Place in .pearai/rules/folkline-ui.md

**Folkline UI v3.0.0** — Utility-first CSS framework.

## CDN
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@realtoheed/folkline-ui@3/dist/folkline.min.css" />
```

## Core Classes
- **Layout**: `flex`, `flex-col`, `items-center`, `justify-between`, `grid`, `grid-cols-{n}`
- **Spacing**: `p-{0-10}`, `m-{0-10}`, `gap-{0-10}`, `mx-auto`, `px-{size}`, `py-{size}`
- **Typography**: `text-{xs..9xl}`, `font-{weight}`, `text-center`, `uppercase`
- **Colors**: `text-{color}-{shade}`, `bg-{color}-{shade}`, `border-{color}-{shade}`
- **Sizing**: `w-full`, `w-1/2`, `h-screen`, `max-w-{size}`
- **Borders**: `border`, `rounded-{sm|lg|xl|full}`, `shadow-{sm|md|lg}`
- **Animations**: `animate-fade-in`, `animate-spin`, `animate-pulse`

## Components
Badge, Spinner, Skeleton, Avatar, Tooltip, Modal, Tabs, Accordion, Dropdown, Toast, Switch, Pagination, Progress, Breadcrumb, Stepper, Timeline, Menu, List Group, Stat, Rating, Code/Kbd, Separator, Carousel, Upload, FAQ, Compare, Hero, Button, Card, Alert, Form, Navbar, Table

## Accessibility
Always include: ARIA roles, focus-visible outlines, keyboard navigation, semantic HTML, aria-labels, aria-expanded, role="alert" for toasts, role="dialog" for modals
