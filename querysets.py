
def home(request):
    """
    shert bir az anlashilmazdir qeyd edim ki
    """
    eid = Employee.objects.filter(access=True).values_list('id')
    Person.objects.filter(id__in=eid).values('name', 'age')
