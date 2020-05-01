class Solution:
    def countAndSay(self, n):
        cur_text = '1'
        next_text = ''
        count = 1
        for i in range(n - 1):
            pre = cur_text[0]
            count = 1
            for j in cur_text[1:]:
                if j == pre:
                    count += 1
                else:
                    next_text += str(count) + pre
                    pre = j
                    count = 1
            next_text += str(count) + pre
            cur_text, next_text = next_text, ''
        return cur_text
