from django.http import HttpResponse, JsonResponse


def home(request):
    print("Home page")
    list1 = ["Anmay","Avyaan","Achintya","Malhar"]
    return JsonResponse(list1,safe=False)



