from os import makedirs

import uvicorn

if __name__ == "__main__":
    makedirs("app/static", exist_ok=True)
    uvicorn.run("app.api:app", host="127.0.0.1", port=8000, reload=True)
