from xtapi import MainApp

app = MainApp()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    app.run(name='first_api:app', reload=True)
