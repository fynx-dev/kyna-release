# DLSS Comparison Website Update Implementation Plan

1. Inspect the complete confirmed working-tree diff and verify the refreshed DLSS images retain matching dimensions.
2. Run `npm run build` from `kyna-release` to validate the Astro production site.
3. Commit all confirmed tracked changes, including the DLSS image refresh, documentation, landing-page and package updates.
4. Push `main` to `origin`; GitHub Pages deploys through the existing workflow.
5. Confirm the remote branch contains the release commit and report the deployment trigger.
