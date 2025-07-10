from pydantic import BaseModel, Field
from typing import List


class XiaoHongShu(BaseModel):
    titles: List[str] = Field(description="产出的5个小红书标题", min_items=5, max_items=5)
    content: str = Field(description="生成的小红书正文")