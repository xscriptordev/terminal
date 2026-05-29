<h1>Plugins (Experimental)</h1>

<p>This directory is in an <strong>experimental</strong> phase. Content may change, break, or be removed without notice.</p>

<p>The goal is to provide example <a href="https://opencode.ai/docs/plugins">OpenCode plugins</a> written in JavaScript and TypeScript that demonstrate how to extend OpenCode with custom hooks and tools.</p>

<h2>Planned Plugins</h2>

<ul>
  <li><strong>notifications</strong> - System notifications on session events</li>
  <li><strong>env-protector</strong> - Prevent reading .env files</li>
  <li><strong>custom-tools</strong> - Example of adding custom tools via the SDK</li>
  <li><strong>session-logger</strong> - Structured session logging</li>
  <li><strong>compaction-hook</strong> - Custom context injection on compaction</li>
</ul>

<h2>Usage</h2>

<p>Copy plugin files to your OpenCode plugins directory:</p>

<pre><code>cp plugins/*.ts ~/.config/opencode/plugins/</code></pre>

<p>Or reference them as npm packages in your <code>opencode.json</code> once published.</p>
