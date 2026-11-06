class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        total = 1
        i = 2

        while i * i <= num:
            if num % i == 0:
                total += i

                if i != num // i:
                    total += num // i

            i += 1

        return total == num

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna