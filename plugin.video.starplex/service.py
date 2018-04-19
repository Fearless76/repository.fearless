# -*- coding: utf-8 -*-

"""
    Starplex Add-on
    Copyright (C) 2016 Starplex

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from resources.lib.modules import log_utils
from resources.lib.modules import control

control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))

try:
    ModuleVersion = control.addon('script.module.starplex').getAddonInfo('version')
    AddonVersion = control.addon('plugin.video.starplex').getAddonInfo('version')
    # RepoVersion = control.addon('repository.fearless').getAddonInfo('version')

    log_utils.log('######################### starplex ############################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT from resources.lib.modules import log_utils
from resources.lib.modules import control

control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))

try:
    ModuleVersion = control.addon('script.module.starplex').getAddonInfo('version')
    AddonVersion = control.addon('plugin.video.starplex').getAddonInfo('version')
    # RepoVersion = control.addon('repository.fearless').getAddonInfo('version')

    log_utils.log('######################### starplex ############################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT from resources.lib.modules import log_utils
from resources.lib.modules import control

control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))

try:
    ModuleVersion = control.addon('script.starplex').getAddonInfo('version')
    AddonVersion = control.addon('plugin.starplex').getAddonInfo('version')
    # RepoVersion = control.addon('repository.fearless').getAddonInfo('version')

    log_utils.log('######################### starplex ############################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT starplex VERSIONS REPORT ######################', log_utils.LOGNOTICE)
    log_utils.log('### starplex PLUGIN VERSION: %s ###' % str(AddonVersion), log_utils.LOGNOTICE)
    log_utils.log('### starplex SCRIPT VERSION: %s ###' % str(ModuleVersion), log_utils.LOGNOTICE)
    # log_utils.log('### Fearless REPOSITORY VERSION: %s ###' % str(RepoVersion), log_utils.LOGNOTICE)
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
except:
    log_utils.log('######################### starplex ############################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT starplex VERSIONS REPORT ######################', log_utils.LOGNOTICE)
    log_utils.log('### ERROR GETTING starplex VERSIONS - NO HELP WILL BE GIVEN AS THIS IS NOT AN OFFICIAL starplex INSTALL. ###', log_utils.LOGNOTICE)
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
 VERSIONS REPORT ######################', log_utils.LOGNOTICE)
    log_utils.log('### starplex PLUGIN VERSION: %s ###' % str(AddonVersion), log_utils.LOGNOTICE)
    log_utils.log('### starplex SCRIPT VERSION: %s ###' % str(ModuleVersion), log_utils.LOGNOTICE)
    # log_utils.log('### Fearless REPOSITORY VERSION: %s ###' % str(RepoVersion), log_utils.LOGNOTICE)
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
except:
    log_utils.log('######################### starplex ############################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT starplex VERSIONS REPORT ######################', log_utils.LOGNOTICE)
    log_utils.log('### ERROR GETTING starplex VERSIONS - NO HELP WILL BE GIVEN AS THIS IS NOT AN OFFICIAL starplex INSTALL. ###', log_utils.LOGNOTICE)
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
 VERSIONS REPORT ######################', log_utils.LOGNOTICE)
    log_utils.log('### starplex PLUGIN VERSION: %s ###' % str(AddonVersion), log_utils.LOGNOTICE)
    log_utils.log('### starplex SCRIPT VERSION: %s ###' % str(ModuleVersion), log_utils.LOGNOTICE)
    # log_utils.log('### Fearless REPOSITORY VERSION: %s ###' % str(RepoVersion), log_utils.LOGNOTICE)
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
except:
    log_utils.log('######################### starplex ############################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT starplex VERSIONS REPORT ######################', log_utils.LOGNOTICE)
    log_utils.log('### ERROR GETTING starplex VERSIONS - NO HELP WILL BE GIVEN AS THIS IS NOT AN OFFICIAL starplex INSTALL. ###', log_utils.LOGNOTICE)
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
