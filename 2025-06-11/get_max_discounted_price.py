#유형별 문제 풀이 - 정렬
# 최대로 할인 적용하기

def get_max_discounted_price(prices, coupons):
    sorted_prices = sorted(prices, reverse=True)
    sorted_coupons = sorted(coupons, reverse=True)
    total = 0
    n = min(len(sorted_prices), len(sorted_coupons))

    for i in range(n):
        total += sorted_prices[i] * (100 - sorted_coupons[i]) // 100

    for i in range(n, len(sorted_prices)):
        total += sorted_prices[i]

    return total

print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))