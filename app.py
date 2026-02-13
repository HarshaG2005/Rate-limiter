from fastapi import FastAPI
app=FastAPI()
@app.get('/')
async def func():
    try:
        return True
    except Exception as e:
        return False