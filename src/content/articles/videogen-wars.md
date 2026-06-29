---
title: "The VideoGen Wars: Who Owns the Final Frame?"
date: 2026-06-29
summary: "Fourteen platforms, three tiers, and one question every legal department eventually asks. A field guide to the video generation market in 2026 — from Runway's shot consistency to the provenance problem that decides who survives contact with a production budget."
hero: "/images/videogen-wars-hero.webp"
heroAlt: "The VideoGen Wars — Who owns the final frame? State of the Union in AI, Article III of IV."
series: "State of the Union in AI · Part 3 of 4"
seriesSlug: "state-of-the-union-in-ai"
seriesPart: 3
draft: false
---

In 2022, a generated video was a five-second curiosity that melted at the edges and gave its subjects seven fingers. In mid-2026, you can type a sentence and get an eight-second clip in 4K with synced dialogue, correct lighting physics, and a protagonist who looks the same in shot three as he did in shot one. The technology has arrived faster than anyone in the room at the studios expected, and it has brought a problem with it. Making a beautiful clip is no longer the hard part. The hard part is knowing whether you can legally put that clip into a client deliverable, a national campaign, or a film that will sit on a balance sheet for ninety years.

That is the real story of the video generation market right now, and it is the thread that runs through everything below. There are roughly fourteen platforms worth knowing across three tiers, and they separate less by quality than by the answer to a single question every legal department eventually asks: where did this come from, and who is liable if the answer is wrong. What follows is a field guide to the tiers, the latest models in each, what they are actually good at, and the licensing fine print that decides which of them survive contact with a production budget.

## The Hosted Tier: Paying by the Second

The premium platforms charge by the generation, run on someone else's GPUs, and compete on fidelity and control. This is where the headline quality lives.

