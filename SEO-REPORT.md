# SEO Implementation and Release Validation Report

Assessment completed 26 November 2026. No deployment was performed.

## Scope and implementation

- **Architecture:** static, single-page HTML/CSS/JavaScript site. `CNAME` identifies `anjanakulasinghe.com`. There is no package manifest, build command, app test suite or CI workflow in the repository.
- **Public page inventory:** one indexable route, `https://anjanakulasinghe.com/`. The sitemap contains that canonical root only. The previous repository version also used the root as its canonical page. Section fragment identifiers changed during the already-approved redesign; they are in-page anchors, not separate page routes.
- **Metadata:** one title and description, root canonical, index/follow directive, Open Graph and X card metadata. The title and descriptions now foreground technology leadership, entrepreneurship, software product creation and the engineering experience behind applied AI, without implying unverified product status.
- **Structured data:** JSON-LD graph contains `WebSite`, `ProfilePage`, `Person` and `Organization`, with stable IDs and owner-confirmed person/company relationships. The graph has no `Product` node because Kounga Engage's product status and public availability are not independently confirmed.
- **Crawl configuration:** `robots.txt` allows crawlers and points to the root sitemap. Sitemap XML parses and its URL matches the canonical.
- **CV privacy:** no CV/Resume link or Drive file reference appears in the current public HTML, sitemap or robots file; the previous local PDF path is absent. The external Drive copy and deployed cache/path cannot be checked from this repository.
- **Regression validation:** `scripts/seo_check.py` checks metadata, JSON-LD parsing and key entity relationships, canonical/sitemap agreement, image alt attributes, local references and CV absence.

The current working-tree CSS and most visible HTML reflect the owner's previously approved redesign iterations. The approved QuizForge addition is the sixth and final product-grid card; with the separate Kounga Engage lead feature, the page identifies seven product builds overall. A supplied product image was converted to a 320-pixel WebP variant (about 26 KB) within the existing card system. No page or section was added.

## Factual verification

