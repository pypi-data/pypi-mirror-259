from pydantic import BaseModel
from fastapi import APIRouter, FastAPI

from dialog.llm import get_llm_class
from dialog import settings

router = APIRouter(prefix="/chatgpt")


class PromptIn(BaseModel):
    prompt: str


class PromptOut(BaseModel):
    answer: str


@router.post("/prompt")
async def prompt(payload: PromptIn) -> PromptOut:
    LLM = get_llm_class()
    llm_instance = LLM(config=settings.PROJECT_CONFIG)
    ai_message = llm_instance.process(payload.prompt)
    return {"answer": ai_message["text"]}


def register_plugin(app: FastAPI):
    app.include_router(router)
