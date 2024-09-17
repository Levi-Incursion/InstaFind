from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Handle,Category

class CategorySerializer(ModelSerializer):
    category_count = SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'

    def get_category_count(self,obj):
        return obj.handle_set.count()

class HandleSerializer(ModelSerializer):
    # Category = categorySerializer()
    category_name = SerializerMethodField()
    class Meta:
        model = Handle
        fields = ['rank','username','channel_info','category_name','posts','followers','avg_likes','profile_pic']

    def get_category_name(self,obj):
        return obj.category.name
