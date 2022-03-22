from rest_framework import serializers
from .models import Transaction



class TransactionSerializer(serializers.ModelSerializer):
    status = serializers.CharField(
        source='get_status_display', read_only=True
    )
    txType = serializers.CharField(
        source='get_txType_display', read_only=True
    )
    class Meta:
        model = Transaction
        fields = ['amount', 'status', 'is_valid', 'time_stamp', 'has_block', 'completed', 'receiver','sender', 'txType']


       