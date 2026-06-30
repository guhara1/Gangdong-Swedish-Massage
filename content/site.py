# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://gangdong-swedish-massage.netlify.app"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 검색엔진 사이트 소유확인 코드
NAVER_VERIFY = "68d81b7414fa4b3e79be2895d23154d1f9bd574b"

# IndexNow 키 — 빌드 시 루트에 "<KEY>.txt" 키 파일이 생성된다.
# Bing·Naver·Yandex 등 IndexNow 참여 검색엔진에 즉시 색인 통보할 때 사용한다.
INDEXNOW_KEY = "074c4beaf3e71261e9e5e5b6df91109a"

# ── 사이트 공통 평점·후기 ──────────────────────────────────────────────
# 전 페이지에 동일하게 노출되는 브랜드 누적 평점과 대표 후기.
# build.py 가 이 값으로 (1) 화면용 후기 배너와 (2) JSON-LD(AggregateRating·Review)를
# 함께 생성하므로, 구조화 데이터와 실제 화면 콘텐츠가 항상 일치한다.
RATING_VALUE = "4.9"
RATING_COUNT = "318"

REVIEWS = [
    {
        "author": "김O현",
        "rating": "5",
        "date": "2026-05-18",
        "area": "천호동",
        "theme": "스웨디시",
        "body": "예약 전화부터 친절했고 도착 시간도 정확했어요. 압을 중간에 조절해 달라고 했는데 바로 맞춰 주셔서 끝나고 바로 잠들었습니다.",
    },
    {
        "author": "이O민",
        "rating": "5",
        "date": "2026-04-30",
        "area": "고덕동",
        "theme": "스포츠·경락",
        "body": "운동 후 뭉친 다리랑 허리 위주로 풀어 달라고 했더니 그 부분을 집중해서 봐 주셨어요. 새 아파트 단지인데 출입 안내도 미리 챙겨 주셔서 편했습니다.",
    },
    {
        "author": "박O영",
        "rating": "5",
        "date": "2026-04-12",
        "area": "둔촌동",
        "theme": "아로마테라피",
        "body": "향이 과하지 않고 은은해서 좋았어요. 집에서 받는데도 샵 못지않게 차분한 분위기로 진행해 주셨습니다. 다음엔 커플로 예약하려고요.",
    },
    {
        "author": "정O우",
        "rating": "4",
        "date": "2026-03-26",
        "area": "성내동",
        "theme": "타이마사지",
        "body": "오래 앉아 일해서 목·어깨가 굳었는데 스트레칭까지 꼼꼼히 해 주셔서 개운했습니다. 퇴근 시간대라 도착이 살짝 늦었지만 미리 연락 주셔서 괜찮았어요.",
    },
    {
        "author": "최O라",
        "rating": "5",
        "date": "2026-03-09",
        "area": "암사동",
        "theme": "발마사지",
        "body": "한강에서 자전거 타고 와서 발이랑 종아리가 퉁퉁 부었는데 시원하게 풀렸어요. 어머니 정기 관리도 같이 부탁드릴 생각입니다.",
    },
    {
        "author": "한O수",
        "rating": "5",
        "date": "2026-02-20",
        "area": "명일동",
        "theme": "홈케어",
        "body": "부모님 댁으로 대리 예약했는데 연락부터 방문까지 매끄러웠습니다. 어르신이 편하게 받으셨다고 좋아하셔서 다음에도 부탁드리려고요.",
    },
]

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("강동 출장마사지", "/massage/", [
        ("출장마사지 안내", "/massage/#service"),
        ("홈타이 안내", "/massage/#hometai"),
        ("전지역 방문 안내", "/massage/#coverage"),
        ("지하철역 인근 안내", "/massage/#stations"),
        ("예약 가능 시간", "/massage/#hours"),
        ("코스 선택 안내", "/massage/#course"),
        ("이용 전 확인사항", "/massage/#check"),
        ("위생·안전 안내", "/massage/#safety"),
        ("자주 묻는 질문", "/massage/#faq"),
    ]),
    ("지역별 안내", "/gangdong-gu/", [
        ("강동구 전체", "/gangdong-gu/"),
        ("강일동", "/gangdong-gu/gangil-dong/"),
        ("상일동", "/gangdong-gu/sangil-dong/"),
        ("명일동", "/gangdong-gu/myeongil-dong/"),
        ("고덕동", "/gangdong-gu/godeok-dong/"),
        ("암사동", "/gangdong-gu/amsa-dong/"),
        ("천호동", "/gangdong-gu/cheonho-dong/"),
        ("성내동", "/gangdong-gu/seongnae-dong/"),
        ("길동", "/gangdong-gu/gil-dong/"),
        ("둔촌동", "/gangdong-gu/dunchon-dong/"),
    ]),
    ("지하철역별 안내", "/gangdong-gu/stations/", [
        ("역 전체", "/gangdong-gu/stations/"),
        ("천호역", "/gangdong-gu/stations/cheonho-station/"),
        ("강동역", "/gangdong-gu/stations/gangdong-station/"),
        ("길동역", "/gangdong-gu/stations/gildong-station/"),
        ("굽은다리역", "/gangdong-gu/stations/gubeundari-station/"),
        ("명일역", "/gangdong-gu/stations/myeongil-station/"),
        ("고덕역", "/gangdong-gu/stations/godeok-station/"),
        ("상일동역", "/gangdong-gu/stations/sangildong-station/"),
        ("강일역", "/gangdong-gu/stations/gangil-station/"),
        ("둔촌동역", "/gangdong-gu/stations/dunchondong-station/"),
        ("암사역", "/gangdong-gu/stations/amsa-station/"),
        ("암사역사공원역", "/gangdong-gu/stations/amsa-park-station/"),
        ("강동구청역", "/gangdong-gu/stations/gangdong-office-station/"),
    ]),
    ("테마별 안내", "/themes/", [
        ("전체 테마", "/themes/"),
        ("스웨디시", "/themes/swedish/"),
        ("로미로미", "/themes/lomilomi/"),
        ("타이마사지", "/themes/thai/"),
        ("중국마사지", "/themes/chinese/"),
        ("아로마테라피", "/themes/aroma/"),
        ("홈케어", "/themes/homecare/"),
        ("호텔식마사지", "/themes/hotel-style/"),
        ("발마사지", "/themes/foot/"),
        ("스포츠·경락", "/themes/sports/"),
        ("스킨케어", "/themes/skincare/"),
        ("왁싱", "/themes/waxing/"),
        ("커플 관리", "/themes/couple/"),
        ("24시간", "/themes/24hours/"),
        ("수면 가능", "/themes/overnight/"),
    ]),
    ("코스안내", "/courses/", [
        ("전체 코스", "/courses/"),
        ("피로 회복 관리", "/courses/#recovery"),
        ("아로마 관리", "/courses/#aroma"),
        ("스포츠 관리", "/courses/#sports"),
        ("홈타이 코스", "/courses/#hometai"),
        ("커플·가족 방문 관리", "/courses/#couple"),
        ("기업·단체 방문 관리", "/courses/#group"),
        ("가격 안내", "/courses/#price"),
        ("코스 선택 가이드", "/courses/#guide"),
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 장소", "/reservation/#place"),
        ("결제 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
        ("예약 전 체크사항", "/reservation/#check"),
    ]),
    ("이용가이드", "/guide/", [
        ("처음 이용하시는 분", "/guide/#first"),
        ("방문 전 준비사항", "/guide/#prepare"),
        ("위생 및 안전 기준", "/guide/#hygiene"),
        ("관리 후 주의사항", "/guide/#after"),
        ("금지행위 안내", "/guide/#prohibited"),
        ("이용 FAQ", "/guide/#faq"),
    ]),
    ("매거진", "/magazine/", [
        ("전체 글", "/magazine/"),
        ("마사지 비교 가이드", "/magazine/swedish-vs-thai/"),
        ("처음 이용 가이드", "/magazine/first-time-guide/"),
        ("수면과 마사지", "/magazine/sleep-and-massage/"),
        ("운동 후 회복", "/magazine/post-workout-timing/"),
        ("어깨·목 결림 관리", "/magazine/neck-shoulder-care/"),
        ("부모님 선물 가이드", "/magazine/parents-gift/"),
    ]),
    ("후기", "/reviews/", [
        ("전체 후기", "/reviews/"),
        ("지역별 후기", "/reviews/#area"),
        ("역세권 후기", "/reviews/#station"),
        ("후기 작성 안내", "/reviews/#write"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("제휴·기업 문의", "/support/#biz"),
        ("개인정보처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
