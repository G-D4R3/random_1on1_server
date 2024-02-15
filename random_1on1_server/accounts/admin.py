from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin

from accounts.models import User, UserProfile


# Register your models here.
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserProfileInline(admin.StackedInline):
    model = UserProfile



class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ['id', 'email', 'name', 'is_active']
    ordering = ("-id",)
    search_fields = ('email', 'profile__name',)
    inlines = [UserProfileInline]

    fieldsets = (
        (None, {'fields': ('email', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'is_superuser', 'is_staff', 'is_active')}
         ),
    )

    def name(self, obj):
        return obj.profile.name

    def email(self, obj):
        return obj.email

admin.site.register(User, UserAdmin)