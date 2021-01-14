"""main."""
from xtapi.main import MainApp

app = MainApp()
# app.mount('/static', 'static', name='static')

# app.register_routers(ROUTER_CONFIG)

if __name__ == '__main__':
    app.run(name='main:app', reload=True)
