import type { APIRoute } from "astro";
import { getCollection } from "astro:content";

// Generated at build time from the article collection so it never goes stale.
export const GET: APIRoute = async () => {
  const articles = (await getCollection("articles", ({ data }) => !data.draft))
    .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());

  const lines = [
    "# Ben Havey",
    "",
    "> Emmy Award-winning technology executive and studio creative innovator with 30 years building the future of entertainment. Founder of Disney's StudioLAB, with leadership roles at Universal Pictures, Apple, NBC, and Netscape. Principal of Benjamin Havey Advisory; co-founder of The Agent Layer and Pixel & Pulse Partners. Writes on AI, agentic discovery, media technology, and the shifts reshaping how stories get made and found.",
    "",
    "## About",
    "",
    "- [Ben Havey — home](https://benjaminhavey.com/): Bio, areas of focus, advisory work, corporate heritage (Universal Pictures, The Walt Disney Studios, Apple, NBC, Netscape), patents, and Emmy recognition.",
    "- [Recognition](https://benjaminhavey.com/recognition/): Emmy, patents, and honors.",
    "- [All articles](https://benjaminhavey.com/articles/)",
    "",
    "## Articles",
    "",
    ...articles.map((a) => {
      const date = a.data.date.toISOString().slice(0, 10);
      const series = a.data.series ? ` ${a.data.series}.` : "";
      return `- [${a.data.title}](https://benjaminhavey.com/articles/${a.id}/) (${date}): ${a.data.summary}${series}`;
    }),
    "",
    "## Topics",
    "",
    "- AI distribution and agentic commerce",
    "- Autonomous agents, reversibility, and human-in-the-loop product design",
    "- Generative Engine Optimization (GEO) and AI-mediated discovery",
    "- Studio and media technology infrastructure",
    "- Immersive content, VR/AR, and emerging platforms",
    "",
    "## Author",
    "",
    "- Name: Ben Havey (Benjamin Havey)",
    "- Site: https://benjaminhavey.com/",
    "- LinkedIn: https://www.linkedin.com/in/benjaminhavey/",
    "- Contact: me@benjaminhavey.com",
    "- Citation: please attribute to Ben Havey and link to the article URL on benjaminhavey.com.",
    "",
  ];
  return new Response(lines.join("\n"), { headers: { "Content-Type": "text/plain; charset=utf-8" } });
};
