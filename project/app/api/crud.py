from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from typing import Union, List


async def post(payload: SummaryPayloadSchema) -> int:
    summary = await TextSummary.create(url=payload.url, summary="dummary")

    return summary.id


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries