---
title: "The CodeGen Wars: Who's Still in the Loop?"
date: 2026-07-06
summary: "Sixteen platforms, four tiers, and one question every engineering team is quietly negotiating: how far do you sit from the keyboard? A field guide to the coding platform market in 2026 — from foundation models to app builders that ship while you're in a different meeting."
hero: "/images/codegen-wars-hero.webp"
heroAlt: "The CodeGen Wars — Who's still in the loop? State of the Union in AI, Article IV of IV."
series: "State of the Union in AI · Part 4 of 4"
seriesSlug: "state-of-the-union-in-ai"
seriesPart: 4
draft: false
---

On June 18th, Google quietly turned off Gemini Code Assist and the Gemini CLI for anyone not paying for an enterprise seat. Individual developers using the free and Pro tiers woke up to a migration notice pointing them to Antigravity, a new agent-first platform that plans, writes, tests, and deploys entire applications from a single prompt while a human watches from the sidelines. Nobody framed it as a retirement. It was one. The IDE extension you typed alongside is gone, and in its place is a system built to work without you typing much at all.

That single decision is the whole story of the coding platform market in 2026, compressed into one product announcement. Two years ago the question was whether an autocomplete tool could finish your function correctly. Today the question is how much of the software development lifecycle you are willing to hand to something that operates while you are in a different meeting, and what you are on the hook for when it gets something wrong. The technology stopped being about generation a while ago. It is now about orchestration, and the platforms competing for your attention have sorted themselves into distinct tiers based on exactly one variable: how far the human sits from the keyboard.

By the end of this piece you will have a map of that landscape, sixteen platforms across four tiers, and a clearer sense of where you personally want to draw the line between supervising the work and simply reading the pull request afterward. That line is not the same for every developer or every company, and pretending otherwise is how teams end up either babysitting a tool that didn't need it or shipping code nobody actually reviewed.

Before getting to the map, it's worth sitting with why the line matters as much as it does. A chat-based assistant that writes a function while you watch fails safely. You see the mistake as it happens and you stop it. An autonomous agent that plans, executes, tests, and opens a pull request across fifteen files while you were getting coffee fails differently. By the time you see the output, the decisions have already been made, the tests have already been written by the same system that wrote the code they're testing, and your review is now the only thing standing between that work and production. The platforms below have made very different bets about where they want you to stand in that process, and the bet a platform makes tells you more about who it's for than any benchmark score does.

## The Foundation Models: Where Judgment Lives

At the base of the stack sit the models developers still reach for directly, through a chat window or an API call, before any editor or agent framework wraps around them.

