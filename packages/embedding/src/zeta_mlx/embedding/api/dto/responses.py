# Copyright 2026 Zeta4Lab
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""API 응답 DTO (외부 세계 - Pydantic)"""
from pydantic import BaseModel, Field


class EmbeddingDataDTO(BaseModel):
    """임베딩 데이터"""
    object: str = "embedding"
    index: int
    embedding: list[float]


class UsageDTO(BaseModel):
    """사용량"""
    prompt_tokens: int
    total_tokens: int


class EmbeddingResponseDTO(BaseModel):
    """OpenAI 호환 임베딩 응답"""
    object: str = "list"
    data: list[EmbeddingDataDTO]
    model: str
    usage: UsageDTO


class ErrorDTO(BaseModel):
    """에러 응답"""
    error: dict = Field(..., description="에러 정보")


class ModelInfoDTO(BaseModel):
    """모델 정보"""
    id: str
    object: str = "model"
    owned_by: str = "zeta-mlx"
    dimension: int
    max_seq_length: int


class ModelsResponseDTO(BaseModel):
    """모델 목록 응답"""
    object: str = "list"
    data: list[ModelInfoDTO]
