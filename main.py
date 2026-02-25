from fastapi import FastAPI
from Day01.two_sum import twoSum
from pydantic import BaseModel
from Day01.prime import isPrime
from Day01.database import SessionLocal, CalculationHistory
from Day02.group_anagrams import groupAnagrams

app = FastAPI()

class TwoSumRequest(BaseModel):
    nums : list[int]
    target : int

class PrimeNumberRequest(BaseModel):
    number : int

class GroupAnagramsRequest(BaseModel):
    strs : list[str]

@app.get("/")
def read_root():
    return {"message": "MacBook M2 is ready for AI", "day": 2}

@app.post("/solve/two-sum", tags=["Day 01"])
def solve_two_sum(request: TwoSumRequest):
    nums = request.nums
    target = request.target
    res = twoSum(nums,target)
    return {"solution":res,"original_data":nums}

@app.post("/solve/prime", tags =["Day 01"])
def solve_prime(request : PrimeNumberRequest):
    num = request.number
    res = isPrime(num)
    if res:
        msg = f"{num} is a prime number"
    else:
        msg = f"{num} is not a prime number"
    
    db = SessionLocal()
    try:
        new_entry = CalculationHistory(
            type="Prime",
            input_data=str(num),
            result = str(res)
        )
        db.add(new_entry)
        db.commit()
    except Exception as e:
        print(f"Error in saving to DB {e}")
    finally:
        db.close()
    return {"solution":res,"original_date":num,"message":msg}

@app.post("/solve/groupAnagram", tags=["Day 02"])
def groupAnagram(request : GroupAnagramsRequest):
    strs = request.strs
    res = groupAnagrams(strs)
    db = SessionLocal()
    try:
        new_entry = CalculationHistory(
            type = "Group Anagrams",
            input_data = ", ".join(strs),
            result = str(res)
        )
        db.add(new_entry)
        db.commit()
    except Exception as e:
        print(f"Error in saving to DB {e}")
    finally:
        db.close()
    return {"solution":res,"original_data":strs,"message":"Successfully executed"}

@app.get("/history")
def get_history():
    db = SessionLocal()
    
    try:
        history = db.query(CalculationHistory).all()
        return {"history":history}
    finally:
        db.close()
    