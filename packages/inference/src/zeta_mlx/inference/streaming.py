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

"""스트리밍 Generator"""
from typing import Iterator, Any
from mlx_lm import stream_generate
from mlx_lm.sample_utils import make_sampler


def mlx_stream_generator(
    model: Any,
    tokenizer: Any,
    prompt: str,
    max_tokens: int = 2048,
    temperature: float = 0.7,
    top_p: float = 0.9,
) -> Iterator[str]:
    """
    MLX 스트리밍 Generator

    mlx_lm.stream_generate를 사용하여 텍스트를 스트리밍합니다.
    각 response.text는 이미 개별 청크이므로 직접 yield합니다.
    """
    sampler = make_sampler(temp=temperature, top_p=top_p)

    for response in stream_generate(
        model=model,
        tokenizer=tokenizer,
        prompt=prompt,
        max_tokens=max_tokens,
        sampler=sampler,
    ):
        if response.text:
            yield response.text


def chunk_stream(
    stream: Iterator[str],
    min_chunk_size: int = 1,
) -> Iterator[str]:
    """
    스트림 청크 조절

    너무 작은 청크를 모아서 전송합니다.
    """
    buffer = ""

    for chunk in stream:
        buffer += chunk

        if len(buffer) >= min_chunk_size:
            yield buffer
            buffer = ""

    if buffer:
        yield buffer
