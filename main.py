# -*- coding: utf-8 -*-
import sys
import json
from wegene_utils import is_genotype_exist


# 永远从 stdin 读取输入
body = sys.stdin.read()
inputs = json.loads(body)['inputs']

try:
    if is_genotype_exist(inputs, 'RS676785') and is_genotype_exist(inputs, 'RS609320'):
        rs676785 = inputs['RS676785']
        rs609320 = inputs['RS609320']
        if rs676785 == 'AA':
            result1 = 'C/C型'
        elif rs676785 == 'GG':
            result1 = 'c/c型'
        else:
            result1 = 'C/c型'
        if rs609320 == 'CC':
            result2 = 'E/E型'
        elif rs609320 == 'GG':
            result2 = 'e/e型'
        else:
            result2 = 'E/e型'
        
        row1 = '|抗原类型|结果|'+'\n'
        row2 = '|:--------: | :--------: |'+'\n'
        row3 = '|C|'+result1+'|'+'\n'
        row4 = '|E|'+result2+'|'
        result = row1+row2+row3+row4
    else:
        sys.stderr.write('您有位点未检出,无法判断')
        exit(2)
    print(result)
except Exception as e:
    sys.stderr.write('计算过程中出现问题，请联系作者解决')
    sys.stderr.write(str(e))
    exit(2)
