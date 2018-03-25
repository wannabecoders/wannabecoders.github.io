import hashlib

def to_color(c):
    return "hsl(%d, 60%%, 50%%)" % (int(c, 16)  * 360 // 16)

s = hashlib.md5(b"wannabecoders").hexdigest()

print("<div style='margin:auto;width:800px;margin-top:100px;font-family:monospace;font-size:24px'>")
for i, c in enumerate(s):
    print('<span style="color:%s">%s</span>' % (to_color(c), c),
        end="\n<br>" if (i+1) % 8 == 0 else "")
print("</div>")
