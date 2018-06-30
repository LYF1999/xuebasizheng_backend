#  coding=utf-8

from rest_framework.response import Response as RestResponse
from rest_framework import status


class Response:
    @staticmethod
    def ok(data):
        return RestResponse(data=data, status=200)

    @staticmethod
    def not_found(data):
        return RestResponse(data=data, status=404)

    @staticmethod
    def unauthorized(data):
        return RestResponse(data=data, status=status.HTTP_401_UNAUTHORIZED)
