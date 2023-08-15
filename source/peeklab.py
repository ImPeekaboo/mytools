def textAn(TEXT, ty='tw'):
    from IPython.display import HTML

    if ty == 'tw':
        textcover = str(len(TEXT) * 0.55)
        return display(HTML('<style>@import url(https://fonts.googleapis.com/css?family=Anonymous+Pro);.line-1{font-family: "Anonymous Pro", monospace;position: relative;font-size: 15px;white-space: nowrap;overflow: hidden;animation: typewriter 3s steps('+str(len(TEXT))+') infinite; }@keyframes typewriter{from{width:0;}to{width:'+textcover+'em;}}</style><div class="line-1">'+TEXT+'</div>'))
    elif ty == 'twg':
        textcover = str(len(TEXT)*0.55)
        return display(HTML('''<style>@import url(https://fonts.googleapis.com/css?family=Anonymous+Pro);.line-1{font-family: 'Anonymous Pro', monospace;    position: relative;   border-right: 1px solid;    font-size: 15px;   white-space: nowrap;    overflow: hidden;    }.anim-typewriter{  animation: typewriter 0.4s steps(44) 0.2s 1 normal both,             blinkTextCursor 600ms steps(44) infinite normal;}@keyframes typewriter{  from{width: 0;}  to{width: '''+textcover+'''em;}}@keyframes blinkTextCursor{  from{border-right:2px;}  to{border-right-color: transparent;}}</style><div class="line-1 anim-typewriter">'''+TEXT+'''</div>'''))


def loadingAn(name="cal"):
    from IPython.display import HTML

    if name == "cal":
        return display(HTML('<style>.lds-ring {   display: inline-block;   position: relative;   width: 34px;   height: 34px; } .lds-ring div {   box-sizing: border-box;   display: block;   position: absolute;   width: 34px;   height: 34px;   margin: 4px;   border: 5px solid #cef;   border-radius: 50%;   animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;   border-color: #cef transparent transparent transparent; } .lds-ring div:nth-child(1) {   animation-delay: -0.45s; } .lds-ring div:nth-child(2) {   animation-delay: -0.3s; } .lds-ring div:nth-child(3) {   animation-delay: -0.15s; } @keyframes lds-ring {   0% {     transform: rotate(0deg);   }   100% {     transform: rotate(360deg);   } }</style><div class="lds-ring"><div></div><div></div><div></div><div></div></div>'))
    elif name == "lds":
        return display(HTML('''<style>.lds-hourglass {  display: inline-block;  position: relative;  width: 34px;  height: 34px;}.lds-hourglass:after {  content: " ";  display: block;  border-radius: 50%;  width: 34px;  height: 34px;  margin: 0px;  box-sizing: border-box;  border: 20px solid #dfc;  border-color: #dfc transparent #dfc transparent;  animation: lds-hourglass 1.2s infinite;}@keyframes lds-hourglass {  0% {    transform: rotate(0);    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);  }  50% {    transform: rotate(900deg);    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);  }  100% {    transform: rotate(1800deg);  }}</style><div class="lds-hourglass"></div>'''))


def runSh(args, *, output=False, shell=True, cd=None):
    import subprocess, shlex

    if not shell:
        if output:
            proc = subprocess.Popen(
                shlex.split(args), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cd
            )
            while True:
                output = proc.stdout.readline()
                if output == b"" and proc.poll() is not None:
                    return
                if output:
                    print(output.decode("utf-8").strip())
        return subprocess.run(shlex.split(args), cwd=cd).returncode
    else:
        if output:
            return (
                subprocess.run(
                    args,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    cwd=cd,
                )
                .stdout.decode("utf-8")
                .strip()
            )
        return subprocess.run(args, shell=True, cwd=cd).returncode


def setupYTA():
    import os
    
    if not os.path.exists("/usr/local/bin/ytarchive"):
        from IPython.display import clear_output
        import os, time

        delete_path = '/content/sample_data'
        if os.path.exists(delete_path):
            runSh('rm -rf "/content/sample_data"')

        loadingAn()
        textAn('Installing yta, yt-dlp, ffmpeg...')
        runSh('cd /content')
        runSh('wget https://www.johnvansickle.com/ffmpeg/old-releases/ffmpeg-5.1.1-amd64-static.tar.xz')
        runSh('tar -xf ffmpeg-5.1.1-amd64-static.tar.xz')
        runSh('cp ffmpeg-*-static/ffmpeg ffmpeg-*-static/ffprobe /usr/local/bin/')
        runSh('rm ffmpeg-5.1.1-amd64-static.tar.xz')
        runSh('rm -rf ffmpeg-*-static')
        runSh('wget https://raw.githubusercontent.com/ImPeekaboo/mytools/main/source/ytarchive -O /usr/local/bin/ytarchive')
        runSh('chmod +x /usr/local/bin/ytarchive')
        runSh('pip install yt-dlp')
        runSh('mkdir archive-result')
        clear_output()
        print('yta, yt-dlp, ffmpeg are Installed!')
        time.sleep(2)
        clear_output()


