# AI enhancement comparison design

## Placement and content

Add an AI enhancement comparison section immediately after Playback Settings. It contains one wide comparison canvas, approximately twice the previous card size, with two accessible tabs. DLSS 5 is selected by default.

- DLSS 5: `s1-1.png` original and `s1-2.png` enhanced.
- Anime4K: `s2-1.png` original and `s2-2.png` enhanced.

Selecting a tab swaps the complete image pair, title, brief algorithm description, labels, and accessible text. Each selection begins at a 50/50 split. The canvas uses the source images' 16:9 ratio so the full screenshots remain visible. The original image is fully visible beneath an enhanced image clipped at the divider. The left label identifies the original image; the right label displays the selected algorithm name (`DLSS 5` or `Anime4K`). A low-emphasis localised caption below the canvas states that the demonstration image is a screenshot from an actual video file.

## Interaction and accessibility

- Use the `DLSS 5` and `Anime4K` tabs with click or keyboard navigation; the selected tab updates the visible algorithm description and resets the split to 50%.
- Drag or tap/click the divider to set the comparison ratio.
- Pointer and touch input use the same coordinate-to-ratio calculation and clamp the result from 0% to 100%.
- The divider is a focusable slider with `aria-valuemin`, `aria-valuemax`, and `aria-valuenow`; left/right arrows change it in 5% increments, with Home and End moving to 0% and 100%. It has no visual active or focus outline.
- Mobile cards remain full width with a fixed, proportionate image area; labels remain legible and do not overlap the handle.

## Localised copy

| Locale | Section eyebrow | Section title | Section body |
| --- | --- | --- | --- |
| English | AI Enhancement Comparison | See the difference, frame by frame. | Drag the divider to compare the original image with real-time enhancement. |
| 简体中文 | AI 视频增强对比 | 在同一帧中看见差别。 | 拖动分割线，对比原始画面与实时增强效果。 |
| 日本語 | AI映像強化比較 | 同じフレームで、違いを見比べる。 | スライダーを動かして、オリジナルとリアルタイム強化を比較できます。 |
| 한국어 | AI 영상 향상 비교 | 같은 프레임에서 차이를 확인하세요. | 분할선을 드래그하여 원본과 실시간 향상 결과를 비교하세요. |

DLSS 5 card: AI reconstruction for clearer fine detail. / AI 重建，让细节更清晰。 / AI再構成で細部まで鮮明に。 / AI 재구성으로 섬세한 디테일까지 선명하게.

Anime4K card: Sharper line work, tuned for animation. / 为动画调校的更锐利线条。 / アニメーションに合わせた、よりくっきりした線。 / 애니메이션에 맞춘 더욱 선명한 라인.

## Verification

Build the Astro site. On desktop and touch-sized viewports, verify each tab renders its correct pair and description, switching resets the split to 50%, and pointer/touch and keyboard controls update the active comparison.
