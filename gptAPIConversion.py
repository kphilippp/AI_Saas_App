from typing import Union

from fastapi import FastAPI

app = FastAPI()

# there are two paths that recieves requests "/" and "/items/{item_id}"
# both paths do GET HTTP Method 
# Things to note is the /items/ endpoint can be int with "item_id" or a string with "q"

@app.get("/{msg}")
def read_root(msg: str):
    return msg


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}