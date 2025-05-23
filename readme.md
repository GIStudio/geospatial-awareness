# 🧠 地理空间感知系统（Geospatial Awareness System）完整项目模板

## 📌 项目概述

本项目旨在构建一个**地理空间感知系统**，帮助智能体（如自动驾驶车辆、机器人、无人机等）感知和理解其周围的地理环境。该系统支持从多种数据源（包括手动输入、GeoJSON 文件、Shapefile 文件）加载地理数据，并提供路径规划、可视化、感知等功能。

---

## 🧱 一、总体架构设计

### ✅ 核心目标
- **统一处理地理数据**：POI、道路网络、坐标点。
- **多数据源支持**：支持 `.geojson` 和 `.shp` 文件导入。
- **自动节点合并**：避免重复的 POI 节点。
- **路径规划与分析**：Dijkstra、A* 等算法。
- **可视化能力**：地图展示、路径高亮、热力图等。
- **模块化结构**：便于扩展、测试和维护。

---

## 📁 二、目录结构（推荐）

```
geospatial-awareness/
├── src/
│   └── geospatial/
│       ├── core/                 # 核心类定义
│       │   ├── graph.py          # LocationGraph 主类
│       │   ├── exceptions.py     # 自定义异常类
│       │   └── observer.py       # 智能体观察者
│       ├── entities/             # 数据实体定义
│       │   ├── coordinate.py     # 经纬度封装
│       │   ├── poi.py            # POI 类
│       │   └── road.py           # Road 类
│       ├── io/                   # 输入输出模块
│       │   ├── geojson_reader.py # GeoJSON 解析
│       │   └── shapefile_reader.py # Shapefile 解析
│       ├── algorithms/           # 路径规划算法
│       │   ├── pathfinding.py    # Dijkstra/A*
│       │   └── perception.py     # 地理感知逻辑
│       ├── visualization/        # 可视化模块
│       │   └── map_visualizer.py # 路网/路径可视化
│       └── utils/                # 工具函数
│           ├── distance.py       # 距离计算
│           └── geometry.py       # 几何操作
├── tests/                        # 单元测试
├── docs/                         # 文档（Sphinx）
├── examples/                     # 使用示例脚本
├── pyproject.toml                # 构建配置文件
├── requirements.txt              # 第三方依赖
└── README.md                     # 项目说明文档
```

---

## 🧩 三、核心类与模块设计

### 1. `LocationGraph`（src/geospatial/core/graph.py）

> 作为整个系统的主入口，负责管理 POI、Road、邻接表，并提供路径查找、数据导入、感知接口。

```python
from typing import Dict, List, Optional
from geospatial.entities.poi import POI
from geospatial.entities.road import Road
from geospatial.utils.geometry import CoordinateMatcher

class LocationGraph:
    def __init__(self):
        self.pois: Dict[str, POI] = {}
        self.roads: Dict[str, Road] = {}
        self.adjacency_list: Dict[str, Dict[str, str]] = {}
        self._coordinate_to_poi_id = CoordinateMatcher()  # 自动去重相同坐标的POI

    def add_poi(self, poi: POI) -> None:
        coord_key = (poi.coordinate.latitude, poi.coordinate.longitude)
        if coord_key in self._coordinate_to_poi_id:
            existing_id = self._coordinate_to_poi_id[coord_key]
            print(f"Coordinate conflict: '{poi.id}' merged with '{existing_id}'")
            return
        if poi.id in self.pois:
            raise ValueError(f"POI ID '{poi.id}' already exists")
        self.pois[poi.id] = poi
        self.adjacency_list[poi.id] = {}

    def add_road(self, road: Road) -> None:
        start_id = road.start_poi.id
        end_id = road.end_poi.id
        if start_id not in self.pois or end_id not in self.pois:
            raise ValueError("Start or End POI does not exist")
        self.roads[road.id] = road
        self.adjacency_list[start_id][end_id] = road.id
        if road.bidirectional:
            self.adjacency_list[end_id][start_id] = road.id

    def find_path(self, start_id: str, end_id: str) -> List[str]:
        # 调用 Dijkstra 或 A*
        from geospatial.algorithms.pathfinding import dijkstra_shortest_path
        return dijkstra_shortest_path(self, start_id, end_id)
```

---

### 2. `CoordinateMatcher`（utils/geometry.py）

> 支持坐标匹配与自动去重。

