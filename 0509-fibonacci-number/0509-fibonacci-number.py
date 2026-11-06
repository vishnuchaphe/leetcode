class Solution(object):
    def fun(self, num):
        if num == 0 or num == 1:
            return num

        return self.fun(num - 1) + self.fun(num - 2)

    def fib(self, n):
        answer = self.fun(n)
        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna