"""
基本示例 - 展示地理空间感知系统的基本功能
"""
import os
import sys
import math
import random
from uuid import uuid4

# 添加项目根目录到Python路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.geospatial.entities.coordinate import Coordinate
from src.geospatial.entities.poi import POI
from src.geospatial.entities.road import Road
from src.geospatial.core.graph import LocationGraph
from src.geospatial.core.observer import Observer
from src.geospatial.algorithms.pathfinding import PathFinder
from src.geospatial.algorithms.perception import PerceptionEngine
from src.geospatial.visualization.map_visualizer import MapVisualizer
from src.geospatial.io.geojson_reader import GeoJSONReader


def create_sample_graph() -> LocationGraph:
    """创建一个示例地理空间图"""
    print("创建示例地理空间图...")
    
    graph = LocationGraph()
    
    # 创建一些POI节点
    pois = [
        POI(Coordinate(39.9075, 116.3972), poi_id="node1", name="天安门", poi_type="landmark"),
        POI(Coordinate(39.9087, 116.4077), poi_id="node2", name="故宫", poi_type="landmark"),
        POI(Coordinate(39.9163, 116.3907), poi_id="node3", name="北海公园", poi_type="park"),
        POI(Coordinate(39.9171, 116.4038), poi_id="node4", name="景山公园", poi_type="park"),
        POI(Coordinate(39.9073, 116.3913), poi_id="node5", name="国家大剧院", poi_type="theater"),
        POI(Coordinate(39.9046, 116.4074), poi_id="node6", name="王府井", poi_type="shopping"),
        POI(Coordinate(39.9100, 116.4040), poi_id="node7", name="中心交叉口", poi_type="junction"),
        POI(Coordinate(39.9130, 116.3970), poi_id="node8", name="西北角", poi_type="junction"),
        POI(Coordinate(39.9130, 116.4070), poi_id="node9", name="东北角", poi_type="junction"),
        POI(Coordinate(39.9060, 116.3970), poi_id="node10", name="西南角", poi_type="junction"),
        POI(Coordinate(39.9060, 116.4070), poi_id="node11", name="东南角", poi_type="junction"),
    ]
    
    # 添加POI节点到图中
    for poi in pois:
        graph.add_node(poi)
    
    # 创建一些道路
    roads = [
        # 外围道路
        Road("node8", "node9", [pois[7].coordinate, pois[8].coordinate], 
             road_id="road1", name="北路", road_type="primary"),
        Road("node9", "node11", [pois[8].coordinate, pois[10].coordinate], 
             road_id="road2", name="东路", road_type="primary"),
        Road("node11", "node10", [pois[10].coordinate, pois[9].coordinate], 
             road_id="road3", name="南路", road_type="primary"),
        Road("node10", "node8", [pois[9].coordinate, pois[7].coordinate], 
             road_id="road4", name="西路", road_type="primary"),
        
        # 内部道路
        Road("node1", "node7", [pois[0].coordinate, pois[6].coordinate], 
             road_id="road5", name="中轴路北段", road_type="secondary"),
        Road("node7", "node2", [pois[6].coordinate, pois[1].coordinate], 
             road_id="road6", name="东宫路", road_type="secondary"),
        Road("node7", "node3", [pois[6].coordinate, pois[2].coordinate], 
             road_id="road7", name="北海路", road_type="tertiary"),
        Road("node7", "node4", [pois[6].coordinate, pois[3].coordinate], 
             road_id="road8", name="景山路", road_type="tertiary"),
        Road("node7", "node5", [pois[6].coordinate, pois[4].coordinate], 
             road_id="road9", name="剧院路", road_type="tertiary"),
        Road("node7", "node6", [pois[6].coordinate, pois[5].coordinate], 
             road_id="road10", name="商业街", road_type="tertiary"),
        
        # 连接外围道路
        Road("node1", "node10", [pois[0].coordinate, pois[9].coordinate], 
             road_id="road11", name="西南连接路", road_type="residential"),
        Road("node1", "node11", [pois[0].coordinate, pois[10].coordinate], 
             road_id="road12", name="东南连接路", road_type="residential"),
        Road("node2", "node9", [pois[1].coordinate, pois[8].coordinate], 
             road_id="road13", name="东北连接路", road_type="residential"),
        Road("node3", "node8", [pois[2].coordinate, pois[7].coordinate], 
             road_id="road14", name="西北连接路", road_type="residential"),
    ]
    
    # 添加道路到图中
    for road in roads:
        graph.add_edge(road)
    
    print(f"创建了 {len(pois)} 个POI节点和 {len(roads)} 条道路")
    
    return graph


def save_sample_graph(graph: LocationGraph, file_path: str) -> None:
    """将示例图保存到GeoJSON文件"""
    print(f"保存地理空间图到 {file_path}...")
    
    # 确保目录存在
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # 保存图
    GeoJSONReader.save_graph(graph, file_path)
    
    print(f"地理空间图已保存到 {file_path}")


def load_graph_from_file(file_path: str) -> LocationGraph:
    """从GeoJSON文件加载地理空间图"""
    print(f"从 {file_path} 加载地理空间图...")
    
    # 加载图
    graph = GeoJSONReader.load_graph(file_path)
    
    print(f"已加载地理空间图，包含 {len(graph.nodes)} 个节点和 {len(graph.edges)} 条边")
    
    return graph


