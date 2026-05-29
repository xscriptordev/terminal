<h1>Skills (Experimental)</h1>

<p>This directory is in an <strong>experimental</strong> phase. Content may change, break, or be removed without notice.</p>

<p>The goal is to provide reusable <a href="https://opencode.ai/docs/skills">OpenCode skill definitions</a> (SKILL.md files) that agents can load on-demand for specific tasks.</p>

<h2>Planned Skills</h2>

<ul>
  <li><strong>git-release</strong> - Create consistent releases and changelogs</li>
  <li><strong>pr-review</strong> - Pull request review workflow</li>
  <li><strong>db-migration</strong> - Database migration patterns and best practices</li>
  <li><strong>deploy-checklist</strong> - Deployment readiness verification</li>
  <li><strong>api-design</strong> - REST/GraphQL API design guidelines</li>
</ul>

<h2>Usage</h2>

<p>Copy skill directories to your OpenCode skills path:</p>

<pre><code>cp -r skills/* ~/.config/opencode/skills/</code></pre>

<p>Agents discover and load skills automatically via the <code>skill</code> tool when needed.</p>
