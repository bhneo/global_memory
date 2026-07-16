from global_memory.extraction import ExtractionService
from global_memory.repository import Repository

_, _, body = ExtractionService(Repository(".")).find("extraction_95c0d98bd7ac31b847b3caa6")
for needle in [
    "在这本书中，这位苏格兰精神病学家",
    "陷入癫狂将是一种了断",
    "1913年，在第一次世界大战前夕",
    "并认为他在自己的癫狂中找到了",
    "精神病症（psychosis）和超智识",
    "在过去的50年",
    "另一次，当第欧根尼被问及来自何处时",
]:
    i = body.find(needle)
    if i < 0:
        print("MISSING", needle)
    else:
        print(repr(body[i : i + 120]))
        print("---")
