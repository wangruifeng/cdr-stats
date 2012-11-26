# -*- coding: utf-8 -*-
#
# CDR-Stats License
# http://www.cdr-stats.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

from django.conf.urls import url, patterns, include
from django.conf import settings
from tastypie.api import Api
from api.user_api import UserResource
from api.switch_api import SwitchResource
from api.hangup_cause_api import HangupCauseResource
from api.cdr_daily_api import CdrDailyResource
from api.cdr_api import CdrResource
from cdr.urls import urlpatterns as urlpatterns_cdr
from cdr_alert.urls import urlpatterns as urlpatterns_cdr_alert
from user_profile.urls import urlpatterns as urlpatterns_user_profile
from frontend.urls import urlpatterns as urlpatterns_frontend
from api.api_playgrounds.urls import urlpatterns as urlpatterns_api_playgrounds
from common_notification.urls import urlpatterns as urlpatterns_common_notification

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# tastypie api
tastypie_api = Api(api_name='v1')
tastypie_api.register(UserResource())
tastypie_api.register(SwitchResource())
tastypie_api.register(HangupCauseResource())
tastypie_api.register(CdrDailyResource())
tastypie_api.register(CdrResource())


urlpatterns = patterns('',

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^admin_tools/', include('admin_tools.urls')),

    (r'^api/', include(tastypie_api.urls)),

    # Serve static
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT}),

    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', \
                            {'url': 'static/cdr_stats/images/favicon.ico'}),
)


urlpatterns += urlpatterns_cdr
urlpatterns += urlpatterns_cdr_alert
urlpatterns += urlpatterns_user_profile
urlpatterns += urlpatterns_frontend
urlpatterns += urlpatterns_api_playgrounds
urlpatterns += urlpatterns_common_notification

urlpatterns += patterns('',
    url("", include('django_socketio.urls')),
)
