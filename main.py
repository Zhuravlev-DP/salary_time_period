import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.salary.app:app", reload=True)
