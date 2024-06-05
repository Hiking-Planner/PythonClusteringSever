from collections import defaultdict
from math import isclose


# 시작 위치 찾는 함수
def find_start_point(hiking_data):
    # 시작 위치 수집
    first_locations = [(record.locations[0].latitude, record.locations[0].longitude) for record in
                       hiking_data]

    # location_counts에는 시작점의 위경도값과 시작점에 가까운 다른 시작점들의 갯수가 딕셔너리 형태로 저장된다.
    location_counts = defaultdict(int)

    # 가까운 시작 위치의 점이 location_counts 딕셔너리 키값에 존재하면 +1 해주고, 존재하지 않으면 위경도 값을 딕셔너리에 추가한다.
    for lat1, lon1 in first_locations:
        found = False
        for (lat2, lon2) in location_counts:
            if is_within_range(lat1, lon1, lat2, lon2):
                location_counts[(lat2, lon2)] += 1
                found = True
                break
        if not found:
            location_counts[(lat1, lon1)] += 1

    start_point = max(location_counts, key=location_counts.get)
    return start_point


# 시작 위치가 가까운 점들은 한 점으로 묶이도록 하는 함수
def is_within_range(lat1, lon1, lat2, lon2, tolerance=0.0005):
    return isclose(lat1, lat2, abs_tol=tolerance) and isclose(lon1, lon2, abs_tol=tolerance)
