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
        "brand": "브랜드명",
        "name": "제품명",
        "shade": "21호",
        "purchasedAt": "2026-10-01",
        "openedAt": "2026-10-03",
        "memo": ""
      }
    ]
  }
}
```

`brand`, `name`만 필수이고 나머지는 선택. 같은 소분류에 제품이 몇 개 있는지 보면 중복 구매를 막을 수 있다.
