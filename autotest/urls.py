#-------------------------------------------------------------------------------
# $Id$
#
# Project: EOxServer <http://eoxserver.org>
# Authors: Stephan Krause <stephan.krause@eox.at>
#          Stephan Meissl <stephan.meissl@eox.at>
#
#-------------------------------------------------------------------------------
# Copyright (C) 2011 EOX IT Services GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies of this Software or works derived from this Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#-------------------------------------------------------------------------------

from django.conf.urls.defaults import *

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib import databrowse
from django.views.static import serve
from django.conf import settings

from eoxserver.services import views

#from eoxserver.server.models import *

#databrowse.site.register(EOxSCoverageEOCollectionRecord)
#databrowse.site.register(EOxSCoverageSingleFileRecord)
#databrowse.site.register(EOxSCoverageSingleFileNonGeoRecord)
#databrowse.site.register(EOxSRangeType)
#databrowse.site.register(EOxSRectifiedGridRecord)
#databrowse.site.register(EOxSChannelRecord)
#databrowse.site.register(EOxSDataDirRecord)
#databrowse.site.register(EOxSLayerMetadataRecord)
#databrowse.site.register(EOxSRangeType2Channel)

urlpatterns = patterns('',
    (r'^ows', views.ows),
    # Example:
    # (r'^eoxserver/', include('eoxserver.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
#    (r'^databrowse/(.*)', databrowse.site.root)
)