alf = "cdefghijklmnopqrstuvwxyzab"
bet = "abcdefghijklmnopqrstuvwxyz"
import string
table = string.maketrans(bet,alf)
raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj map."
result = raw.translate(table)
print(result)
