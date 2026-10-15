from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


class EmailRequest(BaseModel):
    """用户发来的邮件"""
    sender: str = Field(..., description="发件人邮箱")
    subject: str = Field(..., description="邮件主题")
    body: str = Field(..., description="邮件正文")


class EmailIntent(BaseModel):
    """解析后的邮件意图"""
    intent: Literal["refund", "shipping", "complaint", "other"] = Field(
        ..., description="邮件意图分类"
    )
    priority: Literal["low", "normal", "high"] = Field(
        default="normal", description="优先级"
    )
    order_id: Optional[str] = Field(default=None, description="订单号，如果有")


class EmailDraft(BaseModel):
    """生成的回复草稿"""
    draft: str = Field(..., description="回复草稿内容")
    confidence: float = Field(..., ge=0, le=1, description="置信度 0-1")
    need_human_review: bool = Field(default=False, description="是否需要人工审核")


class EmailResponse(BaseModel):
    """最终返回给用户的结果"""
    intent: EmailIntent
    draft: EmailDraft
    created_at: datetime = Field(default_factory=datetime.now)
