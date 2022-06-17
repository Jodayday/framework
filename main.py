from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


# 문제 풀이 수 제출 화면
@app.get("/problem/")
def read_root():
    return {"messages": "문제풀기를 눌렀을경우"}

# 문제 풀이 수 제출


@app.get("/problem/{count}")
def read_root(count: int):
    return {"messages": "개수 선택후 시작을 누른경우"}


@app.get("/solution/")
def read_item():
    # 각 회원가입된 정보 필요
    return {"messages": "풀이 확인 눌렸을때"}


@app.get("/Additional/")
def read_item():
    return {"messages": "문제등록을 눌렸을때"}


@app.post("/Additional/")
def read_item():
    # 회원정보 필요
    return {"messages": "문제 등록"}


@app.get("/problem/")
def read_root():
    return {"messages": "문제확인"}


@app.get("/problem/{number}")
def read_root(number: int):
    return {"messages": "개별 문제 확인"}
