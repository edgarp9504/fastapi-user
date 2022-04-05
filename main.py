import uvicorn
from app.app import app



## Run the app
if __name__ == '__main__':
    uvicorn.run(app)