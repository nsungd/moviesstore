from django.shortcuts import render
from django.db.models import Count
from cart.models import Item

def popularity_map(request):
    # Count how many times each movie was purchased in each region
    region_top_movies_qs = (
        Item.objects
        .values('order__region', 'movie__name')  # region via order, movie via foreign key
        .annotate(purchase_count=Count('id'))
        .order_by('order__region', '-purchase_count')
    )

    # Keep only the top movie for each region
    region_top_movies = {}
    for entry in region_top_movies_qs:
        region = entry['order__region']
        if region not in region_top_movies:
            region_top_movies[region] = {
                'movie': entry['movie__name'],
                'count': entry['purchase_count'],
            }

    return render(request, 'popularityMap/map.html', {'region_top_movies': region_top_movies})
