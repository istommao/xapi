"""template demo"""
from xtapi import MainApp, Templates, Request

app = MainApp()

templates = Templates(directory='html')


@app.get("/")
async def root(request: Request):
    return templates.render('index.html',  {"request": request})


if __name__ == '__main__':
    app.run(name='template_demo:app', reload=True)
