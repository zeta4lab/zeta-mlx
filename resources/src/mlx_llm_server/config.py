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

"""Configuration for MLX LLM server."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Server configuration settings."""

    model_name: str = "mlx-community/Qwen3-8B-4bit"
    host: str = "0.0.0.0"
    port: int = 9044
    max_tokens: int = 2048
    temperature: float = 0.7
    top_p: float = 0.9


settings = Settings()
