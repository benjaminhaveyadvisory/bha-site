// Single source of truth for the author entity. Every JSON-LD block on the site
// references this @id so Google, Bing and LLM crawlers resolve one Person node.
export const SITE = "https://benjaminhavey.com";
export const PERSON_ID = `${SITE}/#person`;

// Add profile URLs here as they exist (Wikidata, Google Patents inventor page,
// Creators Guild of America bio, IMDb, podcast pages). Each one strengthens the
// entity match. Only list pages that are actually about Ben.
export const PERSON_SAME_AS = [
  "https://www.linkedin.com/in/benjaminhavey/",
];
