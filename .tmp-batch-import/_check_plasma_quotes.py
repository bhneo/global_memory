from global_memory.extraction import ExtractionService
from global_memory.repository import Repository

_, _, body = ExtractionService(Repository(".")).find("extraction_275083c46743bccdd54985ba")
pairs = [
    ("作为物质的第四态，等离子体物质", "典型的如恒星物质。"),
    ("低温等离子体只有几十度", "例如等离子体电视屏幕。"),
    ("当不均匀的磁场呈现两头强中间弱时", "因此这种磁场结构被形象的称作为磁瓶。"),
    ("该设备最初由苏联的研究人员于上世纪50年代发明", "它也是一种螺旋形状磁场。"),
    ("基于以上这种扭转磁场的装置被称作仿星器（stellarator）", "重要的反应堆设备候选者。"),
    ("目前世界上约有60台托卡马克和10台仿星器在运行。", "这两种反应器都有一定的优点。"),
]
for a, b in pairs:
    ok = a in body and b in body
    print(ok, a[:30], "->", b[:20])
