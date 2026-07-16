from global_memory.extraction import ExtractionService
from global_memory.repository import Repository

_, _, body = ExtractionService(Repository(".")).find("extraction_c4f0793e6fac8c18c8ed3a6f")
markers = [
    "为了描述这种连续变化的对称，我们就要借助李群",
    "李群的不可约表示空间的基",
    "规范群就是一个李群",
    "定义一个李群为一个集合",
    "只有紧致连通李群指数映射才是满射",
    "李代数只能反映李群的局部性质",
    "对于正方形的对称变换一共有8个元素",
]
for m in markers:
    print(m in body, m[:40])
