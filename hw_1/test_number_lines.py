import subprocess

import difflib

generate_p = subprocess.Popen(['python3', 'generate_newlines.py', '10'], stdout=subprocess.PIPE)
generate_out, _ = generate_p.communicate()

number_p = subprocess.Popen(['python3', 'number_lines.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
number_out, _ = number_p.communicate(generate_out)

nl_p = subprocess.Popen(['nl', '-b', 'a'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
nl_out, _ = nl_p.communicate(generate_out)


differ = difflib.Differ()
for number, nl in zip(number_out.decode('utf-8').split('\n'), nl_out.decode('utf-8').split('\n')):
    if number != nl:
        print(differ.compare([number], [nl]))
        raise Exception("{} != {}".format(number, nl))

generate_p.wait()
number_p.wait()
nl_p.wait()
