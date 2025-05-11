# IO 模块 API 文档

## GeoJSONReader 类

GeoJSON 格式数据读写器。

### 主要方法

#### `load_graph(file_path: str) -> LocationGraph`
从GeoJSON文件加载地理空间图

#### `save_graph(graph: LocationGraph, file_path: str) -> None`
将地理空间图保存为GeoJSON文件

#### `load_pois(file_path: str) -> List[POI]`
从GeoJSON文件加载POI列表

#### `save_pois(pois: List[POI], file_path: str) -> None`
将POI列表保存为GeoJSON文件

#### `load_roads(file_path: str) -> List[Road]`
从GeoJSON文件加载道路列表

#### `save_roads(roads: List[Road], file_path: str) -> None`
将道路列表保存为GeoJSON文件

## ShapefileReader 类

Shapefile 格式数据读写器。

### 主要方法

#### `load_graph(file_path: str) -> LocationGraph`
从Shapefile加载地理空间图

#### `save_graph(graph: LocationGraph, file_path: str) -> None`
将地理空间图保存为Shapefile

#### `load_pois(file_path: str) -> List[POI]`
从Shapefile加载POI列表

#### `save_pois(pois: List[POI], file_path: str) -> None`
将POI列表保存为Shapefile

#### `load_roads(file_path: str) -> List[Road]`
从Shapefile加载道路列表

#### `save_roads(roads: List[Road], file_path: str) -> None`
将道路列表保存为Shapefile

### 注意事项
1. 使用Shapefile功能需要安装geopandas库
2. Shapefile保存时会生成多个相关文件(.shp, .shx, .dbf等)
3. 属性字段名称可能会被截断或修改以适应Shapefile限制