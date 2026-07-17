<h1>Theme Build Script</h1>

<p>Generates <a href="https://opencode.ai/docs/themes">OpenCode built-in theme</a> JSON files from the Xscriptor color palette collection.</p>

<h2>Requirements</h2>

<ul>
  <li>Python 3.7 or later</li>
</ul>

<h2>Usage</h2>

<h3>Standalone mode (built-in data)</h3>

<p>Uses the 12 pre-defined themes compiled into the script:</p>

<pre><code>./generate.py
./generate.py --output ../dist</code></pre>

<h3>Parse from colors.md</h3>

<p>Reads ANSI color definitions from <code>colors.md</code> and converts them to the full OpenCode semantic theme format with auto-generated dark/light variants:</p>

<pre><code>./generate.py --colors ../../colors.md
./generate.py --colors ../../colors.md --output ../dist</code></pre>

<h2>Output</h2>

<p>All generated theme JSON files are written to the specified output directory (default: <code>dist/</code>). Each file follows the <code>https://opencode.ai/theme.json</code> schema with:</p>

<ul>
  <li><code>defs</code> - Color definitions with <code>dark</code> and <code>light</code> prefixed references</li>
  <li><code>theme</code> - Semantic color mappings with <code>{ "dark": "...", "light": "..." }</code> variant objects</li>
</ul>

<h2>Generated Themes</h2>

<table>
  <thead>
    <tr>
      <th>Theme</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>x</td><td>Dark</td><td>Deep dark with vibrant pink, green, and cyan accents</td></tr>
    <tr><td>madrid</td><td>Light</td><td>Clean light with deep red, green, and blue tones</td></tr>
    <tr><td>lahabana</td><td>Dark</td><td>Dark gray with bright neon accents</td></tr>
    <tr><td>miami</td><td>Dark</td><td>True black with synthwave-inspired colors</td></tr>
    <tr><td>paris</td><td>Dark</td><td>Purple-black with pastel cyan and blue</td></tr>
    <tr><td>tokio</td><td>Dark</td><td>Dark gray with balanced warm and cool tones</td></tr>
    <tr><td>oslo</td><td>Dark</td><td>Blue-gray with professional muted palette</td></tr>
    <tr><td>helsinki</td><td>Light</td><td>Near-white with earthy, natural tones</td></tr>
    <tr><td>berlin</td><td>Dark</td><td>Black with monochrome grayscale palette</td></tr>
    <tr><td>london</td><td>Light</td><td>White with sophisticated grayscale tones</td></tr>
    <tr><td>praha</td><td>Dark</td><td>Dark with Dracula-inspired vibrant colors</td></tr>
    <tr><td>bogota</td><td>Dark</td><td>Maroon-black with cyan and warm accents</td></tr>
  </tbody>
</table>

<h2>How It Works</h2>

<ol>
  <li><strong>Standalone mode:</strong> Uses theme data built into the script with pre-designed dark/light variants for each scheme.</li>
  <li><strong>colors.md mode:</strong> Parses the markdown file, extracts ANSI color tables (color0-color15), and auto-generates full OpenCode themes. Light variants are derived by swapping background/foreground and blending accent colors.</li>
  <li>Each theme is written as a separate JSON file in the output directory.</li>
</ol>

<h2>Using the Output</h2>

<p>The generated files are ready for submission as built-in themes in the OpenCode repository. Copy them to:</p>

<pre><code>packages/opencode/src/cli/cmd/tui/context/theme/</code></pre>

<p>Then register each theme in <code>theme.tsx</code> by adding an import and an entry in the <code>DEFAULT_THEMES</code> object.</p>
