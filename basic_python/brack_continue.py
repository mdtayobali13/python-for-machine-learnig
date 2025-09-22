# for i in range(100):
#     if i == 5: break
#     if i == 6: continue
#     print(i)

send = "I Love Bangladesh"

for i in send.split():
    if i == 'end':
        break
    print(i)