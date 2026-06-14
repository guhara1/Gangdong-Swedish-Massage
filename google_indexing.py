#!/usr/bin/env python3
"""구글 Indexing API 색인 통보 스크립트 (선택 사항).

⚠️ 솔직한 안내 — 꼭 읽으세요
  구글 Indexing API는 공식적으로 'JobPosting'·'BroadcastEvent' 구조화 데이터
  페이지만 지원합니다(https://developers.google.com/search/apis/indexing-api).
  일반 콘텐츠 페이지에 쓰는 것은 구글 가이드 범위 밖이며, 색인을 보장하지
  않습니다. 일반 페이지의 정석 빠른 색인 경로는 다음과 같습니다:
    1) sitemap.xml 제출(Search Console) + lastmod 신선도 유지
    2) Search Console > URL 검사 > '색인 생성 요청'(수동)
    3) IndexNow(indexnow.py) — 빙·네이버는 즉시 통보
    4) 내부 링크·RSS 로 신규 글 발견성 높이기
  이 스크립트는 그 점을 이해한 상태에서 본인 사이트에 한해 보조적으로
  쓰기 위한 것입니다.

준비물
  1) Google Cloud 프로젝트에서 Indexing API 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드
  3) Search Console 속성에 그 서비스 계정 이메일을 '소유자'로 추가
  4) pip install google-auth requests

사용법
  export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
  python3 google_indexing.py                  # sitemap.xml 전체
  python3 google_indexing.py /magazine/새글/   # 특정 경로
  python3 google_indexing.py --deleted /old/  # 삭제 통보(URL_DELETED)
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content.site import BASE_URL  # noqa: E402

SITE = BASE_URL.rstrip("/")
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def sitemap_urls():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def normalize(arg):
    if arg.startswith("http://") or arg.startswith("https://"):
        return arg
    return f"{SITE}/{arg.lstrip('/')}"


def main():
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("먼저 설치하세요:  pip install google-auth requests")

    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스 계정 JSON 경로를 지정하세요.")

    deleted = "--deleted" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--deleted"]
    urls = [normalize(a) for a in args] if args else sitemap_urls()
    notif_type = "URL_DELETED" if deleted else "URL_UPDATED"

    creds = service_account.Credentials.from_service_account_file(
        cred_path, scopes=SCOPES)
    session = AuthorizedSession(creds)

    ok = 0
    for u in urls:
        r = session.post(ENDPOINT, json={"url": u, "type": notif_type})
        flag = "OK" if r.status_code == 200 else f"ERR {r.status_code}"
        print(f"[{flag}] {notif_type} {u}")
        if r.status_code != 200:
            print("      ", r.text[:300])
        else:
            ok += 1
    print(f"\n{ok}/{len(urls)} 건 통보 완료. (일 200건 쿼터 주의)")


if __name__ == "__main__":
    main()
