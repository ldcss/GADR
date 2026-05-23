# 6. Migrate to Pure Lua Neovim Configuration

Date: 2025-10-04

## Status

Accepted

Supersedes [4. Use vim-plug in favour of Vundle](0004-use-vim-plug-in-favour-of-vundle.md)

Supersedes [5. Use coc in place of YCM](0005-use-coc-in-place-of-ycm.md)

## Context

The Neovim configuration had evolved into a hybrid setup with both Vimscript (`.vimrc`) and Lua files, using vim-plug
for plugin management and a mix of traditional Vim plugins and modern Neovim plugins. This created several issues:

1. **Maintenance complexity**: Managing two configuration languages and understanding which parts were Vimscript vs Lua
2. **Plugin manager limitations**: vim-plug, while good, is primarily designed for Vimscript and doesn't take full
   advantage of Neovim's Lua capabilities
3. **Performance**: Vimscript is slower than Lua, and vim-plug loads all plugins at startup
4. **Modern tooling**: Newer Neovim plugins are increasingly Lua-first, and some popular plugins (like NERDTree,
   vim-airline) have superior Lua-native alternatives
5. **Archived plugins**: null-ls (used for formatting/linting) was archived, with the community moving to more focused
   tools

## Decision

Completely migrate to a pure Lua Neovim configuration using lazy.nvim as the plugin manager, replacing all Vimscript
files and upgrading to modern Lua-native plugins where appropriate.

### Plugin Manager

- **From**: vim-plug
- **To**: [lazy.nvim](https://github.com/folke/lazy.nvim)
- **Rationale**: Lazy.nvim provides lazy-loading by default, better startup performance, cleaner plugin specifications
  in Lua, and is actively maintained for Neovim

### Plugin Upgrades

- **NERDTree** → **nvim-tree**: Lua-native file explorer with better performance
- **vim-airline** → **lualine**: Lua-native statusline, lighter and faster
- **vim-gitgutter** → **gitsigns.nvim**: Lua-native git integration with better features
- **ALE** → Removed (using LSP + conform.nvim + nvim-lint instead)
- **null-ls** → Replaced with **conform.nvim** (formatting) and **nvim-lint** (linting)
- **coc.nvim** → **nvim-lspconfig** (native LSP support)

### Configuration Structure

All Vimscript files removed and replaced with Lua:

- `dotfiles/.vimrc` (167 lines) → Migrated to `lua/plugins/*.lua` files
- `vim/ftplugin/*.vim` → `.config/nvim/ftplugin/*.lua`
- `.config/nvim/vscode/settings.vim` → `.config/nvim/vscode/settings.lua`

Plugin organization:

- `lua/plugins/theme.lua` - Colorscheme
- `lua/plugins/editor.lua` - Core editor enhancements
- `lua/plugins/ui.lua` - UI components (lualine, nvim-tree)
- `lua/plugins/git.lua` - Git integration
- `lua/plugins/languages.lua` - Language-specific plugins
- `lua/plugins/lsp.lua` - LSP configuration
- `lua/plugins/completion.lua` - nvim-cmp and sources
- `lua/plugins/formatting.lua` - conform.nvim
- `lua/plugins/linting.lua` - nvim-lint
- `lua/plugins/mason.lua` - Tool installer
- And others for telescope, treesitter, hop, etc.

### Tool Installation

Added Mason for automatic installation of formatters, linters, and LSP servers, reducing manual setup on new machines.

## Consequences

### Positive

1. **Better performance**: Lazy-loading plugins and Lua's speed improve startup time
2. **Cleaner codebase**: Single language (Lua) for all configuration
3. **Modern tooling**: Access to the latest Neovim ecosystem
4. **Better documentation**: Lua configurations are more readable and self-documenting
5. **Easier maintenance**: Separation of concerns with focused plugins (formatting vs linting)
6. **Portability**: Mason auto-installs tools, making setup easier on new machines
7. **Active maintenance**: All core plugins are actively maintained

### Negative

1. **Learning curve**: Need to understand Lua and lazy.nvim syntax
2. **Migration effort**: One-time cost of converting all Vimscript to Lua
3. **Some Vimscript remains**: Language-specific plugins (vim-go, Copilot, fugitive) still use Vimscript but work fine
   with Lua configuration

### Breaking Changes

1. Plugin commands changed:
   - `:PlugInstall` → `:Lazy install`
   - `:PlugUpdate` → `:Lazy update`
   - `:PlugClean` → `:Lazy clean`
2. Plugin storage location:
   - `~/.vim/plugged/` → `~/.local/share/nvim/lazy/`
3. No longer maintaining `.vimrc` (pure Neovim, no Vim compatibility)
4. Formatters/linters now managed by Mason instead of system packages

### Migration Notes

- Old `~/.vimrc` symlink removed
- All ftplugin files converted to Lua
- Autocmds migrated to `lua/user/autocmds.lua`
- VS Code integration updated to use Lua functions
- CLAUDE.md and README.md updated to reflect new architecture
