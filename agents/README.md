<h1>Agents (Experimental)</h1>

<p>This directory is in an <strong>experimental</strong> phase. Content may change, break, or be removed without notice.</p>

<p>The goal is to provide a collection of ready-to-use <a href="https://opencode.ai/docs/agents">OpenCode agent definitions</a> for specific workflows and roles.</p>

<h2>Planned Agents</h2>

<ul>
  <li><strong>code-reviewer</strong> - Read-only agent focused on code quality and security</li>
  <li><strong>docs-writer</strong> - Technical writing agent for documentation</li>
  <li><strong>security-auditor</strong> - Security-focused analysis agent</li>
  <li><strong>db-migrator</strong> - Database migration specialist</li>
  <li><strong>technical-expert</strong> - Deep technical analysis agent</li>
</ul>

<h2>Usage</h2>

<p>Copy the agent markdown files to your OpenCode agents directory:</p>

<pre><code>cp agents/*.md ~/.config/opencode/agents/</code></pre>

<p>Once loaded, agents can be invoked with the <code>@</code> mention in OpenCode.</p>
