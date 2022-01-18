from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate


from apls.users.forms import LoginForm


def login_view(request):
	if request.user.is_authenticated:
		return redirect('/')

	form = LoginForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('/')
	return render(request, 'users/auth/login.html', {'form': form})