#!/usr/bin/env python3
"""Folkline UI Generator — Generate HTML components by name"""
import sys
import json

COMPONENTS = {
    "button": '<button class="btn btn-primary">Button</button>',
    "button-outline": '<button class="btn btn-outline-primary">Outline</button>',
    "button-success": '<button class="btn btn-success">Success</button>',
    "button-danger": '<button class="btn btn-danger">Danger</button>',
    "button-sm": '<button class="btn btn-sm">Small</button>',
    "button-lg": '<button class="btn btn-lg">Large</button>',
    "button-block": '<button class="btn btn-primary btn-block">Full Width</button>',
    "card": '<div class="card"><div class="card-header">Header</div><div class="card-body"><h5 class="card-title">Title</h5><p class="card-text">Content</p></div><div class="card-footer">Footer</div></div>',
    "badge": '<span class="badge badge-primary">Badge</span>',
    "badge-pill": '<span class="badge badge-pill badge-primary">Pill</span>',
    "alert": '<div class="alert alert-primary" role="alert"><strong>Info:</strong> Alert message</div>',
    "alert-success": '<div class="alert alert-success" role="alert">Success message</div>',
    "alert-danger": '<div class="alert alert-danger" role="alert">Danger message</div>',
    "spinner": '<div class="spinner" role="status" aria-label="Loading"></div>',
    "progress": '<div class="progress" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"><div class="progress-bar" style="width:60%"></div></div>',
    "skeleton": '<div class="skeleton" style="width:100%;height:16px;border-radius:4px"></div>',
    "avatar": '<div class="avatar">JD</div>',
    "avatar-group": '<div class="avatar-group"><div class="avatar">A</div><div class="avatar">B</div></div>',
    "breadcrumb": '<nav class="breadcrumb" aria-label="Breadcrumb"><a href="#" class="breadcrumb-item">Home</a><span class="breadcrumb-item active" aria-current="page">Current</span></nav>',
    "pagination": '<nav class="pagination" aria-label="Page navigation"><a href="#" class="pagination-item">1</a><a href="#" class="pagination-item active" aria-current="page">2</a><a href="#" class="pagination-item">3</a></nav>',
    "toast": '<div class="toast" role="alert">Message<button class="toast-close" aria-label="Close">x</button></div>',
    "switch": '<label class="switch" aria-label="Toggle"><input type="checkbox" role="switch" /><span class="switch-slider"></span></label>',
    "tooltip": '<button data-tooltip="Tooltip text" class="btn btn-sm">Hover me</button>',
    "modal": '<div class="modal" role="dialog" aria-modal="true" aria-label="Dialog"><div class="modal-overlay"></div><div class="modal-content"><div class="modal-header"><h3 class="modal-title">Title</h3><button class="modal-close" aria-label="Close">x</button></div><div class="modal-body"><p>Content</p></div><div class="modal-footer"><button class="btn btn-primary">OK</button></div></div></div>',
    "form-input": '<div class="form-group"><label class="form-label" for="input">Label</label><input type="text" id="input" class="input-group" placeholder="Enter text" /></div>',
    "form-select": '<div class="form-group"><label class="form-label">Select</label><select class="input-group"><option>Option 1</option><option>Option 2</option></select></div>',
    "navbar": '<nav class="navbar"><a href="#" class="navbar-brand">Brand</a><div class="navbar-nav"><a href="#">Link</a><a href="#">Link</a></div></nav>',
    "hero": '<section class="hero-section text-center p-8"><h1>Hero Title</h1><p class="text-muted">Subtitle text here.</p><button class="btn btn-primary btn-lg">CTA</button></section>',
    "stat": '<div class="stat"><div class="stat-label">Users</div><div class="stat-value">12,847</div><div class="stat-desc">+12% growth</div></div>',
    "table": '<table class="table"><thead><tr><th>Name</th><th>Role</th></tr></thead><tbody><tr><td>John</td><td>Admin</td></tr></tbody></table>',
    "menu": '<div class="menu" role="menu"><a href="#" class="menu-item active" role="menuitem">Dashboard</a><a href="#" class="menu-item" role="menuitem">Settings</a></div>',
    "timeline": '<div class="timeline"><div class="timeline-item"><div class="timeline-dot"></div><div class="timeline-content"><h4>Event</h4><p class="text-muted">Description</p></div></div></div>',
    "rating": '<div class="rating"><span class="rating-star filled">star</span><span class="rating-star filled">star</span><span class="rating-star">star</span></div>',
    "code": '<code class="code">npm install</code>',
    "kbd": '<kbd class="kbd">Ctrl+C</kbd>',
    "separator": '<hr class="separator" />',
    "upload-zone": '<div class="upload-zone" role="button" tabindex="0"><span class="upload-zone-icon">Upload</span><p class="upload-zone-text">Drop files here</p></div>',
    "faq": '<details class="faq-item"><summary class="faq-question">Question?</summary><div class="faq-answer">Answer text.</div></details>',
    "stepper": '<div class="stepper" aria-label="Progress"><div class="stepper-item completed"><span class="stepper-number">1</span><span class="stepper-label">Step 1</span></div><div class="stepper-item active"><span class="stepper-number">2</span><span class="stepper-label">Step 2</span></div></div>',
    "list-group": '<div class="list-group"><div class="list-group-item">Item</div><div class="list-group-item active">Active</div></div>',
}

def main():
    if len(sys.argv) < 2:
        print("Usage: python generator.py <component_name>")
        print("Available components: " + ", ".join(sorted(COMPONENTS.keys())))
        return

    name = sys.argv[1].lower().replace(" ", "-").replace("_", "-")
    if name == "--list":
        print("\n".join(sorted(COMPONENTS.keys())))
        return

    if name not in COMPONENTS:
        print(json.dumps({"error": f"Component '{name}' not found", "available": list(COMPONENTS.keys())}))
        sys.exit(1)

    result = {
        "name": name,
        "html": COMPONENTS[name],
        "framework": "Folkline UI v3.0.0",
        "cdn": "https://cdn.jsdelivr.net/npm/@realtoheed/folkline-ui@3/dist/folkline.min.css",
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
