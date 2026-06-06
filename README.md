# 🧪 AI A/B Testing

AI A/B测试工具，支持实验设计、统计分析、结果解读。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🧪 实验设计
- 📊 结果分析
- 📏 样本量计算
- 💡 改进建议
- 📋 报告生成
- 🔬 多变量测试

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_ab_testing import create_tools

tools = create_tools()

# 实验设计
experiment = tools.design_experiment("新按钮会提高点击率", ["点击率", "转化率"])

# 结果分析
analysis = tools.analyze_results(results)

# 样本量计算
sample = tools.calculate_sample_size("5%", "10%", 0.05)

# 改进建议
improvements = tools.suggest_improvements(current_metrics, "提高转化")

# 报告生成
report = tools.generate_report(experiment, results)

# 多变量测试
mvt = tools.design_multivariate_test(["按钮颜色", "文案", "位置"])
```

## 📁 项目结构

```
ai-ab-testing/
├── tools.py       # A/B测试工具核心
└── README.md
```

## 📄 许可证

MIT License
