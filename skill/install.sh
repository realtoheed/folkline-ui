#!/usr/bin/env bash
# Folkline UI Skill Installer
# Installs the Folkline UI skill for all supported AI coding platforms.
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_NAME="folkline-ui"
PLATFORMS=()

info()  { echo -e "\033[1;34m→\033[0m $1"; }
success() { echo -e "\033[1;32m✓\033[0m $1"; }
warn()  { echo -e "\033[1;33m!\033[0m $1"; }

# Detect home directory
HOME_DIR="${HOME}"
if [ -z "${HOME_DIR}" ]; then
    warn "HOME not set, using /root"
    HOME_DIR="/root"
fi

install_opencode() {
    local dest="${HOME_DIR}/.opencode/skills/${SKILL_NAME}"
    mkdir -p "${dest}"
    cp -r "${SKILL_DIR}/SKILL.md" "${dest}/"
    cp -r "${SKILL_DIR}/data" "${dest}/"
    cp -r "${SKILL_DIR}/scripts" "${dest}/"
    cp -r "${SKILL_DIR}/configs/opencode.yaml" "${dest}/opencode.yaml" 2>/dev/null || true
    PLATFORMS+=("opencode")
    success "Installed OpenCode skill at ${dest}"
}

install_claude() {
    local dest="${HOME_DIR}/.claude/skills/${SKILL_NAME}"
    mkdir -p "${dest}"
    cp -r "${SKILL_DIR}/SKILL.md" "${dest}/"
    cp -r "${SKILL_DIR}/data" "${dest}/"
    cp -r "${SKILL_DIR}/configs/claude.yaml" "${dest}/claude.yaml" 2>/dev/null || true
    PLATFORMS+=("claude")
    success "Installed Claude Code skill at ${dest}"
}

install_cursor() {
    local dest="${HOME_DIR}/.cursor/rules"
    mkdir -p "${dest}"
    cp "${SKILL_DIR}/configs/cursor.mdc" "${dest}/${SKILL_NAME}.mdc" 2>/dev/null || true
    PLATFORMS+=("cursor")
    success "Installed Cursor rules at ${dest}/${SKILL_NAME}.mdc"
}

install_windsurf() {
    local dest="${HOME_DIR}/.windsurf/rules"
    mkdir -p "${dest}"
    cp "${SKILL_DIR}/configs/windsurf.md" "${dest}/${SKILL_NAME}.md" 2>/dev/null || true
    PLATFORMS+=("windsurf")
    success "Installed Windsurf rules at ${dest}/${SKILL_NAME}.md"
}

install_copilot() {
    local dest=".github"
    if [ -d ".github" ]; then
        cp "${SKILL_DIR}/configs/copilot.md" "${dest}/copilot-instructions.md" 2>/dev/null || true
        PLATFORMS+=("copilot")
        success "Installed GitHub Copilot instructions at ${dest}/copilot-instructions.md"
    else
        warn "No .github directory found. Skipping Copilot. Run from project root or create .github/ manually."
    fi
}

install_continue() {
    local dest="${HOME_DIR}/.continue/skills"
    mkdir -p "${dest}"
    cp "${SKILL_DIR}/configs/continue.json" "${dest}/${SKILL_NAME}.json" 2>/dev/null || true
    PLATFORMS+=("continue")
    success "Installed Continue.dev skill at ${dest}/${SKILL_NAME}.json"
}

install_codegpt() {
    local dest="${HOME_DIR}/.codegpt/skills/${SKILL_NAME}"
    mkdir -p "${dest}"
    cp "${SKILL_DIR}/configs/codegpt.yaml" "${dest}/codegpt.yaml" 2>/dev/null || true
    PLATFORMS+=("codegpt")
    success "Installed CodeGPT skill at ${dest}"
}

install_pearai() {
    local dest="${HOME_DIR}/.pearai/rules"
    mkdir -p "${dest}"
    cp "${SKILL_DIR}/configs/pearai.md" "${dest}/${SKILL_NAME}.md" 2>/dev/null || true
    PLATFORMS+=("pearai")
    success "Installed PearAI rules at ${dest}/${SKILL_NAME}.md"
}

install_cline() {
    local dest="${HOME_DIR}/.cline/rules"
    mkdir -p "${dest}"
    cp "${SKILL_DIR}/configs/cline.md" "${dest}/${SKILL_NAME}.md" 2>/dev/null || true
    PLATFORMS+=("cline")
    success "Installed Cline rules at ${dest}/${SKILL_NAME}.md"
}

install_roocode() {
    local dest="${HOME_DIR}/.roocode/rules"
    mkdir -p "${dest}"
    cp "${SKILL_DIR}/configs/roocode.md" "${dest}/${SKILL_NAME}.md" 2>/dev/null || true
    PLATFORMS+=("roocode")
    success "Installed Roo Code rules at ${dest}/${SKILL_NAME}.md"
}

install_superflex() {
    local dest="${HOME_DIR}/.superflex/rules"
    mkdir -p "${dest}"
    cp "${SKILL_DIR}/configs/superflex.md" "${dest}/${SKILL_NAME}.md" 2>/dev/null || true
    PLATFORMS+=("superflex")
    success "Installed Superflex rules at ${dest}/${SKILL_NAME}.md"
}

# Main installation
echo ""
echo -e "\033[1;36m  Folkline UI Skill Installer\033[0m"
echo -e "\033[1;36m  ==========================\033[0m"
echo ""

info "Installing Folkline UI v3.0.0 skill..."

install_opencode
install_claude
install_cursor
install_windsurf
install_copilot
install_continue
install_codegpt
install_pearai
install_cline
install_roocode
install_superflex

echo ""
if [ ${#PLATFORMS[@]} -gt 0 ]; then
    success "Folkline UI skill installed for: ${PLATFORMS[*]}"
    echo ""
    echo -e "\033[1;32mUsage:\033[0m"
    echo "  Folkline UI is ready. When coding, ask for components or layouts"
    echo "  using utility classes and the skill will apply the correct patterns."
    echo ""
    echo -e "\033[1;32mCDN:\033[0m  https://cdn.jsdelivr.net/npm/@realtoheed/folkline-ui@3/dist/folkline.min.css"
    echo -e "\033[1;32mnpm:\033[0m  @realtoheed/folkline-ui"
else
    warn "No platforms were installed. Check your permissions."
fi
