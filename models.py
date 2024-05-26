from django.db import models
from django.forms import ValidationError

class Usuario(models.Model):
    username = models.CharField(max_length=255, unique=True)  # Nome de usuário para login
    password = models.CharField(max_length=128)  # Armazena a senha de forma segura (hashed)

    # Campos adicionais do usuário (opcional)
    # name = models.CharField(max_length=255, blank=True)
    # email = models.EmailField(blank=True)

    def __str__(self):
        return self.username

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, blank=True, null=True)
    documento = models.CharField(max_length=14, null=True, default="")
    titulo_eleitor = models.CharField(max_length=12, null=True, default="")
    telefone = models.CharField(max_length=20, blank=True, null=True, default="Sem Telefone")
    email = models.EmailField(blank=True, null=True, default="sem_email@exemplo.com")
    endereco = models.CharField(max_length=255, blank=True, null=True, default="Sem Endereço Cadastrado")
    estado_civil = models.CharField(max_length=20, blank=True, null=True)
    tipo_servico = models.CharField(max_length=20, blank=True, null=True)
    senha_gov = models.CharField(max_length=20, null=False, default="valor_padrao")
    info_adicionais = models.TextField(max_length=255, blank=True, null=True)
    
    def save(self, *args, **kwargs):

        if Usuario.objects.filter(nome=self.nome, documento=self.documento, titulo_eleitor=self.titulo_eleitor, telefone=self.telefone, email=self.email, endereco=self.endereco, estado_civil=self.estado_civil, tipo_servico=self.tipo_servico, senha_gov=self.senha_gov, info_adicionais=self.info_adicionais).exists():

            pass

        else:

            super(Usuario, self).save(*args, **kwargs)  
                


   
            

        
    
            
    


