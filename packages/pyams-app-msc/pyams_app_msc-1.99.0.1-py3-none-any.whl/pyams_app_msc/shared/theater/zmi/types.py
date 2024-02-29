#
# Copyright (c) 2015-2024 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_*** module

"""

__docformat__ = 'restructuredtext'

from pyams_app_msc.shared.theater import IMovieTheater
from pyams_content.interfaces import MANAGE_TOOL_PERMISSION
from pyams_content.shared.common.zmi.types import DataTypesAddAction, ISharedToolTypesTable
from pyams_content.shared.common.zmi.types.container import SharedToolTypesMenu, SharedToolTypesView
from pyams_layer.interfaces import IPyAMSLayer
from pyams_pagelet.pagelet import pagelet_config
from pyams_viewlet.viewlet import viewlet_config
from pyams_zmi.interfaces import IAdminLayer

from pyams_app_msc import _
from pyams_zmi.interfaces.viewlet import IPropertiesMenu, IToolbarViewletManager


@viewlet_config(name='data-types.menu',
                context=IMovieTheater, layer=IAdminLayer,
                manager=IPropertiesMenu, weight=400,
                permission=MANAGE_TOOL_PERMISSION)
class MovieTheaterSharedToolTypesMenu(SharedToolTypesMenu):
    """Shared tool data types menu"""

    label = _("Activity types")


@viewlet_config(name='add-data-type.action',
                context=IMovieTheater, layer=IAdminLayer, view=ISharedToolTypesTable,
                manager=IToolbarViewletManager, weight=20,
                permission=MANAGE_TOOL_PERMISSION)
class MovieTheaterDataTypesAddAction(DataTypesAddAction):
    """Data type add action"""

    label = _("Add activity type")


@pagelet_config(name='data-types.html',
                context=IMovieTheater, layer=IPyAMSLayer,
                permission=MANAGE_TOOL_PERMISSION)
class MovieTheaterSharedToolTypesView(SharedToolTypesView):
    """Shared tool data types view"""

    title = _("Activities types")
    table_label = _("Movie theater activities types list")
