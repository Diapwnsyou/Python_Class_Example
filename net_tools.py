class nettools:
    def __init__(self, target):
        self.target = target

    def pinger(self):
        import os

        response = os.system('ping -c 3 {} 2>&1 > /dev/null'.format(self.target))

        if response == 0:
            return True
        else:
            return False

    def tracer(self):
        import subprocess
        import re
            
        final_list = []

        response = subprocess.check_output('traceroute {}'.format(self.target), shell=True)

        res_list = [ line for line in response.split('\n') if not re.match(r'^traceroute', line, re.M|re.I)]

        if len(res_list) > 22:
            return False
        else:
            for hops in res_list:
                try:
                    match_ip = re.search(r'\(((?:\d+\.){3}\d+)\)', hops, re.M|re.I)
                    if match_ip.group(1) != None:
                        final_list.append(match_ip.group(1))
                except AttributeError:
                    pass

            return final_list
