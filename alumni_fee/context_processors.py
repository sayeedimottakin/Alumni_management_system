from .models import Fee_Info
from news.models import News_Letter
def add_variable_to_context(request):
    year_fee = Fee_Info.objects.get()
    current_news_letter = News_Letter.objects.all().order_by('-start_date').first()
    return {
        'yearFee': year_fee.yearly_fee,
        'current_news_letter':current_news_letter,
    }