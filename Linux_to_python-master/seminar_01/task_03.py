import subprocess

if __name__ == '__main__':
    result = subprocess.run('cat /etc/os-release\n', shell=True,
                            stdout=subprocess.PIPE, encoding='utf 8')
    out = result.stdout
    # print(out)
    # lines = '\n'.join(out)
    lines = out.split('\n')
    print(lines)

    if result.returncode == 0:
        if 'VERSION="22.04.1 LTS (Jammy Jellyfish)"' in lines and 'VERSION_CODENAME=jammy' in lines:
            print('SUCCESS')
        else:
            print('FAIL')
    else:
        print('FAIL')
