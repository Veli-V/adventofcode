#!/usr/bin/env python3
import sys

data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
data = "nppdvjthqldpwncqszvftbrmjlhg"
data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
data = "rgffbnnqvqhhmtmzzmmpmllcggsdswwvvwzzpptbppgngsnncwcnwcwnwgwrwrrnqnlqlccwggrcgrccjgcgwghgffjgjgrgmmsrrhchfcfdccjwwzdzcdcbcjjtfjjltlvvtstvttszsvsmmfccwcjwwzmzhhjvjpvjpppcwppdtdvtdvtvztzvzffdfqqgbgffrgrpgphhbcctssncsnncfcppvnpvnvfnfvnnfggtpplggwsggldllzvzrznncbbjpplbbrrnsrssmrsrhhmqmnqqhpqqnrqnrrtrnnrwrwhhpjhphlhvvgbgzztqtvvmssdshhqnhnjjvhjhqqbrqrrmrlrdllvrlvlccfvcffhfssgvsswhwqqfwfwhhcffjmmjrrbgrgjgrrvsrvvwmwsmmszzvmzvmmwmtthvvfbfllpjpwpwjpwpnpjpqqwtqtwwqpwqqrsqqcpqqssrgsrrjwwqmwmgwgrggmvmgmfgmffjfhjfjttcztccmtmmccnznhhcgcffmnfmmqjjhwwtccbzbhhwnhnsnmsnmnqqchhhnggbzbjzjzszsfsjfjvffnlffvrvddbhhqccdnnzwnznjnpnmppthhqddjhddqjqlqplqqjpjwppqttswsvwvfwflfplffnbfbwfwhhlhtlhtltzzmlmslmlwwgzwzrrwhhlnnrfnnmpppjpgpbbhpbhppbrppbhhzgzczqcqvqggwppcnnhnznvznzhhcpctptpjtppdhhprhrcrpcprpplrprzrnrfnrnlrlvrrfqqnnsqsqrssnrnvvvghvvbzzqppjsjnnrprwrrmqqtfqfwwrdrsddprddbdzbdbndbdjdljjrtjrrnzrzjrzzpssftfmfbflbbcpcsppwrppntnhthlthtbbsmsbmsmggpssnhnjjtsjjwssdjdwwppcbpcclmccwzzrggmgmnnwjnnqppjttvllmhhvcctptbpbdpdhdqqgggbnnqcchlhssltstllvqlvqvdvjdvvqvsvfvhfhlfftqffztzdttfvvzmvzznvnsnjjvqjvjljplpvvzlzhzghgddbbzbmbnztgthrnpsqhhdvprtpdftmqfvgjzgdvqwmvgwbczvbschqfhdvqcfnmbgmtqmlmsqcbfhshrzzbrtpgnwwtzgnjghzrlwhntprqhvshjcfvlnchccbtnswfnmpccdppqrqrhngvlwrpplbnpgzbzwtzwrsptmsmlndcfmbnqgvnqvzwpvrtfsrwfvfwdvplrfdddwcnwhzchmwfjsfvbtbrjchmgqwfvvmpzhqcbzhrcmjrzmgrtnzrcqdqdqnpwjctlhrjcphbbcvhvqnhtwjrvrbzfzfzzplshvrcchvtgtjcnhlzsttwdhcmdvrdlgsngvtzqsjrcptwwbgvfbsvgnmfhmvgqtfzbhhmdznjlsghhnlwzhvplfvlqzbrsjhdvrshjbnfqgpscbpzmnmmcsdbtwbwmsvfjwdvtctslcqfssrhczdptlrjbfzjctqrcbppcfcbqqzhhftdjchtscwgwcnpvrrjvnnwrqtrqmbgdfcpqhddnvdnmlmqcgsndwbcfvfrzsrflsnqrpmszqrdlshlcsfrmnsqmtrvjwqcllftscwrtmvcjsmrlqvdfjzgfdtswqzldqgjvhczpqrfbclnbwcjprjncvhgfmjhgfgnvfzfnvbbstgsgtspdhtfsncttlwmllbbvqftjtshfjlqtjwlvrbwmzfhdmcbhtqdzqtzmdljqprwhqwcvbtfqbpjwztgqrvlrqdwmqrqzvptsgjdqnqdfwfpjdglwgpdrcfrrzmpjmtbwwrqqcsnmphcqtthlnlzlfftrjmtjwwqrldcfjjclzrsqvltsfchfggcwbzbtpqcjfvgpwnwwqrdbdvjplgsgctdhqvttmtpmmjfcqdslhjgtdppbmzbrfbrrjncfdhlmjgdwjrmbgpcgctghbvphpgfvvfvtplqrhnjjhqntjvbsggvrvjgrwptcgqgrmjtprvhnvjsdsfqrqrrltlhvfsjsqpbwndbsnjzplcfqtfbdqdzdvnljcsmjnrmwwjzqwsjbdlclsmccbqwnlpltqhqhmthhrdjwlqwrbltghsvblqntvjqzpmmpqwrrwvhmtfqzhrmjfglwfpthhgbhdmrtprtqgqbdcfqlbbvmzmchzglmpzdvhpqchhclbcvrcmhtzqfzrplbvmdhghsttzgdjbgmmtvlqjsstgwlwchhwmflwbgljgszghvfdsngbtbcnhzmmdmsjqfbcsmgpjwjqgwqdlrgznnmhphbrzcgnqczpcbljjmhnnrmzlpqbswwcjpjqcrtdmgprpmmbprwlmpzcmwlnbzqjsgftrncvmjmjwvqgszsrmrczhjnwlghgndhbthwlhfbncrwqfgnshrmdfhwmfvllhvbmmllwfbgrnrttpzffzvcfjfbrmdqfcfrdqsltpbbttnqnbncfhwghfbgwrltbhwmmlpczsvvdnwhchgfplnjsttsqvsznwvlwzgfnhfrrgplsfwrwnbfhblwtjpldjmzrglhppgsjsgzssbbgrrbdmpwhgjjmlfnpdbvtntcwrvltgfnrgwttvvjhqljjvvnmztwgzcclgbjnjspzwnpgtgvhhhqbzrnvmdcljcdncvpnpdhrhqwvlhllbsrmjbzlgczwjsrvqrqfqmtjrnpbtdhsrfbhrgtgnrmlgcwcmrvrdfcqbfcqczjchgrjpzqfqqmcpvnvbrssfrfsrjmlngplqqsnclgvpfhjbzdppjftlgbmcgdbrvqrclvtdnzhhcmzlrdrgbrqrlvfcnvznnqwswvhdpbbjmsqzcrmjngzmdftjzsjvgfdtcvdwhnwwjlcgcmflzzpzpgzrvmptbjgrdjbzscrglhcjppdjdshnvvbsnnddtbwsdrpnbnlrtppcrzbbjrfzhbwgmjqtmgjvmrjgfdndlmqvhgwprsjnhcmrnfdfdzggjjzcccnsnwwbjzmsfjjfhclptfcwqjhnphpwzszjmsrtnbqpqsvcfcvrrgclwlbrqngdcdlzrdfpvbgtznjzdvjngrgswhjnrpgswtqflpgvnpbsvcrtgtzcbhdjpbjwnpdzcmprtzlppbqvpzrrlbssmwhhvqqpmwggnzwcfdnzccjrrncnvjqgbpstctwpqvhdsbcsjrpbzbdlwwvjngtbnvpthppglgsnrbwnvpzldhsgwqhclgwrdsvcfdclvdsbrhcfnbgrtqswstnjfmfrdgphpvgjfqzcwnpcghdhtflgdnhhnnnwrpnmppszgqdcqjqpnccfsqjsmwtqvzwfqvtwtthwswmcqqcqjwcgwgzgmnpzbfpzrqbvqhbhtsvvbppbmqzfnsmwppzvsctgcncztsqdfhnlwjjtvwcchvnphwpnpzqsjhlrcmnbthtqlfclnsfdtpwfzljdpfszvhgzdpzhbjtphbfbmwgfrfplntfqhgpbjzghmblzzhdcbptngqwrtfmvtbhphpvdwpswbscrwzhnvqfwlbwwqqgstgmbqlllspbhbpjmmrfhmjwzdnsdwmpvlrspgzmdjwqwcjpbgwspsghjdvrbbsbtgwptqdvvdhbhqbdhpbzdsdwsjdbjnztdqqrdhwhtpvcbblbmjgmbpqghdsfthzjffrdvldfsnpcsmnzwzcqlnvcrcbqnfcdrfbffrvhqsbqjnnbzsqvqqdqwmsvbqvtgmnnlthpngfsljqnrdhhzpmwsnqvrgdnvlbgnndfcpjfgmzqssvnnrwbmslcqpnhnnwzggsjvqcsqpfzjcmcppntmsdtfggzdncqbfjsqvbzgnnlsdbgjqffsmvnbqlsrjwdmcjbrsrpchnnhdtlcdhfdltmlvtrwjpzphtbhzzrlrwbbhhpntgbcfmphnbrjdhrhvmvhfglrncngjdsvbfrqtqzsgvlzjqzcqnwdcfgvnpsqpphwfsdvpgnchjnnjhsqgvlqcvhzzzcrsqcvrbsbjbdbgddlbb"

position = 0

for i in range(4, len(data)):
    code = data[int(i)-4:int(i)]
    if len(code) == len(set(code)):
        position = i
        break


print("Part1")
print("First all unique 4 position: {}".format(position))


for i in range(14, len(data)):
    code = data[int(i)-14:int(i)]
    if len(code) == len(set(code)):
        position = i
        break

print("Part2")
print("First all unique 14 position: {}".format(position))