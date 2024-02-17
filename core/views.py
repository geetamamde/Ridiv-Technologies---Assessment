
from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer




# Create your views here.


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.prefetch_related('invoice_detail_set')

class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     invoice_id = self.request.query_params.get('invoice')
    #     if invoice_id:
    #         return queryset.filter(invoice_id=invoice_id)
    #     return queryset