from django.shortcuts import render
from django.views import View

from aircraft.models import Aircraft, AircraftEquipment


class AircraftList(View):
    def get(self, request):
        aircrafts = Aircraft.objects.all()

        return render(request, 'aircraft.html', {'aircrafts': aircrafts})


class AircraftView(View):
    def get(self, request, tailnum):

        try:
            aircraft = Aircraft.objects.get(tailnum=tailnum)
        except Aircraft.DoesNotExist:
            return render(request, '404.html')

        all_aircraft = Aircraft.objects.all()

        equipment = AircraftEquipment.objects.filter(aircraft=aircraft).order_by(
            'category__category_order', 'equipment_order')

        return render(request, 'aircraft-detail.html', {
            'aircraft': aircraft,
            'equipment': equipment,
            'aircraft_menu': all_aircraft,
        })