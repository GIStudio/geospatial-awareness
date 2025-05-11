# 贡献指南

欢迎参与地理空间感知系统的开发！请仔细阅读以下指南。

## 1. 开发环境设置

1. 克隆仓库：
```bash
git clone https://github.com/your-repo/geospatial-awareness.git
cd geospatial-awareness
```

2. 创建开发分支：
```bash
git checkout -b dev
```

3. 安装开发依赖：
```bash
pip install -r requirements-dev.txt
```

4. 安装预提交钩子：
```bash
pre-commit install
```

## 2. 代码规范

### 代码风格
- 遵循PEP 8规范
- 使用Black格式化代码
- 类型注解(Type hints)强制要求
- 文档字符串(Docstrings)强制要求

### 提交信息
使用约定式提交(Conventional Commits)：
```
<类型>[可选 范围]: <描述>

[可选 正文]

[可选 脚注]
```

示例：
```
feat(core): add shortest path caching

Add LRU cache for shortest path results to improve performance

Closes #123
```

## 3. 分支管理

- `main`: 稳定生产分支
- `dev`: 主要开发分支
- `feature/*`: 新特性开发
- `bugfix/*`: 问题修复

分支命名示例：
```
feature/pathfinding-optimization
bugfix/issue-123
```

## 4. 测试要求

1. 新代码必须包含单元测试
2. 测试覆盖率不低于80%
3. 运行所有测试：
```bash
pytest --cov=src tests/
```

4. 生成覆盖率报告：
```bash
pytest --cov=src --cov-report=html tests/
```

## 5. 文档更新

1. 新功能必须更新API文档
2. 重大变更需更新README和设计文档
3. 示例代码保持同步更新

## 6. Pull Request流程

1. Fork主仓库
2. 创建特性分支
3. 提交代码变更
4. 确保测试通过
5. 提交Pull Request到`dev`分支
6. 通过CI检查和代码审查

## 7. 开发流程示例

1. 创建特性分支：
```bash
git checkout -b feature/awesome-feature
```

2. 开发并提交代码：
```bash
git add .
git commit -m "feat(module): add awesome feature"
git push origin feature/awesome-feature
```

3. 创建Pull Request：
- 在GitHub界面操作
- 描述变更内容和影响
- 关联相关Issue

4. 解决审查意见：
- 根据反馈修改代码
- 重新测试
- 追加提交或压缩提交

## 联系方式

如有问题，请联系：
- 项目维护者: maintainer@example.com
- GitHub Issues: https://github.com/your-repo/geospatial-awareness/issues