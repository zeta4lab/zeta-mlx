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

"""DTOs for API"""
from zeta_mlx.inference.api.dto.requests import ChatRequestDTO, MessageDTO
from zeta_mlx.inference.api.dto.responses import (
    ChatResponseDTO, StreamResponseDTO,
    ChoiceDTO, MessageResponseDTO, UsageDTO,
    StreamChoiceDTO, DeltaDTO,
    ModelsResponseDTO, ModelDTO,
    HealthResponseDTO, ErrorResponseDTO,
)

__all__ = [
    "ChatRequestDTO", "MessageDTO",
    "ChatResponseDTO", "StreamResponseDTO",
    "ChoiceDTO", "MessageResponseDTO", "UsageDTO",
    "StreamChoiceDTO", "DeltaDTO",
    "ModelsResponseDTO", "ModelDTO",
    "HealthResponseDTO", "ErrorResponseDTO",
]