[Claude](https://claude.com) remains the model people paste an entire codebase into when they need to reason about it rather than just extend it. Claude Sonnet 5, now running with a native 1M-token context window, is the default inside Claude Code and the model most consistently credited with catching subtle logic bugs during large refactors rather than just producing code that compiles. The reasoning is the product here. Everything Anthropic ships downstream, including the terminal tooling covered below, is really a wrapper around getting that reasoning closer to where the work happens.

[Gemini 3](https://gemini.google.com) is the more interesting case precisely because of what Google just did to it. The model itself is excellent — Google's own documentation calls it the most capable option available to Code Assist subscribers — and its multi-million-token context window remains the best answer to "how do I ask an architectural question about a codebase I haven't fully read myself." But Google has decided the model doesn't belong inside a conventional IDE extension anymore. It belongs inside Antigravity, running its own agents against your repository. That's a strategic statement as much as a product one: Google is betting that the extension-plus-chat-window format is already obsolete.

[GPT-5.4](https://openai.com/codex/), running through OpenAI's Codex line, is the ubiquitous backbone. GPT-5.1-Codex-Max shipped as the frontier agentic coding model late last year, GPT-5.3-Codex-Spark followed as a smaller, near-instant variant clocking over a thousand tokens a second for developers who want speed over depth, and GPT-5.4 now sits at the top as the general-purpose flagship. Codex is less a single product than an API layer that half the tools in the next three tiers are quietly built on top of.

## The AI-Native IDEs: The Workflow Habitats

One level up, the editor itself gets rebuilt around the agent instead of bolting one on as a sidebar.

[Cursor](https://cursor.com), forked from VS Code, is still the category's reference point. Composer 2.5 handles multi-file refactors at the scale of an entire file tree, Cursor 3.3 added the ability to spawn multiple subagents from a single prompt and work on them in parallel, and cloud agents now run in isolated VMs that keep working after you close your laptop, with an iOS beta letting you check in on them from your phone. Cursor sells contextual flow. It indexes your repository locally and the agent understands how a change in one file ripples into three others without you explaining the relationship.

[Devin Desktop](https://windsurf.com) is Cursor's most direct rival, and its backstory is one of the stranger footnotes of the last year. It was Windsurf until July 2025, when its founding team departed for Google in a reverse-acquihire and Cognition, the company behind Devin, stepped in within 72 days to acquire the remaining product, brand, and roughly 250 engineers. Cognition rebranded it Devin Desktop in June 2026 and wired in a direct handoff to its cloud agent, so you can plan a change locally in the editor and hand execution off to Devin running in a sandboxed VM elsewhere. SWE-1.6, the model underneath, scores meaningfully better than its predecessor on SWE-Bench Pro. Pro tier pricing landed at $20 a month, matching Cursor exactly, which tells you how directly these two now compete.

[Google Antigravity 2.0](https://antigravity.google) is the newest and most aggressive entrant, and the one that absorbed Gemini Code Assist's individual users. It's free, it runs as a standalone desktop app rather than an extension, and it delegates a task across specialized sub-agents — one for frontend, one for backend, one that opens a live Chrome instance to test what the others built, and one that deploys it. You are meant to watch the process rather than drive it.

[GitHub Copilot](https://github.com/features/copilot), still the most widely installed tool in this tier by raw numbers, reached agent-mode general availability across both VS Code and JetBrains in March 2026, closing the gap that had excluded a large share of Java, Kotlin, and Python developers who never left JetBrains. Assign it a GitHub issue and it works in the background, writing code, running tests, and opening a pull request without further prompting. Agentic code review, added the same month, lets Copilot gather full project context before commenting on a PR and can hand its own suggestions straight to the coding agent to generate a fix.

## The Terminal Agents: Where the Keyboard Goes Quiet

Below the editor, a different set of tools skip the visual layer entirely and operate where a lot of senior engineers actually prefer to live.

[Claude Code](https://claude.com/product/claude-code) runs directly in the local environment, reading files, executing terminal commands, running your test suite, and committing to git on your instruction. The latest release train added hierarchical agent spawning, where a parent agent delegates to child agents up to three levels deep for work that spans multiple modules, plus Artifacts that turn a session into a shareable, updating web page, useful for a PR walkthrough or an incident summary that a teammate can open without re-running anything.

[Codex CLI](https://developers.openai.com/codex/cli) is OpenAI's answer, running gpt-5.1-codex-max by default for signed-in ChatGPT users and switchable to gpt-5.3-codex-spark when speed matters more than depth. It inspects a repository, edits files, and runs commands the same way Claude Code does, and the two now compete less on capability than on which foundation model a team already trusts.

[Gemini CLI](https://geminicli.com) uses a reason-and-act loop against local and remote MCP servers and remains genuinely capable, though it's caught in the same transition as its IDE sibling: individual-tier access folded into Antigravity CLI as of June 18th, leaving the standalone CLI increasingly positioned as an enterprise and Google Cloud tool rather than a general-purpose one.

[Aider](https://aider.chat) is the holdout, and deliberately so. It's MIT-licensed, model-agnostic, and git-first by design, committing every change it makes with a clean message so a developer can roll back anything that misses the mark. With roughly 44,000 GitHub stars, 6.8 million PyPI installs, and by some estimates 15 billion tokens processed weekly across its user base, it remains one of the top three terminal agents by daily active developers, and the cleanest answer available to anyone who wants AI pair programming without signing over their workflow to one vendor's ecosystem.

## The App Builders: Code You Never See

The last tier barely resembles software development as it existed five years ago. You describe an outcome, and the platform produces a running, deployed application. The code exists, but it is increasingly treated as an implementation detail rather than the product.

[Replit Agent 3](https://replit.com/agent) frames itself as ten times more autonomous than its predecessor, testing its own output live in a browser and fixing what it finds using a proprietary testing loop the company claims is far cheaper than a general-purpose computer-use model. Its Max Autonomy mode is built explicitly to run for extended stretches on well-defined goals with minimal check-ins, and a new Design Mode lets you sketch the frontend before the agent writes a line of code.

[Devin](https://devin.ai), in its original cloud form (distinct from the desktop editor above), takes a whole task asynchronously, works inside a sandboxed environment with its own shell, browser, and sub-agents, and returns with a finished pull request. Cognition's newly announced enterprise partnership with Cognizant is a bet that this async, ticket-in-PR-out model is what large organizations actually want from an AI engineer, not a smarter autocomplete.

[v0](https://v0.dev), from Vercel, stays narrow on purpose, generating production-quality React components styled in Tailwind for teams already living inside Next.js. It doesn't touch a database or a backend, and that restraint is the feature.

[Bolt.new](https://bolt.new), from StackBlitz, is the fastest path from idea to a running full-stack app, backend included, though reviewers consistently note the code quality varies more than its competitors once you look past the demo.

[Lovable](https://lovable.dev) targets the same full-stack territory with more emphasis on production-readiness, generating Supabase-backed React applications and handling hosting itself through Lovable Cloud, which makes it the most common starting point for a non-technical founder trying to ship a real product rather than a prototype.

<figure class="fig">
  <img src="/images/codegen-wars-landscape.webp" alt="The CodeGen Wars: sixteen platforms across four tiers — Foundation Models, AI-Native IDEs, Terminal Agents, and App Builders — scored on autonomy, code quality, context depth, IP safety, and cost." />
  <figcaption>State of the Union — sixteen platforms across four tiers, scored on autonomy, code quality, context, IP safety, and cost.</figcaption>
</figure>

## The Accountability Question: Who Signs the PR

Here is where the tiers stop being a taxonomy and start being a decision. Move down this list, from foundation model to IDE to terminal agent to app builder, and you are not just choosing a tool. You are choosing how much of the work happens before a human looks at it, and therefore what your review process is actually reviewing. A chat-based model fails in front of you. A background agent that spawns sub-agents, tests its own work, and opens a PR fails somewhere you weren't looking, and the review step is the entire safety net.

That question of trust has a legal shadow attached to it that predates all of this year's autonomy, and it's worth knowing where it stands. Doe v. GitHub, the class action alleging that Copilot was trained on copyrighted code without permission, has been narrowed sharply by Judge Jon Tigar in the Northern District of California, who dismissed the claim that Copilot reproduces developers' code verbatim for lack of evidence and rejected the DMCA claim outright. What survives, and remains in discovery as of this year, are two counts of breach of contract and open-source license violation, meaning the live legal question is no longer "did this copy my code" so much as "did this violate the license terms my code was released under." It's a narrower fight than it started as, but not a resolved one, and it's the reason Aider's model-agnostic, bring-your-own-model approach carries an appeal that goes beyond philosophy.

## The Outlook

The pattern from the image and video markets is repeating here, just with the stakes inverted. There, the fight was over who owns the pixel. Here, ownership of the code was never really in question — most output resembles no single source closely enough to matter, and licensing terms rather than copyright claims will likely settle what's left of the legal argument. The fight that actually matters in this market is over supervision, and it is moving in one direction only. Google didn't retire Gemini Code Assist because the extension model failed technically. It retired it because the company has concluded that watching an agent work is where developers are headed, not typing alongside one. Cursor, Devin Desktop, and Antigravity are converging on the same bet from different starting points, and the app builders have already arrived. The platforms that win the next round won't be the ones with the best autocomplete. They'll be the ones that make it easiest to trust a pull request you didn't watch get written, and easiest to catch the one time out of twenty that trust was misplaced.

---

*This is Part 4 of a 4-part series on the State of the Union in AI. Part 1 covers the LLM market. Part 2 covers image generation. Part 3 covers video generation.*
