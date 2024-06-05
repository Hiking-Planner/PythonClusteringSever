# 가장 많이 이용한 경로 찾는 함수
def most_frequent_path(graph, start_node):
    path = [start_node]
    current_node = start_node
    visited = set()  # 이미 지나온 노드는 제외하기 위한 visited 집합 선언

    while True:
        visited.add(current_node)  # 현재 노드를 visited 에 추가
        neighbors = list(graph[current_node].items())  # 이웃하는 노드 리스트
        neighbors = [n for n in neighbors if n[0] not in visited]  # visited 고려하여 이미 지나온 노드는 제외

        # neighbors = [(neighbor1, edge_data1), (neighbor2, edge_data2), ...]
        # neighbor(이웃 노드), edge_data(엣지에 대한 추가정보(weight)가 담긴 딕셔너리)
        if not neighbors:
            break
        next_node = max(neighbors, key=lambda x: x[1]['weight'])[0]  # 엣지 가중치가 가장 큰 이웃노드 구하기
        path.append(next_node)
        current_node = next_node
    return path
