import subprocess
def run(cmd):
    subprocess.call(cmd, shell=True)   # 위험: 셸 인젝션
# 악의적인 변경 1787809645
