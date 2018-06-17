from django.shortcuts import render


from . import forms

def hello_world(request):
	return render(request, "home.html")

def suggestion_view(request):
	form = forms.SuggestionForm()
	if request.method == 'POST':
		form = forms.SuggestionForm(request.POST)
		if form.is_valid():
			print("Good form!")
	return render(request, 'suggestion_form.html', {'form':form})
