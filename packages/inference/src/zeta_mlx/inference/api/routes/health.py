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

"""Health Check 라우트"""
from fastapi import APIRouter
from zeta_mlx.inference import ModelManager
from zeta_mlx.inference.api.dto.responses import HealthResponseDTO
from zeta_mlx.inference.api.converters import create_health_response

router = APIRouter(tags=["health"])

# 버전 정보
VERSION = "0.1.0"

# 모델 관리자 (의존성 주입으로 설정)
_model_manager: ModelManager | None = None


def set_model_manager(manager: ModelManager) -> None:
    """모델 관리자 설정"""
    global _model_manager
    _model_manager = manager


def get_model_manager() -> ModelManager | None:
    """모델 관리자 조회"""
    return _model_manager


@router.get("/health", response_model=HealthResponseDTO)
async def health_check() -> HealthResponseDTO:
    """헬스 체크 엔드포인트"""
    if _model_manager is None:
        return create_health_response(
            status="unhealthy",
            model=None,
            version=VERSION,
        )

    # 로드된 모델이 있으면 첫 번째 모델 표시
    loaded = _model_manager.list_loaded()
    current_model = loaded[0] if loaded else _model_manager.default_alias

    return create_health_response(
        status="healthy",
        model=current_model,
        version=VERSION,
    )


@router.get("/health/detail")
async def health_detail():
    """상세 헬스 체크"""
    if _model_manager is None:
        return {
            "status": "unhealthy",
            "version": VERSION,
            "models": {
                "available": [],
                "loaded": [],
                "default": "",
            },
        }

    return {
        "status": "healthy",
        "version": VERSION,
        "models": {
            "available": _model_manager.list_available(),
            "loaded": _model_manager.list_loaded(),
            "default": _model_manager.default_alias,
        },
    }
