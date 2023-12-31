from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def get_total_combinations(request):
    number_of_dice = 2
    sides = 6
    total = sides ** number_of_dice
    return JsonResponse({"total": total})

@require_http_methods(["GET"])
def get_distribution(request):
    sides = 6
    distribution_list = []
    for i in range(1, sides + 1):
        for j in range(1, sides + 1):
            combination_map = {
                "Sum": i + j,
                "Die B": j,
                "Die A":i,
            }
            distribution_list.append(combination_map)
    return JsonResponse({"distribution": distribution_list})

@require_http_methods(["GET"])
def get_probability(request):
    sides = 6
    distribution = [0] * 11
    for i in range(1, sides + 1):
        for j in range(1, sides + 1):
            distribution[i + j - 2] += 1

    probability_map = {}
    for i in range(11):
        probability_map[i + 2] = f"{distribution[i]}/{36}"

    return JsonResponse({"probability": probability_map})