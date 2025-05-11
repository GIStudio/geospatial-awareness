# 快速开始指南

## 1. 基本概念

地理空间感知系统包含以下核心概念：

- **Coordinate**: 表示地理坐标(纬度,经度)
- **POI**: 兴趣点(Point of Interest)
- **Road**: 连接POI的道路
- **LocationGraph**: 由POI和Road组成的地理空间网络
- **Observer**: 在环境中移动的智能体

## 2. 典型工作流程

1. 创建或加载地理空间图
2. 添加/修改POI和Road
3. 执行路径规划或感知分析
4. 可视化结果

## 3. 完整示例

```python
# 导入必要模块
from src.geospatial.core.graph import LocationGraph
from src.geospatial.entities import Coordinate, POI, Road
from src.geospatial.algorithms.pathfinding import PathFinder
from src.geospatial.visualization.map_visualizer import MapVisualizer

# 1. 创建地理空间图
graph = LocationGraph()

# 2. 添加三个城市作为POI
beijing = POI(Coordinate(39.9042, 116.4074), "北京", "city")
shanghai = POI(Coordinate(31.2304, 121.4737), "上海", "city")
guangzhou = POI(Coordinate(23.1291, 113.2644), "广州", "city")

graph.add_node(beijing)
graph.add_node(shanghai)
graph.add_node(guangzhou)

# 3. 添加连接道路
graph.add_edge(Road("北京", "上海", [beijing.coordinate, shanghai.coordinate], 
                   name="京沪线", length=1200))
graph.add_edge(Road("上海", "广州", [shanghai.coordinate, guangzhou.coordinate], 
                   name="沪广线", length=1400))

# 4. 路径规划
pathfinder = PathFinder(graph)
path = pathfinder.find_shortest_path("北京", "广州")

print(f"从北京到广州的路径:")
print(f"- 途经: {' -> '.join(path['path'])}")
print(f"- 总距离: {path['total_distance']:.1f}公里")
print(f"- 预计时间: {path['total_time']*60:.1f}分钟")

# 5. 可视化
visualizer = MapVisualizer()
visualizer.plot_graph(graph)
visualizer.plot_path(path['coordinates'], color='red', linewidth=3)
visualizer.save_figure("output/journey.png")
```

## 4. 预期输出

### 控制台输出
```
从北京到广州的路径:
- 途经: 北京 -> 上海 -> 广州
- 总距离: 2600.0公里
- 预计时间: 26.0分钟
```

### 可视化输出
将生成一个PNG图像文件`journey.png`，显示：
- 三个城市节点(北京、上海、广州)
- 两条连接道路(京沪线、沪广线)
- 用红色粗线标记的路径

## 下一步
- 尝试修改示例中的坐标和参数
- 查看[示例代码](../examples/)获取更多灵感
- 阅读[API文档](./api/)了解详细功能