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

"""Embedding 에러 타입 (OR Types / Sum Types)"""
from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class ModelLoadError:
    """모델 로드 실패"""
    model_name: str
    reason: str

    def __str__(self) -> str:
        return f"Failed to load model '{self.model_name}': {self.reason}"


@dataclass(frozen=True)
class EmbeddingError:
    """임베딩 생성 실패"""
    reason: str

    def __str__(self) -> str:
        return f"Embedding failed: {self.reason}"


@dataclass(frozen=True)
class ValidationError:
    """입력 검증 실패"""
    field: str
    message: str

    def __str__(self) -> str:
        return f"Validation error on '{self.field}': {self.message}"


@dataclass(frozen=True)
class BatchSizeExceededError:
    """배치 크기 초과"""
    actual: int
    limit: int

    def __str__(self) -> str:
        return f"Batch size {self.actual} exceeds limit {self.limit}"


# Union type for all embedding errors
EmbeddingServiceError = Union[
    ModelLoadError,
    EmbeddingError,
    ValidationError,
    BatchSizeExceededError,
]
