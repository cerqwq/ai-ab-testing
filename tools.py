"""
AI A/B Testing - AI A/B测试工具
支持实验设计、统计分析、结果解读
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIABTestingTools:
    """
    AI A/B测试工具
    支持：设计、分析、解读
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_experiment(self, hypothesis: str, metrics: List[str]) -> Dict:
        """设计实验"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        metrics_text = ", ".join(metrics)

        prompt = f"""请设计A/B测试实验：

假设：{hypothesis}
指标：{metrics_text}

请返回JSON格式：
{{
    "hypothesis": "假设",
    "variants": ["变体"],
    "primary_metric": "主要指标",
    "secondary_metrics": ["次要指标"],
    "sample_size": "样本量",
    "duration": "测试时长",
    "significance_level": "显著性水平"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"experiment": content}

    def analyze_results(self, results: Dict) -> Dict:
        """分析结果"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        results_text = json.dumps(results, ensure_ascii=False)

        prompt = f"""请分析A/B测试结果：

{results_text}

请返回JSON格式：
{{
    "winner": "赢家",
    "confidence": "置信度",
    "lift": "提升幅度",
    "interpretation": "结果解读",
    "recommendations": ["建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def calculate_sample_size(self, baseline_rate: str, mde: str, significance: float = 0.05) -> Dict:
        """计算样本量"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请计算A/B测试所需样本量：

基准转化率：{baseline_rate}
最小可检测效应：{mde}
显著性水平：{significance}

请返回JSON格式：
{{
    "sample_size_per_variant": "每组样本量",
    "total_sample_size": "总样本量",
    "duration_estimate": "测试时长估算",
    "assumptions": ["假设条件"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"sample_size": content}

    def suggest_improvements(self, current_metrics: Dict, goal: str) -> Dict:
        """建议改进"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        metrics_text = json.dumps(current_metrics, ensure_ascii=False)

        prompt = f"""请根据当前指标建议改进：

当前指标：{metrics_text}
目标：{goal}

请返回JSON格式：
{{
    "experiments": [
        {{"name": "实验名", "hypothesis": "假设", "expected_impact": "预期影响"}}
    ],
    "priority": "优先级排序"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"improvements": content}

    def generate_report(self, experiment: Dict, results: Dict) -> str:
        """生成报告"""
        if not self.client:
            return "LLM客户端未配置"

        exp_text = json.dumps(experiment, ensure_ascii=False)
        res_text = json.dumps(results, ensure_ascii=False)

        prompt = f"""请生成A/B测试报告：

实验：{exp_text}
结果：{res_text}

要求：
1. 执行摘要
2. 方法论
3. 结果分析
4. 结论和建议"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def design_multivariate_test(self, factors: List[str]) -> Dict:
        """设计多变量测试"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        factors_text = ", ".join(factors)

        prompt = f"""请设计多变量测试：

因素：{factors_text}

请返回JSON格式：
{{
    "factors": [
        {{"name": "因素", "levels": ["水平"]}}
    ],
    "combinations": "组合数",
    "design": "实验设计",
    "analysis": "分析方法"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"mvt": content}


def create_tools(**kwargs) -> AIABTestingTools:
    """创建A/B测试工具"""
    return AIABTestingTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI A/B Testing Tools")
    print()

    # 测试
    experiment = tools.design_experiment("新按钮颜色会提高点击率", ["点击率", "转化率"])
    print(json.dumps(experiment, ensure_ascii=False, indent=2))
