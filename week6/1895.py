# r: 행, c: 열
r, c = map(int, input().split())

# 원본 이미지를 저장
image = []

# 입력 받기
for _ in range(r):
    image.append(list(map(int, input().split())))

t = int(input())

pixel_count = 0

# 필터링 후 중앙값을 저장할 리스트
filtered_image = []

# 3x3 필터를 적용하여 새로운 이미지 생성
for i in range(r - 2):
    for j in range(c - 2):
        # 정렬해서 중앙값 찾기
        sub_matrix = [image[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
        sub_matrix.sort()
        median_value = sub_matrix[4]

        # 중앙값이 임계값 이상인지 확인
        if median_value >= t:
            pixel_count += 1

        filtered_image.append(median_value)

print(pixel_count)
