#作者：xbillow
kk="""Beuvq ulevhou. Nlxtuoveh prn mvaatgteu ulevhou.
Uotgt prn re tmht ul uovn mrgjetnn uoru xrmt ovn orfjqtn gvnt.
Evet mrdn uotd orm ytte gvmveh, elguo rem elguoptnu rem uote elguo rhrve,
arguotg rem arguotg aglx uot Prqq, orgm le uot ugrfj la r yrem la Pvqmqveh grvmtgn.
Trfo mrd orm ytte plgnt uore uot mrd uoru orm flxt ytalgt vu.
Ulmrd prn uot plgnu la rqq. R flqm pvem prn yqlpveh lbu la uot elguo,
rem vu xrmt uot ugttn gbnuqt qvjt qviveh uovehn. Rqq mrd,
Pvqq orm atqu rn uolbho nlxtuoveh ptgt prufoveh ovx,
nlxtuoveh flqm rem vxsqrfryqt uoru qlitm ovx elu.
Hrgtm orm atqu vu ull. Pvqq preutm eluoveh nl xbfo rn ul gvmt
otqqyteu alg uot nratud la uot Prqq, ybu uoru prn elu r attqveh ul norgt pvuo dlbg flxxremtg."""

#加密是用访射密码，求明文和密钥。提示：明文有单词darkness

ss=""#A到Z的集合
for i in range(26):
    ss+=chr(ord('A')+i)
for k1 in [1,3,5,7,9,11,15,17,19,21,23,25]:
    for k2 in range(26):
        ee=""#明文
        for c in kk:
            if c.upper() in ss:
                if c in ss:
                    c=chr(((ord(c)-k2)*k1)%26+ord('A'))
                else:
                    c=chr(((ord(c.upper())-k2)*k1)%26+ord('a'))
            ee+=c
        if "darkness" in ee:
             break
    if "darkness" in ee:
        break
print("解密密钥:\nk1={}   k2={}".format(k1,k2))
print("########################明文#####################")
print(ee)
