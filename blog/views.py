from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import PostForm

# Create your views here.



def home(request):
    post = BlogPost.objects.all()
    datos = {
        'post':post
    }
    return render(request, 'blog/Index.html',datos) 


#def form_post(request):
#    form= PostForm()
#    return render(request,'blog/form_noticia.html',{'form':form})

def form_post(request):
    datos = {
        'form':PostForm()
    }
    if(request.method == 'POST'):
        formulario = PostForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'
    return render(request,'blog/form_noticia.html',datos)



def form_mod_post(request, id):
    post = BlogPost.objects.get(title=id)
    posts = BlogPost.objects.all()
    datos = {
        'form':PostForm(instance=post),
        'post':posts
    }
    if(request.method=='POST'):
        formulario = PostForm(data=request.POST, instance=post)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificados correctamente'

    return render(request,'blog/form_mod_noticia.html',datos)


def form_del_post(request, id):
    post = BlogPost.objects.get(title=id)
    post.delete()

    return redirect(to='home')



class Cliente:
    def __init__(self, rut, nombre, edad):
        self.rut = rut      
        self.nombre = nombre
        self.edad = edad
        super().__init__()




def hom(request):
    post = BlogPost.objects.all()
    datos = {
        'post':post
    }
    return render(request,'blog/Index.html')