```python
from typing import Tuple, Dict

class CoordinateMatcher:
    def __init__(self, tolerance=1e-5):
        self.tolerance = tolerance
        self._map = {}  # {(lat, lon): poi_id}

    def __contains__(self, coord: Tuple[float, float]):
        for stored in self._map:
            if abs(stored[0] - coord[0]) < self.tolerance and \
               abs(stored[1] - coord[1]) < self.tolerance:
                return True
        return False

    def get_closest(self, coord: Tuple[float, float]) -> Optional[Tuple[float, float]]:
        for stored in self._map:
            if abs(stored[0] - coord[0]) < self.tolerance and \
               abs(stored[1] - coord[1]) < self.tolerance:
                return stored
        return None

    def add(self, coord: Tuple[float, float], poi_id: str):
        closest = self.get_closest(coord)
        if closest:
            return self._map[closest]
        self._map[coord] = poi_id
        return poi_id
```

---

### 3. `ShapefileReader`（io/shapefile_reader.py）

> 使用 `geopandas` 加载 `.shp` 文件并构建路网结构。

```python
import geopandas as gpd
from shapely.geometry import LineString
from geospatial.entities.poi import POI
from geospatial.entities.road import Road
from geospatial.entities.coordinate import Coordinate

class ShapefileReader:
    @staticmethod
    def read(shapefile_path: str) -> dict:
        gdf = gpd.read_file(shapefile_path)
        pois = []
        roads = []

        for _, row in gdf.iterrows():
            geom = row.geometry
            if isinstance(geom, LineString):
                coords = list(geom.coords)
                start_lon, start_lat = coords[0]
                end_lon, end_lat = coords[-1]

                start_poi = POI(
                    id=f"poi_{start_lat}_{start_lon}",
                    name="Node Start",
                    type="Intersection",
                    coordinate=Coordinate(start_lat, start_lon)
                )
                end_poi = POI(
                    id=f"poi_{end_lat}_{end_lon}",
                    name="Node End",
                    type="Intersection",
                    coordinate=Coordinate(end_lat, end_lon)
                )

                road = Road(
                    id=row.get('road_id', f"road_{len(roads)}"),
                    start_poi=start_poi,
                    end_poi=end_poi,
                    road_type=row.get('type', 'unknown'),
                    speed_limit=row.get('speed', 50),
                    bidirectional=True
                )
                pois.append(start_poi)
                pois.append(end_poi)
                roads.append(road)

        return {'pois': pois, 'roads': roads}
```

---

### 4. `Observer`（core/observer.py）

> 智能体观察者，可基于不同定位方式感知周围环境。

```python
from typing import Union
from geospatial.entities.poi import POI
from geospatial.entities.coordinate import Coordinate
from geospatial.core.graph import LocationGraph

class Observer:
    def __init__(self, position: Union[POI, Coordinate, str]):
        self.position = position

    def perceive(self, graph: LocationGraph):
        from geospatial.algorithms.perception import perceive_surroundings
        return perceive_surroundings(graph, self.position)
```

---

### 5. `perceive_surroundings`（algorithms/perception.py）

```python
from typing import Union
from geospatial.core.graph import LocationGraph
from geospatial.entities.poi import POI
from geospatial.entities.coordinate import Coordinate

def perceive_surroundings(
    graph: LocationGraph,
    position: Union[POI, Coordinate, str]
):
    # 实现感知逻辑
    nearby_pois = graph.find_nearby_pois(position)
    nearby_roads = graph.find_nearby_roads(position)
    return {
        "nearby_pois": nearby_pois,
        "nearby_roads": nearby_roads
    }
```

---

## 📦 四、依赖管理（requirements.txt）

```txt
geopandas>=0.13.0
shapely>=2.0.0
pyproj>=3.6.0
matplotlib>=3.7.0
networkx>=3.0
```

---

## 🧪 五、使用示例（examples/example_usage.py）

```python
from geospatial.core.graph import LocationGraph
from geospatial.io.shapefile_reader import ShapefileReader

graph = LocationGraph()

# 从 Shapefile 加载路网
result = ShapefileReader.read("data/roads.shp")
for poi in result['pois']:
    graph.add_poi(poi)
for road in result['roads']:
    graph.add_road(road)

# 查找路径
path = graph.find_path("poi_1", "poi_2")
print("Path:", path)
```

---

## 📘 六、文档生成（docs/）

使用 Sphinx + MyST Parser 支持 Markdown 编写 API 文档：

```bash
sphinx-quickstart
pip install sphinx myst-parser
```

---

## 🧪 七、测试框架（tests/）

使用 `pytest` 进行单元测试：

```bash
pytest tests/test_graph.py
```

---

## ✅ 八、总结

| 功能 | 实现方式 |
|------|----------|
| 自动节点合并 | 使用 `CoordinateMatcher` 去重相同坐标的 POI |
| 支持 GeoJSON 导入 | `GeoJsonReader` 解析 FeatureCollection |
| 支持 Shapefile 导入 | `ShapefileReader` 使用 `geopandas` |
| 路径规划 | `Dijkstra`, `A*` 算法实现 |
| 观察者模型 | `Observer` 抽象类感知周围信息 |
| 模块化设计 | 分为 core/io/entities/algorithms/visualization/utils |


