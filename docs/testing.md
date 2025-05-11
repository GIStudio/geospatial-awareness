# 测试指南

## 1. 测试环境设置

1. 安装测试依赖：
```bash
pip install -r requirements-test.txt
```

2. 配置测试数据库（如需要）：
```bash
python tests/setup_test_db.py
```

## 2. 测试目录结构

```
tests/
├── __init__.py
├── conftest.py          # 测试配置和fixture
├── unit/                # 单元测试
│   ├── core/
│   │   ├── test_graph.py
│   │   └── test_observer.py
│   ├── entities/
│   │   ├── test_coordinate.py
│   │   └── test_poi.py
│   └── algorithms/
│       ├── test_pathfinding.py
│       └── test_perception.py
├── integration/         # 集成测试
│   ├── test_io.py
│   └── test_visualization.py
└── performance/         # 性能测试
    ├── test_graph_scale.py
    └── test_pathfinding.py
```

## 3. 单元测试规范

### 测试类结构
```python
import unittest
from src.geospatial.core.graph import LocationGraph

class TestLocationGraph(unittest.TestCase):
    """LocationGraph 单元测试"""
    
    def setUp(self):
        """每个测试前的初始化"""
        self.graph = LocationGraph()
        self.sample_poi = POI(...)
        
    def tearDown(self):
        """每个测试后的清理"""
        self.graph.clear()
        
    def test_add_node_success(self):
        """测试成功添加节点"""
        self.graph.add_node(self.sample_poi)
        self.assertIn(self.sample_poi.poi_id, self.graph.nodes)
        
    def test_add_node_duplicate(self):
        """测试添加重复节点"""
        self.graph.add_node(self.sample_poi)
        with self.assertRaises(ValueError):
            self.graph.add_node(self.sample_poi)
```

### 测试要求
- 每个测试方法只测试一个功能点
- 使用描述性的测试方法名
- 包含正面和负面测试用例
- 使用适当的断言方法

## 4. 集成测试指南

### 测试场景
```python
from src.geospatial.io.geojson_reader import GeoJSONReader

class TestGeoJSONIntegration(unittest.TestCase):
    """GeoJSON 集成测试"""
    
    def test_load_and_save_roundtrip(self):
        """测试加载保存往返"""
        original_graph = create_sample_graph()
        GeoJSONReader.save_graph(original_graph, "temp.geojson")
        loaded_graph = GeoJSONReader.load_graph("temp.geojson")
        
        self.assertEqual(len(original_graph.nodes), len(loaded_graph.nodes))
        self.assertEqual(len(original_graph.edges), len(loaded_graph.edges))
```

## 5. 性能测试方法

### 基准测试示例
```python
import timeit

class TestGraphPerformance(unittest.TestCase):
    """图性能测试"""
    
    def setUp(self):
        self.large_graph = create_large_graph(1000)  # 1000个节点
    
    def test_pathfinding_performance(self):
        """路径规划性能测试"""
        def test():
            pathfinder = PathFinder(self.large_graph)
            pathfinder.find_shortest_path("node1", "node999")
            
        elapsed = timeit.timeit(test, number=100)
        self.assertLess(elapsed, 5.0)  # 100次执行应小于5秒
```

## 6. 测试覆盖率

1. 运行测试并生成覆盖率报告：
```bash
pytest --cov=src --cov-report=html tests/
```

2. 覆盖率要求：
- 核心模块：>=90%
- 其他模块：>=80%
- 关键算法：100%

3. 查看报告：
```bash
open htmlcov/index.html  # Mac
start htmlcov/index.html # Windows
```

## 7. 常用测试模式

### Mock示例
```python
from unittest.mock import patch

class TestObserver(unittest.TestCase):
    """Observer 测试"""
    
    @patch('src.geospatial.algorithms.perception.PercepEngine')
    def test_update_perception(self, mock_engine):
        """测试感知更新"""
        observer = Observer(...)
        mock_engine.return_value.detect_nearby_pois.return_value = []
        
        result = observer.update_perception()
        
        self.assertEqual(result['visible_pois'], [])
        mock_engine.assert_called_once()
```

### Fixture示例
```python
# conftest.py
import pytest

@pytest.fixture
def sample_graph():
    graph = LocationGraph()
    # 添加测试数据
    return graph

# test_graph.py
def test_graph_operations(sample_graph):
    """使用fixture的测试"""
    assert len(sample_graph.nodes) == 10
```

## 8. 运行测试

1. 运行所有测试：
```bash
pytest tests/
```

2. 运行特定测试：
```bash
pytest tests/unit/core/test_graph.py -v
```

3. 带覆盖率运行：
```bash
pytest --cov=src tests/
```

4. 性能测试：
```bash
pytest tests/performance/ -m "not slow"
```