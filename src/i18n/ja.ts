import type { InstallCopy, LandingCopy } from './types';

export const ja: LandingCopy = {
  locale: 'ja', direction: 'ltr',
  seo: { title: 'Kyna Player — 映像を、あなたの空間で。', description: 'Kyna Playerは、ローカル動画再生、字幕、音声コントロール、TVキャスティングに特化したWindows用超高速メディアプレーヤーです。' },
  skip: 'コンテンツへスキップ',
  navigation: { features: '機能', docs: 'ドキュメント', install: 'インストール', feedback: 'フィードバック' },
  hero: { eyebrow: 'Windows 超高速メディアプレーヤー', title: '純粋な視聴。', accent: '最高の映像体験。', lead: '次世代のWindowsローカルメディアプレーヤー。軽量ネイティブエンジン、トラッカーゼロ。Dolby VisionとローカルAI字幕強化に完全対応。', download: 'Windows版をダウンロード', explore: '全機能を見る ↓', note: '安全・検証済み · インストーラーとSHA-256チェックサムはGitHub Releasesで公開されています', nowPlaying: '再生中', screenshot: 'main.webp', screenshotAlt: 'Kyna Player インターフェース' },
  badges: ['⚡ 超高速ネイティブ描画', '🎬 Dolby Vision & 10-bit HDR', '🛡️ 100% オフラインAIプライバシー', '📡 相互DLNAキャスティング'],
  intro: 'ローカルメディアを再定義する。無駄を削ぎ落とし、圧倒的な色彩とコントロールをその手に。',
  highlights: [
    {
      icon: '⚡',
      tag: 'ネイティブエンジン',
      title: 'ミリ秒単位の超高速起動',
      description: 'C++ / Slint軽量アーキテクチャを採用。メモリ使用量を極限まで抑え、4K高ビットレート動画も即座に再生。'
    },
    {
      icon: '🎬',
      tag: '高画質技術',
      title: 'Dolby Vision & 10-bit HDR',
      description: '高精度SDR Tone Mappingを搭載。通常のディスプレイでも鮮やかで深い明暗表現と色域を再現。'
    },
    {
      icon: '✨',
      tag: 'ローカルAI',
      title: 'Whisper オフライン音声文字起こし',
      description: 'ローカルAIモデルを直接実行して字幕生成＆翻訳。データは一切外部サーバーに送信されません。'
    },
    {
      icon: '📡',
      tag: 'キャスティング',
      title: '相互DLNAワイヤレス転送',
      description: 'ワンタップでテレビの大画面へ動画を転送。またPCをDLNA受信機として利用することも可能。'
    }
  ],
  features: {
    playback: { number: '01', eyebrow: 'ミニマル再生', title: '映像だけに集中。', body: '洗練された再生画面、正確なシーク、トラック選択、フルスクリーン再生で、コンテンツそのものに没入。', screenshot: 'minimal.webp', screenshotAlt: 'Kyna Player ミニマル再生画面' },
    thumbnails: { number: '02', eyebrow: 'タイムラインサムネイル', title: '高速な位置合わせ。', body: 'タイムライン上にマウスを乗せるだけで高解像度フレームをリアルタイムプレビュー。目的のシーンを即座に特定。', screenshot: 'thumbnails.webp', screenshotAlt: 'Kyna Player タイムラインサムネイル' },
    library: { number: '03', eyebrow: 'プレイリスト', title: '次の作品もスムーズに。', body: 'プレーヤーを離れることなく、プレイリストの検索、並べ替え、保存、連続再生モードの選択が可能。', screenshot: 'playlist.webp', screenshotAlt: 'Kyna Player プレイリスト管理' },
    settings: {
      number: '04',
      eyebrow: '再生設定',
      title: '細部まで自由自在。',
      body: 'カラープリセット、音声遅延調整、ボイス強調から、二重字幕の配置・同期まで、サイドパネルで直感的にコントロール。',
      tabs: {
        audio: {
          id: 'audio',
          label: 'オーディオ',
          hint: '音声同期 & ボイス強調',
          title: 'すべての音をクリアに。',
          body: '音声を微調整し、ナイトモードやボイス強調をトグル。リアルタイム波形フィードバックで直感制御。',
          screenshot: 'playback-audio.webp',
          screenshotAlt: 'Kyna Player オーディオ設定'
        },
        picture: {
          id: 'picture',
          label: 'ビデオ',
          hint: '画角 & カラー調整',
          title: '理想の画質を追求。',
          body: 'ウィンドウサイズ、画面アスペクト比、明るさ、コントラスト、彩度、カラープリセットをカスタマイズ。',
          screenshot: 'playback-picture.webp',
          screenshotAlt: 'Kyna Player 画質設定'
        },
        subtitles: {
          id: 'subtitles',
          label: '字幕',
          hint: '二重字幕 & デザイン',
          title: '読みやすい字幕表示。',
          body: '主字幕・副字幕のフォントサイズ、配置、縁取り、透明度、秒単位のタイミング同期を調整。',
          screenshot: 'playback-subtitle.webp',
          screenshotAlt: 'Kyna Player 字幕設定'
        }
      }
    },
    enhancement: {
      eyebrow: 'AI映像強化比較',
      title: '同じフレームで、違いを見比べる。',
      body: 'スライダーを動かして、オリジナルとリアルタイム強化を比較できます。',
      demoCaption: 'デモ映像は実際の動画ファイルからのスクリーンショットです。',
      cards: {
        dlss: { title: 'DLSS 5', body: 'AI再構成で細部まで鮮明に。', originalLabel: 'オリジナル', enhancedLabel: '強化後', sliderLabel: 'DLSS 5 画像比較', originalAlt: 'DLSS 5 比較用オリジナル画像', enhancedAlt: 'DLSS 5 強化画像' },
        anime4k: { title: 'Anime4K', body: 'アニメーションに合わせた、よりくっきりした線。', originalLabel: 'オリジナル', enhancedLabel: '強化後', sliderLabel: 'Anime4K 画像比較', originalAlt: 'Anime4K 比較用オリジナル画像', enhancedAlt: 'Anime4K 強化画像' }
      }
    },
    subtitles: {
      number: '05',
      eyebrow: '字幕ツール',
      title: 'ローカルAIで理解深まる。',
      body: 'Whisper音声文字起こしとAI字幕翻訳機能を内蔵。外部サーバーに依存せずプライバシーを守りながら言語の壁を解消。',
      tabs: {
        transcript: {
          id: 'transcript',
          label: '文字起こし',
          hint: 'Whisper オフライン文字起こし',
          title: '音声から字幕を自動生成。',
          body: '言語を自動検知し、ローカルWhisperモデルを呼び出して高精度srt字幕を生成。ワンクリックで適用可能。',
          screenshot: 'subtitle-transcript.webp',
          screenshotAlt: 'Kyna Player Whisper字幕転送ツール'
        },
        translate: {
          id: 'translate',
          label: '字幕翻訳',
          hint: 'ローカル & AI翻訳',
          title: '字幕をあなたの言語へ。',
          body: 'ローカルOllamaモデルやAPIと連携し、既存の字幕を多言語にスマート翻訳。海外作品も快適鑑賞。',
          screenshot: 'subtitle-translate.webp',
          screenshotAlt: 'Kyna Player AI字幕翻訳ツール'
        }
      }
    },
    casting: {
      number: '06',
      eyebrow: 'ワイヤレスキャスティング',
      title: '大画面で楽しむ。',
      body: 'ローカル動画をテレビへワンタップ転送。またはPCをDLNA受信機にしてスマホからの映像を受け入れ。',
      tabs: {
        send: {
          id: 'send',
          label: 'TVへ転送',
          hint: '大画面再生 & コントロール',
          title: 'リビングのテレビで続きを。',
          body: 'ネットワーク上の対応テレビを検出。Kyna Playerから直接再生と音量をリモートコントロール。',
          screenshot: 'cast_send.webp',
          screenshotAlt: 'Kyna Player TVキャスティング'
        },
        receive: {
          id: 'receive',
          label: 'キャスティング受信',
          hint: 'PCを画面にする',
          title: 'Kyna Playerを受信ディスプレイに。',
          body: 'DLNA受信サービスを有効化し、スマホや他デバイスからキャストされたストリーミングを再生。',
          screenshot: 'cast_recv.webp',
          screenshotAlt: 'Kyna Player DLNA受信画面'
        }
      }
    },
    flexibility: { number: '07', eyebrow: 'フレキシブル再生', title: '自由なスタイルで鑑賞。', body: 'ストリーミング動画を開き、コンパクトなミニプレーヤーに切り替えて作業中も快適に視聴。', screenshot: 'mini.webp', screenshotAlt: 'Kyna Player ミニプレーヤー' },
    hdr: { number: '08', eyebrow: 'Dolby Vision & HDR', title: 'Dolby Vision & 10-bit HDRトーンマッピング。', body: 'Dolby VisionおよびHDR 10-bit動画デコードに対応。高度なSDRトーンマッピングにより、一般的なモニターでも豊かな色彩と明暗を表現。', screenshot: 'dolby-vision.webp', screenshotAlt: 'Kyna Player Dolby Vision & HDR' },
  },
  install: { eyebrow: 'Windows', title: '準備完了、今すぐ開始。', body: 'GitHub Releasesから最新インストーラーとSHA-256チェックサムをダウンロード。', download: 'Kyna Playerをダウンロード', guide: 'インストールガイドを読む →' },
  footer: 'Kyna Player for Windows · ローカルメディアは、常にローカルに。', screenshots: { add: '製品スクリーンショットを追加' },
  paths: { home: '/ja/', install: '/ja/docs/installation/', docs: '/ja/docs/', alternateHome: '/', alternateInstall: '/docs/installation/' },
};

