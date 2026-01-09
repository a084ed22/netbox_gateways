from django.utils.translation import gettext_lazy as _

from ipam.models import IPAddress, Prefix, VRF
from netbox.forms import PrimaryModelImportForm
from utilities.forms.fields import CSVModelChoiceField

from netbox_gateways.models import Gateway

__all__ = (
    'GatewayImportForm',
)


class GatewayImportForm(PrimaryModelImportForm):
    vrf = CSVModelChoiceField(
        label=_('VRF'),
        queryset=VRF.objects.all(),
        to_field_name='name',
        required=False,
        help_text=_('Assigned VRF')
    )
    prefix = CSVModelChoiceField(
        label=_('Prefix'),
        queryset=Prefix.objects.all(),
        to_field_name='prefix',
        required=False,
        help_text=_('Assigned prefix')
    )
    gateway_ip = CSVModelChoiceField(
        label=_('Gateway IP'),
        queryset=IPAddress.objects.all(),
        to_field_name='address',
        required=False,
        help_text=_('Assigned gateway IP address')
    )

    class Meta:
        model = Gateway
        fields = ('vrf', 'prefix', 'gateway_ip', 'tags')
