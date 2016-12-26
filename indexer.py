from subprocess import (Popen, PIPE)

URL = YOUR_URL

stderr_out = Popen(['wget', '-r', '--spider', '--no-parent', URL], stdout=PIPE, stderr=PIPE).communicate()[1]

err_list = stderr_out.split(' ')
out_list = []

for i, item in enumerate(err_list):
    if '200' in item:
        out_list.append(err_list[i+2])
    if '404:' in item:
        out_list.append('0')
    if 'http://' in item:
        out_list.append(err_list[i].split('\n')[0])

print(out_list)
