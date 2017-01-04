from django.shortcuts import render_to_response, render, get_object_or_404

# Create your views here.
def kidney_care(request):
    a =1
    context = request
    return render_to_response('./kidney_care/index.html',
                              {'a': a},
                              context)