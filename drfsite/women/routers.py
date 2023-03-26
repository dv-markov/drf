from rest_framework import routers


# создание собственного класса роутера (по идее должен прописываться в routers.py)
class MyCustomRouter(routers.SimpleRouter):
    routes = [
        # объекты класса Route, каждый определяет отдельный маршрут
        routers.Route(url=r'^{prefix}{trailing_slash}$',
                      mapping={'get': 'list'},
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}{trailing_slash}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'})
    ]