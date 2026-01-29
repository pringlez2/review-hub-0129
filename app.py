from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

# Dummy Data Configuration
REVIEWS = [
    {
        "id": 1,
        "title": "다낭·호이안, 바나힐/스톤마사지 90분, 3박5일, 미케비치 4성급 호텔",
        "author": "이*원",
        "author_avatar": "https://picsum.photos/seed/avatar1/100/100",
        "date": "2026.1.23 금",
        "departure_date": "2026.1.18",
        "price": "549,000원",
        "rating": 4.3,
        "rating_detail": {"accommodation": 5, "food": 4, "guide": 3},
        "tags": ["30대", "형제/자매", "휴가"],
        "images": [
            "https://images.unsplash.com/photo-1528127269322-539801943592?w=800&auto=format&fit=crop", 
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1557713013-16a8ed39556a?w=800&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1528128483300-85579883b83a?w=800&auto=format&fit=crop"
        ],
        "content_preview": "처음 패키지여행 갔다 왔는데 너무 좋았어요~ 가 있는 동안 날씨도 너무 좋아서 만족했습니다. 처음 패키지여행 갔다 왔는데...",
        "content_full": "패키지로 모르는분들과 다녔는데 처음엔 서먹서먹했지만 밥을 같이 먹다보니 친해지게되고 여행일정도 타이트하지 않으니 서로 서로 재미있게 다녀올수 있었습니다\n가이드님도 친절하고 화장실도 미리미리 챙기고 즐거운 여행이였습니다 또한 다낭성당갔을때는 갑자기 내린 폭우같은 소나기로 입구에서 돌아올수밖에 없었지만 그것역시 추억으로 간직될것같습니다",
        "likes": 5,
        "product_name": "다낭/호이안 5일 #특급호텔 #바나힐 #전신마사지",
        "product_city": "다낭",
        "product_type": "패키지",
        "product_duration": "3박 5일",
        "product_departure": "인천 출발",
        "product_image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800&auto=format&fit=crop"
    },
    {
        "id": 2,
        "title": "다낭·호이안, 바나힐/스톤마사지 90분, 3박5일, 미케비치 4성급 호텔",
        "author": "김*지",
        "author_avatar": "https://picsum.photos/seed/avatar2/100/100",
        "date": "2026.1.23 금",
        "departure_date": "2026.1.18",
        "price": "499,000원",
        "rating": 4.3,
        "rating_detail": {"accommodation": 4, "food": 5, "guide": 5},
        "tags": ["50대", "배우자", "관광"],
        "images": [
            "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1528127269322-539801943592?w=800&auto=format&fit=crop"
        ],
        "content_preview": "처음 패키지여행 갔다 왔는데 너무 좋았어요~ 가 있는 동안 날씨도 너무 좋아서 만족했습니다. 처음 패키지여행 갔다 왔는데...",
        "content_full": "두 번째 방문인데 역시나 좋았습니다. 부모님 모시고 가기 딱 좋은 코스였어요. 식사도 현지식과 한식이 적절히 섞여 있어서 부담 없었고, 리조트 시설도 훌륭했습니다. 특히 마사지가 정말 시원했어요!",
        "likes": 5,
        "product_name": "다낭/호이안 5일 #빈펄리조트 #호이안야경",
        "product_city": "다낭",
        "product_type": "패키지",
        "product_duration": "3박 5일",
        "product_departure": "부산 출발",
        "product_image": "https://images.unsplash.com/photo-1557713013-16a8ed39556a?w=800&auto=format&fit=crop"
    },
    {
        "id": 3,
        "title": "다낭·호이안, 바나힐/스톤마사지 90분, 3박5일, 미케비치 4성급 호텔",
        "author": "박*수",
        "author_avatar": "https://picsum.photos/seed/avatar3/100/100",
        "date": "2026.1.23 금",
        "departure_date": "2026.1.18",
        "price": "459,000원",
        "rating": 4.3,
        "tags": ["30대", "형제/자매", "휴가"],
        "rating_detail": {"accommodation": 5, "food": 3, "guide": 4},
        "images": [], 
        "content_preview": "처음 패키지여행 갔다 왔는데 너무 좋았어요~ 가 있는 동안 날씨도 너무 좋아서 만족했습니다. 처음 패키지여행 갔다 왔는데...",
        "content_full": "가격 대비 정말 알찬 여행이었습니다. 가이드님이 설명을 너무 재미있게 해주셔서 이동하는 동안 지루할 틈이 없었어요. 쇼핑센터 방문도 강요 없어서 편안했습니다.",
        "likes": 5,
        "product_name": "[마감임박] 다낭 5일 #핵심관광 #가성비",
        "product_city": "다낭",
        "product_type": "패키지",
        "product_duration": "3박 5일",
        "product_departure": "인천 출발",
        "product_image": "https://images.unsplash.com/photo-1528128483300-85579883b83a?w=800&auto=format&fit=crop"
    },
     {
        "id": 4,
        "title": "다낭·호이안, 바나힐/스톤마사지 90분, 3박5일, 미케비치 4성급 호텔",
        "author": "최*영",
        "author_avatar": "https://picsum.photos/seed/avatar4/100/100",
        "date": "2026.1.23 금",
        "departure_date": "2026.1.18",
        "price": "529,000원",
        "rating": 4.3,
        "rating_detail": {"accommodation": 4, "food": 4, "guide": 5},
        "tags": ["30대", "형제/자매", "휴가"],
        "images": [
             "https://images.unsplash.com/photo-1557713013-16a8ed39556a?w=800&auto=format&fit=crop",
             "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop",
             "https://images.unsplash.com/photo-1528127269322-539801943592?w=800&auto=format&fit=crop",
             "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800&auto=format&fit=crop",
             "https://images.unsplash.com/photo-1555400038-63f5ba517a47?w=800&auto=format&fit=crop" 
        ],
        "content_preview": "여동생이랑 패키지 여행 다녀왔어요. 숙소는 보통이었고 조식은 별로였네요. 베트남은 이동하는 동선이 짧아 버스타고 불편한건 없었습니다...",
        "content_full": "여동생이랑 패키지 여행 다녀왔어요. 숙소는 보통이었고 조식은 별로였네요. 베트남은 이동하는 동선이 짧아 버스타고 불편한건 없었습니다. 다만 날씨가 너무 더워서 조금 힘들었네요 ㅠㅠ 그래도 사진은 예쁘게 잘 나와서 만족합니다!",
        "likes": 5,
        "product_name": "다낭/호이안 5일 #4성급 #자유시간",
        "product_city": "다낭",
        "product_type": "패키지",
        "product_duration": "3박 5일",
        "product_departure": "대구 출발",
        "product_image": "https://images.unsplash.com/photo-1528128483300-85579883b83a?w=800&auto=format&fit=crop"
    },
    {
        "id": 5,
        "title": "다낭·호이안, 바나힐/스톤마사지 90분, 3박5일, 미케비치 4성급 호텔",
        "author": "박*미",
        "author_avatar": "https://picsum.photos/seed/avatar5/100/100",
        "date": "2026.1.22 목",
        "departure_date": "2026.1.17",
        "price": "620,000원",
        "rating": 5.0,
        "rating_detail": {"accommodation": 5, "food": 5, "guide": 5},
        "tags": ["20대", "친구", "식도락", "쇼핑"],
        "images": [
             "https://images.unsplash.com/photo-1528127269322-539801943592?w=800&auto=format&fit=crop",
             "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800&auto=format&fit=crop",
             "https://images.unsplash.com/photo-1557713013-16a8ed39556a?w=800&auto=format&fit=crop" 
        ],
        "content_preview": "친구들이랑 졸업여행으로 다녀왔는데 인생샷 백만장 건졌어요! 특히 호이안 야경이 너무 예뻤고, 콩카페 코코넛커피도 JMT! 가이드님이...",
        "content_full": "친구들이랑 졸업여행으로 다녀왔는데 인생샷 백만장 건졌어요! 특히 호이안 야경이 너무 예뻤고, 콩카페 코코넛커피도 JMT! 가이드님이 사진 스팟을 잘 아셔서 편하게 다녔습니다. 숙소 루프탑 수영장도 최고였어요.",
        "likes": 12,
        "product_name": "다낭/호이안 5일 #인생샷 #카페투어",
        "product_city": "다낭",
        "product_type": "패키지",
        "product_duration": "3박 5일",
        "product_departure": "인천 출발",
        "product_image": "https://images.unsplash.com/photo-1528127269322-539801943592?w=800&auto=format&fit=crop"
    },
    {
        "id": 6,
        "title": "다낭·호이안, 효도관광 3박5일, 5성급 호텔",
        "author": "강*호",
        "author_avatar": "https://picsum.photos/seed/avatar6/100/100",
        "date": "2026.1.21 수",
        "departure_date": "2026.1.16",
        "price": "750,000원",
        "rating": 5.0,
        "rating_detail": {"accommodation": 5, "food": 4, "guide": 5},
        "tags": ["50대", "부모", "효도 관광"],
        "images": [
             "https://images.unsplash.com/photo-1528128483300-85579883b83a?w=800&auto=format&fit=crop"
        ],
        "content_preview": "부모님 환갑 기념으로 보내드렸는데 두 분 모두 너무 만족해하셨습니다. 음식이 입에 맞으실까 걱정했는데 한식당도 가고 현지식도...",
        "content_full": "부모님 환갑 기념으로 보내드렸는데 두 분 모두 너무 만족해하셨습니다. 음식이 입에 맞으실까 걱정했는데 한식당도 가고 현지식도 거부감 없는 곳으로 데려가 주셔서 잘 드셨다고 하네요. 가이드님이 세심하게 챙겨주셔서 감사했습니다.",
        "likes": 8,
        "product_name": "다낭 효도관광 5일 #노팁 #노옵션",
        "product_city": "다낭",
        "product_type": "패키지",
        "product_duration": "3박 5일",
        "product_departure": "인천 출발",
        "product_image": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800&auto=format&fit=crop"
    },
    {
        "id": 7,
        "title": "다낭·호이안, 바나힐/스톤마사지 90분, 3박5일",
        "author": "정*우",
        "author_avatar": "https://picsum.photos/seed/avatar7/100/100",
        "date": "2026.1.20 화",
        "departure_date": "2026.1.15",
        "price": "430,000원",
        "rating": 4.0,
        "rating_detail": {"accommodation": 3, "food": 4, "guide": 4},
        "tags": ["30대", "연인(커플)", "관광"],
        "images": [
             "https://images.unsplash.com/photo-1528127269322-539801943592?w=800&auto=format&fit=crop",
             "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop",
             "https://images.unsplash.com/photo-1557713013-16a8ed39556a?w=800&auto=format&fit=crop",
             "https://images.unsplash.com/photo-1528128483300-85579883b83a?w=800&auto=format&fit=crop" 
        ],
        "content_preview": "커플 여행으로 다녀왔습니다. 바나힐 투어는 사람이 좀 많아서 힘들었지만 케이블카 경치는 끝내줬어요. 마사지는 쏘쏘였지만...",
        "content_full": "커플 여행으로 다녀왔습니다. 바나힐 투어는 사람이 좀 많아서 힘들었지만 케이블카 경치는 끝내줬어요. 마사지는 쏘쏘였지만 전반적으로 가성비 좋은 여행이었습니다. 미케비치 근처 호텔 위치가 좋아서 저녁에 산책하기 좋았어요.",
        "likes": 3,
        "product_name": "다낭 실속 5일 #자유일정포함",
        "product_city": "다낭",
        "product_type": "에어텔",
        "product_duration": "3박 5일",
        "product_departure": "부산 출발",
        "product_image": "https://images.unsplash.com/photo-1557713013-16a8ed39556a?w=800&auto=format&fit=crop"
    },
    {
        "id": 8,
        "title": "다낭·호이안 가족여행 4박6일",
        "author": "최*수",
        "author_avatar": "https://picsum.photos/seed/avatar8/100/100",
        "date": "2026.1.19 월",
        "departure_date": "2026.1.13",
        "price": "680,000원",
        "rating": 4.8,
        "rating_detail": {"accommodation": 5, "food": 5, "guide": 5},
        "tags": ["40대", "자녀", "휴양/휴가", "레저/스포츠"],
        "images": [
             "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop",
             "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800&auto=format&fit=crop"
        ],
        "content_preview": "아이들이 물놀이를 너무 좋아해서 리조트 위주로 알아봤는데 탁월한 선택이었습니다. 키즈클럽도 잘 되어있고 직원들도 아이들에게...",
        "content_full": "아이들이 물놀이를 너무 좋아해서 리조트 위주로 알아봤는데 탁월한 선택이었습니다. 키즈클럽도 잘 되어있고 직원들도 아이들에게 친절해서 편하게 쉬다 왔습니다. 호이안 바구니배 체험도 아이들이 재미있어했어요.",
        "likes": 10,
        "product_name": "다낭/호이안 6일 #풀빌라 #가족여행",
        "product_city": "다낭",
        "product_type": "패키지",
        "product_duration": "4박 6일",
        "product_departure": "인천 출발",
        "product_image": "https://images.unsplash.com/photo-1528128483300-85579883b83a?w=800&auto=format&fit=crop"
    },
    {
        "id": 9,
        "title": "다낭 3박5일, 나홀로 힐링 여행",
        "author": "윤*서",
        "author_avatar": "https://picsum.photos/seed/avatar9/100/100",
        "date": "2026.1.18 일",
        "departure_date": "2026.1.13",
        "price": "550,000원",
        "rating": 4.5,
        "rating_detail": {"accommodation": 4, "food": 4, "guide": 5},
        "tags": ["30대", "혼자", "휴양/휴가"],
        "images": [],
        "content_preview": "혼자 가는 패키지라 걱정했는데 가이드님이 잘 챙겨주셔서 외롭지 않았습니다. 자유시간이 넉넉해서 카페 투어도 하고 마사지도 매일...",
        "content_full": "혼자 가는 패키지라 걱정했는데 가이드님이 잘 챙겨주셔서 외롭지 않았습니다. 자유시간이 넉넉해서 카페 투어도 하고 마사지도 매일 받았네요. 재충전 제대로 하고 갑니다. 다음엔 부모님 모시고 오고 싶네요.",
        "likes": 7,
        "product_name": "다낭 힐링 5일 #1인예약가능",
        "product_city": "다낭",
        "product_type": "패키지",
        "product_duration": "3박 5일",
        "product_departure": "청주 출발",
        "product_image": "https://images.unsplash.com/photo-1557713013-16a8ed39556a?w=800&auto=format&fit=crop"
    },
    {
        "id": 10,
        "title": "다낭·호이안 쇼핑&관광 3박5일",
        "author": "임*재",
        "author_avatar": "https://picsum.photos/seed/avatar10/100/100",
        "date": "2026.1.17 토",
        "departure_date": "2026.1.12",
        "price": "480,000원",
        "rating": 4.7,
        "rating_detail": {"accommodation": 5, "food": 4, "guide": 4},
        "tags": ["40대", "배우자", "쇼핑", "관광"],
        "images": [
             "https://images.unsplash.com/photo-1528127269322-539801943592?w=800&auto=format&fit=crop",
             "https://images.unsplash.com/photo-1557713013-16a8ed39556a?w=800&auto=format&fit=crop",
             "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800&auto=format&fit=crop"
        ],
        "content_preview": "와이프랑 다녀왔는데 롯데마트랑 한시장 쇼핑하기 너무 좋았어요. 과일도 실컷 먹고 마사지도 받고 힐링했습니다. 숙소 컨디션도...",
        "content_full": "와이프랑 다녀왔는데 롯데마트랑 한시장 쇼핑하기 너무 좋았어요. 과일도 실컷 먹고 마사지도 받고 힐링했습니다. 숙소 컨디션도 깔끔하고 조식도 맛있었습니다. 가성비 최고!",
        "likes": 6,
        "product_name": "다낭 쇼핑 5일 #쇼핑센터방문 #특가",
        "product_city": "다낭",
        "product_type": "패키지",
        "product_duration": "3박 5일",
        "product_departure": "인천 출발",
        "product_image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop"
    }
]

