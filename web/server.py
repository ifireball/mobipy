from os import environ
from sanic import Sanic
from sanic.response import text

app = Sanic("My Hello, world app")

@app.get("/")
async def hello_world(request):
    return text("Hello, world. From Sanic")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(environ.get("PORT") or "8000"))
