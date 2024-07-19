# - PythonClusteringSever -
*그래프이론을 이용한 경로 추출 서버 for Hiking-Planner*

가장 많이 이용한 등산경로를 추출함.

## ❓그래프 이론이란? 
- 노드, 엣지로 이루어진 그래프를 이용해 자연이나 사회현상, 네트워크 구조를 점과 선으로 단순화해 이해하고 분석하는 이론

### 가중치 그래프
- 엣지가 가중치(weight)를 가지는 그래프. 가중치 값은 문제에 따라 노드 간의 거리 중요도 등 문제의 목적에 따라 달라질 수 있음.

### 등산경로를 나타내기 위한 그래프 활용 방식
- 노드 : 수집된 위도, 경도 값 (lat,lon)
- 엣지 : 이용자의 이동 경로
- 가중치 : 각 경로를 지나간 빈도 수 

## 📌코드 설명

1. 백엔드 서버에서 파이썬 서버로 **POST /get_frequent_path/{mt_id}** API를 호출한다. 각 산의 유저등산정보를 리스트로 request body에 담아 전송한다.

![image](https://github.com/Hiking-Planner/PythonClusteringSever/assets/56792033/9800e903-b22e-4ed2-b93a-8093eb16d252)


```
// Request body
[
  {
    "userid": "string",
    "locations": [
      {
        "latitude": 0,
        "longitude": 0,
        "timestamp": 0
      }
    ]
  }
]
```
2. 등산 기록으로 *NetworkX 라이브러리* 활용하여 *방향성 있는 가중치 그래프* 생성 **create_graph()**

    ![image](https://github.com/Hiking-Planner/PythonClusteringSever/assets/56792033/512b4ddf-2fea-47f5-9a2b-119002afb3a3)

3. 가장 많이 나타난 등산 시작 지점 구하기 **find_start_point()**

4. 시작 지점 노드부터 차례로 이웃하는 노드간의 가중치를 비교하여 가중치가 가장 큰 노드를 *결과 집합에 추가*
   -> 더이상 비교할 이웃노드가 없을 때 까지 (지나온 노드 제외) 비교 **most_frequent_path(G,start_point)**
  ![image](https://github.com/Hiking-Planner/PythonClusteringSever/assets/56792033/10a2f488-2b8f-488f-9b55-953049258db6)


6. 결과 집합과 시작 지점 등 도출한 등산로 정보를 백엔드 서버로 반환
```
{
  "update_time": "2024-06-20T09:25:42.548Z",
  "mountain_id": 0,
  "new_path": [
    "string"
  ],
  "start_point": [
    "string"
  ],
  "end_point": [
    "string"
  ]
}
```
