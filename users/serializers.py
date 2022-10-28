from dataclasses import field
import imp
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= "__all__"

#해싱 유저는 set패스워드 해줘야해서 구체적 명시 해줘야한다
    def create(self, validated_data):
        user=super().create(validated_data) #이건 db에 전달 됐다
        # print(validated_data) # {'password': '123', 'email': '123123123@123123123.com'}
        password = user.password # 패스워드를 꺼낸다
        # print(user.password) #해싱 전 후 찍어본다
        user.set_password(password) #여긴 아직 전달안돼서 db에서는 해싱 안된게 저장됐을거다 아직
        # print(user.password)
        user.save()
        return user
    def update(self, validated_data): #업데이트도 똑같네 근데 이걸 어떻게 입력을 받지? 퓨어에서는 html에서 받았는데
        user= super().update(validated_data)
        password=user.password
        user.set_password(password)
        user.save()
        return user
        