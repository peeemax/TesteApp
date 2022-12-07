from django.shortcuts import render
from .forms import UploadFileForm
from .models import CessaoFundo



# Função imaginária para manipular um upload de arquivo.
from .tratamentoarquivo import handle_uploaded_file

def upload_file(request):
    
    if request.method == 'POST':
        
        csv_file = request.FILES['csv_upload']
        file_data = csv_file.read().decode("Windows-1252")
        
        
        # file_data.pop('Taxa de Juros (a.m.)')
        # 'Principal R$', 'Juros R$', 'IOF R$', 'Comissão R$', 'Multa', 'Mora', 'Data de Compra CCB'], axis=1, inplace=True)
        csv_data = file_data.split("\n")
        
        for x in csv_data:
            fields = x.split(";")
            created = CessaoFundo.objects.update_or_create(
                ORIGINADOR = fields[0],
                DOC_ORIGINADOR = fields[1], 
                CEDENTE = fields[2],
                DOC_CEDENTE = fields[3],
                CCB = fields[4],
                ID_EXTERNO = fields[5],
                CLIENTE = fields[6],
                CPF_CNPJ = fields[7],
                ENDEREÇO = fields[8],
                CEP = fields[9],
                CIDADE = fields[10],
                UF = fields[11],
                VALOR_DO_EMPRESTIMO = fields[12],
                VALOR_DA_PARCELA = fields[14],
                TOTAL_PARCELAS = fields[19],
                PARCELA = fields[20],
                DATA_DE_EMISSAO = fields[23],
                DATA_DE_VENCIMENTO = fields[24],
                PRECO_DE_AQUISICAO = fields[26],
            )
            print(fields[0])
            print(fields[1])
            print(fields[2])
            print(fields[3])
            print(fields[4])
            print(fields[5])
            print(fields[6])
            print(fields[7])
            print(fields[8])
            print(fields[9])
            print(fields[10])
            print(fields[11])
            print(fields[12])
            print(fields[13])
            print(fields[14])
            print(fields[15])
            print(fields[16])
            print(fields[17])
    
    form = UploadFileForm()
    data = {'form': form}
    return render(request, 'testeempirica/index.html', data)


