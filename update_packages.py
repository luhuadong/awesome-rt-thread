"""
File: update_packages.py
Author: luhuadong
Date: 2024-05-12
Description: Update and generate RT-Thread package list.
"""

import os
import json

# 存放的数据列表
package_name = []
package_desc = []
url = []
license = []

package_dict = {'iot': 'IoT', 'ai': 'AI', 'language': 'Language', 'misc': 'Misc', 
                'multimedia': 'Multimedia', 'peripherals': 'Peripherals', 'security': 'Security', 
                'system': 'System', 'tools': 'Tools','signalprocess': 'Signal process'}

ignore_dirs = ['.git', '.github', '.vscode', 'arduino']
packages_dir = "~/.env/packages/packages"
output_file = 'rtthread_packages.md'
target_file = 'README.md'

def delete_packages(file_path):
    # 读取原始文件内容
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 查找 `## Packages` 行的索引
    packages_index = None
    for i, line in enumerate(lines):
        if line.strip() == '## Packages':
            packages_index = i
            break

    if packages_index is not None:
        # 查找下一个二级标题的索引
        next_heading_index = None
        for i in range(packages_index + 1, len(lines)):
            if lines[i].strip().startswith('## '):
                next_heading_index = i
                break

        if next_heading_index is not None:
            # 删除 `## Packages` 行到下一个二级标题之间的内容
            del lines[packages_index:next_heading_index]
            print("start: {}, next: {}".format(packages_index, next_heading_index))
        else:
            # 删除 `## Packages` 行到文件末尾的所有内容
            del lines[packages_index:]
            print("start: {}, end.".format(packages_index))

        # 将修改后的内容写回文件
        with open(file_path, 'w') as file:
            file.writelines(lines)

    return packages_index
        

def update_packages():
    group_name = []
    curren_name = []
    packages_root = os.path.expanduser(packages_dir)
    total_count = 0
    output_count = 0

    with open(output_file, 'w', encoding='utf-8') as file_object:
        file_object.write("## Packages\n\n")

        for root, dirs, files in os.walk(packages_root):
            
            if '.git' in root or 'arduino' in root:
                # print("!!! Ignore {}".format(os.path.basename(root)))
                continue

            for f in files:
                curren_name = os.path.basename(os.path.abspath(os.path.join(root, "..")))
                
                if os.path.splitext(f)[1] == '.json':
                    total_count = total_count + 1

                    if curren_name == 'arduino':
                        print("Skip " + curren_name)
                        continue
                    
                    if group_name != curren_name:
                        if curren_name in package_dict:
                            group_name = curren_name
                            file_object.write("\n")
                            file_object.write("### " + package_dict[group_name] + "\n\n")
                        elif curren_name == 'arduino':
                            print("Skip " + curren_name)
                            continue

                    package_name = os.path.basename(os.path.join(root))
                    json_path = os.path.join(root, f)

                    with open(json_path, 'r', encoding='utf-8') as json_file:
                        json_dict = json.load(json_file)

                        for dict in json_dict.items():

                            if dict[0] == "description":
                                package_desc = dict[1]

                                if ':' in package_desc:
                                    splitted_parts = package_desc.split(':', 1)
                                    if len(splitted_parts) > 1:
                                        package_desc = splitted_parts[1]

                                package_desc = package_desc.lstrip()
                                package_desc = package_desc.strip()
                                if not package_desc.endswith('.'):
                                    package_desc += '.'

                            if dict[0] == "license":
                                license = dict[1]

                            if dict[0] == "repository":
                                url = dict[1]

                    file_object.write("- [" + package_name + "](" + url + ") - " + package_desc + " `" + license + "`\n")
                    output_count = output_count + 1

        print("Update {} packages, total {}".format(output_count, total_count))


if __name__ == '__main__':
    line = delete_packages(target_file)
    update_packages()
