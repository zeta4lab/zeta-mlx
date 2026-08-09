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

"""Custom model loader with dynamic model registration."""

import sys
import importlib


def register_qwen3_model():
    """Register Qwen3 model to MLX-LM dynamically."""
    # Import our custom Qwen3 implementation
    from mlx_llm_server.custom_models import qwen3

    # Register it as mlx_lm.models.qwen3 so MLX-LM can find it
    sys.modules['mlx_lm.models.qwen3'] = qwen3

    print("Qwen3 model registered successfully")


def setup_custom_models():
    """Setup all custom model implementations."""
    register_qwen3_model()
