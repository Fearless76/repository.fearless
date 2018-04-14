import xbmc
import os.path
HOME        = xbmc.translatePath('special://home/')
done      =  os.path.join(HOME, 'done.xml')
if os.path.exists(done):
    exit()
xbmc.sleep(1000)
xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.vistatv-wizard",return)')
