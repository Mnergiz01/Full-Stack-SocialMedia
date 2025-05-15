from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SignupForm

@api_view(['GET'])  # Yalnızca GET isteği kabul edilir
def me(request):
    return JsonResponse({
        'id':request.user.id,
        'email':request.user.email,
        'name':request.user.name,
    })
@api_view(['POST'])  # Yalnızca POST isteği kabul edilir
@authentication_classes([])  # Gerekirse burada authentication sınıfını belirtebilirsiniz
@permission_classes([])  # Gerekirse burada izin sınıfını belirtebilirsiniz
def signup(request):
    data = request.data  # request.data kullanmalısınız, dict gibi davranır
    message = 'success'
    
    form = SignupForm({
        'email': data.get('email'),  # data.get kullanmalısınız, köşeli parantez değil
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2')
    })
    
    if form.is_valid():
        form.save()  # Formu kaydedin
    else:
        message = 'error'
        return JsonResponse({'message': message, 'errors': form.errors}, status=400)  # Hataları döndür

    return JsonResponse({'message': message})
