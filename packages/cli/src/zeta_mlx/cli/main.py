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

"""Zeta MLX CLI 메인 엔트리"""
import typer
from rich.console import Console
from zeta_mlx.cli.commands import llm, chat, models, embedding

console = Console()

app = typer.Typer(
    name="zeta-mlx",
    help="Zeta MLX - OpenAI-compatible LLM/Embedding inference on Apple Silicon",
    add_completion=False,
)

# 서브커맨드 등록
app.add_typer(llm.app, name="llm", help="LLM 서버 (포트 9044)")
app.add_typer(embedding.app, name="embedding", help="임베딩 서버 (포트 9045)")
app.add_typer(chat.app, name="chat")
app.add_typer(models.app, name="models")


@app.callback()
def main_callback() -> None:
    """Zeta MLX CLI"""
    pass


@app.command()
def version() -> None:
    """버전 정보 출력"""
    from zeta_mlx.cli import __version__
    console.print(f"[bold blue]zeta-mlx[/bold blue] version [green]{__version__}[/green]")


def cli() -> None:
    """CLI 진입점"""
    app()


if __name__ == "__main__":
    cli()
