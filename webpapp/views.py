from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse

from PIL import Image

# Create your views here.

def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        myname = myfile.name

        temp_name = f'tmp/{myname}'
        with open(temp_name, 'wb') as f:
            f.write(myfile.read())	

        new_name = myfile.name.replace('.webp','.jpg')     
        new_name = f'tmp/{new_name}'
        im = Image.open(temp_name).convert("RGB")
        im.save(new_name)

        fs = FileSystemStorage()
        response = FileResponse(fs.open(new_name, 'rb'), content_type='image/jpeg')
        response['Content-Disposition'] = 'attachment'
             
        return response             

    return render(request, 'webpapp/index.html', {})