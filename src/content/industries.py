# -*- coding: utf-8 -*-
"""Merged industry hook table. One concrete line per industry, used to keep
industry and service pages from reading interchangeably."""

from .industries_healthcare import H
from .industries_trades import T
from .industries_dtc import DT
from .industries_ps import P

INDUSTRY_HOOKS = {}
for _d in (H, T, DT, P):
    INDUSTRY_HOOKS.update(_d)
