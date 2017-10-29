from django.shortcuts import render
from django.views import View

from faq.models import Section


class MembershipView(View):
    def get(self, request):
        sections = Section.objects.all()

        return render(request, 'membership.html', {'sections': sections})