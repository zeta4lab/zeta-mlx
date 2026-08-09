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

"""API 요청 DTO (외부 세계 - Pydantic)"""
from pydantic import BaseModel, Field


class EmbeddingRequestDTO(BaseModel):
    """OpenAI 호환 임베딩 요청"""
    model: str = Field(..., description="모델 이름")
    input: str | list[str] = Field(..., description="임베딩할 텍스트 (단일 또는 배열)")
    encoding_format: str = Field(default="float", description="인코딩 포맷 (float, base64)")

    def to_input_list(self) -> list[str]:
        """입력을 리스트로 정규화"""
        if isinstance(self.input, str):
            return [self.input]
        return self.input
