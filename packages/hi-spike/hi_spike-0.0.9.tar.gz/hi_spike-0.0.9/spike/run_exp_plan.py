import os
from spike.utils import run_cmd, echo
import datetime
import time


def run():
    
    project_path = os.getcwd()
    log_path = os.path.join(project_path, "logs/")
    echo("")
    echo("")
    echo("")
    echo("")
    echo("")
    echo("         __                         __  ___      __                ____")
    echo("        / /   ____ _____  __  __   /  |/  /___ _/ /_____  _____   / __ )__  _________  __")
    echo("       / /   / __ `/_  / / / / /  / /|_/ / __ `/ //_/ _ \\/ ___/  / __  / / / / ___/ / / /")
    echo("      / /___/ /_/ / / /_/ /_/ /  / /  / / /_/ / ,< /  __(__  )  / /_/ / /_/ (__  ) /_/ /")
    echo("     /_____/\\__,_/ /___/\\__, /  /_/  /_/\\__,_/_/|_|\\___/____/  /_____/\\__,_/____/\\__, /")
    echo("                       /____/                                                   /____/")
    echo("")
    echo("")
    echo("")
    echo("")
    echo("当前目录下（{}）共发现以下实验计划：".format(project_path))
    
    # 获取可选的项目名
    projects = os.listdir(os.path.join(project_path, "exp_plans/"))
    for i, project in enumerate(projects):
        echo("{}、 {}".format(i + 1, project.split(".")[0]), "#FF6AB3")
    
    # ---------------------------------------------------------------------------- #
    #                         获取实验计划                                     
    # ---------------------------------------------------------------------------- #
    echo("\n请选择要启动的实验计划：")
    exp_num = int(input())
    exp_plan_path = project_path + "/exp_plans/" + projects[exp_num - 1]
    
    # 读取计划命令列表
    ori_exp_plan = open(exp_plan_path, "r").readlines()
    cmd = ''
    cmd_list = []
    for idx, line in enumerate(ori_exp_plan):
        if line == "\n":
            print(cmd)
            cmd_list.append(cmd)
            cmd = ''
        else:
            cmd += line.strip().replace("\n", "").replace("\\", " ")
    exp_plan = [cmd_list.strip() for line in exp_plan if line.strip()]
    echo("计划共启动 {} 个实验！\n".format(len(exp_plan)))
        
    
    for i, line in enumerate(exp_plan):
        log_path = os.path.join(project_path, "{}/{}.log".format(log_path, "{}".format(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))))
        
        parent_path = "/".join(log_path.split("/")[:-1])
        if not os.path.exists(parent_path):
            os.makedirs(parent_path)
        
        cmd = "nohup {} > {} 2>&1 &".format(line, log_path)
        echo("查看日志：tail -f {}".format(log_path))
        run_cmd(cmd, show_cmd=False)
            
        echo("\n实验 {} 已启动！".format(str(i + 1)), "#F48671")
        if i + 1 != exp_num:
            time.sleep(60 * 2)

    
    echo("\n所有实验均已启动！不如趁现在去喝杯咖啡！", "green")
    
