import subprocess
import string
import re

if __name__ == '__main__':

    def func(com: str, text: str):
        result = subprocess.run(com, shell=True,
                                stdout=subprocess.PIPE, encoding='utf 8')
        out = result.stdout
        for p in string.punctuation:
            if p in out:
                out_rep = out.replace(p, ' ')

        if result.returncode == 0:
            if re.search(text, out_rep):
                print(True)
            else:
                print(False)
        else:
            print(False)


    func('cat /etc/os-release', '22.04.1')
