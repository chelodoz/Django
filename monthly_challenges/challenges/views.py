from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Wal for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Wal for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Wal for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Wal for at least 20 minutes every day!",
    "december": None
}


def index(request):

    list_items = ""
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

    return render(request,"challenges/index.html",{
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
