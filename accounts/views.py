from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from main_app.models import User, Perfil, Carrera, Empleo
from django.views.generic import View, TemplateView
from accounts.forms import PerfilForm, UserForm
from django.contrib import messages


class RedirectLoginView(TemplateView):
    template_name = 'candidate_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Index"
        return context


class RegisterForm(TemplateView):
    template_name = 'register.html'

    def validate(self, request):
        """
        Valida que el formulario haya sido llenado correctamente
        :param request: La request recibida
        :return: Tupla cuyo primer valor es un booleano que indica si el formulario es valido y cuyo segundo valor
        contiene los datos ingresados al formulario
        """
        email = request.POST['email']
        username = request.POST['confirm-email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        rut = request.POST['rut']
        carrera = request.POST.get('carrera')
        empleo = request.POST.get('empleo')
        ano_ingreso = request.POST['ano-ingreso']
        ano_egreso = request.POST['ano-egreso']
        perfil_pro = request.POST['perfil-pro']
        cv = request.POST['cv']
        foto_perfil = request.POST['foto-perfil']
        egresado = request.POST.get('egresado', '') == 'on'
        spam = request.POST.get('spam', '') == 'on'
        eula = request.POST.get('eula', '') == 'on'

        warnings = False

        if first_name == "":
            messages.warning(request, 'Por favor, ingrese un nombre.')
            warnings = True
        if last_name == "":
            messages.warning(request, 'Por favor, ingrese un apellido.')
            warnings = True
        if rut == "":
            messages.warning(request, 'Por favor, ingrese un rut.')
            warnings = True
        if email == "":
            messages.warning(request, 'Por favor, ingrese un email.')
            warnings = True
        if email != username:
            messages.warning(request, 'Los correos no coinciden.')
            warnings = True
        if password == "":
            messages.warning(request, 'Por favor, ingrese una contraseña.')
            warnings = True
        if len(password) < 6:
            messages.warning(request, 'La contraseña debe tener al menos 6 caracteres.')
            warnings = True
        if password != confirm_password:
            messages.warning(request, 'Las contraseñas no coinciden.')
            warnings = True
        if carrera == None:
            messages.warning(request, 'Por favor, seleccione una carrera.')
            warnings = True
        if empleo == None:
            messages.warning(request, 'Por favor, seleccione el tipo de empleo que busca.')
            warnings = True
        if ano_ingreso == "":
            messages.warning(request, 'Por favor, indique su año de ingreso a la universidad.')
            warnings = True
        if ano_egreso == "":
            messages.warning(request, 'Por favor, indique el año esperado de su egreso.')
            warnings = True
        if perfil_pro == "":
            messages.warning(request, 'Por favor, escriba su perfil profesional.')
            warnings = True
        if cv == "":
            messages.warning(request, 'Por favor, agregue un Currículum Vitae.')
            warnings = True
        if foto_perfil == "":
            messages.warning(request, 'Por favor, agregue una foto de perfil.')
            warnings = True
        if not eula:
            messages.warning(request, 'Para continuar debe aceptar los Términos y Condiciones.')
            warnings = True
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Ya existe una cuenta con ese correo.')
            warnings = True
        if Perfil.objects.filter(rut=rut).exists():
            messages.warning(request, 'Ya existe una cuenta con ese rut')
            warnings = True

        datos = {
            'first_name': first_name,
            'last_name': last_name,
            'rut': rut,
            'email': email,
            'password': password,
            'carrera': carrera,
            'empleo': empleo,
            'ano_ingreso': ano_ingreso,
            'ano_egreso': ano_egreso,
            'perfil_pro': perfil_pro,
            'cv': cv,
            'foto_perfil': foto_perfil,
            'egresado': egresado,
            'spam': spam,
            'eula': eula
        }

        if warnings:
            return False, datos

        return True, datos

    def post(self, request, *args, **kwargs):
        valid, datos = self.validate(request)

        if valid:
            user = User(username=datos['email'], email=datos['email'], first_name=datos['first_name'],
                        last_name=datos['last_name'], password=datos['password'])
            user.save()
            carrera = Carrera.objects.get(plan=datos['carrera'])
            empleo = Empleo.objects.get(tipo=datos['empleo'])
            perfil = Perfil(usuario=user, rut=datos['rut'], carrera=carrera, empleo=empleo,
                            ano_ingreso=datos['ano_ingreso'], ano_egreso=datos['ano_egreso'],
                            perfil_pro=datos['perfil_pro'], cv=datos['cv'], foto_perfil=datos['foto_perfil'],
                            egresado=datos['egresado'], spam=datos['spam'], eula=datos['eula'])
            perfil.save()
            return redirect('profile')
        else:
            context = datos
            del context['password']
            context['carreras'] = Carrera.objects.all().order_by('plan').values_list('plan', flat=True)
            context['empleos'] = Empleo.objects.all().values_list('tipo', flat=True)
            return render(request, 'register.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carreras'] = Carrera.objects.all().order_by('plan').values_list('plan', flat=True)
        context['empleos'] = Empleo.objects.all().values_list('tipo', flat=True)
        return context
