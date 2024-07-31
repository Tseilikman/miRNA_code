#открываем файлы с информацией по генам и микроРНК по каждому из генов
genes = open('genes.txt', 'r')

bdnf = open('BDNF.txt', 'r')
nr3c1 = open('NR3C1.txt', 'r')
crp = open('CRP.txt', 'r')
faah = open('FAAH.txt', 'r')
ska2 = open('SKA2.txt', 'r')
dicer1 = open('DICER1.txt', 'r')
adcyap1r1 = open('ADCYAP1R1.txt', 'r')
comt = open('COMT.txt', 'r')
orm1 = open('ORM1.txt', 'r')
txnrd1 = open('TXNRD1.txt', 'r')
tubb1 = open('TUBB1.txt', 'r')
fkbp5 = open('FKBP5.txt', 'r')
zbp1 = open('ZBP1.txt', 'r')
erk1_2 = open('ERK1\2.txt', 'r')
zbtb16 = open('ZBTB16.txt', 'r')
gstm1 = open('GSTM1.txt', 'r')
hla = open('HLA-DRB5.txt', 'r')
camkmt = open('CAMKMT.txt', 'r')
man2c1 = open('MAN2C1.txt', 'r')
asah1 = open('ASAH1.txt', 'r')
fkbp4 = open('FKBP4.txt', 'r')
ero1a = open('ERO1A.txt', 'r')
nnt = open('NNT.txt', 'r')

#словарь для "ген-повышение при ПТСР"
gene_dict = dict()
for gene in genes.readlines():
    if gene.split()[1] == 'Up':
        gene_dict[gene.split()[0]] = True
    else:
        gene_dict[gene.split()[0]] = False
#словарь для микроРНК "микроРНК-[гены, повышение экспрессии, IR]
miRNA_dict = dict()
for mirna in bdnf.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['BDNF'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('BDNF')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in nr3c1.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['NR3C1'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('NR3C1')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in crp.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['CRP'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('CRP')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in faah.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['FAAH'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('FAAH')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in ska2.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['SKA2'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('SKA2')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in dicer1.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['DICER1'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('DICER1')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in adcyap1r1.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['ADCYAP1R1'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('ADCYAP1R1')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in comt.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['COMT'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('COMT')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in orm1.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['ORM1'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('ORM1')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in txnrd1.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['TXNRD1'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('TXNRD1')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in tubb1.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['TUBB1'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('TUBB1')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in fkbp5.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['FKBP5'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('FKBP5')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in zbp1.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['ZBP1'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('ZBP1')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in erk1_2.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['ERK1\2'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('ERK1\2')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in zbtb16.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['ZBTB16'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('ZBTB16')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in gstm1.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['GSTM1'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('GSTM1')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in hla.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['HLA-DRB5'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('HLA-DRB5')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in camkmt.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['CAMKMT'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('CAMKMT')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in man2c1.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['MAN2C1'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('MAN2C1')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in asah1.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['ASAH1'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('ASAH1')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in fkbp4.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['FKBP4'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('FKBP4')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in ero1a.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['ERO1A'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('ERO1A')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])
for mirna in nnt.readlines():
    if mirna.split()[0] not in miRNA_dict.keys():
        miRNA_dict[mirna.split()[0]] = [['NNT'], float(mirna.split()[1])]
    else:
        miRNA_dict[mirna.split()[0]][0].append('NNT')
        miRNA_dict[mirna.split()[0]][1] += float(mirna.split()[1])

#биение на три группы
only_positive, only_negative, mixed = [], [], []
for mirna in miRNA_dict.keys():
    decreased_only = True
    increased_only = True
    for gene in miRNA_dict[mirna][0]:
        if gene_dict[gene] == True:
            decreased_only = False
        else:
            increased_only = False
    if decreased_only:
        only_negative.append(mirna)
    elif increased_only:
        only_positive.append(mirna)
    else:
        mixed.append(mirna)

for mirna in only_positive:
    print(miRNA_dict[mirna])
print('')
for mirna in mixed:
    print(miRNA_dict[mirna])
print('')
for mirna in only_negative:
    print(miRNA_dict[mirna])