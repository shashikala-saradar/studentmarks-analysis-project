monthly_sales=[
    [1000,1200,1300],
    [900,1100,1400]
]
for month in monthly_sales:
    total=0
    for sale in month:
        total+=sale
    print("monthly total",total)