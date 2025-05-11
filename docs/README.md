# 地理空间感知系统 (Geospatial Awareness System)

## 项目介绍

![系统架构图](./images/system_architecture.md)

地理空间感知系统是一个用于处理、分析和可视化地理空间数据的Python框架。它提供了以下核心功能：

- 地理空间网络建模（节点和边）
- 路径规划算法（Dijkstra, A*, BFS等）
- 环境感知和智能体模拟
- 多种数据格式支持（GeoJSON, Shapefile）
- 交互式可视化

典型应用场景：
- 智能交通系统
- 物流路径规划
- 城市基础设施管理
- 游戏和模拟环境

## 安装说明

### 系统要求
- Python 3.8+
- 推荐使用虚拟环境

### 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/your-repo/geospatial-awareness.git
cd geospatial-awareness
```

2. 创建并激活虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

### 可选依赖
对于Shapefile支持：
```bash
pip install geopandas
```

对于交互式可视化：
```bash
pip install ipywidgets
```

## 快速开始

5分钟快速体验系统功能：

```python
# 导入必要模块
from src.geospatial.core.graph import LocationGraph
from src.geospatial.entities import Coordinate
from src.geospatial.visualization.map_visualizer import MapVisualizer

# 创建简单地图
graph = LocationGraph()

# 添加三个地点
beijing = Coordinate(39.9042, 116.4074)
shanghai = Coordinate(31.2304, 121.4737)
guangzhou = Coordinate(23.1291, 113.2644)

graph.add_node(POI(beijing, "北京", "city"))
graph.add_node(POI(shanghai, "上海", "city")) 
graph.add_node(POI(guangzhou, "广州", "city"))

# 添加连接道路
graph.add_edge(Road("北京", "上海", [beijing, shanghai], name="京沪线"))
graph.add_edge(Road("上海", "广州", [shanghai, guangzhou], name="沪广线"))

# 可视化地图
visualizer = MapVisualizer()
visualizer.plot_graph(graph)
visualizer.show()

# 查找北京到广州的路径
from src.geospatial.algorithms.pathfinding import PathFinder
pathfinder = PathFinder(graph)
path = pathfinder.find_shortest_path("北京", "广州")
print(f"路径: {path['path']}, 距离: {path['total_distance']:.1f}公里")
```

## 使用示例

### 基本用法

```python
from src.geospatial.core.graph import LocationGraph
from src.geospatial.entities import Coordinate, POI, Road
from src.geospatial.algorithms.pathfinding import PathFinder

# 创建图
graph = LocationGraph()

# 添加POI节点
poi1 = POI(Coordinate(39.9075, 116.3972), name="天安门")
graph.add_node(poi1)

# 添加道路
road = Road("node1", "node2", [Coordinate(39.9075, 116.3972), Coordinate(39.9087, 116.4077)])
graph.add_edge(road)

# 路径规划
pathfinder = PathFinder(graph)
path = pathfinder.find_shortest_path("node1", "node2")
print(f"路径: {path['path']}, 距离: {path['total_distance']:.1f}米")
```

### 从文件加载数据

```python
from src.geospatial.io.geojson_reader import GeoJSONReader

# 从GeoJSON加载
graph = GeoJSONReader.load_graph("data/map.geojson")

# 保存图
GeoJSONReader.save_graph(graph, "output/saved_map.geojson")
```

### 可视化

```python
from src.geospatial.visualization.map_visualizer import MapVisualizer

visualizer = MapVisualizer()
visualizer.plot_graph(graph)
visualizer.plot_path(path['coordinates'])
visualizer.save_figure("output/path.png")
```

## API文档

完整的API文档请参考：

- [核心模块](docs/api/core.md)
- [实体类](docs/api/entities.md) 
- [算法](docs/api/algorithms.md)
- [IO模块](docs/api/io.md)
- [可视化](docs/api/visualization.md)

## 贡献指南

欢迎贡献！请遵循以下步骤：

1. Fork仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 发起Pull Request

## 许可证

本项目采用 MIT 许可证 - 详情请见 [LICENSE](LICENSE) 文件

## 联系方式

如有问题或建议，请联系：
- 邮箱: your-email@example.com
- GitHub Issues: https://github.com/your-repo/geospatial-awareness/issues