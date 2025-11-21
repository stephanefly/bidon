
from apps.main.forms import ConfigurationForm
from apps.main.models import UtilitaireConfiguration

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def configuration_view(request):
    config, created = UtilitaireConfiguration.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ConfigurationForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            return redirect('configuration')
    else:
        form = ConfigurationForm(instance=config)

    return render(request, 'trunks/main/configuration.html', {'form': form})