@app.route('/')
def index():
    companion = request.args.get('companion')
    style = request.args.get('style')
    age = request.args.get('age')
    travelers = request.args.get('travelers')
    sort_option = request.args.get('sort', '추천 많은 순')

    filtered_reviews = list(REVIEWS)

    if companion:
        filtered_reviews = [r for r in filtered_reviews if any(t in companion or companion in t for t in r['tags'])]
    if style:
         filtered_reviews = [r for r in filtered_reviews if any(t in style or style in t for t in r['tags'])]
    if age:
         filtered_reviews = [r for r in filtered_reviews if any(t in age or age in t for t in r['tags'])]
    
    if sort_option == '최근 등록 순':
        filtered_reviews.sort(key=lambda x: datetime.strptime(x['date'].split(' ')[0], '%Y.%m.%d'), reverse=True)
    else:
        filtered_reviews.sort(key=lambda x: x['likes'], reverse=True)

    return render_template('index.html', reviews=filtered_reviews, active_filters=request.args, current_sort=sort_option)

@app.route('/detail/<int:review_id>')
def detail(review_id):
    review = next((r for r in REVIEWS if r['id'] == review_id), None)
    if not review:
        return "Review not found", 404
    
    # Simple navigation logic: find index in REVIEWS
    review_index = next((i for i, r in enumerate(REVIEWS) if r['id'] == review_id), 0)
    prev_review = REVIEWS[review_index - 1] if review_index > 0 else None
    next_review = REVIEWS[review_index + 1] if review_index < len(REVIEWS) - 1 else None

    # Filter out current review from related reviews
    related_reviews = [r for r in REVIEWS if r['id'] != review_id]
    is_sold_out = random.choice([True, False])
    
    return render_template('detail.html', 
                         review=review, 
                         related_reviews=related_reviews, 
                         prev_review=prev_review, 
                         next_review=next_review,
                         is_sold_out=is_sold_out)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
