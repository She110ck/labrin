from home import Salary

def home(render):
    salaries = Salary.objects.filter(retired=True).exclude(amount = 5300)
    return salaries
