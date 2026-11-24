"""程式檢查：研究模型簡報（research-model-deck loop）。

用法（在專案根目錄執行）：
    python -I .claude/skills/research-model-deck/check_deck.py presentation/research-model/deck.html

檢查項目：
1. 頁數 8–15
2. 每頁至少一個 <cite data-wiki="...">
3. 被引用的 wiki 頁面存在
4. 每頁的數字（年份、小數、百分比）能在該頁引用的 wiki 頁面中找到

渲染溢出需另用瀏覽器檢查（見 SKILL.md）。
結束碼：0 = 全過；1 = 有問題。
"""
import html
import os
import re
import sys
from html.parser import HTMLParser

MIN_PAGES, MAX_PAGES = 8, 15
NUMBER = re.compile(r"\d+\.\d+%?|\d+%|(?<!\d)(?:19|20)\d{2}(?!\d)")


class SlideParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = []      # [{"text": str, "cites": [path], "cite_text": str}]
        self._depth = 0       # nesting depth inside current slide section
        self._in_cite = 0
        self._skip = 0        # inside <script>/<style>

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self._skip += 1
            return
        if tag == "section" and "slide" in (a.get("class") or "").split():
            if self._depth == 0:
                self.slides.append({"text": "", "cites": [], "cite_text": ""})
                self._depth = 1
                return
        if self._depth:
            if tag == "section":
                self._depth += 1
            if tag == "cite":
                self._in_cite += 1
                if a.get("data-wiki"):
                    self.slides[-1]["cites"].append(a["data-wiki"].split("#")[0])

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip = max(0, self._skip - 1)
            return
        if not self._depth:
            return
        if tag == "cite" and self._in_cite:
            self._in_cite -= 1
        if tag == "section":
            self._depth -= 1

    def handle_data(self, data):
        if self._depth and not self._skip:
            key = "cite_text" if self._in_cite else "text"
            self.slides[-1][key] += data + " "


def normalize(s):
    return html.unescape(s).replace("−", "-").replace(",", "")


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    deck = sys.argv[1]
    root = os.getcwd()
    parser = SlideParser()
    parser.feed(open(deck, encoding="utf-8").read())
    slides = parser.slides
    problems = []

    if not (MIN_PAGES <= len(slides) <= MAX_PAGES):
        problems.append(f"全體：頁數 {len(slides)}，應為 {MIN_PAGES}–{MAX_PAGES} 頁")

    cache = {}
    for i, s in enumerate(slides, 1):
        if not s["cites"]:
            problems.append(f"第 {i} 頁：沒有 <cite data-wiki> 出處")
            continue
        texts = []
        for c in s["cites"]:
            p = os.path.normpath(os.path.join(root, c))
            if not os.path.isfile(p):
                problems.append(f"第 {i} 頁：引用的頁面不存在：{c}")
                continue
            if p not in cache:
                cache[p] = normalize(open(p, encoding="utf-8").read())
            texts.append(cache[p])
        if not texts:
            continue
        source = "\n".join(texts)
        for n in sorted(set(NUMBER.findall(normalize(s["text"])))):
            if n not in source:
                problems.append(f"第 {i} 頁：數字「{n}」在引用頁面中找不到")

    print(f"頁數：{len(slides)}")
    if problems:
        print(f"未通過，共 {len(problems)} 項：")
        for p in problems:
            print("- " + p)
        return 1
    print("程式檢查全部通過（渲染溢出請另用瀏覽器檢查）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
