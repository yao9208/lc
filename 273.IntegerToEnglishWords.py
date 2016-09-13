class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return 'Zero'
        thousand = ['','Thousand','Million','Billion']
        word = ''
        i = 0
        while num!=0:
            if num%1000!=0:
                word = self.generate(num%1000)+thousand[i] + ' '+word
            i += 1
            num /= 1000
        return word.strip()

    def generate(self, num):
        twenty = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty']
        ten = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        if num==0:
            return ''
        if num<=20:
            return twenty[num]+' '
        if num<100:
            return ten[num/10]+' ' + self.generate(num%10)
        return self.generate(num/100) + 'Hundred ' + self.generate(num%100)
        
