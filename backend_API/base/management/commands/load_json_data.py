import json
from django.core.management.base import BaseCommand
from base.models import Handle

class Command(BaseCommand):
    help = 'C:/Development/InstagramAPI/backend_API/sample_data.json'
    
    def add_arguments(self,parser):
        parser.add_argument('file_path', type=str, help='C:/Development/InstagramAPI/backend_API/sample_data.json')

    def handle(self,*args,**kwargs):
        file_path = kwargs['file_path']
        print(f"Received file path: {file_path}") 

        with open(file_path,'r') as f:
            data = json.load(f)

        for item in data:
            Handle.objects.create(
                rank = item['rank'],
                username = item['username'],
                channel_info = item['channel_info'],
                category_id = item['category_id'],
                posts = item['posts'],
                followers = item['followers'],
                avg_likes = item['avg_likes'],
                profile_pic = item['profile_pic']
        )
            
        self.stdout.write(self.style.SUCCESS('Sample Data Imported Successfully!'))




