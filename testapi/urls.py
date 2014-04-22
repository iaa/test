# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from tastypie.api import Api
from api.resources import SmsResource
import logging

logger = logging.getLogger(__name__)


class SmsApi(SmsResource):

    def send_message(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        status = 'ok'
        phone = request.POST['phone']
        if not request.POST['phone'] == '79149009900':
            status = 'error'
            error_code = 3500
            msg = 'Невозможно отправить сообщение указанному абоненту'
            logger.error(msg, extra={'info': request.POST['phone']})
            return self.create_response(request, {'status': status,
                                                  'phone': phone,
                                                  'error_code': error_code,
                                                  'error_msg': msg}
                                        )
        msg = 'Сообщение отправлено'
        logger.info(msg, extra={'info': request.POST['phone']})
        return self.create_response(request, {'status': status, 'phone': phone})


class SmsSomeApi(SmsResource):

    def send_message(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        status = 'ok'
        message = kwargs['message']
        if len(message) > 20:
            status = 'error'
            error_code = 3500
            msg = 'Сообщение слишком длинное'
            logger.error(msg, extra={'info': kwargs['message']})
            return self.create_response(request, {'status': status,
                                                  'error_code': error_code,
                                                  'error_msg': msg}
                                        )
        msg = 'Сообщение отправлено'
        logger.info(msg, extra={'info': kwargs['message'], 'status': status})
        return self.create_response(request, {'status': status, 'msg': msg})


class SmsSuperApi(SmsResource):

    def send_message(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        status = 'ok'
        message = kwargs['message']
        if len(message) < 20:
            status = 'error'
            error_code = 3500
            msg = 'Сообщение слишком короткое'
            logger.error(msg, extra={'info': kwargs['message']})
            return self.create_response(request, {'status': status,
                                                  'error_code': error_code,
                                                  'error_msg': msg}
                                        )
        msg = 'Сообщение отправлено'
        logger.info(msg, extra={'info': kwargs['message'], 'status': status})
        return self.create_response(request, {'status': status, 'msg': msg})

sms_api = Api(api_name='sms-api')
sms_api.register(SmsApi())

sms_some_api = Api(api_name='some-api')
sms_some_api.register(SmsSomeApi())

sms_super_api = Api(api_name='super-api')
sms_super_api.register(SmsSuperApi())

urlpatterns = patterns('',
    url(r'^$', 'testapi.views.home', name='home'),
    url(r'', include(sms_api.urls)),
    url(r'', include(sms_some_api.urls)),
    url(r'', include(sms_super_api.urls)),

)
