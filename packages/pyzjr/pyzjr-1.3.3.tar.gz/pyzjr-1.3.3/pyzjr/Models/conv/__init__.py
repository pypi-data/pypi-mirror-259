"""
收录或复现的其他改进的卷积
"""
from .Snake_Conv import DSConv
from .Depthwise_Conv import DepthSepConv
from .Partial_Conv import PartialConv

__all__ = ["DSConv", "DepthSepConv", "PartialConv"]