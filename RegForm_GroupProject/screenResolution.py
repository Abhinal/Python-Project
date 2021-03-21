from subprocess import Popen, PIPE

class screenSize:
    def __init__(self):

        cmd = ['xrandr']
        cmd2 = ['grep', '*']
        p = Popen(cmd, stdout=PIPE)
        p2 = Popen(cmd2, stdin=p.stdout, stdout=PIPE)
        p.stdout.close()
        resolution_string, junk = p2.communicate()
        resolution = resolution_string.split()[0]

        self.width = int(str(resolution).split("'")[1].split('x')[0])
        self.height = int(str(resolution).split("'")[1].split('x')[1])