from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202   # 204的话不会返回任何值
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake'
    error_code = 999


class ClientTypeError(APIException):
    # 400 请求参数错误
    # 401 未授权
    # 403 禁止访问
    # 404 没有找到资源
    # 500 服务器产生未知错误
    # 200 请求成功，201 创建或更新成，204 删除成功
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not_found'
    error_code = 1001


class AuthFailed(APIException):
    code = 401  # 401授权失败
    msg = 'authorization failed'
    error_code = 1005


class Forbidden(APIException):
    code = 403   # 403禁止访问
    error_code = 1004
    msg = 'forbidden, not in scope'


class DuplicateGift(APIException):
    code = 400
    error_code = 2001
    msg = 'the current book has already in gift'
