from fastapi import FastAPI
from Day01.two_sum import twoSum
from pydantic import BaseModel
from Day01.prime import isPrime

app = FastAPI()

class TwoSumRequest(BaseModel):
    nums : list[int]
    target : int

class PrimeNumberRequest(BaseModel):
    number : int


@app.get("/")
def read_root():
    return {"message": "MacBook M2 is ready for AI", "day": 1}

@app.post("/solve/two-sum")
def solve_two_sum(request: TwoSumRequest):
    nums = request.nums
    target = request.target
    res = twoSum(nums,target)
    return {"solution":res,"original_data":nums}

@app.post("/solve/prime")
def solve_prime(request : PrimeNumberRequest):
    num = request.number
    res = isPrime(num)
    if res:
        msg = {f"{num} is a prime number"}
    else:
        msg = {f"{num} is not a prime number"}
    return {"solution":res,"original_date":num,"message":msg}