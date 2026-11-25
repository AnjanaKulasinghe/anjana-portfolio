#!/usr/bin/env python3
"""Dependency-free SEO regression checks for this static portfolio."""

from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_count = 0
        self.title_text = []
        self.in_title = False
        self.meta = {}
        self.links = []
        self.assets = []
        self.images = []
        self.jsonld = []
        self.ids = set()
        self.in_jsonld = False
        self.jsonld_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "title":
            self.title_count += 1
            self.in_title = True
        if tag == "meta":
            key = attrs.get("name") or attrs.get("property")
            if key:
                self.meta.setdefault(key.lower(), []).append(attrs.get("content", ""))
        if tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.links.append(("canonical", attrs.get("href", "")))
        if tag in {"a", "img", "script"}:
            if tag == "a":
                self.links.append(("anchor", attrs.get("href", "")))
            elif tag == "img":
                self.images.append(attrs)
                self.assets.append(attrs.get("src", ""))
            elif tag == "script" and attrs.get("type") == "application/ld+json":
                self.in_jsonld = True
                self.jsonld_text = []

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script" and self.in_jsonld:
            self.jsonld.append("".join(self.jsonld_text))
            self.in_jsonld = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text.append(data)
        if self.in_jsonld:
            self.jsonld_text.append(data)


def main():
    failures = []
    page = (ROOT / "index.html").read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(page)
    title = "".join(parser.title_text).strip()
    if parser.title_count != 1 or not title:
        failures.append("Expected one non-empty title element")
    if len(parser.meta.get("description", [])) != 1 or not parser.meta["description"][0].strip():
        failures.append("Expected one non-empty meta description")
    if len([item for item in parser.links if item[0] == "canonical"]) != 1:
        failures.append("Expected exactly one canonical URL")
    canonical = next((value for kind, value in parser.links if kind == "canonical"), "")
    if canonical != "https://anjanakulasinghe.com/":
        failures.append(f"Unexpected canonical URL: {canonical}")
    for required in ("og:title", "og:description", "og:url", "og:image", "twitter:card"):
        if len(parser.meta.get(required, [])) != 1 or not parser.meta[required][0].strip():
            failures.append(f"Expected one non-empty {required} metadata value")
    if not parser.jsonld:
        failures.append("Missing JSON-LD")
    else:
        jsonld_values = []
        for block in parser.jsonld:
            try:
                jsonld_values.append(json.loads(block))
            except json.JSONDecodeError as error:
                failures.append(f"Invalid JSON-LD: {error}")
        nodes = []
        for value in jsonld_values:
            if isinstance(value, dict):
                nodes.extend(value.get("@graph", []))
                if value.get("@type"):
                    nodes.append(value)
        person = next((node for node in nodes if node.get("@type") == "Person"), {})
        organization = next((node for node in nodes if node.get("@type") == "Organization"), {})
        if person.get("name") != "Anjana Kulasinghe":
            failures.append("Expected canonical Person name Anjana Kulasinghe")
        if not person.get("hasCredential", {}).get("name"):
            failures.append("Person schema must include the verified credential")
        if person.get("worksFor", {}).get("@id") != organization.get("@id"):
            failures.append("Person worksFor must reference the declared Organization")
        if organization.get("legalName") != "AJ&W Consulting Limited":
            failures.append("Organization schema legalName is inconsistent")
        if organization.get("alternateName") != "Kounga Solutions":
            failures.append("Organization schema must identify Kounga Solutions as the trading identity")
        if organization.get("brand", {}).get("name") != "Kounga Games":
            failures.append("Organization schema must identify the Kounga Games brand")
    for image in parser.images:
        if "alt" not in image:
            failures.append(f"Image missing alt attribute: {image.get('src', '(no src)')}")
    for kind, value in parser.links:
        if kind == "anchor" and value.startswith("./"):
            local_path = (ROOT / value[2:].split("#", 1)[0]).resolve()
            if not local_path.exists():
                failures.append(f"Missing local asset: {value}")
        elif kind == "anchor" and value.startswith("#") and value != "#":
            if value[1:] not in parser.ids:
                failures.append(f"Missing in-page anchor target: {value}")
    for value in parser.assets:
        if value.startswith("./"):
            local_path = (ROOT / value[2:].split("#", 1)[0]).resolve()
            if not local_path.exists():
                failures.append(f"Missing image asset: {value}")
    for filename in ("index.html", "sitemap.xml", "robots.txt"):
        content = (ROOT / filename).read_text(encoding="utf-8")
        if re.search(r"(?i)(CV\s*/\s*Resume|Resume_Anjana|drive\.google\.com/file/d/1Spm064)", content):
            failures.append(f"Prohibited CV reference remains in {filename}")
    if (ROOT / "assets/docs/Resume_AnjanaKulasinghe_AJ.pdf").exists():
        failures.append("Public CV PDF still exists")
    try:
        sitemap = ET.parse(ROOT / "sitemap.xml").getroot()
        namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        urls = [node.text for node in sitemap.findall("sm:url/sm:loc", namespace)]
        if urls != [canonical]:
            failures.append(f"Sitemap URLs do not match canonical root: {urls}")
    except (ET.ParseError, OSError) as error:
        failures.append(f"Invalid sitemap: {error}")

    if failures:
        print("SEO checks failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"SEO checks passed for {title}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
