from django.shortcuts import render

# Create your views here.
def user_define_filters(request):
    d={'data':'HaI hoW Are YoU'}
    return render(request,'user_define_filters.html',d)
