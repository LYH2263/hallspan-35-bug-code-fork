"""页侧投影：只从 plan（issues 派生）取数，禁止另写一套计数。

三口同码约定：行说明 / 违规列表 / 分类计数全部由 plan.issues 派生。
本模块不做任何计数，只做投影与透传；任何“页侧另算”都视为冒码。
"""
from __future__ import annotations


def mix_stats(data: dict, stats: dict | None = None) -> dict:
    """统计口径唯一来源：plan.stats（由 issues 派生）。原样透传，不加不减。"""
    return dict(stats or data.get("stats") or {})


def mix_violations(data: dict) -> dict:
    """违规/未排列投影：直接取 plan 的 issues/unplaced，不拼造额外条目。"""
    return {
        "issues": list(data.get("issues") or []),
        "unplaced": list(data.get("unplaced") or []),
    }
