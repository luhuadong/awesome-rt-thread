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

package_list = ['iot', 'ai', 'language', 'misc', 'multimedia',
                'peripherals', 'security', 'system', 'tools','signalprocess']
ignore_dirs = ['.git', '.github', '.vscode', 'arduino']
packages_dir = "~/.env/packages/packages"
output_file = 'rtthread_packages.md'

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
                        if curren_name in package_list:
                            group_name = curren_name
                            file_object.write("\n")
                            file_object.write("### " + group_name + "\n\n")
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
    update_packages()
