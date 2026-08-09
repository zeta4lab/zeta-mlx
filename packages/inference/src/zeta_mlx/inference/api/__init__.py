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

"""Zeta MLX Inference API - FastAPI Server (Multi-Model)"""
from zeta_mlx.inference.api.app import (
    create_app,
    create_app_from_yaml,
    create_app_with_manager,
)
from zeta_mlx.inference.api.dto import (
    ChatRequestDTO, MessageDTO,
    ChatResponseDTO, StreamResponseDTO,
    ChoiceDTO, MessageResponseDTO, UsageDTO,
    StreamChoiceDTO, DeltaDTO,
    ModelsResponseDTO, ModelDTO,
    HealthResponseDTO, ErrorResponseDTO,
)
from zeta_mlx.inference.api.converters import (
    chat_request_dto_to_domain,
    create_chat_response,
    create_stream_chunk,
    create_models_response,
    create_health_response,
    create_error_response,
)

__version__ = "0.1.0"

__all__ = [
    # App factory
    "create_app",
    "create_app_from_yaml",
    "create_app_with_manager",
    # Request DTOs
    "ChatRequestDTO",
    "MessageDTO",
    # Response DTOs
    "ChatResponseDTO",
    "StreamResponseDTO",
    "ChoiceDTO",
    "MessageResponseDTO",
    "UsageDTO",
    "StreamChoiceDTO",
    "DeltaDTO",
    "ModelsResponseDTO",
    "ModelDTO",
    "HealthResponseDTO",
    "ErrorResponseDTO",
    # Converters
    "chat_request_dto_to_domain",
    "create_chat_response",
    "create_stream_chunk",
    "create_models_response",
    "create_health_response",
    "create_error_response",
]
