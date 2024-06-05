import networkx as nx


def create_graph(hiking_data):
    # 그래프 생성
    G = nx.DiGraph()  # 방향성이 존재하는 그래프

    # 노드 및 엣지 추가
    for record in hiking_data:
        locations = record.locations
        for i in range(len(locations) - 1):
            start = (locations[i].latitude, locations[i].longitude)
            end = (locations[i + 1].latitude, locations[i + 1].longitude)
            # 존재하는 엣지라면 가중치 추가
            if G.has_edge(start, end):
                G[start][end]['weight'] += 1
            # 존재하지 않는 엣지라면 생성
            else:
                G.add_edge(start, end, weight=1)
    return G
