from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Advocate,Company

class CompanySerializer(ModelSerializer):
    employee_count = SerializerMethodField()
    class Meta:
        model = Company
        fields = '__all__'

    def get_employee_count(self,obj):
        return obj.advocate_set.count()

class AdvocateSerializer(ModelSerializer):
    # company = CompanySerializer()
    company_name = SerializerMethodField()
    class Meta:
        model = Advocate
        fields = ['username','bio','company_name']

    def get_company_name(self,obj):
        return obj.company.name
