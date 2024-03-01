import hashlib
import json

import aiohttp
import loguru
import requests
from aioredis import Redis

from eirStru import SpotData, develop_mode


async def send_wx_message(title, message, openid_list=None):
    data = {'first': {'value': title,
                      'color': '#173177'},
            'keyword1': {'value': message,
                         'color': '#173177'},
            'keyword2': {'value': f'',
                         'color': '#173177'},
            'keyword3': {'value': f'',
                         'color': '#173177'},
            'remark': {'value': f'',
                       'color': '#173177'}}
    if not openid_list:
        openid_list = ['ouYVowI3kLgwVo6WEuKXvj0gGoD4', 'ouYVowBn4G5vxlnYS91pnPxUBLQ4']
    for openid in openid_list:
        await send_wx(openid, data)


async def send_price_wx(redis_clt: Redis, spot_data: SpotData, openid_list=None):
    if openid_list is None:
        openid_list = []
    data = {'character_string3': {'value': f'{spot_data.carrier_id} {spot_data.vessel}/{spot_data.voyage}'.upper()},
            'thing10': {'value': f'{spot_data.from_port_id}-{spot_data.to_port_id} {spot_data.ctntype_id}'.upper(),
                        'color': '#173177'},
            'thing1': {'value': f'ETD:{spot_data.etd}航程{spot_data.days}天',
                       'color': '#173177'},
            'thing9': {'value': f'${spot_data.base_price} S:{spot_data.spot_price}'}
            }

    if not openid_list or develop_mode:
        openid_list += ['ouYVowI3kLgwVo6WEuKXvj0gGoD4', 'ouYVowBn4G5vxlnYS91pnPxUBLQ4']

    for openid in openid_list:
        key_md5 = hashlib.md5(spot_data.model_dump_json(
            include={'carrier_id', 'vessel', 'voyage', 'from_port_id', 'to_port_id', 'ctntype_id'}).encode(
            'utf-8')).hexdigest()
        detail_md5 = hashlib.md5(f'{spot_data.spot_price}/{spot_data.base_price}'.encode('utf-8')).hexdigest()
        try:
            pre_detail_md5 = await redis_clt.getset(key_md5, detail_md5)
            await redis_clt.expire(key_md5, 24 * 60 * 60)
            if pre_detail_md5 != detail_md5:
                await send_wx(openid, data, 'pto-35_QZ_IfDfu1-mwKS7jJWa1GrFZtCpm61Px_4X0')
        except Exception as e:
            await send_wx(openid, data, 'pto-35_QZ_IfDfu1-mwKS7jJWa1GrFZtCpm61Px_4X0')


async def send_wx(openid, data, template_id='Hv8mju06e6KQ_pMeeFA5smt8j2cDWKEpRTPGjO4hTc8'):
    param = {
        'template_id': template_id,
        'url': '',
        'topcolor': '#173177',
        'data': data}

    url = 'http://meian.expressgo.cn/wechat/sendTemplateMsg/'
    param_str = json.dumps(param)
    payload = {
        'weChatConfigId': '4544c916-0ee1-4d89-8c8d-10d21287334a',
        'openidList': openid,
        'msgJson': param_str

    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, params=payload) as resp:
            if resp.status in [200, 201]:
                r_text = await resp.text()
                return r_text


def send_wx_text_msg():
    url = "http://218.0.55.172:30001/SendTextMsg_NoSrc"

    payload = json.dumps({
        "wxidorgid": "nb238ai",
        "msg": "大佬~\n你好"
    })
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': '218.0.55.172:30001',
        'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
