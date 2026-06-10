# Folkline UI Reference Examples

## Button Variants
```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Danger</button>
<button class="btn btn-warning">Warning</button>
<button class="btn btn-info">Info</button>
<button class="btn btn-outline-primary">Outline Primary</button>
<button class="btn btn-sm">Small</button>
<button class="btn btn-lg">Large</button>
<button class="btn btn-primary btn-block">Full Width</button>
```

## Card Layouts
```html
<div class="card">
  <div class="card-header">Header</div>
  <div class="card-body">
    <h5 class="card-title">Title</h5>
    <p class="card-text">Content here.</p>
  </div>
  <div class="card-footer">Footer</div>
</div>

<div class="card card-hover">
  <div class="card-body">
    <h5 class="card-title">Hover Card</h5>
    <p class="card-text">Hover effect applied.</p>
  </div>
</div>
```

## Layout Patterns
```html
<!-- Flexbox row with centered items -->
<div class="flex items-center justify-between p-4">
  <div class="fw-700 fs-lg">Logo</div>
  <nav class="flex gap-4">
    <a href="#" class="text-muted">Link</a>
    <a href="#" class="text-muted">Link</a>
  </nav>
  <button class="btn btn-primary btn-sm">Action</button>
</div>

<!-- Grid layout -->
<div class="grid grid-cols-3 gap-4">
  <div class="p-4 border rounded-lg">Item 1</div>
  <div class="p-4 border rounded-lg">Item 2</div>
  <div class="p-4 border rounded-lg">Item 3</div>
</div>
```

## Form
```html
<div class="form-group">
  <label class="form-label" for="email">Email</label>
  <input type="email" id="email" class="input-group" placeholder="you@example.com" />
  <small class="form-text">We'll never share your email.</small>
</div>
<div class="input-error">This field is required.</div>
```

## Responsive Layout
```html
<div class="container">
  <div class="row">
    <div class="col-12 col-md-6">Half on desktop, full on mobile</div>
    <div class="col-12 col-md-6">Half on desktop, full on mobile</div>
  </div>
</div>
```

## Alert Messages
```html
<div class="alert alert-primary" role="alert"><strong>Info:</strong> Message here.</div>
<div class="alert alert-success" role="alert">Success message.</div>
<div class="alert alert-danger" role="alert">Error message.</div>
<div class="alert alert-warning" role="alert">Warning message.</div>
```

## Navbar
```html
<nav class="navbar">
  <a href="#" class="navbar-brand">Brand</a>
  <div class="navbar-nav">
    <a href="#">Home</a>
    <a href="#">About</a>
    <a href="#">Contact</a>
  </div>
  <button class="navbar-toggle" aria-label="Toggle navigation">☰</button>
</nav>
```

## Common Class Combinations
```html
<!-- Avatar with status -->
<div class="avatar avatar-lg">
  JD
  <span class="avatar-status-dot online"></span>
</div>

<!-- Stats card -->
<div class="stat-card">
  <div class="stat-label">Revenue</div>
  <div class="stat-value">$48,290</div>
  <div class="stat-desc">↑ 12.5% from last month</div>
</div>

<!-- Button group -->
<div class="flex gap-2">
  <button class="btn btn-primary">Save</button>
  <button class="btn btn-outline-primary">Cancel</button>
</div>

<!-- Full-width hero -->
<section class="hero-section text-center p-8">
  <h1>Welcome</h1>
  <p class="text-muted fs-lg mb-4">Subtitle goes here.</p>
  <button class="btn btn-primary btn-lg">Get Started</button>
</section>
```