def installRclone():
    import os
    
    if not os.path.exists("/usr/bin/rclone"):
        from IPython.display import clear_output
        import os, time
    
        delete_path = '/content/sample_data'
        if os.path.exists(delete_path):
            runSh('rm -rf "/content/sample_data"')
    
        loadingAn()
        textAn('Installing Rclone...')
        runSh('curl https://rclone.org/install.sh | sudo bash')
        runSh('sudo apt-get -y install fuse3')
        clear_output()
        print('Rclone is Installed!')
        time.sleep(2)
        clear_output()


def installRcloneB():
    import os
    
    if not os.path.exists("/usr/bin/rclone"):
        from IPython.display import clear_output
        import os, time
    
        delete_path = '/content/sample_data'
        if os.path.exists(delete_path):
            runSh('rm -rf "/content/sample_data"')
    
        loadingAn()
        textAn('Installing Rclone beta...')
        runSh('curl https://rclone.org/install.sh | sudo bash -s beta')
        runSh('sudo apt-get -y install fuse3')
        clear_output()
        print('Rclone beta is Installed!')
        time.sleep(2)
        clear_output()


def installGF():
    import os
    
    if not os.path.exists("/usr/local/bin/gofile"):
        from IPython.display import clear_output
        import time, os
    
        delete_path = '/content/sample_data'
        if os.path.exists(delete_path):
            runSh('rm -rf "/content/sample_data"')

        loadingAn()
        textAn('Installing Gofile...')
        runSh('wget https://raw.githubusercontent.com/ImPeekaboo/mytools/main/source/gofile -O /usr/local/bin/gofile')
        runSh('chmod +x /usr/local/bin/gofile')
        clear_output()
        print('Gofile is Installed!')
        time.sleep(2)
        clear_output()


def installCD():
    import importlib
    
    if importlib.util.find_spec("cyberdrop_dl") is None:
        from IPython.display import clear_output
        import time, os
    
        delete_path = '/content/sample_data'
        if os.path.exists(delete_path):
            runSh('rm -rf "/content/sample_data"')

        loadingAn()
        textAn('Installing Cyberdrop-dl...')
        runSh('pip install cyberdrop-dl')
        clear_output()
        print('Cyberdrop-dl is Installed!')
        time.sleep(2)
        clear_output()


def installMEGA():
    import os
    
    if not os.path.exists("/usr/bin/mega-cmd"):
        from IPython.display import clear_output
        import time, os
    
        delete_path = '/content/sample_data'
        if os.path.exists(delete_path):
            runSh('rm -rf "/content/sample_data"')

        loadingAn()
        textAn("Installing MEGA...")
        runSh('sudo apt-get -y update')
        #runSh('sudo apt-get -y install libssl-dev libmms0 libc-ares2 libc6 libcrypto++6 libgcc1 libmediainfo0v5 libpcre3 libpcrecpp0v5 libssl1.1 libstdc++6 libzen0v5 zlib1g apt-transport-https')
        runSh('sudo curl -sL -o /var/cache/apt/archives/MEGAcmd.deb https://mega.nz/linux/repo/xUbuntu_22.04/amd64/megacmd_1.6.3-2.1_amd64.deb')
        runSh('sudo dpkg -i /var/cache/apt/archives/MEGAcmd.deb')
        runSh('sudo apt --fix-broken install')
        clear_output()
        print("MEGA is Installed!")
        time.sleep(2)
        clear_output()


def installLT():
    import importlib
    
    if importlib.util.find_spec("libtorrent") is None:
        from IPython.display import clear_output
        import time, os
    
        delete_path = '/content/sample_data'
        if os.path.exists(delete_path):
            runSh('rm -rf "/content/sample_data"')

        loadingAn()
        textAn('Installing Libtorrent...')
        runSh('pip install libtorrent')
        clear_output()
        print('Libtorrent is Installed!')
        time.sleep(2)
        clear_output()


def installLX():
    import importlib
    
    if importlib.util.find_spec("libtorrentx") is None:
        from IPython.display import clear_output
        import time, os
    
        delete_path = '/content/sample_data'
        if os.path.exists(delete_path):
            runSh('rm -rf "/content/sample_data"')

        loadingAn()
        textAn('Installing Libtorrentx...')
        runSh('git clone https://github.com/imneonizer/libtorrentx')
        runSh('cd libtorrentx && pip install .')
        runSh('rm -rf /content/libtorrentx')
        clear_output()
        print('Libtorrentx is Installed!')
        time.sleep(2)
        clear_output()


def uploadConf():
    from google.colab import files
    from IPython.display import clear_output
    import shutil, os, time

    try:
        os.makedirs("/root/.config/rclone", exist_ok=True)
    except OSError as error:
        pass

    if os.path.exists('/root/.config/rclone/rclone.conf'):
        print('rclone.conf already exist!')
        time.sleep(1)
        clear_output()
    else:
        uploaded = files.upload()
        destination_directory = '/root/.config/rclone'

        for filename in uploaded.keys():
            shutil.move(filename, destination_directory + '/' + filename)
            clear_output()
            print(filename, 'success uploaded')

    time.sleep(2)
    clear_output()
