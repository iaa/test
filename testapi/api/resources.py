from tastypie.resources import Resource
from django.conf.urls import url


class SmsResource(Resource):

    class Meta:
        pass

    def send_message(self, request, **kwargs):
        pass

    def determine_format(self, request):
        return 'application/json'

    def prepend_urls(self):
        return [
            url(r'^(?P<message>[\w\s]+)/$', self.wrap_view('send_message')),
        ]
