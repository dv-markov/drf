import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


# # стандартный способ описания сериализатора (через ModelSerializer)
# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id')


# способ задания всех свойств сериализатора вручную (через Serializer)
class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    # чтобы сериализатор не требовал введения определенных полей в методе POST, их нужно задавать как readonly
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    # идентификатор категории в сериализаторе записывается как целое значение
    cat_id = serializers.IntegerField()
#
#
# # тестовый класс, локальные свойства модели и имена переменных в сериализаторе должны совпадать
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#
# # простой способ описания сериализатора (через Serializer)
# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#
# тестовые функции кодирования и декодирования
# def encode():
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
#     # при кодировании через сериализатор передается просто сама модель
#     model_sr = WomenSerializer(model)
#     # мета-класс сериализатора преобразовывает свойства модели в словарь data
#     print(model_sr.data, type(model_sr), sep='\n')
#     # преобразование словаря в JSON-строку
#     json = JSONRenderer().render(model_sr.data)
#     print(json, type(json), sep='\n')
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"ContentL Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     # чтобы сериализатор декодировал данные из словаря в объект сериализации,
#     # нужно использовать именованный параметр data
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     # после отработки валидатора в коллекции сериализатора появляется коллекция validated_data
#     print(serializer.validated_data)





