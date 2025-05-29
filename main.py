from fastapi import FastAPI, Request
#from fastapi.staticfiles import StaticFiles
import mysql.connector
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory='static')

@app.post('/data/{name}')
@app.get('/data/{name}')
async def get_data(name: str):

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="spark",
    database="solar_site" )
                
    cursor = mydb.cursor()
    cursor.execute(f"select * from {name}")
    ans = cursor.fetchall()    
    mydb.close()

    return ans

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})





if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
