def max_profit(n):
    buildings = [
        ("T", 5, 1500),
        ("P", 4, 1000),
        ("C", 10, 2000)
    ]

    dp = [0] * (n + 1)
    plans = [[] for _ in range(n + 1)]

    for time in range(1, n + 1):
        dp[time] = dp[time - 1]
        plans[time] = plans[time - 1].copy()

        for name, build_time, income in buildings:
            if time >= build_time:
                profit = dp[time - build_time] + (n - time) * income

                if profit > dp[time]:
                    dp[time] = profit
                    plans[time] = plans[time - build_time] + [name]

    best_plan = plans[n]

    print("Earnings: $", dp[n])
    print("T:", best_plan.count("T"),
          "P:", best_plan.count("P"),
          "C:", best_plan.count("C"))


n = int(input("Enter time units: "))
max_profit(n)