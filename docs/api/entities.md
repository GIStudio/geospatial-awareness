# 实体类 API 文档

## Coordinate 类

地理坐标表示类。

### 初始化
```python
Coordinate(latitude: float, longitude: float, elevation: Optional[float] = None)
```

### 属性
- `latitude`: 纬度 (度)
- `longitude`: 经度 (度) 
- `elevation`: 海拔高度 (米，可选)

### 方法
#### `to_tuple() -> Tuple[float, float]`
返回(经度, 纬度)元组

#### `distance_to(other: Coordinate) -> float`
计算到另一个坐标的距离(米)

## POI 类

兴趣点(Point of Interest)表示类。

### 初始化
```python
POI(coordinate: Coordinate, 
    poi_id: Optional[str] = None,
    name: str = "", 
    poi_type: str = "generic",
    properties: Dict = {})
```

### 属性
- `coordinate`: 坐标位置
- `poi_id`: 唯一标识符
- `name`: 名称
- `poi_type`: 类型
- `properties`: 额外属性字典

## Road 类

道路表示类。

### 初始化
```python
Road(start_node_id: str,
     end_node_id: str,
     coordinates: List[Coordinate],
     road_id: Optional[str] = None,
     name: str = "",
     road_type: str = "street",
     bidirectional: bool = True)
```

### 属性
- `start_node_id`: 起始节点ID
- `end_node_id`: 终止节点ID  
- `coordinates`: 坐标点列表
- `length`: 道路长度(米)
- `speed_limit`: 限速(km/h)

### 方法
#### `get_travel_time() -> float`
计算理论通行时间(小时)