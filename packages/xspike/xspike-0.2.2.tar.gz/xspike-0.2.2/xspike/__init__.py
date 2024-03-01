import os
import ast



# 获取当前包的目录
package_dir = os.path.dirname(os.path.abspath(__file__))
# 定义一个函数来解析模块并找出公共对象
def find_public_objects(module_source):
    # 解析模块的抽象语法树
    tree = ast.parse(module_source)
    public_objects = []
    
    # 遍历所有的节点
    for node in ast.walk(tree):
        # 检查是否有一个类定义
        if isinstance(node, ast.ClassDef):
            # 类名是公共的
            public_objects.append(node.name)
        # 检查是否有一个函数定义
        elif isinstance(node, ast.FunctionDef):
            # 函数名是公共的
            public_objects.append(node.name)
        # 检查是否有一个赋值语句，可能是一个公共变量
        elif isinstance(node, ast.Assign):
            # 只考虑顶层的赋值语句
            if isinstance(node.targets[0], ast.Name):
                public_objects.append(node.targets[0].id)
    
    return public_objects
# 遍历当前包下的所有模块
for filename in os.listdir(package_dir):
    if filename.endswith('.py') and filename != '__init__.py':
        # 获取模块的完整路径
        full_path = os.path.join(package_dir, filename)
        # 读取模块的源代码
        with open(full_path, 'r', encoding='utf-8') as file:
            module_source = file.read()
        
        # 找出公共对象
        public_objects = find_public_objects(module_source)
        
        # 导入公共对象
        for obj_name in public_objects:
            # 构建模块的路径
            module_path = f"{__package__}.{filename[:-3]}"
            # 动态导入对象
            from importlib import import_module
            module = import_module(module_path)
            globals()[obj_name] = getattr(module, obj_name)
