from decimal import Decimal
from typing import Any, Literal
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

from board.forms import ApplicationForm
from board.models import Category, Listing

class ListingList(ListView):
    model = Listing
    template_name = 'board/boards.html'
    context_object_name = 'listings'

    def get_queryset(self):
        base_query = Listing.objects.prefetch_related('images').select_related('user', 'category')
        search = self.request.GET.get("search")
        if search  and len(search) > 0 :
            base_query = base_query.filter(Q(title__icontains=search) | Q(description__icontains=search))
        try:
            from_price = Decimal(self.request.GET.get("price-from")) if self.request.GET.get("price-from") else None
            to_price = Decimal(self.request.GET.get("price-from")) if self.request.GET.get("price-to") else None
            condition: Literal["new", "user"] = self.request.GET.get("condition")
            category = int(self.request.GET.get("category")) if self.request.GET.get("category") else None
        except Exception as e:
            print(e)
            return []
        
        if from_price:
            base_query = base_query.filter(price__gte=from_price)
        if to_price:
            base_query = base_query.filter(price__lt=to_price)
        if condition:
            base_query = base_query.filter(condition=condition)
        if category:
            base_query = base_query.filter(category__id=category)
        return base_query.all()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        categories = Category.objects.all()
        kwargs.update({'categories': categories})
        return super().get_context_data(**kwargs)



def get_detail(request: HttpRequest, year: int, month: int, day: int, slug: str):
    listing = (Listing.objects
            .select_related('user', 'category')
            .prefetch_related('images')
            .prefetch_related('applications')
            .get(slug=slug, created_at__year=year, created_at__month=month, created_at__day=day))
    if request.method == "POST":
        if request.user.is_authenticated and listing.applications.filter(user=request.user).count() == 0:
            form = ApplicationForm(request.POST)
            if form.is_valid():
                app = form.save(commit=False)
                app.listing_id = listing.id
                app.user = request.user
                app.save()
                return render(request, "board/detail.html", {"listing": listing, "form": ApplicationForm})
        else:
            return render(request, "board/detail.html", {"listing": listing, "form": ApplicationForm})
    return render(request, "board/detail.html", {"listing": listing, "form": ApplicationForm})
