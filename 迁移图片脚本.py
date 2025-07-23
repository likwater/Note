import os
import re
import shutil
from datetime import datetime

def batch_update_image_paths(directory):
    """
    批量更新 Markdown 文件中的图片路径，支持标准格式和缩放后的 HTML 格式
    """
    # 统计处理结果
    results = {
        'files_processed': 0,
        'images_updated': 0,
        'backup_created': False,
        'markdown_images': 0,
        'html_images': 0
    }
    
    # 遍历目录中的所有 Markdown 文件
    for filename in os.listdir(directory):
        if not filename.lower().endswith('.md'):
            continue
            
        filepath = os.path.join(directory, filename)
        print(f"处理文件: {filename}")
        
        # 读取文件内容
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 统计原始图片数量
        original_count = content.count("../图片/")
        
        # 处理标准 Markdown 图片格式: ![alt](../图片/...)
        markdown_pattern = r'(!\[[^\]]*\]\()\.\./图片/([^\)]+\))'
        content, markdown_count = re.subn(
            markdown_pattern, 
            r'\1./图片/\2', 
            content
        )
        results['markdown_images'] += markdown_count
        
        # 处理缩放后的 HTML 图片格式: <img src="../图片/..." ...>
        html_pattern = r'(<img\s+[^>]*?src=")\.\./图片/([^">]+"[^>]*?>)'
        content, html_count = re.subn(
            html_pattern, 
            r'\1./图片/\2', 
            content
        )
        results['html_images'] += html_count
        
        # 写入修改后的内容
        if markdown_count > 0 or html_count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            results['files_processed'] += 1
            results['images_updated'] += (markdown_count + html_count)
            # 移动 .assets 文件夹（通过文件名定位）
            moved = move_assets_folder_by_filename(filename, os.path.dirname(filepath))
            print(f"  → 更新了 {markdown_count} 个标准图片和 {html_count} 个缩放图片")
            print(f"  → 移动了 {moved} 个 .assets 文件夹")
        else:
            print("  → 未发现需要更新的图片路径")
    
    return results

def move_assets_folder_by_filename(filename, md_dir):
    # 通过 Markdown 文件名定位 .assets 文件夹
    base_name = os.path.splitext(filename)[0]
    old_folder = os.path.normpath(os.path.join(md_dir, '..', '图片', f'{base_name}.assets'))
    new_folder = os.path.normpath(os.path.join(md_dir, '图片', f'{base_name}.assets'))
    print(f"尝试移动文件夹: {old_folder} -> {new_folder}")
    moved = 0
    if os.path.exists(old_folder):
        # 如果目标已存在，先删除再移动，避免shutil.move报错
        if os.path.exists(new_folder):
            shutil.rmtree(new_folder)
        shutil.move(old_folder, new_folder)
        print("  成功移动文件夹")
        moved = 1
    else:
        print("  源文件夹不存在")
    return moved

if __name__ == "__main__":
    print("Typora 图片路径迁移工具")
    print("=" * 50)
    
    # 设置要处理的目录（脚本所在目录）
    target_directory = os.path.dirname(os.path.abspath(__file__))
    
    print(f"将处理目录: {target_directory}")
    
    results = batch_update_image_paths(target_directory)
    
    print("\n处理完成!")
    print("=" * 50)
    print(f"已处理文件数: {results['files_processed']}")
    print(f"已更新图片总数: {results['images_updated']}")
    print(f"  → 标准 Markdown 图片: {results['markdown_images']}")
    print(f"  → HTML 缩放图片: {results['html_images']}")