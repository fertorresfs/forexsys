from django.db import models

# Create your models here.
class Processos(models.Model):
    id_processo = models.IntegerField(default=0)
    id_vara = models.IntegerField(default=0)
    id_juiz = models.IntegerField(default=0)
    id_aux_jus = models.IntegerField(default=0)
    data_nomeacao = models.DateTimeField("data da nomeação")
    honorarios = models.IntegerField(default=0)
    data_intimacao = models.DateTimeField("data da intimação")
    data_aceite = models.DateTimeField("data da petição de aceite")
    assunto = models.CharField(max_length=300)
    requerente = models.CharField(max_length=300)
    requerido = models.CharField(max_length=300)
    data_inicio_pericia = models.DateTimeField("data inicio da pericia")
    data_final_pericia = models.DateTimeField("data final da pericia")
    data_laudo_protocolado = models.DateTimeField("data do laudo protocolado")


class Auxiliar_justica(models.Model):
    id_aux_jus = models.IntegerField(default=0)
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    especialidade = models.CharField(max_length=200)
    data_cadastro = models.DateTimeField("data do cadastro do perito")
    cpf = models.IntegerField(default=0)
    tel = models.IntegerField(default=0)
    cel = models.IntegerField(default=0)
    email1 = models.CharField(max_length=200)
    email2 = models.CharField(max_length=200)


class Vara(models.Model):
    id_vara = models.IntegerField(default=0)
    endereco = models.CharField(max_length=200)
    tel = models.IntegerField(default=0)
    email = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)


class Juiz(models.Model):
    id_juiz = models.IntegerField(default=0)
    nome = models.CharField(max_length=200)
    id_vara = models.IntegerField(default=0)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text