from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import RequestSerializer


class view(APIView):
    serializer_class = RequestSerializer
    #post function
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        # validation of serializers so as to perform operation
        if serializer.is_valid(raise_exception=True):
            if serializer.data["operation_type"] == "addition":
                result = serializer.data["x"] + serializer.data["y"]

            elif serializer.data["operation_type"] == "subtraction":
                result = serializer.data["x"] - serializer.data["y"]
 
            elif serializer.data["operation_type"] == "multiplication":
                result = serializer.data["x"] * serializer.data["y"]
            else:
                result = serializer.data["x"] / serializer.data["y"]
                
            #Response format
            return Response(
                {
                "status": True,
                "slackUsername": "maca",
                "operation_type": serializer.data["operation_type"],
                "result": result
                },status=status.HTTP_200_OK)