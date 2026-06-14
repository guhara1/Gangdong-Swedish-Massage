#!/usr/bin/env python3
"""IndexNow 색인 통보 스크립트 — Bing·Naver·Yandex 등에 즉시 통보.

IndexNow는 한 번 제출하면 참여 검색엔진(Bing, Naver, Yandex, Seznam 등)에
색인 요청이 함께 전달되는 프로토콜입니다. 구글은 IndexNow에 참여하지 않으므로
구글은 sitemap.xml + Search Console로 따로 처리합니다(INDEXING.md 참고).

사용법:
  python3 indexnow.py                 # sitemap.xml 의 모든 URL 통보
  python3 indexnow.py /magazine/새글/  # 특정 경로(들)만 통보
  python3 indexnow.py https://.../foo/ # 전체 URL 직접 지정도 가능
  python3 indexnow.py --dry-run        # 전송 없이 대상만 출력

의존성 없음(파이썬 표준 라이브러리만 사용).
"""
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

SITE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", SITE)
ENDPOINT = "https://api.indexnow.org/indexnow"  # 참여 엔진에 자동 분배
KEY_LOCATION = f"{SITE}/{INDEXNOW_KEY}.txt"


def sitemap_urls():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def normalize(arg):
    if arg.startswith("http://") or arg.startswith("https://"):
        return arg
    return f"{SITE}/{arg.lstrip('/')}"


def submit(urls):
    body = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=body,
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, resp.read().decode("utf-8", "replace")


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv
    urls = [normalize(a) for a in args] if args else sitemap_urls()
    urls = urls[:10000]  # IndexNow 1회 최대 10,000건

    print(f"host        : {HOST}")
    print(f"keyLocation : {KEY_LOCATION}")
    print(f"대상 URL    : {len(urls)}건")
    for u in urls:
        print("  -", u)
    if dry:
        print("\n[--dry-run] 전송하지 않았습니다.")
        return

    try:
        status, text = submit(urls)
    except Exception as e:  # 네트워크 오류 등
        print(f"\n전송 실패: {e}", file=sys.stderr)
        sys.exit(1)
    # 200/202 = 정상 수신, 그 외는 본문 확인
    print(f"\n응답: HTTP {status} {text or '(본문 없음 — 정상)'}")
    if status not in (200, 202):
        sys.exit(1)


if __name__ == "__main__":
    main()
