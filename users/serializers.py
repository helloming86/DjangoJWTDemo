from django.contrib.auth.models import User
from .models import Profile
from rest_framework import serializers


# 自定义序列化程序
class ProfileSerializer(serializers.ModelSerializer):
    # 从表附加主表信息
    # 创建新字段，是定为serializers.CharField，并且使用source属性关联字段
    # 格式：CharField(source='<本model中的外键>.<外键指向的model的相应属性>')
    uid = serializers.CharField(source='user.id')
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Profile
        fields = ['uid', 'username', 'mobile', 'created']


class UserSerializer(serializers.ModelSerializer):
    # 主表附加从表信息
    # # 反向取字段，通过related_name，进行serializer嵌套
    # 注意这里的变量名user_profile必须与Profile模型设置的related_name一致
    # 但是实现的效果跟想要的略有差别
    user_profile = ProfileSerializer(read_only=True)
    token = serializers.CharField(label='token', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'user_profile']
