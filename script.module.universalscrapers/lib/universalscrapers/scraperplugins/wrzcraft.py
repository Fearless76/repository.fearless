# -*- coding: utf-8 -*-

import re,xbmc,xbmcaddon,urllib,time
from ..scraper import Scraper
import requests
from ..common import clean_title,clean_search, filter_host, get_rd_domains,send_log,error_log 

dev_log = xbmcaddon.Addon('script.module.universalscrapers').getSetting("dev_log")

User_Agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'


class Wzrcraft(Scraper):
    domains = ['wzrcraft.net']
    name = "wzrcraft"
    sources = []
    
    def __init__(self):
        self.domains = ['wrzcraft.net']
        self.base_link = 'http://wrzcraft.net'
        #self.search_link = '/search/%s+%s/feed/rss2/'
        self.sources = []
        if dev_log=='true':
            self.start_time = time.time() 

    def scrape_movie(self, title, year, imdb, debrid=False):
        try:
            if not debrid:
                return []
            search_id = clean_search(title.lower())  
                        
            start_url = "%s/?s=%s+%s" % (self.base_link, search_id.replace(' ','+'),year)
            #print start_url
            headers = {'User_Agent':User_Agent}
            OPEN = requests.get(start_url,headers=headers,timeout=5).content
            
            content = re.compile('<h2><a href="(.+?)"',re.DOTALL).findall(OPEN)
            for url in content:
                if 'truehd' in url:
                    continue
                if not clean_title(title).lower() in clean_title(url).lower():
                    continue
                #print 'PASS '+url
                self.get_source(url)                        
            return self.sources
        except Exception, argument:        
            if dev_log == 'true':
                error_log(self.name,'Check Search')
            return self.sources  

    def scrape_episode(self,title, show_year, year, season, episode, imdb, tvdb, debrid = False):
        try:
            if not debrid:
                return []
            season_url = "0%s"%season if len(season)<2 else season
            episode_url = "0%s"%episode if len(episode)<2 else episode
            sea_epi ='s%se%s'%(season_url,episode_url)
            
            search_id = clean_search(title.lower())  
            start_url = "%s/?s=%s+%s" % (self.base_link, search_id.replace(' ','+'),sea_epi)
            print start_url
            headers = {'User_Agent':User_Agent}
            OPEN = requests.get(start_url,headers=headers,timeout=5).content
            content = re.compile('<h2><a href="(.+?)"',re.DOTALL).findall(OPEN)
            for url in content:
                if not clean_title(title).lower() in clean_title(url).lower():
                    continue
                #print 'PASS '+url
                self.get_source(url)                        
            return self.sources
        except Exception, argument:        
            if dev_log == 'true':
                error_log(self.name,'Check Search')
            return self.sources  

    def get_source(self,url):
        try:        
            headers = {'User_Agent':User_Agent}
            links = requests.get(url,headers=headers,timeout=3).content
            Regex = re.compile('<singlelink>(.+?)</strong><br',re.DOTALL).findall(links)           
            LINK = re.compile('href="([^"]+)"',re.DOTALL).findall(str(Regex))
            count = 0            
            for url in LINK:
                if '.rar' not in url:
                    if '.srt' not in url:
                        if '1080' in url:
                            res = '1080p'
                        elif '720' in url:
                            res = '720p'
                        elif 'HDTV' in url:
                            res = 'DVD'
                        else:
                            pass

                        host = url.split('//')[1].replace('www.','')
                        host = host.split('/')[0].lower()

                        # if not filter_host(host):
                            # continue
                                # if debrid == "true":
                        rd_domains = get_rd_domains()
                        if host in rd_domains:
                            count +=1
                            self.sources.append({'source': host,'quality': res,'scraper': self.name,'url': url,'direct': False, 'debridonly': True})
            if dev_log=='true':
                end_time = time.time() - self.start_time
                send_log(self.name,end_time,count)                

        except:pass
