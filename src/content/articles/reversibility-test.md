---
title: "The Reversibility Test"
date: 2026-10-22
summary: "OpenAI shipped Dots, Meta shipped Muse, and now Duet has arrived — three bets that we're ready to stop chatting with AI and start delegating to it. A simpler way to judge whether that bet pays off: can the mistake be undone?"
hero: "/images/reversibility-test-hero.webp"
heroAlt: "The Reversibility Test — a dark navy title card reading 'Agents succeed where mistakes are cheap to undo. Capability is not the constraint.'"
linkedin: "https://www.linkedin.com/pulse/reversibility-test-benjamin-havey-usvkc/"
draft: false
---

In the space of about six weeks, OpenAI shipped Dots, Meta shipped Muse, and now Duet has arrived. Three major platforms, one shared bet: that we are ready to stop chatting with AI and start delegating to it. After thirty years of building consumer products at Disney, Universal, and Apple, I have a simpler way to judge whether that bet pays off. I call it the reversibility test.

## The shift from answering to acting

For three years the consumer AI interaction has been a conversation. You ask, it answers, you decide. The new generation of autonomous agents breaks that loop. Dots runs tasks in the background and reports back. Muse executes inside a secure virtual machine with a separate sentinel process watching its behaviour. Google's always-on Spark agent, Perplexity Computer, Manus, and Lindy all promise some version of the same thing: give me a goal, and I will go do the work.

The pricing tells you how settled this market already is. Every major player has converged on an identical ladder: a free tier, roughly $20 a month, then $100 and $200 tiers for heavier usage. Price is no longer the differentiator. Surfaces and autonomy are.

## The guardrails that actually matter

Three patterns are emerging, and they are worth understanding because they determine what an agent can safely be trusted with.

**Sandboxing.** The agent operates inside a contained environment, as Muse does with its secure VM. Whatever it breaks, it breaks in a box.

**Confirmation gates.** The agent pauses before sensitive actions and asks a human. This is Google's approach, and it is the most familiar: it keeps a person in the loop at exactly the moments that matter.

**Scoped credentials.** The agent gets a wallet with a spending cap, or a login with limited permissions, rather than your real accounts. It can act, but only within a boundary you set in advance.

Each of these is really a different answer to the same question: what happens when the agent gets it wrong?

## The reversibility test

Here is the pattern I keep seeing. Autonomous agents succeed where mistakes are cheap to undo, and they struggle where mistakes are permanent. Capability is not the constraint. Reversibility is.

An agent that drafts your inbox replies is reversible: you read before you send. An agent that books a refundable hotel is reversible. An agent that researches twenty vendors and builds a comparison table is reversible, because the output is a document you review, not an action in the world. An agent that sends the email, books the non-refundable flight, or transfers the funds is not.

This is why the guardrails above matter so much. Sandboxing, confirmation gates, and scoped credentials are all mechanisms for manufacturing reversibility, for turning a permanent action into one that can be caught, capped, or contained before it lands.

## Where it works today

On the personal side, the use cases that hold up are research-and-draft: trip planning, comparison shopping, inbox triage, and bookings with a cap. Tedious, bounded, and recoverable.

Here is how the three consumer platforms answer the question. Notice that none of them differentiates on capability. They differentiate on how a mistake gets caught.

<figure class="fig">
  <img src="/images/reversibility-consumer.webp" alt="Dots, Muse, and Duet compared on model, where it runs, guardrail, reach, access, and reversibility strategy — contain it, sandbox it, gate it." />
  <figcaption>Consumer agents — three platforms, one question: can the mistake be undone?</figcaption>
</figure>

The enterprise side answers the same question differently. Google, Microsoft, and Salesforce do not ask the user to confirm. They give the agent an identity, put it under the tenant's admin controls, and price every action. Reversibility is bought with governance and a meter rather than a dialog box.

<figure class="fig">
  <img src="/images/reversibility-work.webp" alt="Gemini Agent, Copilot, and Agentforce compared on model, where it runs, guardrail, reach, access, and reversibility strategy — govern it, identify it, meter it." />
  <figcaption>Work agents — same question, different answer: who signs off before it ships?</figcaption>
</figure>

Different mechanisms, same principle: nobody has shipped an agent that is trusted to be wrong without a way back.

In business, the pattern is overnight work. Lead research, report assembly, data pulls, first-pass support tickets. Anything where the agent produces a draft and a human reviews it before it ships. The agent does the eighty percent that is labour; the human does the twenty percent that is judgement.

This is the human-in-the-loop principle I have written about before, and autonomy does not retire it. It relocates it. The human moves from the middle of the loop to the end of it, where the irreversible decision gets made.

## What this means for entertainment

For those of us in media, the implications are immediate. Ticketing, content discovery, and subscription management are all transactional, and all about to be mediated by agents acting on a consumer's behalf. The platforms that win will be the ones that make their transactions legible and reversible to an agent: clear cancellation terms, confirmable steps, and APIs that expose intent rather than hide it. Studios and distributors who treat agents as a threat to be blocked will find consumers routing around them.

The question for every product leader is no longer whether AI can do the task. It is whether a mistake can be undone, and whether you have built the product so that an agent can tell the difference.

*Ben Havey is Principal of Benjamin Havey Advisory and co-founder of The Agent Layer and Pixel & Pulse Partners.*
