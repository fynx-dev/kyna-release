import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://fynx-dev.github.io',
  base: '/kyna-release',
  trailingSlash: 'always',
  integrations: [sitemap()],
  server: {
    host: '127.0.0.1',
    port: 4300,
  },
});
