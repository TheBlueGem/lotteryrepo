from django.http import HttpResponse
from lottery.forms import PostModelForm
from django.shortcuts import render

def index(request):
	return HttpResponse("Welcome to the lottery")	
	
def post(request):
	if request.method == 'GET':
		form = PostModelForm()		
	else:
		form = PostModelForm(request.POST)
	
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email adress']
			ticket_amount = form.cleaned_data['ticket_amount']
			post = m.Post.objects.create(name=name, email=email, ticket_amount=ticket_amount)
			post.save()
			return HttpResponseRedirect(reverse('registerConfirmed', kwargs={'post_id': post_id}))
	return render(request, 'post/register.html', {'form':form})
	
def registerConfirmed(request):
	return HttpResponse("You have been added to the contestant list!")
	
def winner(request, lottery_id):
	#Wegens tijdsgebrek is deze pagina in commentaar
	#De methode om de winnaars te berekenen zou er open
	#neer moeten komen dat de deelnemer die de meeste
	#lootjes gekocht heeft de grootste kans heeft om te
	#winnen. De grootte van de kans world bepaalt
	#door het aantal gekochte lootjes te delen door
	#het totale aantal lootjes dat verkocht is
	#en vervolgens een machtsvermenigvuldiging te doen
	return HttpResponse("Contestant ### has won the lottery!")
	
	
