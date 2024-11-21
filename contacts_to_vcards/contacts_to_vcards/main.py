import csv
import vobject

def csv_to_vcards(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            vcard = vobject.vCard()
            vcard.add('n')
            vcard.n.value = vobject.vcard.Name(family=row['last'], given=row['first'])
            vcard.add('fn')
            vcard.fn.value = row['first'] + " " + row['last']
            vcard.add('role')
            vcard.role.value = row['role']
            vcard.add('email')
            vcard.email.value = row['email']
            vcard.add('tel')
            vcard.tel.value = row['phone']
            vcard.tel.type_param = 'CELL'
            with open(f"{row['first']}_{row['last']}.vcf", 'w') as vcf_file:
                vcf_file.write(vcard.serialize())

csv_to_vcards('../contacts.csv')