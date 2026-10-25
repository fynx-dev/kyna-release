# DLSS Comparison Website Update Design

**Date:** 2026-10-25
**Status:** Approved design

## Goal

Publish the confirmed website changes in `kyna-release`, including the refreshed DLSS comparison images, through the existing GitHub Pages deployment workflow.

## Scope

The release includes every currently modified tracked file in `kyna-release`:

- refreshed homepage DLSS comparison assets `public/assets/images/features/s1-1.png` and `s1-2.png`;
- confirmed landing-page, README, installation-documentation, and package metadata updates.

No source-player binaries, runtime manifests beyond currently tracked changes, or unrelated repositories are changed.

## Delivery

Run the Astro production build locally. If it succeeds, commit the confirmed working tree on `main` and push it to `origin/main`. The existing `.github/workflows/deploy-pages.yml` workflow deploys the generated site to GitHub Pages.

## Verification

- `npm run build` completes successfully.
- The commit contains only the confirmed `kyna-release` changes.
- The push succeeds and GitHub Actions is responsible for deployment.
