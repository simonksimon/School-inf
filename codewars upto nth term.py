def series_sum(n):
    if n == 0:
        return "0.00"
    else:
        sum = 1
        nextint = 1
        for i in range(n-1):
            nextint = nextint + 3
            sum = sum + (1 / nextint)

            sum = str(sum)
            if len(sum) > 4:
                enddigit = int(sum[4])
                if enddigit > 4:
                    lastdigit = int(sum[3])
                    lastdigit += 1
                    sum = (sum[:3] + str(lastdigit))
                else:
                    sum = sum[:4]
            else:
                sum = sum[:4]

            if sum == "1":
                sum = "1.00"
            return sum

parameter=32
result=series_sum(parameter)
print(result)