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

"""API Routes"""
from zeta_mlx.embedding.api.routes.embeddings import router as embeddings_router
from zeta_mlx.embedding.api.routes.embeddings import set_engine as set_embeddings_engine
from zeta_mlx.embedding.api.routes.health import router as health_router
from zeta_mlx.embedding.api.routes.health import set_engine as set_health_engine

__all__ = [
    "embeddings_router",
    "health_router",
    "set_embeddings_engine",
    "set_health_engine",
]
