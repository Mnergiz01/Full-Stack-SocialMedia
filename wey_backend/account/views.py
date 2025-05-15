from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .forms import SignupForm
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
import json

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def signup_view(request):
    try:
        # JSON verisini işle
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            data = request.data
            
        form = SignupForm(data)
        
        if form.is_valid():
            user = form.save(commit=False)
            
            # Email'i username olarak ayarla (gerekiyorsa)
            user.username = form.cleaned_data['email']
            user.save()
            
            # Başarılı yanıt
            return Response({
                'message': 'Kullanıcı başarıyla oluşturuldu',
                'email': user.email,
                'name': user.name
            }, status=status.HTTP_201_CREATED)
        else:
            # Form hatalarını işle
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [error for error in error_list]
            
            return Response({
                'message': 'Kayıt sırasında hata oluştu',
                'errors': errors
            }, status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        # Beklenmeyen hatalar
        return Response({
            'message': 'Sunucu hatası',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)