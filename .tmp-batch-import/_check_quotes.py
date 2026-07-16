from global_memory.extraction import ExtractionService
from global_memory.repository import Repository

_, _, body = ExtractionService(Repository(".")).find("extraction_b2b09f628e4a2fab15043dd6")
tests = [
    "正如2016年Scam Nation频道在YouTube上发布的一段视频所演示的那样",
    "当“真理元素”频道（Veritasium）的主持人德里克·穆勒（Derek Muller）",
    "“或许我注意到的最奇怪的事情就是对自己心脏的感觉，”他说。",
    "“参与了对视实验的人说，他们产生了前所未有的强烈感受，”",
    "研究人员在2015年的一项实验中也证明了类似的效果",
    "当然，这不是一门严谨的科学，因为每个人的大脑都会对奇怪的东西产生不一样的反应",
]
for text in tests:
    print(text in body, text[:50])
