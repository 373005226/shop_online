from rest_framework import serializers
from .models import *


class PCVisitNumberSerializers(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = PCVisitNumber
        fields = "__all__"


class MobileVisitNumberSerializers(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = MobileVisitNumber
        fields = "__all__"
