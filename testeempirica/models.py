from django.db import models

class CessaoFundo(models.Model):
    
    ID_CESSAO = models.AutoField(primary_key=True)
    ORIGINADOR = models.CharField(max_length=250, null=False)
    DOC_ORIGINADOR = models.IntegerField(null=False)
    CEDENTE = models.CharField(max_length=250, null=False)
    DOC_CEDENTE = models.IntegerField(default=0, null=False)
    CCB = models.IntegerField(null=False)
    ID_EXTERNO = models.IntegerField(null=False)
    CLIENTE = models.CharField(max_length=250, null=False)
    CPF_CNPJ = models.CharField(max_length=50, null=False)
    ENDEREÇO = models.CharField(max_length=250, null=False)
    CEP = models.CharField(max_length=50, null=False)
    CIDADE = models.CharField(max_length=250, null=False)
    UF = models.CharField(max_length=50, null=False)
    VALOR_DO_EMPRESTIMO = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    VALOR_DA_PARCELA = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    TOTAL_PARCELAS = models.IntegerField(null=False)
    PARCELA = models.IntegerField(null=False)
    DATA_DE_EMISSAO = models.DateField(null=False)
    DATA_DE_VENCIMENTO = models.DateField(null=False)
    PRECO_DE_AQUISICAO = models.DecimalField(max_digits=10, decimal_places=2, null=False)