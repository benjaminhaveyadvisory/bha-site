import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const articles = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/articles" }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    summary: z.string(),
    hero: z.string().optional(),
    heroAlt: z.string().optional(),
    series: z.string().optional(),
    seriesSlug: z.string().optional(),
    seriesPart: z.number().optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { articles };
