<h1 align="center">X OpenCode</h1>

<p align="center"><img src="https://raw.githubusercontent.com/xscriptor/xassets/main/xrepos/opencode/logo.svg" width="100" alt="Opencode Xscriptor logo" /></p>

<p>A collection of themes, configurations, and tooling for <a href="https://opencode.ai">OpenCode</a>, the open source AI coding agent for the terminal.</p>

<p>This repository contains carefully crafted terminal color schemes translated into OpenCode's semantic theme format, along with utilities for installation and management.</p>


<h2 align="center">Contents</h2>

<ul>
  <li><a href="colors.md"><code>colors.md</code></a> - ANSI terminal color palette definitions (12 schemes)</li>
  <li><a href="themes/xscriptor-themes/"><code>themes/xscriptor-themes/</code></a> - OpenCode theme JSON files ready to use</li>
  <li><a href="themes/xscriptor-themes/install.sh"><code>install.sh</code></a> - Automated installation script (local or remote)</li>
</ul>

<h2 align="center">Themes</h2>

<table>
  <thead>
    <tr>
      <th>Theme</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>x</code></td>
      <td>Dark</td>
      <td>Deep dark with vibrant pink, green, and cyan accents</td>
    </tr>
    <tr>
      <td><code>madrid</code></td>
      <td>Light</td>
      <td>Clean light with deep red, green, and blue tones</td>
    </tr>
    <tr>
      <td><code>lahabana</code></td>
      <td>Dark</td>
      <td>Dark gray with bright neon accents</td>
    </tr>
    <tr>
      <td><code>miami</code></td>
      <td>Dark</td>
      <td>True black with synthwave-inspired colors</td>
    </tr>
    <tr>
      <td><code>paris</code></td>
      <td>Dark</td>
      <td>Purple-black with pastel cyan and blue</td>
    </tr>
    <tr>
      <td><code>tokio</code></td>
      <td>Dark</td>
      <td>Dark gray with balanced warm and cool tones</td>
    </tr>
    <tr>
      <td><code>oslo</code></td>
      <td>Dark</td>
      <td>Blue-gray with professional muted palette</td>
    </tr>
    <tr>
      <td><code>helsinki</code></td>
      <td>Light</td>
      <td>Near-white with earthy, natural tones</td>
    </tr>
    <tr>
      <td><code>berlin</code></td>
      <td>Dark</td>
      <td>Black with monochrome grayscale palette</td>
    </tr>
    <tr>
      <td><code>london</code></td>
      <td>Light</td>
      <td>White with sophisticated grayscale tones</td>
    </tr>
    <tr>
      <td><code>praha</code></td>
      <td>Dark</td>
      <td>Dark with Dracula-inspired vibrant colors</td>
    </tr>
    <tr>
      <td><code>bogota</code></td>
      <td>Dark</td>
      <td>Maroon-black with cyan and warm accents</td>
    </tr>
  </tbody>
</table>

<h2 align="center">Quick Start</h2>

<pre><code>curl -fsSL https://raw.githubusercontent.com/xscriptor/opencode/main/themes/xscriptor-themes/install.sh | bash</code></pre>

<p>Then select a theme in OpenCode with <code>/theme</code> or set it in <code>tui.json</code>:</p>

<pre><code>{
  "theme": "x"
}</code></pre>

<h2 align="center">Resources</h2>

<ul>
  <li><a href="https://opencode.ai">OpenCode Website</a></li>
  <li><a href="https://opencode.ai/docs/themes">OpenCode Themes Documentation</a></li>
  <li><a href="https://github.com/anomalyco/opencode">OpenCode GitHub Repository</a></li>
  <li><a href="themes/xscriptor-themes/README.md">Theme Installation Guide</a></li>
</ul>

<h2 align="center">License</h2>

<p>MIT</p>