export const installJa: InstallCopy = {
  locale: 'ja', seo: { title: 'WindowsにKyna Playerをインストール', description: 'Windows版Kyna Playerのダウンロード、検証、インストール、アップデート、アンインストール方法。' },
  heading: 'WindowsにKyna Playerをインストール', lead: 'GitHub Releasesから最新のWindowsインストーラーを入手し、インストール前にハッシュ値を検証してください。', download: 'GitHub Releasesを開く', back: '← Kyna Playerに戻る', skip: 'コンテンツへスキップ', paths: ja.paths,
  sections: [
    { title: 'インストール', steps: ['GitHub Releasesから最新のKyna Player WindowsインストーラーとSHA256SUMSファイルをダウンロードします。', 'PowerShellでGet-FileHashコマンドを実行し、SHA-256の結果をSHA256SUMSと比較して検証します。', 'インストーラーを実行します。セットアップウィザードでインストール先ディレクトリを選択できます。', 'スタートメニューまたはインストール先からKyna Playerを起動します。'] },
    { title: '最初の使用', steps: ['インストーラーにはWhisperモデルやサンプルメディアは含まれていません。', '字幕を作成する前に、アプリ内で対応モデルをインポートするか、モデルダウンロード機能を利用してください。'] },
    { title: 'アップデートとアンインストール', steps: ['アップデート前にKyna Playerを終了してください。', '同じインストールディレクトリで新しいインストーラーを実行するとアップデートできます。', 'インポートされたモデルや設定はユーザーデータディレクトリに保持されます。', 'アンインストールはWindowsの「Appと機能」またはスタートメニューから行えます。'] },
  ],
};
