import graphene
from graphene_file_upload.scalars import Upload
from models.fornecedor import FornecedorModel
from models import db
from utils import save_image

class Fornecedor(graphene.ObjectType):
    id = graphene.Int()
    nome = graphene.String()
    logo = graphene.String()
    estado = graphene.String()
    custo_por_kwh = graphene.Float()
    limite_minimo_kwh = graphene.Int()
    num_clientes = graphene.Int()
    avaliacao_media = graphene.Float()

class Query(graphene.ObjectType):
    fornecedores = graphene.List(Fornecedor, limite_minimo_kwh=graphene.Int())
    fornecedor = graphene.Field(Fornecedor, id=graphene.Int(required=True))

    def resolve_fornecedores(self, info, limite_minimo_kwh=None):
        
        if limite_minimo_kwh is not None:
            return FornecedorModel.query.filter(FornecedorModel.limite_minimo_kwh > limite_minimo_kwh).all()
        return FornecedorModel.query.all()  

    def resolve_fornecedor(self, info, id):
        return FornecedorModel.query.get(id)

class CreateFornecedor(graphene.Mutation):
    class Arguments:
        nome = graphene.String(required=True)
        estado = graphene.String(required=True)
        custo_por_kwh = graphene.Float(required=True)
        limite_minimo_kwh = graphene.Int(required=True)
        num_clientes = graphene.Int(required=True)
        avaliacao_media = graphene.Float(required=True)
        logo = Upload(required=True)

    fornecedor = graphene.Field(Fornecedor)

    def mutate(self, info, nome, estado, custo_por_kwh, limite_minimo_kwh, num_clientes, avaliacao_media, logo=None):
        logo_path = save_image(logo, nome) if logo else None  

        fornecedor = FornecedorModel(
            nome=nome,
            logo=logo_path,
            estado=estado,
            custo_por_kwh=custo_por_kwh,
            limite_minimo_kwh=limite_minimo_kwh,
            num_clientes=num_clientes,
            avaliacao_media=avaliacao_media
        )
        db.session.add(fornecedor)
        db.session.commit()
        return CreateFornecedor(fornecedor=fornecedor)

class UpdateFornecedor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        nome = graphene.String()
        estado = graphene.String()
        custo_por_kwh = graphene.Float()
        limite_minimo_kwh = graphene.Int()
        num_clientes = graphene.Int()
        avaliacao_media = graphene.Float()
        logo = Upload()

    fornecedor = graphene.Field(Fornecedor)

    def mutate(self, info, id, nome=None, estado=None, custo_por_kwh=None,
               limite_minimo_kwh=None, num_clients=None, avaliacao_media=None, logo=None):
        fornecedor = FornecedorModel.query.get(id)
        if not fornecedor:
            raise Exception("Fornecedor não encontrado!")

        if nome:
            fornecedor.nome = nome
        if estado:
            fornecedor.estado = estado
        if custo_por_kwh is not None:
            fornecedor.custo_por_kwh = custo_por_kwh
        if limite_minimo_kwh is not None:
            fornecedor.limite_minimo_kwh = limite_minimo_kwh
        if num_clients is not None:
            fornecedor.num_clients = num_clients
        if avaliacao_media is not None:
            fornecedor.avaliacao_media = avaliacao_media
        if logo:
            fornecedor.logo = save_image(logo, nome)

        db.session.commit()
        return UpdateFornecedor(fornecedor=fornecedor)

class DeleteFornecedor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        fornecedor = FornecedorModel.query.get(id)
        if not fornecedor:
            raise Exception("Fornecedor não encontrado!")

        db.session.delete(fornecedor)
        db.session.commit()
        return DeleteFornecedor(success=True)

class Mutation(graphene.ObjectType):
    create_fornecedor = CreateFornecedor.Field()
    update_fornecedor = UpdateFornecedor.Field()
    delete_fornecedor = DeleteFornecedor.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
