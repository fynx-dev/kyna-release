import type { InstallCopy, LandingCopy } from './types';

export const en: LandingCopy = {
  locale: 'en', direction: 'ltr',
  seo: { title: 'Kyna Player — Pure Cinema. Next-Gen Control.', description: 'Kyna Player is a focused Windows media player for local playback, subtitles, sound controls, and TV casting.' },
  skip: 'Skip to content',
  navigation: { features: 'Features', docs: 'Docs', install: 'Install', feedback: 'Feedback' },
  hero: { eyebrow: 'Ultra-Fast Windows Media Player', title: 'Pure Cinema.', accent: 'Next-Gen Control.', lead: 'The next-generation local media player for Windows. Native C++ engine, zero trackers, built for Dolby Vision & local AI enhancement.', download: 'Download for Windows', explore: 'Explore features ↓', note: 'Secure & Verified · Installer and SHA-256 checksum published together on GitHub Releases.', nowPlaying: 'Now playing', screenshot: 'main.webp', screenshotAlt: 'Kyna Player interface' },
  badges: ['⚡ Instant Native Performance', '🎬 Dolby Vision & 10-bit HDR', '🛡️ 100% Offline AI Privacy', '📡 Two-Way DLNA Stream'],
  intro: 'Redefining local media. Strip away bloated UI and experience true color accuracy with absolute control.',
  highlights: [
    {
      icon: '⚡',
      tag: 'Native Engine',
      title: 'Sub-Millisecond Launch',
      description: 'Built with C++ & Slint for lightweight memory footprint and instant 4K high-bitrate playback.'
    },
    {
      icon: '🎬',
      tag: 'Picture Processing',
      title: 'Dolby Vision & 10-bit HDR',
      description: 'Advanced SDR Tone Mapping delivers vibrant color depth and deep shadows even on standard displays.'
    },
    {
      icon: '✨',
      tag: 'Local AI Power',
      title: 'Offline Whisper Transcription',
      description: 'Run local AI models for instant subtitle generation and smart translation without uploading any data.'
    },
    {
      icon: '📡',
      tag: 'Seamless Casting',
      title: 'Two-Way DLNA Streaming',
      description: 'Cast to big-screen TVs or turn Kyna Player into a local receiver for streams from mobile devices.'
    }
  ],
  features: {
    playback: { number: '01', eyebrow: 'Minimal Playback', title: 'Stay with the film.', body: 'A clean player surface, precise seeking, track selection, and fullscreen playback put the focus where it belongs.', screenshot: 'minimal.webp', screenshotAlt: 'Kyna Player minimal player interface' },
    thumbnails: { number: '02', eyebrow: 'Timeline Thumbnails', title: 'Fast seeking at a glance.', body: 'Hover over the timeline to preview high-definition video frames and pinpoint your exact scene instantly.', screenshot: 'thumbnails.webp', screenshotAlt: 'Kyna Player timeline thumbnail preview' },
    library: { number: '03', eyebrow: 'Library', title: 'Keep the next thing close.', body: 'Search, sort, save playlists, and choose how playback continues without leaving the player.', screenshot: 'playlist.webp', screenshotAlt: 'Kyna Player playlist management' },
    settings: {
      number: '04',
      eyebrow: 'Playback Settings',
      title: 'Fine-tune every detail.',
      body: 'From color presets and audio delay to dual-subtitle formatting and sync, control everything with intuitive side panels.',
      tabs: {
        audio: {
          id: 'audio',
          label: 'Audio',
          hint: 'Sound sync & voice clarity',
          title: 'Hear every detail.',
          body: 'Tune audio delay and toggle Night Mode or Voice Enhance with real-time waveform feedback.',
          screenshot: 'playback-audio.webp',
          screenshotAlt: 'Kyna Player audio settings panel'
        },
        picture: {
          id: 'picture',
          label: 'Video',
          hint: 'Framing & color tuning',
          title: 'Craft your ideal picture.',
          body: 'Adjust window sizing, picture fill mode, and fine-tune brightness, contrast, saturation, and color presets.',
          screenshot: 'playback-picture.webp',
          screenshotAlt: 'Kyna Player picture and video settings panel'
        },
        subtitles: {
          id: 'subtitles',
          label: 'Subtitles',
          hint: 'Dual subs & appearance',
          title: 'Clear, readable lines.',
          body: 'Customize primary and secondary subtitle sizes, placement, outline strength, opacity, and timing offsets.',
          screenshot: 'playback-subtitle.webp',
          screenshotAlt: 'Kyna Player subtitle appearance settings panel'
        }
      }
    },
    enhancement: {
      eyebrow: 'AI Enhancement Comparison',
      title: 'See the difference, frame by frame.',
      body: 'Drag the divider to compare the original image with real-time enhancement.',
      demoCaption: 'Demonstration frames are screenshots from actual video files.',
      cards: {
        dlss: { title: 'DLSS 5', body: 'AI reconstruction for clearer fine detail.', originalLabel: 'Original', enhancedLabel: 'Enhanced', sliderLabel: 'DLSS 5 image comparison', originalAlt: 'Original DLSS 5 comparison image', enhancedAlt: 'DLSS 5 enhanced comparison image' },
        anime4k: { title: 'Anime4K', body: 'Sharper line work, tuned for animation.', originalLabel: 'Original', enhancedLabel: 'Enhanced', sliderLabel: 'Anime4K image comparison', originalAlt: 'Original Anime4K comparison image', enhancedAlt: 'Anime4K enhanced comparison image' }
      }
    },
    subtitles: {
      number: '05',
      eyebrow: 'Subtitle Tools',
      title: 'Local AI transcription & translation.',
      body: 'Transcribe spoken audio locally with Whisper and translate subtitle files using AI models without sending data away.',
      tabs: {
        transcript: {
          id: 'transcript',
          label: 'Transcription',
          hint: 'Whisper local transcription',
          title: 'Generate subtitles from audio.',
          body: 'Auto-detect source language and run local Whisper models to generate precision srt subtitles ready to load.',
          screenshot: 'subtitle-transcript.webp',
          screenshotAlt: 'Kyna Player Whisper transcription tool'
        },
        translate: {
          id: 'translate',
          label: 'Translation',
          hint: 'Local & cloud AI translation',
          title: 'Translate subtitles into your language.',
          body: 'Connect to local Ollama models or API endpoints to translate subtitle files for effortless international viewing.',
          screenshot: 'subtitle-translate.webp',
          screenshotAlt: 'Kyna Player AI subtitle translation tool'
        }
      }
    },
    casting: {
      number: '06',
      eyebrow: 'Wireless Casting',
      title: 'Move media freely.',
      body: 'Cast local video to compatible TVs, or turn Kyna Player into a ready receiver for streams across your local network.',
      tabs: {
        send: {
          id: 'send',
          label: 'Cast to TV',
          hint: 'Big screen playback control',
          title: 'Continue on the bigger screen.',
          body: 'Scan compatible TVs and displays on your local network, choose a target, and control playback directly.',
          screenshot: 'cast_send.webp',
          screenshotAlt: 'Kyna Player Cast to TV'
        },
        receive: {
          id: 'receive',
          label: 'Receive Cast',
          hint: 'Turn Kyna Player into a screen',
          title: 'Make Kyna Player your display.',
          body: 'Enable DLNA receiving to accept video streams sent from other devices on your local network.',
          screenshot: 'cast_recv.webp',
          screenshotAlt: 'Kyna Player DLNA receive screen'
        }
      }
    },
    flexibility: { number: '07', eyebrow: 'Flexibility', title: 'Watch your way.', body: 'Open network media when you need it, then move into a compact Mini Player without losing control.', screenshot: 'mini.webp', screenshotAlt: 'Kyna Player compact mini player' },
    hdr: { number: '08', eyebrow: 'Dolby Vision & HDR', title: 'Dolby Vision & HDR 10-bit tone mapping.', body: 'Native support for Dolby Vision dynamic range and HDR 10-bit video decoding with intelligent SDR tone mapping, bringing vibrant colors and deep shadow details to standard displays.', screenshot: 'dolby-vision.webp', screenshotAlt: 'Kyna Player Dolby Vision and HDR tone mapping' },
  },
  install: { eyebrow: 'Windows', title: 'Ready when you are.', body: 'Download the latest installer and its SHA-256 checksum from GitHub Releases.', download: 'Download Kyna Player', guide: 'Read the installation guide →' },
  footer: 'Kyna Player for Windows · Local media, kept local.', screenshots: { add: 'Add product screenshot' },
  paths: { home: '/', install: '/docs/installation/', docs: '/docs/', alternateHome: '/zh-CN/', alternateInstall: '/zh-CN/docs/installation/' },
};

