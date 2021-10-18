import uvicorn
from fastapi import FastAPI

products_sp = [{'item_id': 1,
       'name': ',банан',
       'description': 'спелый',
        'price': 39.0},
      {'item_id': 2,
       'name': 'яблоко',
       'description': 'сладкое',
       'price': 15.9}
      ]


app = FastAPI()
#  /docs


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/products")  # +
async def products():
    global products_sp
    return products_sp


@app.get("/api/products/{item_id}")  # +
async def products_2(item_id: int):
    global products_sp
    for i in products_sp:
        if i['item_id'] == item_id:
            return i
    else:
        return 'нет такого товара'



@app.post("/api/products/item_id/{item_id}")   # -
async def products_new(item_id: int, name: str, description: str, price: float):
    global products_sp
    flag = True
    for i in products_sp:
        if i["item_id"] == item_id:
            flag = False
            print(flag)
            break
    if not flag:
        return 'продукт с таким индексом существует'
    else:
        product = {'item_id': item_id,
                    'name': name,
                    'description': description,
                    'price': price}
        products_sp.append(product)
        return products_sp


@app.put("/api/products/edit/{item_id}")  # +
async def products_edit(item_id: int, name: str = None, description: str = None, price: float = None):
    global products_sp
    for i in products_sp:
        if i['item_id'] == item_id:
            i['name'] = name
            i['description'] = description
            i['price'] = price
            return products_sp



@app.delete("/api/products/delete/{item_id}")  # +
async def products_delete(item_id: int):
    global products_sp
    for i in products_sp:
        if i['item_id'] == item_id:
            products_sp.remove(i)
    return products_sp


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)