<h1>Config Presets (Experimental)</h1>

<p>This directory is in an <strong>experimental</strong> phase. Content may change, break, or be removed without notice.</p>

<p>The goal is to provide pre-configured <a href="https://opencode.ai/docs/config">OpenCode configuration profiles</a> for different workflows and use cases.</p>

<h2>Planned Presets</h2>

<ul>
  <li><strong>strict-security</strong> - All write operations set to <code>ask</code>, minimal tool access</li>
  <li><strong>full-automation</strong> - Maximum tool permissions for CI/automation workflows</li>
  <li><strong>pair-programming</strong> - Balanced permissions with safety prompts</li>
  <li><strong>minimal</strong> - Clean starter config with recommended defaults</li>
  <li><strong>keybinds</strong> - Custom keybinding profiles (vim-like, emacs-like)</li>
</ul>

<h2>Contents</h2>

<ul>
  <li><code>opencode.json</code> - Main configuration</li>
  <li><code>tui.json</code> - Terminal UI configuration and theme selection</li>
  <li><code>keybinds.json</code> - Custom keybinding mappings</li>
</ul>
