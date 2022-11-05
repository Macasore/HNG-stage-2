from rest_framework import serializers

#operation types allowed in tuple format
OPERATION_TYPE = (
        ('addition','addition'),
        ('subtraction','subtraction'),
        ('division','division'),
        ('multiplication','multiplication'),
)


class RequestSerializer(serializers.Serializer):
    #declaring the variables needed for the resquest
    # slackUsername = serializers.CharField(max_length=100)
    operation_type = serializers.ChoiceField(choices=OPERATION_TYPE)
    x = serializers.IntegerField()
    y = serializers.IntegerField()

    #validation of attributes
    def validate(self, attrs):
        if attrs["x"] is None:
            raise serializers.ValidationError("x cannot be Empty")
        if attrs["y"] is None:
            raise serializers.ValidationError("y cannot be Empty")
        if attrs["operation_type"] is None:
            raise serializers.ValidationError("operation_type cannot be Empty")
        if attrs["operation_type"] not in OPERATION_TYPE[0]:
            raise serializers.ValidationError("the operation_type you entered does not exist")

        #return attribute if validate
        return attrs
        

#response format
class ResponseSerializer(serializers.Serializer):
    slackUsername = serializers.CharField(max_length=100)
    operation_type = serializers.ChoiceField(choices=OPERATION_TYPE)
    result = serializers.IntegerField()

