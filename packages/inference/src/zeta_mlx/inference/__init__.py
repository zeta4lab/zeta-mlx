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

"""MLX LLM Inference - MLX Integration Layer"""
from zeta_mlx.inference.engine import (
    InferenceEngine,
    GenerateFn, StreamFn, TokenCountFn, TemplateFn,
    parse_tool_calls,
)
from zeta_mlx.inference.manager import (
    ModelManager, LoadedModel,
    create_model_manager, create_model_manager_from_yaml,
)
from zeta_mlx.inference.loader import (
    ModelBundle,
    load_model, load_model_safe, unload_model,
)
from zeta_mlx.inference.streaming import (
    mlx_stream_generator, chunk_stream,
)

__version__ = "0.1.0"

__all__ = [
    # Engine (단일 모델)
    "InferenceEngine",
    "parse_tool_calls",
    # Manager (다중 모델)
    "ModelManager",
    "LoadedModel",
    "create_model_manager",
    "create_model_manager_from_yaml",
    # Types
    "GenerateFn", "StreamFn", "TokenCountFn", "TemplateFn",
    # Loader
    "ModelBundle",
    "load_model", "load_model_safe", "unload_model",
    # Streaming
    "mlx_stream_generator", "chunk_stream",
]
