import os

def process_file_removals():
    # Read data file
    with open('data.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Process each line of data
    for line in lines:
        parts = line.strip().split('| ')
        if len(parts) < 4:
            continue
            
        # Parse data
        en_path = '..' + parts[0].replace('文档路径 = ', '').strip()
        title = parts[1].replace('标题 = ', '').strip()
        wrong_url = parts[2].replace('错误的url = ', '').strip()
        
        try:
            # Read the English file
            with open(en_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Find and remove the link while keeping the title text
            lines = content.split('\n')
            updated_lines = []
            
            for line in lines:
                if wrong_url and f']({wrong_url})' in line:
                    # Replace [any_title](wrong_url) with just the title text
                    updated_line = line.replace(f']({wrong_url})', '')
                    updated_line = updated_line.replace('[', '')
                    updated_lines.append(updated_line)
                elif wrong_url and f'<a href="{wrong_url}">' in line:
                    # Replace <a href="wrong_url">any_title</a> with just the title text
                    start_idx = line.find(f'<a href="{wrong_url}">')
                    end_idx = line.find('</a>', start_idx)
                    if end_idx != -1:
                        link_text = line[start_idx + len(f'<a href="{wrong_url}">'):end_idx]
                        updated_line = line[:start_idx] + link_text + line[end_idx + 4:]
                        updated_lines.append(updated_line)
                    else:
                        updated_lines.append(line)
                else:
                    updated_lines.append(line)
            
            updated_content = '\n'.join(updated_lines)
            
            # Write back to the file
            with open(en_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
                
            print(f"Updated {en_path} - Removed link for '{title}'")
                
        except FileNotFoundError as e:
            print(f"File not found: {e.filename}")
        except Exception as e:
            print(f"Error processing {en_path}: {str(e)}")

if __name__ == "__main__":
    process_file_removals()