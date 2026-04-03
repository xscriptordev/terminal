<h1 align="center"> Contributing to Xscriptor Helix </h1>

<div align="center">
<p>First off, thank you for considering contributing to <b>Helix - Xscriptor</b>! It's people like you that make these themes a more accessible and beautiful experience for everyone.</p>
</div>

<hr />

<h2 align="center" id="how-can-i-contribute"> How Can I Contribute? </h2>

<h3 align="center"> 1. Reporting Bugs </h3>
<p>If you find a broken color palette, an issue with the installer script, or a syntax highlighting bug in the themes, please report it!</p>
<ul>
  <li>Check if the issue has already been reported in the issues tab.</li>
  <li>Open a new issue with a clear title and description.</li>
  <li>Include your Helix version and the specific theme you are using.</li>
</ul>

<h3 align="center"> 2. Suggesting Enhancements </h3>
<p>Have an idea for a new color scheme, a better installer flag, or an accessibility improvement?</p>
<ul>
  <li>Open an issue describing your idea.</li>
  <li>Explain how it benefits the accessibility or aesthetics of the project.</li>
</ul>

<h3 align="center"> 3. Submitting Pull Requests (PRs) </h3>
<p>We welcome contributions! To submit a change:</p>

<ol>
  <li><b>Fork the repository</b> to your own GitHub account.</li>
  <li><b>Create a branch</b> for your feature or bug fix (<code>git checkout -b feature/amazing-theme</code>).</li>
  <li><b>Make your changes</b>. Please keep your code clean and follow the project structure.</li>
  <li><b>Test your changes</b> directly in Helix by loading the modified theme.</li>
  <li><b>Commit your changes</b> with a clear and descriptive commit message.</li>
  <li><b>Push to your fork</b> (<code>git push origin feature/amazing-theme</code>).</li>
  <li><b>Open a Pull Request</b> against the <code>main</code> branch of Xscriptor Helix.</li>
</ol>

<hr />

<h2 align="center" id="development-guidelines"> Development Guidelines </h2>

<h3 align="center"> Themes (TOML) </h3>
<ul>
  <li>All themes must be located in the <code>themes/</code> directory.</li>
  <li>Ensure the color palette follows accessibility standards (good contrast).</li>
  <li>Use standard Helix scope names to ensure compatibility with different languages.</li>
</ul>

<h3 align="center"> Installer & Scripts (Shell/Rust) </h3>
<ul>
  <li>Ensure the <code>install.sh</code> remains compatible with both <code>curl</code> and <code>wget</code>.</li>
  <li>If you modify the installation logic, test all flags (<code>--minimal</code>, <code>--themes-only</code>, etc.).</li>
  <li>Maintain POSIX compliance in shell scripts where possible.</li>
</ul>

<h3 align="center"> Configuration </h3>
<ul>
  <li>Avoid hardcoding system-specific paths in <code>config.toml</code> templates.</li>
  <li>Keep the <code>minimal</code> configuration strictly essential.</li>
</ul>

<hr />

<div align="center">
  <p><b>Thank you for your contributions!</b></p>
</div>