from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, aauthenticate
from django.http import HttpResponse
from django.urls import reverse

#função para cadastrar usuário
def signUp(request):
    User = get_user_model()
    if request.user.is_authenticated:
        return render(request=request, template_name='account/home.html') #trocar depois
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        nascimento = request.POST.get('nascimento', '')
        redesocial = request.POST.get('redesocial', '')

        #criando o objeto do usuário com variáveis de instância
        user = User.objects.create_user(username=username, email=email,
                                        password=password, dob=dob, gender=gender,
                                        nascimento=nascimento, redesocial=redesocial)
        
        #autentica as informações do usuário e cria o perfil
        user = aauthenticate(username=username, password=password)

        #redireciona o usuário para a página principal
        if user is not None:
            login(request, user)
        return redirect('/')
    
    #se recebermos uma requisição do tipo get
    return render(request=request, template_name='account/signUp.html', context={})


#função para fazer login
def signIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) #verifica se o usuário possui cadastro
        if user is not None:
            login(request, user)
            request.session['username'] = username
            request.session.save()
            return redirect('/')
        else:
            return HttpResponse('fail')
    
    #se recebermos uma requisição do tipo get
    return render(request=request, template_name='account/signIn.html', context={})


def home(request):
    return render(request=request, template_name='account/home.html', context={})

def signOut(request):
    if request.user.is_authenticated:
        logout(request) #Limpa a sessão do usuário
        return HttpResponse('<strong>Logout realizado com sucesso. <a href="/sigIn"> Ir para a página de Login</a></strong>')
    else:
        return HttpResponse('<strong> Solicitação Inválida!</strong>')


def redirect_me(request):
    return redirect(reverse('home'))


