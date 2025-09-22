from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SecuritySetting
from .forms import SecuritySettingForm
from .forms import SecurityCheckForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import SecurityQuestion
from .forms import SecurityQuestionForm


@login_required
def update_security_settings(request):
    try:
        settings = request.user.securitysetting
    except SecuritySetting.DoesNotExist:
        settings = None

    if request.method == 'POST':
        form = SecuritySettingForm(request.POST, instance=settings)
        if form.is_valid():
            security_setting = form.save(commit=False)
            security_setting.user = request.user
            security_setting.save()
            return redirect('settingsapp.update_security')
    else:
        form = SecuritySettingForm(instance=settings)

    return render(request, 'settingsapp/update_security.html', {
        'form': form,
        'template_data': {'title': 'Security Settings'}
    })

@login_required
def index(request):
    return render(request, 'settingsapp/index.html')

def forgot_password(request):
    if request.method == 'POST':
        form = SecurityCheckForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            answer = form.cleaned_data['answer']
            new_password = form.cleaned_data['new_password']

            try:
                user = User.objects.get(username=username)
                security = SecuritySetting.objects.get(user=user)

                if security.answer == answer:
                    user.set_password(new_password)
                    user.save()
                    messages.success(request, "Password successfully reset! You can now log in.")
                    return redirect('login')
                else:
                    messages.error(request, "Security answer is incorrect.")
            except (User.DoesNotExist, SecuritySetting.DoesNotExist):
                messages.error(request, "User or security settings not found.")
    else:
        form = SecurityCheckForm()

    return render(request, 'settingsapp/forgot_password.html', {'form': form})

@login_required
def set_security(request):
    try:
        security = SecurityQuestion.objects.get(user=request.user)
    except SecurityQuestion.DoesNotExist:
        security = None

    if request.method == "POST":
        form = SecurityQuestionForm(request.POST, instance=security)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("settingsapp:set_security")  # reload page after save
    else:
        form = SecurityQuestionForm(instance=security)

    return render(request, "settingsapp/set_security.html", {"form": form})
