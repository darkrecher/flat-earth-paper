from typing import Optional

import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.extensions import SchemaExtension
from graphql import GraphQLError



from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World all is well for now"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
