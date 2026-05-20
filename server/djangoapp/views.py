from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def get_dealers(request):
    dealers = [
        {"id": 1, "full_name": "Best Cars Kansas City", "city": "Kansas City", "state": "Kansas"},
        {"id": 2, "full_name": "Best Cars New York", "city": "New York", "state": "New York"},
        {"id": 3, "full_name": "Best Cars Dallas", "city": "Dallas", "state": "Texas"}
    ]
    return JsonResponse({"dealers": dealers})

def get_dealer_by_id(request, dealer_id):
    return JsonResponse({
        "id": dealer_id,
        "full_name": "Best Cars Kansas City",
        "city": "Kansas City",
        "state": "Kansas"
    })

def get_dealers_by_state(request, state):
    return JsonResponse({
        "dealers": [
            {"id": 1, "full_name": "Best Cars Kansas City", "city": "Kansas City", "state": state}
        ]
    })

def get_dealer_reviews(request, dealer_id):
    return JsonResponse({
        "reviews": [
            {
                "id": 101,
                "dealerId": dealer_id,
                "name": "Thinh",
                "review": "Fantastic services",
                "purchase": True,
                "sentiment": "positive"
            }
        ]
    })
