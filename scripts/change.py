import os

def process_file_replacements():
    # 读取数据文件
    with open('data.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 处理每一行数据
    for line in lines:
        parts = line.strip().split('| ')
        if len(parts) < 4:
            continue
            
        # 解析数据
        en_path = '..' + parts[0].replace('文档路径 = ', '').strip()
        title = parts[1].replace('标题 = ', '').strip()
        wrong_url = parts[2].replace('错误的url = ', '').strip()
        
        # 构造中文路径
        zh_path = en_path.replace('/en-US/', '/zh-CN/')
        
        try:
            # 读取英文文件
            with open(en_path, 'r', encoding='utf-8') as f:
                en_content = f.read()
                
            # 读取中文文件    
            with open(zh_path, 'r', encoding='utf-8') as f:
                zh_content = f.read()
                
            # 在中文内容中查找标题对应的链接
            zh_lines = zh_content.split('\n')
            new_url = None
            
            for line in zh_lines:
                if f'[{title}]' in line:
                    # 提取链接
                    start = line.find('](') + 2
                    end = line.find(')', start)
                    if start > 1 and end > start:
                        new_url = line[start:end]
                        break
            
            if new_url:
                # 检查new_url是否指向存在的文件
                # 获取当前文件的目录路径
                current_dir = os.path.dirname(os.path.abspath(en_path))
                target_path = os.path.normpath(os.path.join(current_dir, new_url))
                
                if os.path.exists(target_path):
                    # 如果文件存在，执行替换
                    updated_content = en_content.replace(wrong_url, new_url)
                    print(f"new_url:{new_url}")
                else:
                    # 如果文件不存在，删除包含wrong_url的行
                    lines = en_content.split('\n')
                    updated_content = '\n'.join(line for line in lines if wrong_url not in line)
                    print(f"Removed line containing {wrong_url} because target file does not exist")
                
                # 写回英文文件
                with open(en_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                    
                print(f"Updated {en_path}")
            else:
                print(f"Could not find matching title '{title}' in {zh_path}")
                
        except FileNotFoundError as e:
            print(f"File not found: {e.filename}")
        except Exception as e:
            print(f"Error processing {en_path}: {str(e)}")

if __name__ == "__main__":
    process_file_replacements()