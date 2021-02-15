# RHCE blood group WeApp-Wegene
此微解读可以通过微基因用户的基因数据对RH血型系统中的C和E抗原进行预测，最终以markdown的形式输出表格。SNP依据论文如下
<https://pubmed.ncbi.nlm.nih.gov/21257350/>
我们的主要任务是编辑main.py这个文件，也就是脚本文件。
##分型判断部分
'''Python
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
'''
##将结果转换成markdown表格形式并输出
'''Python
row1 = '|抗原类型|结果|'+'\n'
row2 = '|:--------: | :--------: |'+'\n'
row3 = '|C|'+result1+'|'+'\n'
row4 = '|E|'+result2+'|'
result = row1+row2+row3+row4
print(result)
'''
