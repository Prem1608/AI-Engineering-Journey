from fastapi import FastAPI
from Day01.two_sum import twoSum
from pydantic import BaseModel

app = FastAPI()

class TwoSumRequest(BaseModel):
    nums : list[int]
    target : int

@app.get("/")
def read_root():
    return {"message": "MacBook M2 is ready for AI", "day": 1}

@app.post("/solve/two-sum")
def solve_two_sum(request: TwoSumRequest):
    nums = request.nums
    target = request.target
    res = twoSum(nums,target)
    return {"solution":res,"original_data":nums}