export const installEn: InstallCopy = {
  locale: 'en', seo: { title: 'Install Kyna Player on Windows', description: 'Download, verify, install, update, and uninstall Kyna Player on Windows.' },
  heading: 'Install Kyna Player on Windows', lead: 'Get the latest Windows Kyna Player installer from GitHub Releases and verify its checksum before installation.', download: 'Open GitHub Releases', back: '← Back to Kyna Player', skip: 'Skip to content', paths: en.paths,
  sections: [
    { title: 'Install', steps: ['Download the latest Kyna Player Windows installer and its matching SHA256SUMS file from GitHub Releases.', 'In PowerShell, run Get-FileHash on the installer with the SHA256 algorithm and compare it with SHA256SUMS.', 'Run the installer. You may choose the installation directory in the setup wizard.', 'Start Kyna Player from the Start menu or the installation directory.'] },
    { title: 'First use', steps: ['The installer does not include Whisper models or sample media.', 'Before creating subtitles, import a compatible model in the app or use the app model-download flow. Models are stored in your user data directory.'] },
    { title: 'Update and uninstall', steps: ['Exit Kyna Player before updating.', 'Run a newer installer in the same installation directory to update the app.', 'Imported models and app settings remain in your user data directory.', 'To uninstall, use Windows Installed Apps or the Start menu uninstall entry.'] },
  ],
};
