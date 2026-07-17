<h1>Xscriptor Themes for OpenCode</h1>

<p>A collection of themes for <a href="https://opencode.ai">OpenCode</a> based on the Xscriptor terminal color schemes. These themes are derived from the ANSI color palettes defined in the <code>colors.md</code> specification and translated into OpenCode's full semantic theme format.</p>

<h2>Available Themes</h2>

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
      <td>Deep dark background with vibrant pink, green, and cyan accents</td>
    </tr>
    <tr>
      <td><code>madrid</code></td>
      <td>Light</td>
      <td>Clean light background with deep red, green, and blue tones</td>
    </tr>
    <tr>
      <td><code>lahabana</code></td>
      <td>Dark</td>
      <td>Dark gray background with bright neon accents</td>
    </tr>
    <tr>
      <td><code>miami</code></td>
      <td>Dark</td>
      <td>True black background with vibrant synthwave-inspired colors</td>
    </tr>
    <tr>
      <td><code>paris</code></td>
      <td>Dark</td>
      <td>Deep purple-black background with pastel cyan and blue accents</td>
    </tr>
    <tr>
      <td><code>tokio</code></td>
      <td>Dark</td>
      <td>Dark gray background with balanced warm and cool tones</td>
    </tr>
    <tr>
      <td><code>oslo</code></td>
      <td>Dark</td>
      <td>Dark blue-gray background with professional muted palette</td>
    </tr>
    <tr>
      <td><code>helsinki</code></td>
      <td>Light</td>
      <td>Near-white background with earthy, natural tones</td>
    </tr>
    <tr>
      <td><code>berlin</code></td>
      <td>Dark</td>
      <td>True black background with monochrome grayscale palette</td>
    </tr>
    <tr>
      <td><code>london</code></td>
      <td>Light</td>
      <td>White background with sophisticated grayscale tones</td>
    </tr>
    <tr>
      <td><code>praha</code></td>
      <td>Dark</td>
      <td>Dark background with Dracula-inspired vibrant colors</td>
    </tr>
    <tr>
      <td><code>bogota</code></td>
      <td>Dark</td>
      <td>Deep maroon-black background with cyan and warm accents</td>
    </tr>
  </tbody>
</table>

<h2>Installation</h2>

<h3>Prerequisites</h3>

<ul>
  <li><a href="https://opencode.ai">OpenCode</a> installed</li>
  <li>Your terminal must support <strong>truecolor</strong> (24-bit color). Run <code>echo $COLORTERM</code> to verify it outputs <code>truecolor</code> or <code>24bit</code></li>
</ul>

<h3>Option 1: Automated Install (Recommended)</h3>

<p>Run the install script directly from GitHub:</p>

<pre><code>curl -fsSL https://raw.githubusercontent.com/xscriptor/opencode/main/themes/xscriptor-themes/install.sh | bash</code></pre>

<p>Or clone the repository and run the script locally:</p>

<pre><code>git clone https://github.com/xscriptor/opencode.git
cd opencode/themes/xscriptor-themes
chmod +x install.sh
./install.sh</code></pre>

<h3>Option 2: Manual Install</h3>

<p>Copy the theme files to the OpenCode themes directory:</p>

<pre><code># Create the themes directory if it doesn't exist
mkdir -p ~/.config/opencode/themes

# Copy all themes
cp colors/*.json ~/.config/opencode/themes/</code></pre>

<h2>Usage</h2>

<p>Once installed, select a theme in OpenCode using the <code>/theme</code> command inside the TUI, or set it directly in your <code>tui.json</code> configuration file:</p>

<pre><code>{
  "$schema": "https://opencode.ai/tui.json",
  "theme": "x"
}</code></pre>

<p>Replace <code>"x"</code> with any of the available theme names (<code>madrid</code>, <code>lahabana</code>, <code>miami</code>, <code>paris</code>, <code>tokio</code>, <code>oslo</code>, <code>helsinki</code>, <code>berlin</code>, <code>london</code>, <code>praha</code>, <code>bogota</code>).</p>

<h2>Theme Locations</h2>

<p>OpenCode loads themes from the following directories, with later directories overriding earlier ones:</p>

<ol>
  <li><strong>Built-in themes</strong> - embedded in the binary</li>
  <li><strong>User config directory</strong> - <code>~/.config/opencode/themes/*.json</code></li>
  <li><strong>Project root directory</strong> - <code>.opencode/themes/*.json</code></li>
  <li><strong>Current working directory</strong> - <code>./.opencode/themes/*.json</code></li>
</ol>

<p>For personal use, install to <code>~/.config/opencode/themes/</code>. For project-specific themes, use <code>.opencode/themes/</code> in your project root.</p>

<h2>Theme Format</h2>

<p>Each theme follows the <a href="https://opencode.ai/docs/themes">OpenCode theme specification</a>. The structure includes:</p>

<ul>
  <li><code>defs</code> - Color definitions referencing the original ANSI terminal palette</li>
  <li><code>theme</code> - Semantic color mappings for the OpenCode UI, including syntax highlighting, markdown rendering, diff views, and interface elements</li>
</ul>

<p>All themes reference the <code>https://opencode.ai/theme.json</code> schema for validation and editor autocompletion.</p>

<h2>Repository Structure</h2>

<pre><code>themes/xscriptor-themes/
  colors/          # Theme JSON files (one per color scheme)
    x.json
    madrid.json
    ...
  install.sh       # Automated installation script
  README.md        # This file</code></pre>

<h2>Source</h2>

<p>The original ANSI color definitions are documented in <a href="https://github.com/xscriptor/opencode/blob/main/colors.md"><code>colors.md</code></a> at the repository root.</p>

<h2>License</h2>

<p>MIT</p>
