# 可视化模块 API 文档

## MapVisualizer 类

静态地图可视化工具。

### 初始化
```python
MapVisualizer(figsize: Tuple[int, int] = (10, 8), dpi: int = 100)
```

### 主要方法

#### `plot_graph(graph: LocationGraph, **kwargs) -> None`
绘制地理空间图

可选参数：
- `show_node_labels`: 是否显示节点标签 (默认False)
- `show_edge_labels`: 是否显示边标签 (默认False)
- `node_size`: 节点大小 (默认30)
- `edge_width`: 边宽度 (默认1.0)

#### `plot_path(path_coords: List[Coordinate], **kwargs) -> None`
绘制路径

可选参数：
- `color`: 路径颜色 (默认'blue')
- `linewidth`: 线宽 (默认2.0)
- `alpha`: 透明度 (默认1.0)
- `label`: 图例标签 (默认'Path')

#### `plot_observer(observer: Observer, **kwargs) -> None`
绘制观察者

可选参数：
- `color`: 颜色 (默认'blue')
- `marker`: 标记样式 (默认'o')
- `size`: 大小 (默认100)

#### `save_figure(file_path: str, dpi: Optional[int] = None) -> None`
保存图形到文件

#### `show() -> None`
显示图形

## InteractiveMapVisualizer 类

交互式地图可视化工具（继承自MapVisualizer）。

### 主要方法

#### `create_interactive_map(graph: LocationGraph) -> Widget`
创建交互式地图控件

功能：
- 动态显示/隐藏节点和边
- 调整节点大小和边宽度
- 控制标签显示

#### `create_path_explorer(graph: LocationGraph, pathfinder: PathFinder) -> Widget`
创建路径探索控件

功能：
- 选择起点和终点
- 选择算法和权重类型
- 可视化路径结果
- 显示路径信息

### 使用示例
```python
# 创建交互式地图
visualizer = InteractiveMapVisualizer()
interactive_map = visualizer.create_interactive_map(graph)

# 在Jupyter中显示
from IPython.display import display
display(interactive_map)
```