from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from .models import Bulletin


def index(request):
    bulletin_list = Bulletin.objects.order_by('-pub_date').all()
    bulletins = _paginate_records(bulletin_list, 5, request)

    return render(request, 'board/index.html', {
        'bulletins': bulletins,
    })


def detail(request, bulletin_id):
    bulletin = get_object_or_404(Bulletin, pk=bulletin_id)

    return render(request, 'board/detail.html', {
        'bulletin': bulletin,
    })


def _paginate_records(records_list, count_per_page, request):
    paginator = Paginator(records_list, count_per_page)

    page = request.GET.get('page')
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)

    return records
