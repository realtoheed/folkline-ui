# Folkline UI — Copilot Instructions
# Place in .github/copilot-instructions.md

You are a Folkline UI expert. Folkline UI v3.0.0 is a utility-first CSS framework with 2,734 utility classes and 30+ components.

## CDN
`https://cdn.jsdelivr.net/npm/@realtoheed/folkline-ui@3/dist/folkline.min.css`

## npm
`@realtoheed/folkline-ui`

## Key Classes
- Spacing: `p-{0..10}`, `m-{0..10}`, `gap-{0..10}`, `px-`, `py-`, `mx-auto`
- Flex: `flex`, `flex-col`, `flex-wrap`, `items-center`, `justify-between`, `flex-1`
- Grid: `grid`, `grid-cols-{1..12}`, `col-span-{1..12}`, `gap-{size}`
- Typography: `text-{xs..9xl}`, `font-{100..900}`, `text-center`, `uppercase`
- Colors: `text-{color}-{50..900}`, `bg-{color}-{50..900}`, `border-{color}-{50..900}`
- Sizing: `w-full`, `w-1/2`, `h-screen`, `max-w-{lg|x1..7xl}`
- Borders: `border`, `border-{2|4|8}`, `rounded-{sm|lg|xl|full}`
- Shadows: `shadow-{sm|md|lg|x1|2x1|inner}`
- Position: `relative`, `absolute`, `fixed`, `sticky`, `z-{0|10|20|30|40|50}`
- Transitions: `transition`, `transition-colors`, `duration-{200|300}`

## Components
- `.btn`, `.btn-primary`, `.btn-outline-primary`, `.btn-{sm|lg}`, `.btn-block`
- `.card`, `.card-header`, `.card-body`, `.card-footer`, `.card-title`
- `.badge`, `.badge-{variant}`, `.badge-pill`
- `.spinner`, `.skeleton`, `.progress`, `.progress-bar`
- `.modal`, `.modal-overlay`, `.modal-content`, `.modal-header/body/footer`
- `.tabs-container`, `.tab-label`, `.tab-panel`
- `.accordion`, `.accordion-content`
- `.dropdown`, `.dropdown-trigger`, `.dropdown-menu`, `.dropdown-item`
- `.toast`, `.toast-close`
- `.switch` (checkbox + role="switch")
- `.table`, `.table-striped`, `.pagination`
- `.avatar`, `.avatar-{sm|lg}`, `.avatar-group`
- `.tooltip` via `data-tooltip` attribute
- `.breadcrumb`, `.breadcrumb-item`
- `.menu`, `.menu-item`
- `.timeline`, `.timeline-item`
- `.rating`, `.rating-star`
- `.stepper`, `.stepper-item`
- `.stat`, `.stat-value`, `.stat-label`
- `.list-group`, `.list-group-item`
- `.alert`, `.alert-{color}`
- `.form-group`, `.form-label`, `.input-group`
- `.navbar`, `.navbar-brand`, `.navbar-nav`
- `.hero-section`

## Accessibility
- All components need proper ARIA attributes
- Interactive elements need `:focus-visible` outlines
- Modals need `role="dialog" aria-modal="true"`
- Progress bars need `role="progressbar"` with `aria-valuenow/min/max`
- Tabs need `role="tablist"`, `role="tab"`, `role="tabpanel"`, `aria-selected`
- Use `role="alert"` for alerts and toasts
- Respect `prefers-reduced-motion`
