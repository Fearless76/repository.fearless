# -*- coding: utf-8 -*-


import os,sys,urlparse

from resources.lib.modules import control
from resources.lib.modules import trakt

import xbmcaddon
__addon__ = xbmcaddon.Addon()
__icon__ = __addon__.getAddonInfo('icon')

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1]) ; control.moderator()

addonFanart = control.addonFanart()

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')


class navigator:
    def movies(self, lite=False):
        self.addDirectoryItem('Search For A Movie', 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.addDirectoryItem('New Movies', 'movieWidget', 'icon.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32017, 'movies&url=trending', 'icon.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32018, 'movies&url=popular', 'icon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32019, 'movies&url=views', 'icon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32020, 'movies&url=boxoffice', 'icon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32021, 'movies&url=oscars', 'icon.png', 'DefaultMovies.png')
        self.addDirectoryItem('In Cinema', 'movies&url=theaters', 'icon.png', 'DefaultRecentlyAddedMovies.png')
        #self.addDirectoryItem('Channels', 'channels', 'icon.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32011, 'movieGenres', 'icon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32012, 'movieYears', 'icon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32013, 'moviePersons', 'icon.png', 'DefaultMovies.png')
        self.addDirectoryItem(32015, 'movieCertificates', 'icon.png', 'DefaultMovies.png')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32003, 'mymovieliteNavigator', 'icon.png', 'DefaultVideoPlaylists.png')

            #self.addDirectoryItem(32028, 'moviePerson', 'icon.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', 'icon.png', 'DefaultMovies.png')

        self.endDirectory()


    def mymovies(self, lite=False):
        self.accountCheck()

        if traktCredentials == True:
            self.addDirectoryItem(32032, 'movies&url=traktcollection', 'icon.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32033, 'movies&url=traktwatchlist', 'icon.png', 'DefaultMovies.png', queue=True)
            self.addDirectoryItem(32035, 'movies&url=traktfeatured', 'icon.png', 'DefaultMovies.png', queue=True)

        if traktIndicators == True:
            self.addDirectoryItem(32036, 'movies&url=trakthistory', 'icon.png', 'DefaultMovies.png', queue=True)

        self.addDirectoryItem(32039, 'movieUserlists', 'icon.png', 'DefaultMovies.png')

        if lite == False:
            self.addDirectoryItem(32031, 'movieliteNavigator', 'movies.png', 'DefaultMovies.png')
            #self.addDirectoryItem(32028, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
            self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'DefaultMovies.png')

        self.endDirectory()


    def tvshows(self, lite=False):
        self.addDirectoryItem('Search For A TV Shows', 'tvSearch', 'icon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32023, 'tvshows&url=rating', 'icon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'tvshows&url=views', 'icon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32017, 'tvshows&url=trending', 'icon.png', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem(32018, 'tvshows&url=popular', 'icon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32011, 'tvGenres', 'icon.png', 'DefaultTVShows.png')
        #self.addDirectoryItem(32016, 'tvNetworks', 'icon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32015, 'tvCertificates', 'icon.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'tvshows&url=airing', 'icon.png', 'DefaultTVShows.png')
        self.addDirectoryItem('New Episodes', 'calendar&url=added', 'icon.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
        self.addDirectoryItem(32027, 'calendars', 'icon.png', 'DefaultRecentlyAddedEpisodes.png')

        if lite == False:
            if not control.setting('lists.widget') == '0':
                self.addDirectoryItem(32004, 'mytvliteNavigator', 'icon.png', 'DefaultVideoPlaylists.png')

            #self.addDirectoryItem(32028, 'tvPerson', 'icon.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'tvSearch', 'icon.png', 'DefaultTVShows.png')

        self.endDirectory()


    def mytvshows(self, lite=False):
        self.accountCheck()

        if traktCredentials == True:
            self.addDirectoryItem(32032, 'tvshows&url=traktcollection', 'icon.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32033, 'tvshows&url=traktwatchlist', 'icon.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32035, 'tvshows&url=traktfeatured', 'icon.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32041, 'episodeUserlists', 'icon.png', 'DefaultTVShows.png')
			
        if traktIndicators == True:
            self.addDirectoryItem(32036, 'calendar&url=trakthistory', 'icon.png', 'DefaultTVShows.png', queue=True)
            self.addDirectoryItem(32037, 'calendar&url=progress', 'icon.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)
            self.addDirectoryItem(32038, 'calendar&url=mycalendar', 'icon.png', 'DefaultRecentlyAddedEpisodes.png', queue=True)

        self.addDirectoryItem(32040, 'tvUserlists', 'icon.png', 'DefaultTVShows.png')

        if lite == False:
            self.addDirectoryItem(32031, 'tvliteNavigator', 'icon.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32028, 'tvPerson', 'icon.png', 'DefaultTVShows.png')
            self.addDirectoryItem(32010, 'tvSearch', 'icon.png', 'DefaultTVShows.png')

        self.endDirectory()

    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'icon.png', 'DefaultMovies.png', isAction=False)
        if len(control.listDir(tv_downloads)[0]) > 0:
            self.addDirectoryItem(32002, tv_downloads, 'icon.png', 'DefaultTVShows.png', isAction=False)

        self.endDirectory()

    def views(self):
        try:
            control.idle()

            items = [ (control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'), (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes') ]

            select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))

            if select == -1: return

            content = items[select][1]

            title = control.lang(32059).encode('utf-8')
            url = '%s?action=addView&content=%s' % (sys.argv[0], content)

            poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

            item = control.item(label=title)
            item.setInfo(type='Video', infoLabels = {'title': title})
            item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'banner': banner})
            item.setProperty('Fanart_Image', fanart)

            control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            control.content(int(sys.argv[1]), content)
            control.directory(int(sys.argv[1]), cacheToDisc=True)

            from resources.lib.modules import cache
            views.setView(content, {})
        except:
            return


    def accountCheck(self):
        if traktCredentials == False:
            control.idle()
            control.infoDialog(control.lang(32042).encode('utf-8'), sound=True, icon='WARNING')
            sys.exit()


    def clearCache(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')

    def clearCacheSearch(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_search()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')
        
    def clearCacheSearch2(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.cache_clear_search2()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')


    def addDirectoryItem(self, name, query, thumb, icon, queue=False, isAction=True, isFolder=True):
        try: name = control.lang(name).encode('utf-8')
        except: pass
        url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
        cm = []
        if queue == True: cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
        item = control.item(label=name)
        item.addContextMenuItems(cm)
        item.setArt({'icon': thumb, 'thumb': thumb})
        if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)


    def endDirectory(self):
        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)


