from rest_framework import serializers

from ..models import Employee, Position

class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ('id', 'name')
        extra_kwargs = {
            'url': {
                'view_name': 'api:user-detail'
            },
        }


class ChiefEmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'url', 'first_name', 'second_name', 'patronym')

class EmployeeSerializer(serializers.ModelSerializer):
    chief = ChiefEmployeeSerializer(many=False, source='parent')
    position = PositionSerializer(many=False)

    class Meta:
        model = Employee
        fields = (
            'id',
            'url',
            'second_name',
            'first_name',
            'patronym',
            'chief',
            'position',
            'level',
            'employment_date',
            'salary',
            'total_accrued')