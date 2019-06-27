from django.db import models
#from django.contrib.postgres.fields import ArrayField


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.nome + self.email

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.cpf

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=20)
    razaoSocial = models.CharField(max_length=40)

    def __str__(self):
        return self.cnpj + self.razaoSocial

class Evento(models.Model):
    nome = models.CharField(max_length=128)
    eventoPrincipal = models.CharField(max_length=256)
    sigla = models.CharField(max_length=14)
    dataEHoraDeInicio = models.DateTimeField(blank=True, null=True)
    palavrasChave = models.CharField(max_length=256)
    logotipo = models.CharField(max_length=40)
    realizador = models.ForeignKey(Pessoa, null=True, blank=False, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)

    def __str__(self):
        return self.nome + self.eventoPrincipal

class EventoCientifico(Evento):
    issn =  models.CharField(max_length=45)

    def __str__(self):
        return self.issn

class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length=300)
    evento = models.ForeignKey(EventoCientifico, null=True, blank=True, on_delete=models.CASCADE)
    #autores = ArrayField(models.CharField(max_length=100), blank=False)

    def __str__(self):
        return self.titulo

class Autor(Pessoa):
    curriculo =  models.CharField(max_length=120)
    #artigos = ArrayField(models.CharField(max_length=100), blank=False)
    artigos = models.ManyToManyField(ArtigoCientifico,blank=True)

    def __str__(self):
        return self.curriculo
