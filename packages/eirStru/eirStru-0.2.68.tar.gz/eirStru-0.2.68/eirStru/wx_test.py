import json

import requests

from eirStru import SpotData


def send_price_wx(openid_list, route: SpotData):
    '''
    船名航次
{{character_string3.DATA}}
装卸港
{{thing10.DATA}}
当前节点
{{thing1.DATA}}
箱量
{{thing9.DATA}}
    '''

    data = {'first': {'value': f'{route.carrier_id} {route.from_port_id}-{route.to_port_id}'.upper(),
                      'color': '#173177'},
            'keyword1': {'value': f'新运价:{route.carrier_id} {route.from_port_id}-{route.to_port_id}'.upper(),
                         'color': '#173177'},
            'keyword2': {'value': f'{route.carrier_line} {route.vessel}/{route.voyage}',
                         'color': '#173177'},
            'keyword3': {
                'value': f'''{route.ctntype_id} price ${route.base_price}\netd:{route.etd} eta:{route.eta} days:{route.days}\n截港日:{route.cut_off_datetime} 截单日:{route.doc_closure_datetime}''',
                'color': '#173177'},
            'remark': {'value': f'',
                       'color': '#173177'}}

    data = {'character_string3': {'value': f'{route.carrier_id} {route.vessel}/{route.voyage}'.upper()},
            'thing10': {'value': f'{route.from_port_id}-{route.to_port_id} {route.ctntype_id}'.upper(),
                        'color': '#173177'},
            'thing1': {'value': f'ETD:{route.etd}航程{route.days}天',
                       'color': '#173177'},
            'thing9': {'value': f'${route.base_price} S:{route.spot_price}'}
            }

    if not openid_list:
        openid_list = ['ouYVowI3kLgwVo6WEuKXvj0gGoD4', 'ouYVowBn4G5vxlnYS91pnPxUBLQ4']

    for openid in openid_list:
        send_wx(openid, data, 'pto-35_QZ_IfDfu1-mwKS7jJWa1GrFZtCpm61Px_4X0')


def send_wx(openid, data, template_id='Hv8mju06e6KQ_pMeeFA5smt8j2cDWKEpRTPGjO4hTc8'):
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

    # md5_data = json.dumps(payload)
    #
    # md5 = hashlib.md5(md5_data.encode(encoding='UTF-8')).hexdigest()
    # wx = await insert_wx(openid, param_str, md5)
    resp = requests.post(url, params=payload)
    print(resp.text)


route = SpotData()
route.carrier_id = 'hpl'
route.vessel = 'vessel'
route.voyage = 'voyage'

route.from_port_id = 'cnngb'
route.to_port_id = 'deham'
route.etd = '2023-01-01'
route.eta = '2023-01-02'
route.days = 23
route.ctntype_id = '20GP'
route.base_price = '10000.00'
route.spot_price = '20000.00'
send_price_wx([], route)
