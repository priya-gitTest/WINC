# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
print(f'Leek is {str(leek_price)} euro per kilo.')

leek_order = 'leek 4'
leek_quantity = leek_order[leek_order.find(' ')+1:]
sum_total = leek_price * int(leek_quantity)
print(sum_total)

broccoli_price = 2.34
brocoli_order = 'broccoli 1.6'
brocoli_quantity = brocoli_order[brocoli_order.find(' ')+1:]
brocoli_total = round(broccoli_price * float(brocoli_quantity),2)
print(str(brocoli_quantity)+'kg broccoli costs '+str(brocoli_total)+'e')