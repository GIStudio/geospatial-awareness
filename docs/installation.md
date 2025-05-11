# 安装指南

## 系统要求

- Python 3.8+
- pip 20.0+
- 推荐使用虚拟环境

## 安装步骤

### 基础安装

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

3. 安装核心依赖：
```bash
pip install -r requirements.txt
```

### 可选组件安装

1. Shapefile支持：
```bash
pip install geopandas
```

2. 交互式可视化：
```bash
pip install ipywidgets
```

3. 开发工具：
```bash
pip install -r requirements-dev.txt
```

## 验证安装

运行测试脚本验证安装：
```bash
python -m pytest tests/
```

或执行示例程序：
```bash
python examples/basic_example.py
```

## 常见安装问题

### 缺少GDAL依赖
在安装geopandas时可能出现的问题：
```bash
# Ubuntu/Debian
sudo apt-get install gdal-bin libgdal-dev

# MacOS
brew install gdal
```

### 可视化问题
如果matplotlib显示有问题，尝试：
```bash
pip install --upgrade matplotlib
```