# 간다GO — 강동 출장마사지·홈타이 안내 사이트

강동구 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호·전화·BASE_URL·메뉴 구조
  main.py           # 메인 페이지 (+ Organization/WebSite/FAQPage JSON-LD)
  areas.py          # 지역별: 강동구 허브 + 대표 동 9개
  stations.py       # 지하철역별: 허브 + 12개 역
  themes.py         # 테마별: 허브 + 14개 테마
  info.py           # 출장마사지 안내·코스·예약·가이드·후기·고객센터·약관
assets/             # CSS, 모바일 내비 JS
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 지역은 대표 동 9개만 (강일·상일·명일·고덕·암사·천호·성내·길·둔촌동) — 숫자 행정동 페이지 없음
- 역은 역 1개당 페이지 1개 — 천호역 같은 환승역도 URL 하나, 출구별 페이지 없음
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지) — 테마는 독립 페이지로만 운영
- 지역·역 메타 디스크립션은 **80자 이내**로 각 페이지 고유 작성 (중복·복사 방지)
- 9호선 4단계 연장 예정역은 별도 색인 페이지 없이 고덕역·강일역 본문 보조 설명으로만 처리
- 실제 오프라인 사업장 주소가 없으므로 **LocalBusiness 계열 Schema 미사용** (Organization·WebSite·FAQPage만)
- 상단/하위 메뉴와 푸터에 키워드·지역명·역명 대량 나열 없음
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
3. Google Search Console에 `sitemap.xml` 제출
