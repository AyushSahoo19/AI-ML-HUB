import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const lecturesCollection = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/lectures" }),
  schema: z.object({
    title: z.string(),
    day: z.number(),
    date: z.string(),
    module: z.string().optional(),
    pdfUrl: z.string().optional(),
    material: z.string().optional(),
    topics: z.array(z.string()).optional(),
  }),
});

const projectsCollection = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/projects" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    language: z.string(),
    stars: z.number(),
    forks: z.number(),
    lastUpdated: z.string(),
    files: z.array(
      z.object({
        path: z.string(),
        content: z.string(),
        language: z.string(),
      })
    ).optional(),
  }),
});

export const collections = {
  'lectures': lecturesCollection,
  'projects': projectsCollection,
};
