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

"""MLX LLM LangChain Integration"""
from zeta_mlx.langchain.chat_model import ChatMLXLLM
from zeta_mlx.langchain.embeddings import MLXLLMEmbeddings
from zeta_mlx.langchain.tools import (
    ToolExecutor,
    create_tool_executor,
    create_tool_prompt,
    parse_tool_response,
)

__version__ = "0.1.0"

__all__ = [
    # Chat Model
    "ChatMLXLLM",
    # Embeddings
    "MLXLLMEmbeddings",
    # Tools
    "ToolExecutor",
    "create_tool_executor",
    "create_tool_prompt",
    "parse_tool_response",
]
