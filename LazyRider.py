import webbrowser
import os

    def start_url_list(urls):
        webbrowser.register('firefox',
            None,
            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        for url in urls:
            webbrowser.get('firefox').open(url)
            
try:
    os.system('start %localappdata%\Discord\\app-1.0.9004\\Discord.exe')
    urls = ['https://www.youtube.com/', 'https://www.twitch.tv/']
    start_url_list(urls)
except Exception as e:
    logf = open("LazyRider_error.log", "w")
    logf.write("Exception: {0}\n\n".format(str(e)))
    
