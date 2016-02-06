myscore = 1000
message = 'i scored %s points'
print(message % myscore)

nums = "What did the number %s say to the number %s? Nice BELT!"
print(nums % (0, 8))

# multiply strings
print(10 * "A")

wl = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing']
print(wl)
print(wl[2])
wl[1] = "ben"
print(wl)

wl.append("new element")
print(wl)

wl.remove("ben")
print(wl)

wl1 = [1, 2, 3, 4]

wl3 = wl + wl1
print(wl3)

l = [1, 2]
l1 = l * 5

print(l1)

# can not divide a list
#l2 = l / 5
#print(l2)

# tuples
tp = (0, 1, 2, 3)
print(tp)

# can not change tuples (immutable)
# tp[1] = 7

