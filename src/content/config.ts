import { z, defineCollection } from 'astro:content';

const lecturesCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    day: z.number(),
    date: z.string(),
    module: z.string().optional(),
  }),
});

const projectsCollection = defineCollection({
  type: 'content',
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
