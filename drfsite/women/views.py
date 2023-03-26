from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = (IsOwnerOrReadOnly, )
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )  # Аутентификация только по обычным токенам


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )


# 8, 9 - ViewSets
# ReadOnlyModelViewSet - только для чтения
# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     # переопределение метода queryset для получения определенного диапазона данных из БД
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#
#         if not pk:
#             return Women.objects.all()[:3]
#
#         return Women.objects.filter(pk=pk)
#
#     # 9 Роутеры
#     # формирование общего списка
#     # @action(methods=['get'], detail=False)
#     # # маршрут в роутере формируется используя имя метода
#     # def category(self, request):
#     #     cats = Category.objects.all()
#     #     return Response({'cats': [c.name for c in cats]})
#
#     # формирование детального представления (имени конкретной категории)
#     @action(methods=['get'], detail=True)
#     # маршрут в роутере формируется используя имя метода
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})

# Эквивалент ModelViewSet
# class WomenViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# 6 - ListAPIView
# generics.DestroyAPIView  # для удаления записей
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# # 7 - UpdateAPIView и RetrieveUpdateDestroyAPIView
# class WomenAPIUpdate(generics.UpdateAPIView):
#     # базовый класс UpdateAPIView отработает queryset и возвратит клиенту только 1 запись
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):  # только для одиночных запросов
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# 5 - Перенос работы с БД в сериализатор
# class WomenAPIView(APIView):
#     def get(self, request):
#         # список статей получаем как набор queryset
#         w = Women.objects.all()
#         # Response вызывает функцию JSON-рендерера,
#         # который преобразовывает словарь/словари data в байтовую json-строку
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()  # вызывает метод create сериализатора
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT is not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()  # вызовет метод update сериализатора, т.к. указаны instance и data
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE is not allowed"})
#
#         try:
#             w = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": f"Object with id {pk} does not exist"})
#
#         w.delete()
#         return Response({"post": "deleted post " + str(pk)})


# # Урок 4 - введение в сериализацию
# class WomenAPIView(APIView):
#     def get(self, request):
#         # список статей получаем как набор queryset
#         w = Women.objects.all()
#         # Response вызывает функцию JSON-рендерера,
#         # который преобразовывает словарь/словари data в байтовую json-строку
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         # сериализатор распаковывает входные данные - выполняет функцию JSON-парсера и проверку входных данных
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         post_new = Women.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id']
#         )
#         return Response({'post': WomenSerializer(post_new).data})


# Урок 3 - базовый класс APIView
# class WomenAPIView(APIView):
#     def get(self, request):
#         # самый простой вариант гет-запроса, возвращающий статические данные
#         # return Response({'title': 'Angeline Jolie'})
#
#         lst = Women.objects.all().values()
#         return Response({'posts': list(lst)})
#
#     def post(self, request):
#         # аналогично - примитивный пост-запрос
#         # return Response({'title': 'Jennifer Shrader Lawrence'})
#
#         post_new = Women.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id']
#         )
#         return Response({'post': model_to_dict(post_new)})
