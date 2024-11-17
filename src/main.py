from datetime import datetime
from typing import List

from path_module.cal_dist import cal_dist
from path_module.create_graph import create_graph
from path_module.find_start_point import find_start_point
from path_module.most_frequent_path import most_frequent_path
from path_module.preproc_location import preproc_location

from fastapi import FastAPI
from pydantic import BaseModel


class Location(BaseModel):
    latitude: float
    longitude: float
    timestamp: int


class HikingRecord(BaseModel):
    userid: str
    locations: List[Location]


class Result(BaseModel):
    update_time: datetime
    mountain_id: int
    new_path: list
    start_point: tuple
    end_point : tuple
    total_length : float
    up_time : int


app = FastAPI()


@app.post("/get_frequent_path/{mtid}", response_model=Result)
async def get_frequent_path(mtid: int, hiking_records: List[HikingRecord]):
    data = preproc_location(hiking_records)

    G = create_graph(data)

    start_point = find_start_point(data)
    result_path = most_frequent_path(G, start_point)
    end_point = (result_path[-1][0],result_path[-1][1])
    dist = cal_dist(result_path) 
    up_time = dist / 38.3
    response = Result(
        update_time= datetime.now(),
        mountain_id= mtid,
        new_path= result_path,
        start_point= start_point,
        end_point = end_point,
        total_length = round(dist / 1000, 2),
        up_time = round(up_time)
    )

    return response
