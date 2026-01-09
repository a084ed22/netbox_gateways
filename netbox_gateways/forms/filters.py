from django import forms

from ipam.models import Prefix, IPAddress, VRF
from netbox.forms import NetBoxModelFilterSetForm
from utilities.forms.fields import DynamicModelChoiceField
from ..models import Gateway

__all__ = (
    'GatewayFilterForm',
)


class GatewayFilterForm(NetBoxModelFilterSetForm):
    model = Gateway
    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all(),
        null_option="Global",
        required=False,
    )
    prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all(),
        required=False,
    )
    gateway_ip = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
    )
