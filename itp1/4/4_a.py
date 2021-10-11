a, b = map(float,input().split())
print(int(a//b), int(a%b), '{:.5f}'.format(a/b))

# a/b ... 小数点以下を切り捨てずに計算
# a//b .. 小数点以下を切り捨てて計算
# a%b ... 除算のあまりを計算

