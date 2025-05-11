# 核心模块 API 文档

## LocationGraph 类

地理空间网络图的核心数据结构。

### 方法

#### `add_node(node: POI) -> None`
添加POI节点到图中

#### `add_edge(edge: Road) -> None` 
添加道路边到图中

#### `find_shortest_path(start_node_id: str, end_node_id: str, algorithm: str = 'dijkstra') -> Dict`
查找最短路径，支持多种算法：
- 'dijkstra' (默认)
- 'a_star'
- 'bfs'

#### `match_coordinate(coord: Coordinate) -> Dict`
将坐标匹配到最近的道路

[查看更多方法...](#)

## Observer 类

地理空间环境中的智能体观察者。

### 方法

#### `update_location(new_location: Coordinate) -> None`
更新观察者位置

#### `update_perception() -> Dict`
更新环境感知结果

#### `get_visible_pois() -> List[POI]`
获取可见的POI列表

[查看更多方法...](#)