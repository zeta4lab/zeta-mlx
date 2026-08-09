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

"""순수 검증 함수"""
from zeta_mlx.core.types import Message, GenerationParams, NonEmptyList
from zeta_mlx.core.result import Result, Success, Failure
from zeta_mlx.core.errors import ValidationError, TokenLimitError


def validate_messages(
    messages: NonEmptyList[Message]
) -> Result[NonEmptyList[Message], ValidationError]:
    """메시지 검증"""
    # 첫 메시지가 assistant이면 안됨
    if messages.head.role == "assistant":
        return Failure(ValidationError(
            field="messages",
            message="First message cannot be from assistant"
        ))

    # 빈 content 검사
    for i, msg in enumerate(messages):
        if not msg.content.strip():
            return Failure(ValidationError(
                field=f"messages[{i}].content",
                message="Message content cannot be empty"
            ))

    return Success(messages)


def validate_params(
    params: GenerationParams
) -> Result[GenerationParams, ValidationError]:
    """파라미터 검증 (이미 타입에서 검증됨, 추가 비즈니스 규칙)"""
    # Temperature와 Top-P 조합 검증
    if params.temperature.value == 0 and params.top_p.value < 1.0:
        return Failure(ValidationError(
            field="temperature,top_p",
            message="When temperature is 0, top_p should be 1.0"
        ))

    return Success(params)


def check_token_limit(
    prompt_tokens: int,
    max_context: int,
    max_tokens: int
) -> Result[int, TokenLimitError]:
    """토큰 제한 검사"""
    total_needed = prompt_tokens + max_tokens
    if total_needed > max_context:
        return Failure(TokenLimitError(
            limit=max_context,
            actual=total_needed
        ))
    return Success(prompt_tokens)
