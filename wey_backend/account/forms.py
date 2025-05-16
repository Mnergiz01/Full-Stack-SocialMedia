from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # username alanını formdan tamamen kaldır
        if 'username' in self.fields:
            del self.fields['username']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # Email'i username olarak ayarla
        user.username = self.cleaned_data['email']  
        if commit:
            user.save()
        return user