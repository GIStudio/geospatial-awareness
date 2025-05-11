# 代码规范指南

## 1. 代码风格

### 通用规则
- 4空格缩进（不使用Tab）
- 每行不超过88个字符
- 运算符周围和逗号后加空格
- 类名使用大驼峰(CamelCase)
- 函数/变量使用小写加下划线(snake_case)

### 导入顺序
1. 标准库
2. 第三方库
3. 本地应用/库

每组导入之间空一行，按字母顺序排序：
```python
import os
import sys

import numpy as np
import pandas as pd

from src.geospatial.core.graph import LocationGraph
from src.geospatial.entities import Coordinate
```

## 2. 命名约定

| 类型 | 约定 | 示例 |
|------|------|------|
| 类 | 大驼峰 | `LocationGraph` |
| 异常 | 大驼峰+Error后缀 | `NodeNotFoundError` |
| 函数/方法 | 小写下划线 | `find_shortest_path` |
| 变量 | 小写下划线 | `node_list` |
| 常量 | 全大写 | `MAX_NODES` |
| 类型变量 | 大驼峰 | `T = TypeVar('T')` |

## 3. 文档字符串

### 模块文档字符串
```python
"""
模块简介

详细描述...
"""
```

### 类文档字符串
```python
class LocationGraph:
    """类简介
    
    详细描述...
    
    Attributes:
        nodes (Dict[str, POI]): 节点字典
        edges (Dict[str, Road]): 边字典
    """
```

### 函数文档字符串
```python
def find_shortest_path(start: str, end: str) -> List[str]:
    """查找最短路径
    
    Args:
        start: 起始节点ID
        end: 终止节点ID
        
    Returns:
        路径节点ID列表
        
    Raises:
        NodeNotFoundError: 如果节点不存在
    """
```

## 4. 类型注解

- 所有函数/方法必须包含类型注解
- 使用Python 3.8+类型语法
- 复杂类型使用`typing`模块

示例：
```python
from typing import Dict, List, Optional, Tuple

def match_coordinate(
    coord: Coordinate,
    max_distance: float = 50.0
) -> Optional[Dict[str, Any]]:
    ...
```

## 5. 测试规范

### 测试文件结构
```
tests/
    __init__.py
    test_core/
        test_graph.py
    test_entities/
        test_coordinate.py
```

### 测试类命名
```python
class TestLocationGraph(unittest.TestCase):
    ...
```

### 测试方法命名
```python
def test_add_node_success(self):
    ...
    
def test_add_node_with_invalid_input(self):
    ...
```

### 测试要求
- 每个测试用例独立
- 使用assert而不是print调试
- 包含边界条件测试
- 模拟外部依赖

## 6. 异常处理

### 自定义异常
```python
class GeospatialError(Exception):
    """基础异常类"""
    pass

class NodeNotFoundError(GeospatialError):
    """节点未找到异常"""
    def __init__(self, node_id):
        super().__init__(f"Node not found: {node_id}")
        self.node_id = node_id
```

### 异常使用
```python
try:
    graph.get_node(node_id)
except NodeNotFoundError as e:
    logger.error(f"Error accessing node: {e}")
    raise
```

## 7. 工具配置

### .editorconfig
```
[*.py]
indent_style = space
indent_size = 4
max_line_length = 88
```

### pre-commit配置
```yaml
repos:
- repo: https://github.com/psf/black
  rev: stable
  hooks:
    - id: black
      language_version: python3
- repo: https://github.com/PyCQA/flake8
  rev: 3.9.2
  hooks:
    - id: flake8
```