- The owner confirms Kounga Engage is an AI-powered customer engagement platform developed under Kounga Solutions, involving conversational AI, real-time voice interactions and virtual agents. A direct HTTP check of the official [Kounga Engage website](https://engage.koungasolutions.co.nz/) returned 200. That confirms reachability only; commercial availability, customer adoption and current development/release status remain unverified. No Product schema or claim about those matters was added.
- The owner supplied QuizForge's name and [official Kounga Solutions URL](https://quizforge.koungasolutions.co.nz/) for an end-position card. The official site returned HTTP 200 in a direct request. Search results surfaced unrelated products with the same name, so no details from those products were used. The new card uses only a general quiz-platform description; features, commercial availability, customer adoption and development/release status remain unverified.
- ReleaseLens AI remains documented as an Anjana-associated software quality and release intelligence development initiative. Public availability was not independently confirmed; it is not represented as commercially launched or attributed to similarly named third-party products.
- Direct HTTP checks of the 16 distinct external destinations linked from the current page returned 200 for 15. Anjana's personal LinkedIn returned HTTP 999, consistent with a bot/rate restriction; this does not establish a dead link. The official Engage and QuizForge URLs were reachable even though the separate browser reader had returned errors for those pages.
- The ordinary free Companies Register search is distinct from the paid PPSR search. The official Companies Register page loaded but stated its company search was unavailable. The official NZBN search form loaded, but the browser tool could not submit a query; local DNS also fails. No report or paid service was purchased. Company number and current registry status remain unverified and are not included in markup. [Official search guide](https://companies-register.companiesoffice.govt.nz/help-centre/getting-support-to-use-the-companies-register/searching-the-companies-register/) · [Official NZBN search](https://www.nzbn.govt.nz/search/SearchForm/)

## Portfolio-wide tone refinement

The text now presents engineering experience and human technical ownership as the foundation, with AI as an intentional capability. Representative updates:

| Previous wording | Revised wording | Reason |
| --- | --- | --- |
| “Engineer. Founder. Product builder.” and “AI product builder” | “Technology Leader & Product Creator”; “Software product creator” | Lead with broad technology leadership and product creation, not AI as the professional identity. |
| “Now building AI-powered customer experiences with Kounga Engage.” | “...creating software products and applying AI where it adds real value.” | Connect applied AI to engineering experience and purposeful use. |
| AI coding agents are used for implementation “with human judgement accountable” | “AI coding agents can support ... I verify their output and own the engineering decisions.” | State the human verification and technical ownership directly. |
| “Have a serious thing to build?” | “Ideas deserve good engineering.” | Make the close an invitation to thoughtful conversation, not a freelance brief request. |

The Kounga Engage feature remains prominent and describes conversational AI, real-time voice and virtual agents. Its capability wording remains owner-confirmed; the website response verifies reachability only. Metadata and `ProfilePage`/`Person` text were aligned with the new identity. No CSS, layout, typography, images, icons, navigation, animation or functionality was changed.

## Final performance, accessibility and release-quality validation

**Validated:** 26 November 2026, against the current local static-site build with Chrome 151.0.7922.72 and Lighthouse 13.6.0. Three comparable default-simulation Lighthouse runs were completed for each device profile. One DevTools-throttled trace was also captured for mobile and desktop. No deployment was performed. This section supersedes the previous conditional release assessment.

The approved design, visible copy, crop position, navigation, card layouts and animations remain in place. Changes in this final pass are limited to responsive encoding of the existing hero portrait, viewport-edge clipping of decorative overflow, contact-hint contrast, native wordmark link names, removal of four invalid generic `aria-label` attributes, and this report.

### Confirmed root causes and corrections

- **LCP:** The mobile and desktop LCP element was consistently the existing hero portrait, `section#hero > div.hero-art > div.portrait-frame > img`. Before correction the browser downloaded `assets/img/Anjana.png` (5,116,506 transferred bytes). In the baseline DevTools-throttled mobile trace it took 39,837 ms to load; the page's simulated mobile LCP was 32.4–34.4 seconds. The image was already discoverable and eager. It did not have `fetchpriority="high"`. The hero was not hidden by `opacity: 0`, a reveal observer, or JavaScript initialization; reveal classes apply to below-hero content. Script evaluation was small and did not explain the delay.
- **Image correction:** Added responsive WebP encodings of the same source with the same aspect ratio: 540 × 592 at quality 92 for the tested phone sizes (47,107 transferred bytes) and 960 × 1,052 at quality 95 for denser/larger screens (about 176 KB). The existing CSS crop (`object-fit: cover; object-position: 50% 21%`) is unchanged. `srcset`/`sizes` select the smaller source when it meets the device's pixel needs, and `fetchpriority="high"` marks the hero portrait as critical. The original PNG remains available for social metadata and structured data.
- **LCP trace after correction:** On the mobile DevTools-throttled run, LCP was 2,519 ms (displayed as 2.5 s): TTFB 2 ms, resource-load delay 611 ms, portrait transfer 1,692 ms, and element-render delay 215 ms. The selected image request was 47,107 bytes at High priority; Lighthouse confirmed it was discoverable, eager, and priority hinted. The same element painted in 493 ms on desktop DevTools throttling.
- **Fonts and rendering:** Google Fonts still load the approved DM Sans, DM Mono, Manrope and Playfair Display families. In the constrained mobile trace, the Google Fonts CSS took about 933 ms and font files about 1.0–1.9 seconds each. They contribute to first-contentful-paint timing, but the portrait transfer was the measured LCP bottleneck. Main-thread work after the fix was modest (about 13 ms script evaluation and no blocking time). The typography and rendering setup were not changed.
- **Horizontal overflow:** The measured excess came from the hero's decorative ellipses: `.orbit-one` is 112% wide and rotated −27 degrees; `.orbit-two` is 116% wide, offset left by 8%, and rotated 47 degrees. At 768 px, `.orbit-two` reached 858 px. On phones, the rotated orbit extended the document scroll width by 14–16 px. The `.signal-strip` also paints beyond its box because of `rotate(-1deg) scale(1.02)`, while its moving track is already clipped by the strip; its overflow extent was smaller than the hero orbits. The minimal fix removes body-wide `overflow-x: hidden` and clips horizontal overflow at the existing `<main>` viewport boundary with `overflow-x: clip`. This keeps the clipping edge at the viewport and leaves the header/mobile navigation outside it.
- **Contrast:** Changed only the contact form's `(optional)` hint color from `#797487` to `#746584`; foreground `#746584` on `#f0ebf6` measures 4.51:1, above the 4.5:1 AA requirement for normal text. Type, size and spacing are unchanged.
- **Accessible names:** Removed the overriding `aria-label` attributes from the header and footer wordmark links. Chrome's accessibility tree now names them from visible text: `Anjana Kulasinghe FOUNDER / PRODUCT CREATOR` and `Anjana Kulasinghe ENGINEER · FOUNDER · CREATOR`.
- **HTML/ARIA:** Removed the four unnecessary `aria-label` attributes from generic `div` elements at the hero roles, hero art, proof strip and company wall. Their existing text and portrait/company image names remain accessible. W3C Nu reports zero errors. Its only remaining message is informational: the trailing slash on the description `<meta>` at line 18 has no effect.

### Before-and-after Lighthouse results

These are local laboratory measurements, not field Core Web Vitals. Each default column summarizes three runs using the same Lighthouse form-factor presets. The baseline runs included the existing Google tag; final Lighthouse runs blocked it to prevent analytics transmission, so score changes are not a perfectly isolated comparison. The traces directly identify the portrait transfer as the LCP bottleneck.

| Measurement | Baseline mobile | Final mobile | Baseline desktop | Final desktop |
| --- | ---: | ---: | ---: | ---: |
| Performance | 74 × 3 | 95 × 3 | 76 × 3 | 99, 100, 100 |
| Accessibility | 96 | 100 × 3 | 96 | 100 × 3 |
| Best Practices | 100 | 100 × 3 | 100 | 100 × 3 |
| SEO | 100 | 100 × 3 | 100 | 100 × 3 |
| Simulated LCP | 32.4–34.4 s | 2.8 s × 3 | 5.4–5.5 s | 0.6 s × 3 |
| FCP | 1.7–1.8 s | 1.7–1.8 s | 0.6–0.7 s | 0.6 s |
| TBT | 3–7 ms | 0 ms | 0 ms | 0 ms |
| CLS | 0 | 0 | 0.0013–0.0016 | 0.0014–0.0016 |

For an additional apples-to-apples constrained trace, mobile DevTools LCP fell from 40.5 s to 2.5 s, with the portrait's transfer duration falling from 39.84 s to 1.69 s. DevTools desktop LCP remained about 0.5 s before and after. The final DevTools mobile performance score was 94; the three standard mobile Lighthouse runs scored 95. Do not interpret the simulated/DevTools difference as real-user data; production RUM/CrUX is not available for this local build.

### Final validation results

- Responsive and full-page Chrome captures were made before and after at 375 × 812, 390 × 844, 768 × 1024, 1440 × 900 and 1920 × 1080. All final document and body scroll widths equal their viewport widths; `scrollX` is zero at all five sizes. The formerly overflowing sizes now report 375/375, 390/390, 768/768, 1440/1440 and 1920/1920 px.
- The 390 and 768 px raw screenshot comparisons include the corrected effective viewport widths: baseline `innerWidth` was 404 and 858 px due to overflow, while final `innerWidth` matches 390 and 768 px. This makes those final layouts respond to the real viewport width. The marquee was also active in both capture sets, so its screen position differs by animation phase. Visual review found the approved composition intact; no text, sections, typography, controls or navigation were changed. The portrait uses the same source framing and CSS crop.
- Local page response: HTTP 200. All page images loaded. Six product cards remain, with QuizForge last. Ten internal fragment links were checked and none point to a missing target. Browser console errors: 0; unhandled exceptions: 0; HTTP error responses: 0; unexpected network failures in the final run: 0.
- Navigation was opened and closed; `aria-expanded` updated and the menu navigated to `#work`. Empty-form validation rejected submission. The success/reset flow passed with a mocked EmailJS response; no real enquiry was sent. The marquee moved, the voice-wave animation ran, and all 20 reveal items became visible after scrolling.
- The existing `python3 scripts/seo_check.py` regression passed, including metadata, canonical, JSON-LD parsing/entity relationships, sitemap agreement, local references, alt text and removed-CV checks. `node --check assets/js/particles.js`, inline-script syntax checks, `xmllint --noout sitemap.xml` and `git diff --check` passed. Lighthouse SEO remained 100 in all six final default runs.
- CV/Resume/Drive references remain absent from public HTML and the former local PDF remains absent, as covered by the repository SEO check. This local validation does not independently verify a deployed CDN cache or external Drive copy.

### Findings by type

- **Confirmed functional defects:** None in the tested navigation, fragment links, images, menu, animations, form validation or mocked form success/reset flow. Live email delivery was not tested.
- **Confirmed visual defects:** The decorative hero orbits caused page overflow and the optional hint missed AA contrast. Both are resolved. No other unintended visual defect was found in the reviewed viewports.
- **Confirmed accessibility and HTML defects:** The two wordmark accessible-name failures and four generic `aria-label` conformance errors are resolved. Contrast is 4.51:1 and W3C Nu reports zero errors.
- **Confirmed SEO defects:** None found. The SEO regression check passes and all six final Lighthouse SEO scores are 100.

### Visual review and modified files

No visible content or component was redesigned. The only intended visible distinction is the small optional-hint color adjustment; the image uses the same portrait and crop with responsive encoding. Horizontal clipping is confined to the existing main content boundary and preserves the decorative overflow that remains inside the viewport.

The release-quality fixes changed `index.html`, `assets/css/style.css`, added `assets/img/Anjana-540.webp` and `assets/img/Anjana-960.webp`, and updated this report. A later asset-housekeeping pass moved the KoungaClub logo into `assets/img/products/` and removed the unreferenced 1.5 MB `QuizForge.png`; the rendered card uses the existing `quizforge.webp`. Other working-tree SEO-document changes and the QuizForge WebP pre-date this housekeeping pass and belong to the previously approved rebuild/product work.

### Environment, validation conduct and remaining limits

- Chrome and the temporary localhost preview needed reviewed execution permission because the sandbox blocks local network binding/requests. The approved Chrome run kept the browser sandbox enabled; `--no-sandbox` was not used. Playwright was not installed, so browser checks used Chrome's DevTools Protocol harness. Lighthouse 13.6.0 and W3C Nu were available.
- The JSON-LD was parsed and checked by the repository regression and Lighthouse SEO audits. A separate Schema.org Validator/Google Rich Results Test was not run against the unpublished local build. Field Core Web Vitals and actual email delivery were not tested.
- **Analytics disclosure:** Early baseline validation loaded the site's existing Google tag despite the instruction not to trigger production analytics. The eight baseline Lighthouse reports each show a completed Google Analytics `/g/collect` request. One intermediate browser capture also completed a page-view and scroll collection through Google's alternate `/g/collect` endpoint. This was a validation mistake; those local-preview events may appear in the property's analytics. Every final Lighthouse/Chrome run blocked the tag loader and both collection endpoints before page load; the final browser report shows no collection request completed. No contact enquiry was sent.

### Optional future improvements

- After deployment, compare field Core Web Vitals with these laboratory results and confirm the live image variants are served with the expected cache headers.
- Validate the deployed JSON-LD with Schema.org Validator/Google Rich Results Test and verify live canonical, robots.txt, sitemap and removed-CV URL behavior.
- If first-contentful-paint needs further work later, assess self-hosting the existing approved font files without changing the typography. No additional optimization is required for this release-quality pass.

### Evidence and rerun commands

Baseline captures and Lighthouse reports: `/private/tmp/anjana-release-validation/baseline/`. Final screenshots, results and Lighthouse reports: `/private/tmp/anjana-release-validation/final-browser/` and `/private/tmp/anjana-release-validation/after/`. The final HTML validation JSON is `/private/tmp/anjana-release-validation/html-validation-final.json`.

To rerun locally from the repository root, use the approved local preview server and existing installed tools:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
CAPTURE=1 node /private/tmp/anjana_cdp_release_final.mjs
python3 scripts/seo_check.py
node --check assets/js/particles.js
xmllint --noout sitemap.xml
git diff --check
/private/tmp/seo-phase2-lighthouse/node_modules/.bin/lighthouse http://127.0.0.1:8765/ --chrome-path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' --chrome-flags='--headless=new' --quiet --only-categories=performance,accessibility,best-practices,seo --form-factor=mobile --blocked-url-patterns='https://www.googletagmanager.com/gtag/js*' --blocked-url-patterns='https://www.google-analytics.com/*' --blocked-url-patterns='https://www.google.com/g/collect*' --output=json --output-path=/private/tmp/anjana-release-validation/lighthouse-mobile.json
```

For desktop, replace `--form-factor=mobile` with `--preset=desktop` and use a desktop output filename. W3C Nu can be rerun without posting site traffic to analytics:

```sh
curl -sS --data-binary @index.html -H 'Content-Type: text/html; charset=utf-8' 'https://validator.w3.org/nu/?out=json'
```

## Release recommendation

**GO.** The targeted performance, overflow, contrast, accessible-name and HTML/ARIA defects are resolved. Lighthouse SEO remains 100; mobile performance scored 95 across three default runs and the constrained mobile LCP is 2.5 s. The reviewed build is ready for production deployment. No deployment was performed. The SEO implementation is complete; no further SEO phase is required.
