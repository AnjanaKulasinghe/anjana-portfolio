# SEO Audit

## Scope and evidence

Reviewed the single-page static portfolio, existing links, CNAME, owner clarifications and available public company/product pages on 25 November 2026. The owner confirms Anjana Kulasinghe's Auckland location, 16+ years of experience, ISTQB CTFL, founder/director role at AJ&W Consulting Limited, its Kounga Solutions trading identity, 2017 establishment and Kounga Games publishing brand. The official Kounga Solutions site also presents Anjana as its founder. Apple's developer listings show AJ&W Consulting Limited as the publisher/provider for multiple portfolio apps, including Body Progress, BumpStory, TripMate, PerkyLoop and Pegra.

The official Companies Register guide distinguishes ordinary company searches from PPSR searches: basic company information is available through the ordinary search, while the PPSR search is the paid service. The official search page opened, but this review interface could not submit a company-name query. No fee was paid. The registry number and current status therefore remain unverified; the legal identity in markup relies on the owner's confirmation and public company/app-store evidence. No private details were added. [Companies Register search guide](https://companies-register.companiesoffice.govt.nz/help-centre/getting-support-to-use-the-companies-register/searching-the-companies-register/)

## Findings and status

| Severity | Finding | Status |
| --- | --- | --- |
| High | A CV link and publicly served resume PDF exposed CV functionality. | Removed both from source. After deployment, the local PDF path should return 404. |
| High | The title described the site as a lead test automation consultant profile. | Updated to reflect technology, quality engineering and product building. |
| Medium | Canonical, description, social tags, sitemap, robots file and structured identity data were absent. | Added for the canonical root page. |
| Medium | The About/contact copy and employer section heading leaned toward a conventional CV structure. | Repositioned copy within existing elements; no new visible section or page. |
| Medium | Entity relationship between person, legal company, trading name and publisher brand was underspecified. | Schema now names AJ&W Consulting Limited as the Organization, Kounga Solutions as its alternate name and Kounga Games as a brand; Person founder/director and company relationship are explicit. |
| Medium | No local SEO regression check existed. | Added `scripts/seo_check.py`; no CI workflow or application test framework exists in this repository. |
| Medium | Applied AI, product case studies and engineering experience lacked a specific future evidence plan. | Added owner-approved topic outlines in `SEO-CONTENT-RECOMMENDATIONS.md`; these remain unpublished. |
| Low | Search Console/Bing verification is not represented in source. | Existing analytics preserved; webmaster setup remains an external owner action. |

## Identity and portfolio verification

- Primary entity name: **Anjana Kulasinghe**. Schema retains the existing public variation “Anjana Kulasinghe (AJ)”. The longer alternate-name form has been withheld because the owner has not confirmed its exact spelling and an official registry result was not obtained.
- Person schema includes owner-confirmed Auckland context, over 16 years in the field, ISTQB CTFL, leadership, entrepreneurship and product creation. Public claims remain limited to visible/owner-approved information.
- Company entity: **AJ&W Consulting Limited**, legal name confirmed by owner; **Kounga Solutions** is the trading identity. The official company website and company LinkedIn identify the public-facing Kounga Solutions brand. A free ordinary register query was attempted but could not be submitted using the available interface; company number and current status remain unverified. The separate paid PPSR search was not used.
- **Kounga Games** is represented as a publisher brand associated with the legal company, as owner-confirmed. Apple's [public developer account](https://apps.apple.com/nz/developer/aj-w-consulting-limited/id1691705009) supports that company's role as publisher/provider for several apps.
- Current personal LinkedIn URL is already present on the portfolio and represented in `sameAs`. The [Kounga Solutions company LinkedIn](https://nz.linkedin.com/company/koungasolutions) confirms Auckland headquarters and 2017 founding and is represented on the Organization. Facebook, Instagram and X links remain only as existing social links, not professional identity assertions.
- Current site and app-store pages support TripMate, Pegra, PerkyLoop, Body Progress and BumpStory as products associated with AJ&W/Kounga; company publisher attribution does not by itself establish Anjana's individual authorship. KoungaClub is already presented with Anjana's design/build role on the portfolio and has an official product site.
- Kounga Engage's official URL was supplied by the owner as [engage.koungasolutions.co.nz](https://engage.koungasolutions.co.nz/). The site could not be fetched by the available browser or local DNS, and no indexed official page was found. Conversational AI, real-time voice interactions and virtual agents are owner-supplied descriptions, not independently verified capabilities. Commercial availability, customer adoption and development status are unverified; no product claim was added to the public page or schema.
- ReleaseLens AI is an owner-confirmed software quality and release intelligence development initiative associated with Anjana Kulasinghe. Its public availability was not independently confirmed. Treat it as a development initiative, not a commercially launched product, and do not conflate it with unrelated similarly named products.

## Remaining technical limitations

- CNAME indicates GitHub Pages, but hosting configuration is not in this repository. Removed CV paths cannot be redirected here; an honest not-found response is appropriate.
- The external Google Drive CV itself was not changed. Any externally hosted copy or cached result requires owner action.
- Desktop and mobile browser rendering plus screenshot comparison were completed locally. At 375px, `body.scrollWidth` is 588px while the viewport/root width is 375px; the hero copy is clipped at the right edge. The same overflow and clipping are present in the baseline, so this is an inherited confirmed defect, not a regression from the metadata update. Desktop body width is 1460px at a 1440px viewport. Eleven nested anchor starts were found in product-card markup; nested links are invalid HTML and can compromise link semantics/keyboard access. These were not changed because this final pass is limited to metadata and documentation.
- Lighthouse and modern HTML5 validation could not run in this environment: no package was present in cache and network/package registry resolution was unavailable. The installed Apple HTML Tidy is from 2006 and does not support current HTML5 elements, so its errors are not a meaningful validation result. An online Rich Results Test and production HTTP checks were not possible because the site was not deployed. Production robots/sitemap delivery remains to be checked after deployment.
- External link checks confirmed several reachable product/store URLs. Some social profiles, App Store pages and product sites could not be fetched by the available reader (cache/reader errors); those outcomes are inconclusive and are not classified as dead links.
- `robots.txt` allows all crawlers, matching prior default behavior; the repository had no explicit model-training crawler directives.

## Guidance

Structured data should match visible content and cannot guarantee rankings or special search presentation. See [Google's ProfilePage guidance](https://developers.google.com/search/docs/appearance/structured-data/profile-page), [structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) and [sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap). The Companies Register describes its search options and fees [here](https://companies-register.companiesoffice.govt.nz/help-centre/getting-support-to-use-the-companies-register/searching-the-companies-register/).
