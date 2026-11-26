# SEO Audit

## Scope and evidence

Reviewed the single-page static portfolio, previous repository state, CNAME, owner clarifications and available public company/product sources on 26 November 2026. The owner confirms Anjana Kulasinghe's Auckland location, 16+ years of experience, ISTQB CTFL, founder/director role at AJ&W Consulting Limited, its Kounga Solutions trading identity, 2017 establishment and Kounga Games publishing brand. The current official Kounga Solutions site presents Anjana as its founder and describes its technology services. Apple's developer listings and Google Play show AJ&W/Kounga product relationships for selected apps; they do not establish Anjana's personal contribution to every product.

The Companies Register's ordinary company search is distinct from PPSR searches. The free official Companies Register search page and its direct search application both loaded, but the Register displayed that company search was unavailable. The official NZBN search form loaded, but its query could not be submitted through the available browser tool; shell requests also fail DNS resolution. No report or paid service was purchased. The registry number and current status therefore remain unverified and have not been added to markup. The legal identity relationship in markup relies on owner confirmation and public company sources. [Companies Register search guide](https://companies-register.companiesoffice.govt.nz/help-centre/getting-support-to-use-the-companies-register/searching-the-companies-register/) · [Official NZBN search](https://www.nzbn.govt.nz/search/SearchForm/)

## Findings and status

| Severity | Finding | Status |
| --- | --- | --- |
| High | A CV link and publicly served resume PDF exposed CV functionality. | Removed both from source. Production currently returns 404 for the former local PDF path. |
| High | The title described the site as a lead test automation consultant profile. | Updated to foreground technology leadership, entrepreneurship and product creation, supported by quality engineering and applied AI. |
| Medium | Canonical, description, social tags, sitemap, robots file and structured identity data were absent. | Added for the canonical root page. |
| Medium | The About/contact copy and employer section heading leaned toward a conventional CV structure. | Repositioned copy within existing elements; no new visible section or page. |
| Medium | Entity relationship between person, legal company, trading name and publisher brand was underspecified. | Schema now names AJ&W Consulting Limited as the Organization, Kounga Solutions as its alternate name and Kounga Games as a brand; Person founder/director and company relationship are explicit. |
| Medium | No local SEO regression check existed. | Added `scripts/seo_check.py`; no CI workflow or application test framework exists in this repository. |
| Medium | Applied AI, product case studies and engineering experience lacked a specific future evidence plan. | Added owner-approved topic outlines in `SEO-CONTENT-RECOMMENDATIONS.md`; these remain unpublished. |
| Low | Search Console/Bing verification is not represented in source. | Existing analytics preserved; webmaster setup remains an external owner action. |

## Identity and portfolio verification

- Primary entity name: **Anjana Kulasinghe**. Schema retains the existing public variation “Anjana Kulasinghe (AJ)”. The longer alternate-name form has been withheld because the owner has not confirmed its exact spelling and an official registry result was not obtained.
- Current positioning leads with Anjana's technology leadership, entrepreneurship and software product creation. His 16+ years in quality engineering provide the engineering foundation; applied AI is described as one purposeful capability, guided by human judgement and technical ownership.
- Person schema includes owner-confirmed Auckland context, over 16 years in the field, ISTQB CTFL, leadership, entrepreneurship and product creation. Public claims remain limited to visible/owner-approved information.
- Company entity: **AJ&W Consulting Limited**, legal name confirmed by owner; **Kounga Solutions** is the trading identity. The official company website and company LinkedIn identify the public-facing Kounga Solutions brand. A free ordinary register query was attempted but could not be submitted using the available interface; company number and current status remain unverified. The separate paid PPSR search was not used.
- **Kounga Games** is represented as a publisher brand associated with the legal company, as owner-confirmed. Apple's [public developer account](https://apps.apple.com/nz/developer/aj-w-consulting-limited/id1691705009) supports that company's role as publisher/provider for several apps.
- Current personal LinkedIn URL is already present on the portfolio and represented in `sameAs`. The [Kounga Solutions company LinkedIn](https://nz.linkedin.com/company/koungasolutions) confirms Auckland headquarters and 2017 founding and is represented on the Organization. Facebook, Instagram and X links remain only as existing social links, not professional identity assertions.
- Current site and app-store pages support TripMate, Pegra, PerkyLoop, Body Progress and BumpStory as products associated with AJ&W/Kounga; company publisher attribution does not by itself establish Anjana's individual authorship. KoungaClub is already presented with Anjana's design/build role on the portfolio and has an official product site.
- QuizForge was added to the end of the existing product grid at the owner's request. The owner supplied its name and Kounga Solutions URL; the official site returned HTTP 200 in a direct request. The card therefore uses a general quiz-platform description only; features, availability, adoption and development/release status remain unverified.
- Kounga Engage's official URL is [engage.koungasolutions.co.nz](https://engage.koungasolutions.co.nz/). The owner confirms it was developed under Kounga Solutions and describes AI-powered customer engagement, conversational AI, real-time voice interactions and virtual agents. The official URL returned HTTP 200; this confirms reachability, not independent verification of capabilities. Commercial availability, customer adoption and current development/release status are unverified. No Product schema or launch, customer or availability claim is made.
- ReleaseLens AI is an owner-confirmed software quality and release intelligence development initiative associated with Anjana Kulasinghe. Its public availability was not independently confirmed. Treat it as a development initiative, not a commercially launched product, and do not conflate it with unrelated similarly named products.

## Remaining technical limitations

- CNAME indicates GitHub Pages, but hosting configuration is not in this repository. Removed CV paths cannot be redirected here; an honest not-found response is appropriate.
- The external Google Drive CV itself was not changed. Any externally hosted copy or cached result requires owner action.
- Final local validation is complete; see `SEO-REPORT.md` for viewport screenshots, browser interaction checks, Lighthouse results and HTML validation. Chrome 151 rendered the current page through the temporary local server. The page has no approved screenshot baseline for pixel-diff comparison.
- Lighthouse 13.6.0 scored SEO 100 on both mobile and desktop; performance was 74/76 and accessibility 96/96. W3C Nu reported four ARIA conformance errors. Contrast and accessible-name findings, minor decorative overflow, package-registry limits and other validation details are recorded in `SEO-REPORT.md`. No automatic source fixes were made.
- Direct HTTP checks reached 15 of 16 distinct outbound destinations with status 200. Personal LinkedIn returned 999, inconclusive due to rate/bot restriction. Production homepage, `robots.txt` and sitemap returned 200; the removed CV path returned 404. Production still serves the earlier homepage because the rebuild has not been deployed.
- The source repository and sitemap expose one public page at the root. The root canonical is preserved from the previous version. The old section fragment IDs changed as part of the approved redesign; they are not separate indexable routes.
- `robots.txt` allows all crawlers, matching prior default behavior; the repository had no explicit model-training crawler directives.

## Guidance

Structured data should match visible content and cannot guarantee rankings or special search presentation. See [Google's ProfilePage guidance](https://developers.google.com/search/docs/appearance/structured-data/profile-page), [structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) and [sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap). The Companies Register describes its search options and fees [here](https://companies-register.companiesoffice.govt.nz/help-centre/getting-support-to-use-the-companies-register/searching-the-companies-register/).
