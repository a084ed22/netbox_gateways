from django.db.models import Count

from netbox.views import generic
from utilities.views import register_model_view

from . import filtersets, forms, models, tables


#
# Gateway views
#


@register_model_view(models.Gateway)
class GatewayView(generic.ObjectView):
    queryset = models.Gateway.objects.all()
    permission_required = "netbox_gateways.view_gateway"


@register_model_view(models.Gateway, 'list', path='', detail=False)
class GatewayListView(generic.ObjectListView):
    queryset = models.Gateway.objects.all()
    table = tables.GatewayTable
    filterset = filtersets.GatewayFilterSet
    filterset_form = forms.GatewayFilterForm
    permission_required = "netbox_gateways.view_gateway"


@register_model_view(models.Gateway, 'edit')
@register_model_view(models.Gateway, 'add', detail=False)
class GatewayEditView(generic.ObjectEditView):
    queryset = models.Gateway.objects.all()
    form = forms.GatewayForm
    permission_required = "netbox_gateways.addedit_gateway"


@register_model_view(models.Gateway, 'delete')
class GatewayDeleteView(generic.ObjectDeleteView):
    queryset = models.Gateway.objects.all()
    permission_required = "netbox_gateways.delete_gateway"


@register_model_view(models.Gateway, 'bulk_import', path='import', detail=False)
class GatewayBulkImportView(generic.BulkImportView):
    queryset = models.Gateway.objects.all()
    model_form = forms.GatewayImportForm
    template_name = 'generic/bulk_import.html'
    permission_required = "netbox_gateways.addedit_gateway"
