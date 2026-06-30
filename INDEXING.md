# 색인(인덱싱) 빠르게 되게 하기 — 간다GO

도메인: `https://gangdong-swedish-massage.netlify.app`

이 사이트는 빌드 시 색인용 파일을 자동 생성합니다.

| 파일 | 위치 | 역할 |
|---|---|---|
| `sitemap.xml` | `/sitemap.xml` | 전체 색인 페이지 목록(lastmod·changefreq·priority 포함) |
| `rss.xml` | `/rss.xml` | 매거진 신규 글 피드(검색엔진·구독기 발견용) |
| `robots.txt` | `/robots.txt` | 크롤 허용 + 사이트맵 위치 명시 |
| IndexNow 키 | `/074c4beaf3e71261e9e5e5b6df91109a.txt` | IndexNow 소유 확인 키 |

> 도메인을 바꾸면 `content/site.py`의 `BASE_URL`을 수정하고 `python3 build.py`를 다시 실행하세요.
> IndexNow 키를 새로 만들려면 같은 파일의 `INDEXNOW_KEY`를 바꾸면 됩니다.

---

## 2026년 현재 "즉시 색인"의 진실

- **구글**: 일반 페이지용 즉시 색인 공개 API는 없습니다. 사이트맵 ping(`google.com/ping`)은 **2023년 폐지**됐습니다. → 사이트맵 제출 + URL 검사 도구 + 신선한 lastmod가 정석.
- **빙**: 자체 ping 폐지, **IndexNow로 일원화**.
- **네이버**: **IndexNow 참여**(즉시 통보 가능) + 서치어드바이저 사이트맵 제출.
- 따라서 **IndexNow 하나로 빙·네이버·얀덱스에 즉시 통보**가 되고, 구글만 사이트맵/콘솔로 따로 챙기면 됩니다.

---

## 1. 최초 1회 — 검색엔진 등록

**구글 Search Console** (https://search.google.com/search-console)
1. 속성 추가 → URL 접두어 → `https://gangdong-swedish-massage.netlify.app`
2. 소유확인(HTML 태그 또는 DNS)
3. 색인 → Sitemaps → `sitemap.xml` 제출

**네이버 서치어드바이저** (https://searchadvisor.naver.com)
1. 사이트 등록 → 소유확인(메인페이지에 `naver-site-verification` 메타 이미 삽입됨)
2. 요청 → 사이트맵 제출 → `sitemap.xml`
3. 요청 → RSS 제출 → `rss.xml`

**빙 웹마스터** (https://www.bing.com/webmasters) — 선택
- 구글 콘솔에서 가져오기(Import) 가능. IndexNow 키도 자동 인식됩니다.

---

## 2. 글 올릴 때마다 — IndexNow 즉시 통보 (빙·네이버·얀덱스)

배포가 끝난 뒤(키 파일이 라이브에 떠야 함) 실행:

```bash
python3 build.py                       # 사이트 재생성(sitemap·rss 갱신)
# git add/commit/push → Cloudflare Pages 배포 완료까지 대기

python3 indexnow.py                     # sitemap.xml 전체 통보
python3 indexnow.py /magazine/새글/      # 새 글만 콕 집어 통보
python3 indexnow.py --dry-run           # 전송 없이 대상만 확인
```

- 의존성 없음(표준 라이브러리만). `api.indexnow.org` 한 곳에 보내면 참여 엔진에 자동 분배됩니다.
- 응답 `HTTP 200/202`면 정상 접수입니다.
- ⚠️ **키 파일이 라이브 URL에서 200으로 열려야** 통보가 유효합니다. 배포 완료 후 실행하세요.

---

## 3. (선택) 구글 Indexing API

`google_indexing.py` 참고. **단, 구글 Indexing API는 공식적으로 JobPosting·BroadcastEvent
페이지만 지원**합니다. 일반 페이지엔 보장이 없으니, 구글은 아래 정석 경로를 권장합니다.

- 정석: 사이트맵 제출 + **Search Console > URL 검사 > 색인 생성 요청**(신규/수정 글마다 수동)
- 그래도 자동화를 원하면 `google_indexing.py` 사용(서비스 계정 + `pip install google-auth requests`).

---

## 4. 색인 더 빠르게 — 체크리스트

- [x] `sitemap.xml` lastmod 자동 갱신(빌드 시)
- [x] `rss.xml` 매거진 피드 + `<head>` 자동 발견 링크
- [x] 내부 링크 촘촘하게(허브 → 지역/역/테마 상호 연결) — 이미 적용됨
- [x] 본문 2,000자 미만 자동 noindex(얇은 페이지 색인 낭비 방지)
- [ ] 콘텐츠 추가 후 `indexnow.py` 실행 습관화
- [ ] 구글은 신규 글마다 Search Console URL 검사로 색인 요청

---

## 빠른 명령 요약

```bash
python3 build.py            # 재생성(sitemap·rss·robots·키파일)
python3 indexnow.py         # 빙·네이버·얀덱스 즉시 통보
python3 indexnow.py /path/  # 특정 URL만 통보
```
