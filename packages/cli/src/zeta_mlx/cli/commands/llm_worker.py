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

"""서버 워커 (데몬 모드용)"""
import argparse
import uvicorn
from pathlib import Path


def main() -> None:
    """데몬 워커 메인"""
    parser = argparse.ArgumentParser(description="MLX LLM Server Worker")
    parser.add_argument("--config", "-c", type=Path, default=None)
    parser.add_argument("--port", "-p", type=int, default=None)
    parser.add_argument("--host", type=str, default=None)
    args = parser.parse_args()

    from zeta_mlx.core import load_config, merge_config, AppConfig, Success, Failure
    from zeta_mlx.inference.api import create_app

    # 설정 로드
    if args.config:
        config_result = load_config(args.config)
        if isinstance(config_result, Failure):
            print(f"Error loading config: {config_result.error}")
            return
        config = config_result.value
    else:
        config_result = load_config()
        if isinstance(config_result, Success):
            config = config_result.value
        else:
            config = AppConfig()

    # CLI 옵션으로 오버라이드
    overrides = {}
    if args.port is not None:
        overrides["server"] = {"port": args.port}
    if args.host is not None:
        if "server" not in overrides:
            overrides["server"] = {}
        overrides["server"]["host"] = args.host

    if overrides:
        config = merge_config(config, overrides)

    # FastAPI 앱 생성
    app = create_app(config)

    print(f"Starting server on {config.server.host}:{config.server.port}")

    # 서버 실행
    uvicorn.run(
        app,
        host=config.server.host,
        port=config.server.port,
        log_level="info",
    )


if __name__ == "__main__":
    main()
