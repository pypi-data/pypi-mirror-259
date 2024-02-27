import json
import os.path
from typing import Any, Optional, Mapping, Sequence

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from starlette.background import BackgroundTask
from starlette.requests import Request
from starlette.responses import JSONResponse, FileResponse, Response, RedirectResponse

from afeng_tools.application_tool.application_models import AppInfo
from afeng_tools.fastapi_tool.core.fastapi_items import ResponseResult, ResponseTemplateResult
from afeng_tools.sqlalchemy_tools.core.sqlalchemy_base_model import is_model_instance
from afeng_tools.sqlalchemy_tools.tool import sqlalchemy_model_tools
from afeng_tools.web_tool import request_tools


def json_resp(error_no: int = 0, message: str | Sequence = 'success', data: Any = None,
              http_status: int = 200) -> JSONResponse:
    """json响应"""
    return JSONResponse(
        status_code=http_status,
        content=jsonable_encoder(ResponseResult(error_no=error_no, message=message, data=data)),
    )


def template_resp(request: Request, resp_result: ResponseTemplateResult, app_info: AppInfo = None) -> Response:
    context_data = resp_result.context_data
    if context_data is None:
        context_data = dict()
    if 'app_info' not in context_data:
        context_data['app_info'] = app_info
    if 'title' not in context_data:
        context_data['title'] = resp_result.title
    if 'message' not in context_data:
        context_data['message'] = resp_result.message
    from afeng_tools.fastapi_tool.fastapi_jinja2_tools import create_template_response
    return create_template_response(request=request,
                                    template_file=resp_result.template_file,
                                    context=context_data)


def resp_404(message: str | Sequence = '页面没找到！', request: Request = None, context_data: dict = None,
             app_info: AppInfo = None):
    if request and not request_tools.is_json(request.headers) and not (app_info and app_info.is_json_api):
        resp_result = ResponseTemplateResult(title='404错误页面', message=message,
                                             template_file='common/views/error/404.html',
                                             context_data=context_data)
        app_info = app_info if app_info else request.scope.get('app_info')
        if app_info:
            resp_result.template_file = f'{app_info.code}/views/error/404.html'
            if app_info.error404_callback_func:
                is_mobile = request_tools.is_mobile(request.headers.get('user-agent'))
                resp_result.context_data = app_info.error404_callback_func(message=message, is_mobile=is_mobile)
                if 'template_file' in context_data:
                    resp_result.template_file = resp_result.context_data['template_file']
        return template_resp(request=request, resp_result=resp_result, app_info=app_info)
    return json_resp(error_no=404, message=message)


def resp_422(message: str | Sequence, app_info: AppInfo = None):
    return json_resp(error_no=422, message=message)


def resp_501(message: str | Sequence, request: Request = None, context_data: dict = None, app_info: AppInfo = None):
    if request and not request_tools.is_json(request.headers) and not (app_info and app_info.is_json_api):
        resp_result = ResponseTemplateResult(title='操作失败页面', message=message,
                                             template_file='common/views/error/501.html',
                                             context_data=context_data)
        app_info = app_info if app_info else request.scope.get('app_info')
        if app_info:
            resp_result.template_file = f'{app_info.code}/views/error/501.html'
            if app_info.error501_callback_func:
                is_mobile = request_tools.is_mobile(request.headers.get('user-agent'))
                resp_result.context_data = app_info.error501_callback_func(message=message, is_mobile=is_mobile)
                if 'template_file' in context_data:
                    resp_result.template_file = resp_result.context_data['template_file']
        return template_resp(request=request, resp_result=resp_result, app_info=app_info)
    return json_resp(error_no=501, message=message)


def resp_500(message: str | Sequence = '服务器内部错误！', request: Request = None, context_data: dict = None,
             app_info: AppInfo = None):
    if request and not request_tools.is_json(request.headers) and not (app_info and app_info.is_json_api):
        resp_result = ResponseTemplateResult(title='500错误页面', message=message,
                                             template_file='common/views/error/500.html',
                                             context_data=context_data)
        app_info = app_info if app_info else request.scope.get('app_info')
        if app_info:
            resp_result.template_file = f'{app_info.code}/views/error/500.html'
            if app_info.error500_callback_func:
                is_mobile = request_tools.is_mobile(request.headers.get('user-agent'))
                resp_result.context_data = app_info.error500_callback_func(message=message, is_mobile=is_mobile)
                if 'template_file' in context_data:
                    resp_result.template_file = resp_result.context_data['template_file']

        return template_resp(request=request, resp_result=resp_result, app_info=app_info)
    return json_resp(error_no=500, message=message)


def resp_json(data: Any = None, error_no: int = 0, message: str | Sequence = 'success', app_info: AppInfo = None):
    if is_model_instance(data) or (data and isinstance(data, list) and len(data) > 0 and is_model_instance(data[0])):
        data = json.loads(sqlalchemy_model_tools.to_json(data))
    if isinstance(data, BaseModel):
        data = data.model_dump(mode='json')
    return json_resp(error_no=error_no, message=message, data=data)


def resp_file(file_path: str, file_name: str = None, download_flag: bool = False,
              context_data: dict = None, app_info: AppInfo = None) -> Response:
    """响应文件"""
    if not os.path.exists(file_path):
        return resp_404(message='您访问的资源不存在！', context_data=context_data, app_info=app_info)
    response = FileResponse(file_path)
    with open(file_path, "rb") as file:
        if download_flag:
            if file_name is None:
                file_name = os.path.split(file_path)[1]
            response.headers["Content-Disposition"] = f"attachment; filename={file_name}"
        response.body = file.read()
        return response


def redirect(target_url: str, status_code: int = 307,
             headers: Optional[Mapping[str, str]] = None,
             background: Optional[BackgroundTask] = None, app_info: AppInfo = None) -> RedirectResponse:
    """重定向"""
    return RedirectResponse(target_url, status_code=status_code, headers=headers, background=background)
