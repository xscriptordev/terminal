<h1>Contributing to Xscriptor OpenCode</h1>

<p>Thank you for your interest in contributing to this project. Contributions are welcome whether you want to add new color schemes, improve existing themes, fix bugs, or enhance documentation.</p>

<h2>How to Contribute</h2>

<h3>Reporting Issues</h3>

<p>If you find a bug or have a suggestion, open an issue at <a href="https://github.com/xscriptor-colors/terminal/issues">github.com/xscriptor-colors/terminal/issues</a>. Include as much detail as possible:</p>

<ul>
  <li>A clear description of the issue</li>
  <li>Steps to reproduce</li>
  <li>Expected vs actual behavior</li>
  <li>Screenshots if applicable</li>
</ul>

<h3>Adding a New Theme</h3>

<ol>
  <li>Define your ANSI color palette (16 colors) in <code>colors.md</code> following the existing format</li>
  <li>Create a corresponding JSON file in <code>themes/xscriptor-themes/colors/</code> using the <a href="https://opencode.ai/docs/themes">OpenCode theme specification</a></li>
  <li>Add the theme name to the <code>THEMES</code> array in <code>install.sh</code></li>
  <li>Update the tables in <code>README.md</code> and <code>themes/xscriptor-themes/README.md</code></li>
</ol>

<h3>Code Standards</h3>

<ul>
  <li>Theme JSON files must be valid JSON and pass <code>python3 -c "import json; json.load(open('file.json'))"</code></li>
  <li>Follow the existing structure: <code>defs</code> for color references, <code>theme</code> for semantic mappings</li>
  <li>Include the <code>$schema</code> field pointing to <code>https://opencode.ai/theme.json</code></li>
  <li>Shell scripts must be POSIX-compatible and pass <code>shellcheck</code></li>
</ul>

<h3>Pull Request Process</h3>

<ol>
  <li>Fork the repository</li>
  <li>Create a feature branch: <code>git checkout -b feature/my-theme</code></li>
  <li>Commit your changes with clear messages</li>
  <li>Push to your fork and open a pull request</li>
  <li>Ensure all checks pass (JSON validation, shellcheck)</li>
</ol>

<h2>Code of Conduct</h2>

<p>All contributors must adhere to the <a href="CODE_OF_CONDUCT.md">Code of Conduct</a>. Be respectful, constructive, and collaborative.</p>

<h2>Contact</h2>

<p>Maintainer: <a href="mailto:x@xscriptor">x@xscriptor</a></p>
