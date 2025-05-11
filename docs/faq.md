# 常见问题解答 (FAQ)

## 1. 安装与配置

### Q: 安装时遇到"GDAL not found"错误怎么办？
A: 这是geopandas的依赖问题。请先安装系统级GDAL库：
```bash
# Ubuntu/Debian
sudo apt-get install gdal-bin libgdal-dev

# MacOS
brew install gdal

# Windows
conda install gdal
```

### Q: 如何启用交互式可视化功能？
A: 需要安装额外依赖：
```bash
pip install ipywidgets
```
然后在Jupyter Notebook中运行：
```python
from src.geospatial.visualization import InteractiveMapVisualizer
visualizer = InteractiveMapVisualizer()
visualizer.create_interactive_map(graph)
```

## 2. 使用问题

### Q: 如何提高路径规划的性能？
A: 可以尝试以下方法：
1. 使用A*算法代替Dijkstra
2. 启用结果缓存：
```python
pathfinder = PathFinder(graph, use_cache=True)
```
3. 简化图结构（合并相邻节点）

### Q: 坐标匹配不准确怎么办？
A: 调整匹配参数：
```python
# 增大搜索半径
matcher = CoordinateMatcher(roads, max_distance=100.0)

# 提高匹配精度
matcher = CoordinateMatcher(roads, precision=0.00001)
```

## 3. 数据处理

### Q: 如何导入自定义地理数据？
A: 推荐步骤：
1. 将数据转换为GeoJSON格式
2. 使用GeoJSONReader加载：
```python
graph = GeoJSONReader.load_graph("custom_data.geojson")
```
3. 或实现自定义Reader继承BaseReader

### Q: 处理大型数据集内存不足？
A: 使用分块处理：
```python
# 分块加载
reader = GeoJSONReader(chunk_size=1000)
for chunk in reader.iter_load("large_data.geojson"):
    process(chunk)
```

## 4. 错误排查

### Q: "NodeNotFoundError"错误如何解决？
A: 检查：
1. 节点ID是否正确
2. 是否已添加该节点
3. 大小写是否匹配
4. 使用graph.has_node()检查节点存在性

### Q: 可视化不显示或显示异常？
A: 排查步骤：
1. 检查坐标范围是否合理
2. 验证数据是否有效：
```python
print(graph.nodes)  # 检查节点
print(graph.edges)  # 检查边
```
3. 尝试简化可视化内容

## 5. 性能优化

### Q: 如何优化大规模图的可视化？
A: 建议：
1. 使用简化版本：
```python
visualizer.plot_graph(graph, simplify=True)
```
2. 只显示特定区域
3. 降低渲染精度

### Q: 路径规划太慢怎么办？
A: 优化建议：
1. 预计算和缓存常用路径
2. 使用空间索引加速搜索
3. 限制搜索深度：
```python
pathfinder.find_shortest_path(..., max_depth=100)
```

## 6. 扩展开发

### Q: 如何添加新的路径规划算法？
A: 实现步骤：
1. 创建算法类继承BasePathFinder
2. 实现find_path方法
3. 注册到系统中：
```python
PathFinder.register_algorithm('my_algo', MyPathFinder)
```

### Q: 如何支持新的文件格式？
A: 开发指南：
1. 实现Reader接口
2. 处理格式转换
3. 添加文件扩展名自动检测
4. 更新IO模块的工厂方法

## 7. 其他问题

### Q: 如何贡献代码？
A: 请参考[贡献指南](./contributing.md)：
1. Fork仓库
2. 创建特性分支
3. 提交Pull Request

### Q: 在哪里报告问题？
A: 通过GitHub Issues:
https://github.com/your-repo/geospatial-awareness/issues

请提供：
1. 错误信息
2. 重现步骤
3. 环境信息
4. 相关代码片段