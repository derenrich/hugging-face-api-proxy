from datetime import date
from typing import Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import httpx
from pydantic import BaseModel, Field


HF_TOKEN = os.environ.get("HF_TOKEN")
HF_BASE_URL = "https://api-inference.huggingface.co"
if not HF_TOKEN:
    raise ValueError("Please set a HF_TOKEN environment variable")

app = FastAPI()


@app.post("/proxy/{file_path:path}")
async def proxy(file_path: str, request: Request) -> dict:
    async with httpx.AsyncClient() as client:
        body = await request.json()
        response = await client.post(f"{HF_BASE_URL}/{file_path}", headers={"Authorization": f"Bearer {HF_TOKEN}"}, json=body, timeout=300)

        try:
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            # reraise exception as fastapi exception

            raise HTTPException(status_code=response.status_code, detail=response.json())
