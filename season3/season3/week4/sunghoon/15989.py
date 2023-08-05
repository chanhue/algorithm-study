'''
/*문제 정보 */
15989번 - 1,2,3 더하기 4
난이도 - 실버 1
/*풀이 방법 */
다른 1,2,3 더하기 문제와 다르게 점화식을 구하지 말고
1로만 구하는 경우, 1,2의 합으로 구하는 경우
1,2,3 의 합으로 구하는 경우로 나눠서 dp로 풀어야 한다.
'''
import sys
input = sys.stdin.readline

t = int(input())

dp = [1] * 10001

for i in range(2,10001):
    dp[i] += dp[i-2]

for i in range(3,10001):
    dp[i] += dp[i-3]

for _ in range(t):
    n = int(input())
    print(dp[n])
'''
/*오답 노트*/
/*느낀 점*/
예전에 1,2,3 더하기 시리즈 푼 기억으로 점화식을 구하려는 생각에
1부터 10까지 경우의 수를 다 적어봤는데, 마땅한 점화식을 구하지 못했다.
인터넷에서 찾아봐 1 / 1,2 / 1,2,3 각각으로 구한 경우의 수를 따로 보면
규칙을 찾을 수 있어서 dp에 저장을 해주었다. 
'''