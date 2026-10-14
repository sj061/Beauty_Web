# Beauty_Web

내가 가진 화장품(기초/색조)을 카테고리별로 관리하는 웹앱.

## 데이터

- `data/categories.json` — 카테고리 목록. `대분류(skincare/makeup) → 소분류 id → 한글 이름`
- `data/my-cosmetics.json` — 내가 가진 화장품. 카테고리와 같은 구조로, 소분류 id 아래에 제품 배열을 둔다.

제품 항목 형식:

```json
{
  "makeup": {
    "cushion": [
      {
        "name": "에스쁘아 프로테일러 쿠션 21호",
        "quantity": 1,
        "openedAt": "2026-10-03",
        "paoMonths": 12,
        "expiresAt": "2028-05-01",
        "price": 32000,
        "store": "올리브영"
      }
    ]
  }
}
```

| 필드 | 뜻 | 비고 |
| --- | --- | --- |
| `name` | 제품명 (브랜드·호수 포함) | 필수 |
| `quantity` | 개수 | 기본 `1` |
| `openedAt` | 개봉일 `YYYY-MM-DD` | 미개봉이면 `null` |
| `paoMonths` | 개봉 후 사용기한 (개월) | 용기의 `12M` 표시 → `12` |
| `expiresAt` | 유통기한 `YYYY-MM-DD` | |
| `price` | 가격 (원) | |
| `store` | 구매처 | |

`name`, `quantity` 외에는 모르면 `null`로 둔다.

같은 제품을 쟁여둔 경우, 개봉일·유통기한이 같은 것끼리는 한 항목으로 묶고 `quantity`에 개수를 적는다.
상태가 다르면 항목을 나눈다. 예) 쓰고 있는 1개 + 미개봉 2개:

```json
"lip-tint": [
  { "name": "롬앤 쥬시래스팅 틴트 06", "quantity": 1, "openedAt": "2026-09-01", "paoMonths": 12, "expiresAt": "2028-03-01", "price": 13000, "store": "올리브영" },
  { "name": "롬앤 쥬시래스팅 틴트 06", "quantity": 2, "openedAt": null, "paoMonths": 12, "expiresAt": "2028-06-01", "price": 13000, "store": "올리브영" }
]
```

제품별 총 개수는 같은 `name` 항목들의 `quantity` 합이다 (위 예시는 3개).
실제 사용 기한은 `openedAt + paoMonths`와 `expiresAt` 중 빠른 날짜다.