[Runway](https://runwayml.com) remains the model that filmmakers reach for first, largely because it solved the problem that made earlier video AI useless for narrative work. The Gen-4 family, including the faster and cheaper Gen-4 Turbo variant, maintains consistent characters, locations, and objects across separate clips, which is the difference between a tech demo and a usable sequence. Recent versions added native audio and a far better grasp of camera terminology and lighting, so a prompt that asks for a slow dolly-in under hard key light now produces something close to what a cinematographer would recognize. Runway is best at the things that matter to people who think in shots and cuts.

Google's [Veo 3.1](https://deepmind.google/models/veo/), released in October 2025 and now available in Fast and Lite variants, is the strongest all-rounder and the one most likely to end up in an enterprise pipeline. It generates clips of four, six, or eight seconds at up to 4K, with natively synchronized audio that includes dialogue and sound design, plus the ability to steer a generation with up to three reference images or by specifying first and last frames. The motion and physics are the most convincing in the hosted tier. Veo also carries something none of its rivals can match, which I will come back to in the licensing section, because it is the reason a cautious studio picks it.

[Luma's Ray3 family](https://lumalabs.ai/ray) pushed the craft side of the conversation forward. Refined through point releases across 2026, the current models generate native 1080p several times faster and cheaper than the previous generation, with a scene-level lighting engine that tracks global illumination across frames so highlights wrap around curved surfaces and shadows move correctly when the camera pans. Ray3 also reasons about a shot before rendering it and offers native 16-bit HDR color, which makes it the choice when the look of the footage is the point. Its Modify feature, which restyles existing footage rather than generating from scratch, is the most useful video-to-video tool in the tier.

[Kling 2.6](https://klingai.com), released by Kuaishou in December 2025, is the value play and the first Kling model to generate synchronized audio and video in a single pass. It produces up to 1080p at 48 frames per second with a ten-second ceiling, and its motion realism and lip-sync are genuinely competitive with anything from the West at a fraction of the cost. It is also a Chinese model, which is not a quality knock but is a licensing one, and that distinction becomes the whole game later in this piece.

The last three names in this tier are not really models at all. [Artlist.io](https://artlist.io), [Higgsfield](https://higgsfield.ai), and [Canva](https://www.canva.com) are storefronts that resell the models above. Artlist aggregates dozens of third-party engines including Veo, Kling, Sora, and Wan, and wraps them in a single universal commercial license, which is its actual product. Higgsfield layers director tooling on top of the same borrowed engines, with per-shot camera control, a character-consistency system called Soul ID, and a Cinema Studio aimed at narrative work. Canva took the simplest path of all, embedding Veo 3 as a "Create a Video Clip" button that produces eight-second clips with audio directly inside the design tool that hundreds of millions of marketers already open every day. None of these three competes on raw capability. They compete on workflow and, in Artlist's case, on licensing clarity, which is exactly the right thing to compete on.

## The Free Tier: Good Enough, With Strings

Below the paid platforms sits a tier that costs nothing at the point of use and recovers the cost in other ways, usually in resolution caps, usage limits, or the rights you quietly sign away.

[HeyGen](https://www.heygen.com) is the standout, because it does one thing better than anyone. Its Avatar V model, released in April 2026, generates a studio-quality talking presenter from a single short recording and holds your face, voice, and mannerisms across angles and runtime rather than just the opening shot. The newer controls let you direct gaze, posture, and energy in plain language. For corporate explainers, localized training content, and spokesperson video at scale, nothing else is close. The free tier gets you short clips to test the platform before the paid plans give you anything you would actually ship.

Meta's offering is the most-used and least-discussed in professional circles, which makes sense once you see what it is for. [Vibes](https://ai.meta.com/vibes/), which Meta spun out as a standalone app in early 2026, is a free remix engine for short-form social video, built for grabbing a clip from your feed and restyling it rather than for original production. Behind it sits Movie Gen, Meta's 30-billion-parameter research model that can generate sixteen-second 1080p video with synced audio, though it remains a research project rather than a public tool. Meta is playing for consumer volume, not creative professionals, and the free price reflects exactly the audience it wants.

[Leonardo.AI](https://leonardo.ai) sits between the image and video worlds and serves the artists who already live there. Its Motion 2.0 model offers camera and effect controls for image-to-video work, and the platform also hosts third-party engines including Veo, Sora, and Kling alongside its own. A daily allotment of free tokens makes it a reasonable place to start for anyone whose work begins with a still image, though serious volume pushes you onto a paid plan quickly.

## The Local Tier: Open Weights, Your Hardware

The most strategically interesting tier is the one that runs on a machine you own. Open-weight video models matured fast in late 2025 and early 2026, and for the first time the gap between what you can run locally and what you can rent is narrow enough to matter.

[Lightricks](https://ltx.io) open-sourced LTX-2 in January 2026 and followed with the LTX-2.3 point release in March, which is the one most people actually run. It was the first open model to generate synced 4K audio and video in a single pass, it ships with a desktop editor that runs the whole pipeline on consumer hardware, and it carries an Apache 2.0 license that is free for commercial use under ten million dollars in annual revenue. For a studio that wants control over its own pipeline without sending frames to a vendor, it is the most complete open option.

Alibaba's [Wan](https://github.com/Wan-Video) is the open all-rounder. Wan 2.2, released in July 2025, uses a mixture-of-experts design that delivers roughly fourteen billion active parameters while running on a 24GB card like an RTX 4090, and the Wan 2.7 suite that followed in April 2026 bundles text-to-video, image-to-video, reference-to-video with voice cloning, and instruction-based editing into one Apache 2.0 package. It is the open model I would hand to a technical team and expect production work out of.

Tencent's [HunyuanVideo 1.5](https://huggingface.co/tencent/HunyuanVideo-1.5), released in November 2025, makes a different argument. At 8.3 billion parameters it delivers state-of-the-art quality while running comfortably on a single consumer GPU, which lowers the barrier as much as any model in this tier. Its licensing carries a wrinkle worth flagging now and examining below, because "open" and "open everywhere" are not the same thing.

[Mochi 1](https://www.genmo.ai) from Genmo deserves a mention mostly as a marker of how fast this tier moved. When it launched in late 2024 it was the largest open video model ever released and a genuine milestone, but it generated 480p, required four H100 GPUs to run, and has since been overtaken by lighter, sharper, more permissive successors. It is the open-source flagship that the open-source community sailed past, and that pace is the real point.

<figure class="fig">
  <img src="/images/videogen-wars-landscape.webp" alt="The VideoGen Wars: fourteen platforms across three tiers — Hosted, Free, and Local — scored on visual quality, native audio, control, IP safety, and cost/access." />
  <figcaption>State of the Union — fourteen platforms across three tiers, scored on quality, audio, control, IP safety, and cost.</figcaption>
</figure>

## The Licensing Question: What "Final Pixel" Actually Requires

Here is where the tiers stop mattering and the fine print takes over. The single most expensive mistake in this market is confusing two different kinds of "free," and the open tier is where people make it most often. An Apache 2.0 license, which LTX-2, Wan, and Mochi all carry, covers the software. It grants you the code and the weights to use commercially without paying. It says nothing about whether the video those weights produce is clean of someone else's copyrighted training data, and it offers no warranty if a rights-holder comes knocking. The code is free. The provenance is your problem.

That distinction is why indemnification, not quality, is the dividing line for serious commercial work. Google indemnifies enterprise customers who generate video through Veo on its Cloud platform, meaning Google will stand behind the output if a copyright claim arrives. That single contractual promise is worth more to a cautious studio than a few points of motion fidelity, and it is the real reason Veo keeps winning enterprise deals. Almost no one else offers an unconditional version of the same guarantee for video, and the Chinese models offer nothing of the kind. Kling, Wan, and Hunyuan are trained on data nobody outside their parent companies has audited, under a copyright regime that diverges sharply from US and EU law, and with no entity willing to absorb your downstream liability. The footage can be beautiful and still be radioactive in a client contract.

HunyuanVideo is the cleanest illustration of how careful you have to read. The 1.5 weights are distributed under permissive terms, but Tencent's broader Hunyuan community license has historically carved out a territory that excludes the European Union, the United Kingdom, and South Korea. A model that is free to commercialize in Los Angeles may not be licensed for the same use in London or Seoul, and discovering that after a campaign ships is not a conversation anyone wants to have with counsel. Read the actual license file, every time, for every open model, because the headline word "open" hides more than it reveals.

Watermarking is the last piece, and it is moving from optional to mandatory. Google embeds an invisible SynthID marker in every Veo frame, the C2PA provenance standard is spreading across the toolchain, and regulators in the EU now require AI-generated media to be disclosed as synthetic. For a meme that disappears in a day none of this matters. For final-pixel work that will be scrutinized, archived, and possibly litigated, an invisible flag that announces "this was generated" is a feature you need to plan around rather than a detail you discover later. The clip that looks indistinguishable from a camera original is not, in fact, indistinguishable to the systems that increasingly check.

## The Outlook

The next twelve months will be decided by the same forces that shaped the image market, only faster, because video is where the budgets are. The hosted tier will keep winning the enterprise on the strength of indemnification rather than fidelity, the open tier will keep closing the quality gap until "run it yourself" becomes the default for studios that can staff it, and the Chinese models will keep being the best value and the hardest to clear for commercial use. The capability fight is largely over. The provenance fight has barely started, and that is the one worth watching. Whoever can credibly promise a clean final frame, and back the promise with a contract, will own this market regardless of who has the prettiest motion.

---

*This is Part 3 of a 4-part series on the State of the Union in AI. Part 1 covers the LLM market. Part 2 covers image generation. Part 4 is coming soon.*
