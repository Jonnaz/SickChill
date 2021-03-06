# coding=utf-8
# Author: Nic Wolfe <nic@wolfeden.ca>
# URL: https://sickchill.github.io
#
# This file is part of SickChill.
#
# SickChill is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SickChill is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SickChill. If not, see <http://www.gnu.org/licenses/>.
# pylint: disable=abstract-method,too-many-lines, R

from __future__ import print_function, unicode_literals

import markdown2
from common import PageTemplate
from home import Home
from routes import Route

import sickbeard
from sickbeard import logger

try:
    import json
except ImportError:
    # noinspection PyPackageRequirements,PyUnresolvedReferences
    import simplejson as json


@Route('/news(/?.*)', name='news')
class HomeNews(Home):
    def __init__(self, *args, **kwargs):
        super(HomeNews, self).__init__(*args, **kwargs)

    def index(self, *args_, **kwargs_):
        # noinspection PyBroadException
        try:
            news = sickbeard.versionCheckScheduler.action.check_for_new_news()
        except Exception:
            logger.log('Could not load news from repo, giving a link!', logger.DEBUG)
            news = _('Could not load news from the repo. [Click here for news.md])({news_url})').format(news_url=sickbeard.NEWS_URL)

        sickbeard.NEWS_LAST_READ = sickbeard.NEWS_LATEST
        sickbeard.NEWS_UNREAD = 0
        sickbeard.save_config()

        t = PageTemplate(rh=self, filename="markdown.mako")
        data = markdown2.markdown(news if news else _("The was a problem connecting to github, please refresh and try again"), extras=['header-ids'])

        return t.render(title=_("News"), header=_("News"), topmenu="system", data=data, controller="news", action="index")
