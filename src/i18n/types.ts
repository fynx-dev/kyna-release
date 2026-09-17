export type FeatureCopy = {
  number: string;
  eyebrow: string;
  title: string;
  body: string;
  screenshot: string;
  screenshotAlt: string;
};

export type TabDeckItemCopy = {
  id: string;
  label: string;
  hint: string;
  title: string;
  body: string;
  screenshot: string;
  screenshotAlt: string;
};

export type DeckSectionCopy = {
  number: string;
  eyebrow: string;
  title: string;
  body: string;
  tabs: Record<string, TabDeckItemCopy>;
};

export type ImageComparisonCardCopy = {
  title: string;
  body: string;
  originalLabel: string;
  enhancedLabel: string;
  sliderLabel: string;
  originalAlt: string;
  enhancedAlt: string;
};

export type EnhancementSectionCopy = {
  eyebrow: string;
  title: string;
  body: string;
  demoCaption: string;
  cards: { dlss: ImageComparisonCardCopy; anime4k: ImageComparisonCardCopy };
};

export type BentoHighlightCopy = {
  icon: string;
  tag: string;
  title: string;
  description: string;
};

export type LandingCopy = {
  locale: 'en' | 'zh-CN' | 'ja' | 'ko';
  direction: 'ltr';
  seo: { title: string; description: string };
  skip: string;
  navigation: { features: string; install: string; docs: string; feedback: string };
  hero: { eyebrow: string; title: string; accent: string; lead: string; download: string; explore: string; note: string; nowPlaying: string; screenshot?: string; screenshotAlt?: string };
  badges: string[];
  intro: string;
  highlights: BentoHighlightCopy[];
  features: {
    playback: FeatureCopy;
    thumbnails: FeatureCopy;
    library: FeatureCopy;
    settings: DeckSectionCopy;
    enhancement: EnhancementSectionCopy;
    subtitles: DeckSectionCopy;
    casting: DeckSectionCopy;
    flexibility: FeatureCopy;
    hdr: FeatureCopy;
  };
  install: { eyebrow: string; title: string; body: string; download: string; guide: string };
  footer: string;
  screenshots: { add: string };
  paths: { home: string; install: string; docs: string; alternateHome: string; alternateInstall: string };
};

export type InstallCopy = {
  locale: LandingCopy['locale'];
  seo: LandingCopy['seo'];
  heading: string;
  lead: string;
  download: string;
  sections: Array<{ title: string; steps: string[] }>;
  back: string;
  skip: string;
  paths: LandingCopy['paths'];
};
