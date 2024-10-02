from django.urls import path
from .views import dashboard_view, option_generate_document, generate_special_testimony_document, \
    download_special_testimony_docx, generate_iva_sales_testimony_document, \
    download_iva_sales_testimony_docx, generate_municipality_notices_document, \
    download_municipality_notices_docx, generate_buy_sell_document, \
    download_buy_sell_docx

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('option-generate-document/', option_generate_document, name='option_generate_document'),
    path('generate-special-testimony-document/', generate_special_testimony_document,
         name='generate_special_testimony_document'),
    path('download-special-testimony-docx/', download_special_testimony_docx, name='download_special_testimony_docx'),
    path('generate-iva-sales-testimony-document/', generate_iva_sales_testimony_document,
         name='generate_iva_sales_testimony_document'),
    path('download-iva-sales-testimony-docx/', download_iva_sales_testimony_docx,
         name='download_iva_sales_testimony_docx'),
    path('generate-municipality-notices-document/', generate_municipality_notices_document,
         name='generate_municipality_notices_document'),
    path('download-municipality-notices-docx/', download_municipality_notices_docx,
         name='download_municipality_notices_docx'),
    path('generate-buy-sell-document/', generate_buy_sell_document,
         name='generate_buy_sell_document'),
    path('download-buy-sell-docx/', download_buy_sell_docx,
         name='download_buy_sell_docx')
]
