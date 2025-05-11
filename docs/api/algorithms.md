# 算法模块 API 文档

## PathFinder 类

路径规划算法实现。

### 初始化
```python
PathFinder(graph: LocationGraph)
```

### 主要方法

#### `find_shortest_path(start_node_id: str, end_node_id: str, weight_type: str = 'distance') -> Dict`
查找最短路径，返回包含路径信息的字典：
```python
{
    'path': List[str],           # 节点ID列表
    'edges': List[Road],         # 道路列表
    'total_distance': float,     # 总距离(米)
    'total_time': float,         # 总时间(小时)
    'coordinates': List[Coordinate] # 路径坐标
}
```

支持权重类型：
- `distance` (默认): 基于距离
- `time`: 基于时间
- `custom`: 自定义权重

#### `find_fastest_path(start_node_id: str, end_node_id: str) -> Dict`
查找最快路径(基于时间权重)

#### `find_alternative_paths(start_node_id: str, end_node_id: str, num_alternatives: int = 3) -> List[Dict]`
查找多条备选路径

## PerceptionEngine 类

地理空间感知引擎。

### 初始化
```python
PerceptionEngine(graph: LocationGraph)
```

### 主要方法

#### `detect_nearby_pois(location: Coordinate, radius: float) -> List[Tuple[POI, float]]`
检测指定半径内的POI

#### `match_coordinate(coord: Coordinate) -> Dict`
将坐标匹配到最近的道路

#### `analyze_trajectory(trajectory: List[Coordinate]) -> Dict`
分析轨迹并检测事件(转弯、停止等)

#### `update_observer(observer: Observer) -> Dict`
更新观察者的环境感知