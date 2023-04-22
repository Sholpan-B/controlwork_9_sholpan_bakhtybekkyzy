from django.http import JsonResponse


def add(request, *args, **kwargs):
    favorite = request.GET.get('fav')
    request.user.favorites.add(favorite)
    response_data = {
        'answer': 'success'
    }
    response = JsonResponse(response_data)
    response.status_code = 200
    return response


def remove(request, *args, **kwargs):
    favorite = request.GET.get('a')
    request.user.favorites.remove(favorite)
    response_data = {
        'answer': 'success'
    }
    response = JsonResponse(response_data)
    response.status_code = 200
    return response