def find_and_visualize_path(graph: LocationGraph, start_id: str, end_id: str) -> None:
    """查找并可视化从起点到终点的路径"""
    print(f"查找从 {start_id} 到 {end_id} 的路径...")
    
    # 创建路径规划器
    pathfinder = PathFinder(graph)
    
    # 查找最短路径
    try:
        path_result = pathfinder.find_shortest_path(start_id, end_id)
        
        print(f"找到路径，长度: {path_result['total_distance']:.1f} 米，预计时间: {path_result['total_time'] * 60:.1f} 分钟")
        print(f"路径: {' -> '.join(path_result['path'])}")
        
        # 创建可视化器
        visualizer = MapVisualizer()
        
        # 绘制图和路径
        visualizer.create_figure()
        visualizer.plot_graph(graph)
        visualizer.plot_path(path_result['coordinates'])
        visualizer.add_legend()
        visualizer.add_scale_bar()
        visualizer.add_north_arrow()
        
        # 保存图形
        os.makedirs('output', exist_ok=True)
        visualizer.save_figure('output/path_visualization.png')
        
        # 查找备选路径
        alt_paths = pathfinder.find_alternative_paths(start_id, end_id, 3)
        
        if len(alt_paths) > 1:
            print(f"找到 {len(alt_paths)} 条备选路径")
            
            # 创建新的可视化器
            alt_visualizer = MapVisualizer()
            alt_visualizer.create_figure()
            alt_visualizer.plot_graph(graph)
            
            # 绘制所有备选路径
            path_coords = [path['coordinates'] for path in alt_paths]
            labels = [f"路径 {i+1} ({path['total_distance']:.1f}m)" for i, path in enumerate(alt_paths)]
            alt_visualizer.plot_multiple_paths(path_coords, labels=labels)
            
            alt_visualizer.add_legend()
            alt_visualizer.add_scale_bar()
            alt_visualizer.add_north_arrow()
            
            # 保存图形
            alt_visualizer.save_figure('output/alternative_paths.png')
    
    except Exception as e:
        print(f"查找路径失败: {str(e)}")


def simulate_observer(graph: LocationGraph) -> None:
    """模拟观察者在地理空间中的感知"""
    print("模拟观察者感知...")
    
    # 创建观察者
    observer_location = Coordinate(39.9090, 116.4000)
    observer = Observer(observer_location, heading=45.0, perception_range=200.0, fov=120.0)
    
    # 创建感知引擎
    perception_engine = PerceptionEngine(graph)
    
    # 更新观察者感知
    perception_result = perception_engine.update_observer(observer)
    
    print(f"观察者位置: {observer.location}")
    print(f"观察者朝向: {observer.heading}°")
    print(f"可见POI数量: {len(perception_result['visible_pois'])}")
    print(f"可见道路数量: {len(perception_result['visible_roads'])}")
    
    if perception_result['matched_road']:
        road = perception_result['matched_road']['road']
        distance = perception_result['matched_road']['distance']
        print(f"观察者位于道路 '{road.name}' 上，距离: {distance:.1f} 米")
    
    # 可视化观察者感知
    visualizer = MapVisualizer()
    visualizer.create_figure()
    visualizer.plot_graph(graph)
    visualizer.plot_observer(observer)
    
    # 保存图形
    visualizer.save_figure('output/observer_perception.png')
    
    # 模拟观察者移动
    print("\n模拟观察者移动...")
    
    # 创建一条模拟轨迹
    trajectory = []
    current_location = observer_location
    
    # 向东北方向移动
    for i in range(10):
        # 每步移动约10米
        lat_step = 0.0001  # 约11米
        lon_step = 0.0001  # 约9米
        
        new_lat = current_location.latitude + lat_step
        new_lon = current_location.longitude + lon_step
        new_location = Coordinate(new_lat, new_lon)
        
        trajectory.append(new_location)
        current_location = new_location
    
    # 分析轨迹
    print("分析观察者轨迹...")
    trajectory_analysis = perception_engine.analyze_trajectory(trajectory)
    
    print(f"轨迹点数量: {len(trajectory)}")
    print(f"匹配到道路上的点数量: {sum(1 for match in trajectory_analysis['matched_trajectory'] if match is not None)}")
    print(f"检测到的转弯事件数量: {len(trajectory_analysis['turn_events'])}")
    print(f"检测到的路口穿越事件数量: {len(trajectory_analysis['junction_crossings'])}")
    print(f"检测到的道路变更事件数量: {len(trajectory_analysis['road_changes'])}")
    
    # 可视化轨迹
    traj_visualizer = MapVisualizer()
    traj_visualizer.create_figure()
    traj_visualizer.plot_graph(graph)
    traj_visualizer.plot_trajectory(trajectory)
    
    # 绘制事件
    if trajectory_analysis['junction_crossings']:
        traj_visualizer.plot_events(trajectory_analysis['junction_crossings'], 'junction_crossing', 
                                  marker='*', color='green', size=150)
    
    if trajectory_analysis['turn_events']:
        traj_visualizer.plot_events(trajectory_analysis['turn_events'], 'turn', 
                                  marker='o', color='red', size=100)
    
    if trajectory_analysis['road_changes']:
        traj_visualizer.plot_events(trajectory_analysis['road_changes'], 'road_change', 
                                  marker='s', color='purple', size=100)
    
    # 保存图形
    traj_visualizer.save_figure('output/trajectory_analysis.png')


def main():
    """主函数"""
    print("地理空间感知系统基本示例")
    print("=" * 50)
    
    # 创建示例图
    graph = create_sample_graph()
    
    # 保存示例图
    geojson_path = 'output/sample_graph.geojson'
    save_sample_graph(graph, geojson_path)
    
    # 从文件加载图
    loaded_graph = load_graph_from_file(geojson_path)
    
    # 查找并可视化路径
    find_and_visualize_path(loaded_graph, "node1", "node4")
    
    # 模拟观察者
    simulate_observer(loaded_graph)
    
    print("\n示例完成，输出文件保存在 'output' 目录中")


if __name__ == "__main__":
    main()