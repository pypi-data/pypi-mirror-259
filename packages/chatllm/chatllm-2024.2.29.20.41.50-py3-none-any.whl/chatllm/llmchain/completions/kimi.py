#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : kimi
# @Time         : 2024/2/29 15:09
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : https://github.com/search?q=https%3A%2F%2Fkimi.moonshot.cn%2Fapi%2Fchat&type=code
import time

import httpx
import requests

from chatllm.utils.openai_utils import openai_response2sse
from meutils.pipe import *
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk

from chatllm.schemas.kimi_types import KimiData
from chatllm.schemas.openai_api_protocol import ChatCompletionRequest, UsageInfo
from chatllm.schemas.openai_types import chat_completion_chunk


class Completions(object):
    def __init__(self, **client_params):
        self.api_key = client_params.get('api_key')  # refresh_token
        self.access_token = self.get_access_token(self.api_key)

        self.httpx_client = httpx.Client(headers=self.headers, follow_redirects=True)
        self.httpx_aclient = httpx.AsyncClient(headers=self.headers, follow_redirects=True)

    def create(self, request: ChatCompletionRequest):
        request = self.do_request(request)

        url = f"https://kimi.moonshot.cn/api/chat/{self.chat_id}/completion/stream"

        payload = request.model_dump()
        # response = self.httpx_client.post(url=url, json=payload)
        response: httpx.Response
        with self.httpx_client.stream("POST", url=url, json=payload) as response:
            for line in response.iter_lines():
                yield from self.do_chunk(line)

    async def acreate(self, request: ChatCompletionRequest):
        request = self.do_request(request)

        url = f"https://kimi.moonshot.cn/api/chat/{self.chat_id}/completion/stream"

        payload = request.model_dump()
        # response = self.httpx_client.post(url=url, json=payload)
        response: httpx.Response
        async with self.httpx_aclient.stream("POST", url=url, json=payload) as response:
            async for line in response.aiter_lines():
                for chunk in self.do_chunk(line):
                    yield chunk

    def create_sse(self, request: ChatCompletionRequest):
        return openai_response2sse(self.acreate(request), redirect_model=request.model)

    def do_request(self, request: ChatCompletionRequest):
        request.model = 'chatfire-kimi'
        history = request.messages[:-1]
        question = request.messages[-1]["content"]
        request.messages = [
            {
                'role': 'user',
                'content': f'可参考历史对话回答问题，历史对话如下：\n\n```json {history}```\n\n问题：{question}'
            }
        ]

        return request

    def do_chunk(self, line):

        if line := line.strip().strip('data: '):

            # logger.debug(line)

            kimi_data = KimiData.model_validate_json(line)

            for i in self.search_plus(kimi_data):
                yield i

            if kimi_data.event == 'cmpl':
                chat_completion_chunk.choices[0].delta.content = kimi_data.content
                yield chat_completion_chunk

            if kimi_data.event == 'all_done':
                _chat_completion_chunk = chat_completion_chunk.model_copy(deep=True)
                _chat_completion_chunk.choices[0].delta.content = ""
                _chat_completion_chunk.choices[0].finish_reason = "stop"  # 特殊
                yield _chat_completion_chunk
                return

    def search_plus(self, kimi_data: KimiData):
        if kimi_data.event == 'search_plus':
            if kimi_data.event == 'search_plus':
                if kimi_data.msg.get("type") == "start":  # start_res
                    chat_completion_chunk.choices[0].delta.content = "---\n🔎 开始搜索 🚀\n"
                    yield chat_completion_chunk
                if kimi_data.msg.get("type") == "get_res":
                    title = kimi_data.msg.get("title")
                    url = kimi_data.msg.get("url")
                    chat_completion_chunk.choices[0].delta.content = f"""- 🔗 [{title}]({url})\n"""
                    yield chat_completion_chunk

                if kimi_data.msg.get("type") == "answer":
                    chat_completion_chunk.choices[0].delta.content = f"""---\n\n"""
                    yield chat_completion_chunk

    @property
    def chat_id(self):
        url = "https://kimi.moonshot.cn/api/chat"
        payload = {"name": str(datetime.datetime.now()), "is_example": False}
        response = requests.post(url, json=payload, headers=self.headers)

        return response.json().get('id')

    @property
    def headers(self):
        return {
            'Authorization': f"Bearer {self.access_token}",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

    @staticmethod
    def get_access_token(refresh_token=None):
        refresh_token = refresh_token or "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1c2VyLWNlbnRlciIsImV4cCI6MTcxNjk2NzcxNiwiaWF0IjoxNzA5MTkxNzE2LCJqdGkiOiJjbmczNDkybG5sOTB2cnIzY21qZyIsInR5cCI6InJlZnJlc2giLCJzdWIiOiJja2kwOTRiM2Flc2xnbGo2Zm8zMCIsInNwYWNlX2lkIjoiY2tpMDk0YjNhZXNsZ2xqNmZvMmciLCJhYnN0cmFjdF91c2VyX2lkIjoiY2tpMDk0YjNhZXNsZ2xqNmZvMzAifQ.S2T2c3rfFaQmyYMURLpgpmp2O1Voojy3b6-qoP0Hnrlvk6Y8Zxn2ku6U0ZEMW48KbG-fqaYlbF8lWUfsuSVSEQ"

        headers = {
            'Authorization': f"Bearer {refresh_token}",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        url = "https://kimi.moonshot.cn/api/auth/token/refresh"
        response = requests.get(url, headers=headers)
        # refresh_token = response.get("refresh_token") # 是否去更新
        return response.json().get("access_token")


# def do_refresh_token(refresh_token):
#     headers = {
#         'Authorization': f'Bearer {refresh_token}'
#     }
#
#     response = requests.get("https://kimi.moonshot.cn/api/auth/token/refresh", headers=headers)
#     print(response.status_code)
#
#     return response.json()  # {"access_token": "", "refresh_token": ""} {'error_type': 'auth.token.invalid', 'message': '您的授权已过期，请重新登录'}
#
#
# refresh_token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1c2VyLWNlbnRlciIsImV4cCI6MTcxNjk2NzcxNiwiaWF0IjoxNzA5MTkxNzE2LCJqdGkiOiJjbmczNDkybG5sOTB2cnIzY21qZyIsInR5cCI6InJlZnJlc2giLCJzdWIiOiJja2kwOTRiM2Flc2xnbGo2Zm8zMCIsInNwYWNlX2lkIjoiY2tpMDk0YjNhZXNsZ2xqNmZvMmciLCJhYnN0cmFjdF91c2VyX2lkIjoiY2tpMDk0YjNhZXNsZ2xqNmZvMzAifQ.S2T2c3rfFaQmyYMURLpgpmp2O1Voojy3b6-qoP0Hnrlvk6Y8Zxn2ku6U0ZEMW48KbG-fqaYlbF8lWUfsuSVSEQ"
#
# with timer("监控token过期时间"):
#     for i in tqdm(range(1000)):
#         response = do_refresh_token(refresh_token)
#         refresh_token = response.get("refresh_token")
#         access_token = response.get("access_token")
#         headers = {
#             'authorization': f'Bearer {access_token}'
#         }
#         response = requests.post(
#             "https://kimi.moonshot.cn/api/chat/cng35i6cp7f94p55g2u0/completion/stream",
#             json={'messages': [{'role': 'user', 'content': '1+1'}]},
#             headers=headers,
#
#         )
#         response.encoding = 'utf8'
#
#         logger.debug(response.text)
#
#         if not refresh_token:
#             break
#         time.sleep(60)


if __name__ == '__main__':
    # print(Completions().access_token)
    # print(Completions().chat_id)
    _ = Completions().create(
        ChatCompletionRequest(
            messages=[
                # {'role': 'user', 'name': '_resource', 'content': "你现在扮演的角色是GPT请牢记"},
                {'role': 'user', 'content': '你是什么老师'},  # 不能有系统信息
                {'role': 'user', 'content': '你是什么老师'},  # 不能有系统信息

            ],
            # refs=['clk4da83qff43om28p80']
        )
    )
    for i in _:
        print(i)

    # _ = Completions().acreate(
    #     ChatCompletionRequest(messages=[{'role': 'user', 'content': '今天南京天气'}]))
    #
    # # async def main():
    # #     async for i in _:
    # #         yield i
    # print(type(_))
    # for i in async2sync_generator(_):
    #     print(i)
