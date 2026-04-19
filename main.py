from decimal import Decimal

class PulHisob:
    def __init__(self, pul):
        self.pul = Decimal(str(pul))

    def katta_qismi(self):
        return self.pul.quantize(Decimal('1'))

    def kichik_qismi(self):
        return self.pul - self.katta_qismi()

    def pulni_topshirish(self, miqdor):
        if miqdor < 0:
            raise ValueError("Miqdor manfiy bo'lishi mumkin emas")
        return PulHisob(self.pul + Decimal(str(miqdor)))

    def pulni_olish(self, miqdor):
        if miqdor < 0:
            raise ValueError("Miqdor manfiy bo'lishi mumkin emas")
        return PulHisob(self.pul - Decimal(str(miqdor)))

    def pulni_kopaytirish(self, qoldirish):
        return PulHisob(self.pul * Decimal(str(qoldirish)))

    def pulni_birlashtirish(self, boshqa_pul):
        return PulHisob(self.pul + boshqa_pul.pul)

    def pulni_ayirish(self, boshqa_pul):
        if boshqa_pul.pul > self.pul:
            raise ValueError("Ayirishda katta pul bo'lishi mumkin emas")
        return PulHisob(self.pul - boshqa_pul.pul)

# Misol:
pul = PulHisob(100.50)
print(pul.katta_qismi())  # 100
print(pul.kichik_qismi())  # 0.50
pul = pul.pulni_topshirish(20)
print(pul.katta_qismi())  # 120
pul = pul.pulni_olish(10)
print(pul.katta_qismi())  # 110
pul = pul.pulni_kopaytirish(2)
print(pul.katta_qismi())  # 220
pul = pul.pulni_birlashtirish(PulHisob(50))
print(pul.katta_qismi())  # 270
pul = pul.pulni_ayirish(PulHisob(20))
print(pul.katta_qismi())  # 250
