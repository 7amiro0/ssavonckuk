import collections
"""After # ----------- # do not touch anything"""
"""Here we have a message that can be changed __
                                                |
                                                V"""
messenger1 = '''QWHTGNBCMNPRDRGMAASLEDITQCFEQIGJSCFMZBWUSGQWEVVZAEPVUQZAEQAGBENYMJPOEVZVPQBNRTDRFWYYTJRTHJNYLQGRTPLBRFHZ
GSMCTCABDQGKCYGSIGCZWZPVNTSNEPIGGRPDFIYPCHJPIEGSYTLORFWYNRZRCHNVGQYYOCGPAGKBRJSMGJSCGSIGPOEVZVBTOYLYIGKC
YFZKBPQPVGMQCBOFZLRFWNNEMQEOYYZVTGBOHCMJGOCRXMGQBLTCMNVPLGETRHWPYOWSVVLGHIEYSSNGMPQAPGZLRFWNNEMNRCCGTWAQ
TEULBSKSWQLANHWYNWZRUHTARXYCQPSZZGJCDRHPBJSCRRIIGHSRTZYKJPFEPNVHSNEVNVWZAXQTJHWVGMVVWDNWBBISEUPZSKHEVYON
PRAEZXRTHSNEERUVZHWLQQHSVDJHVWYNWIEISCFPVFGKPPLVAQHOROQPCHPJPKNPBZGNWAUSNELBRYSNNYVBVVLYWWJVVTFRZBWBOGSM
OTOGRXMANWGVYONPRORLLJJCDGCCTIZPQSMEGVLIPKBPGPPCIGGRTGQIECPZIPWHTDZBCXBYSCGZIQFCCQPBECQEGSMJQFWQHQYNZTGE
TRPCERYWENCYTCMZGAMRCEUCHHRDILJSCRMCGKHNNYVRXSCSZZTGHHULBGJSJQTLUGFPVEQFHCCHDBUGZTITVTTOEUPZGQPPQPLVEOER
OPRTSEBEPRWBQVYQFJSOJZZXYVTPSBUGMHUZNBWUSGSMEGVLIPBUWGQNCABPCMYJIQXOYPPLVVWDELBUGFQBCCFVCMRSMEGRPQTKNVSO
GZBUGUCRLBGCGVEPUNKBTARJRHCCRFAGJOESCWZVVPFPPBPCCROLRCRHREIXGWYPCMNUSOQPDBVWZAEWGJOEPLCFGTZEHPVEVEUPGTCJ
PGSMYCGESFTYOSLFFZRQTORGWGKCYGSIGYSSRCMUKUSYJZRUCWIPBUCHEUPARFSLQDPNNZYBEPNXSOVPLVPJLVYBUCHEUTAACHTBYCAF
SCTZLFJOWYSIIGOYRHJVTHSBQNEGSOBXIAFHSNEOBXSCAXMAVCQGSMCGCAYPJLVVPCPWCNSQBCBUGDPBATRUVLYWVBVDPETAUHFZZEPR
GOCGS'''

"""Here we have a message that can be changed __
                                                |
                                                V"""
messenger2 = '''FCNEROTBHTHNNWOCDBADEHPIAMETUWEGATLEGHAIATOEADAAGRROETIFWHODAONALFRNCTWRERSTAMLTTHTAOHSDIIREEOIWNNACT
OSNBMVNDTLREEEAVPOORAEDLENNEWEETNRETDRSSIRRDAETFHRCYOHAUSLAIAFTEDEHAKIBEAMERAACEOTTEHHVLUAOOTEHYLASDL
AEAASOESHNRFOTOMFEBPEHPATSMAOODNSUHRTHITTNNEIENIDEOOTECEAWEEGCWSWETONICINETNEEENATETAAMETROTDIEGEHHET
LTHTIIIOETNPAHDSNGNCTCEOSTAHWGDREIDWREECCDREOWADCWWINOGMHSRINFTTIEFTVATETRHIEKHWUEVSOYNTTOORIDETRNEUT
THEDKRDTOCFIEEALSFTHHIRVTESNVDITNNRHAETRMHVETOYEFELLPHTRURSYAREOFOSIAACINRDCTPSNANRDLENDRIATHRNNYOOVD
DELNWMATLLHRVEDETFFANSPFOOGHIHAIGVSGRIDETOOBAESADACTEENATRTANNDHUDHORIAOOEDETOITORRBAAETEOWHDIOHITODE
EENDWTHGREFNACIHRBECTGTEIFSFHODWEEDITAOCYTSLUDIAEGEETDHOEINTAUGAVWHEAAENHPTOOPELEFHTREEEGFRUONCNNTOVL
TDAORITLAEENAGIEVRIETAONNNESIDODEEGBEDAWETIAITISATLOSHAEVATOHEAEFNPRWUTULRENETACCWNLHOHVLGEOGHANATBUR
RDTTRLTTLEETYBCVRHEHTRENHBIDTUIWHHOHETAODESEUEDAORAMNOTRENDEIAEOHURHGHTMREOTRHSTHEATDNTHTNOLEBOENTRTE
LHPRESNRREHSAVAOASGRTOEEINEIYETTOTHLRAQORANAITNTHTRASCDOCCNUATRAFOTECOCPOHEALIAREEVIETNNTILTIGRTELHTA
SWNDENOREOLIUEEIAASGEVSTFORPTORHLLLEOMRWHUAEGAYEIULGEECHONSOIEFTHHRBVDRRSHETTESAGRHOSOETNSVNASWTAEFEE
VNWELOHEALHIVHIIDDLAIFDDGNOPEELTOHOIOE'''
#---------------------------------------------------------------------------------------------------------------------#
counter = 0
mstr = 'ETAOIN' #<- here most popular later
count = collections.Counter(messenger1)

print('messenger nomers one most likely')

length = len(mstr)
"""first massege"""
for i in count.most_common(length):
    if i[0] in mstr:
        counter += 1
if (counter / length) * 100 >= 50:
    print('letters have changed their position')
    print(int((counter / length) * 100), "%")
if (counter / length) * 100 < 50:
    print("Letters in the text are replaced")
    print(int((counter / length) * 100), "%")

counter = 0
count = collections.Counter(messenger2)

print('messenger nomers two most likely')

"""second massege"""
for i in count.most_common(length):
    if i[0] in mstr:
        counter += 1
if (counter / length) * 100 >= 50:
    print('letters have changed their position')
    print(int((counter / length) * 100), "%")
if (counter / length) * 100 < 50:
    print("Letters in the text are replaced")
    print(int((counter / length) * 100), "%")
