import json
import io
import pytest


@pytest.fixture
def fornecedor_teste(client):
    """
    Fixture para criar e remover um fornecedor de teste automaticamente.
    """
    query = """
    mutation ($file: Upload!, $nome: String!, $estado: String!, $custoPorKwh: Float!, $limiteMinimoKwh: Int!, $numClientes: Int!, $avaliacaoMedia: Float!) {
        createFornecedor(
            nome: $nome,
            estado: $estado,
            custoPorKwh: $custoPorKwh,
            limiteMinimoKwh: $limiteMinimoKwh,
            numClientes: $numClientes,
            avaliacaoMedia: $avaliacaoMedia,
            logo: $file
        ) {
            fornecedor {
                id
                nome
                logo
            }
        }
    }
    """

    logo_file = (io.BytesIO(b"fake image data"), "logo.png")

    data = {
        "operations": json.dumps({
            "query": query,
            "variables": {
                "file": None,
                "nome": "Fornecedor Teste",
                "estado": "SP",
                "custoPorKwh": 0.5,
                "limiteMinimoKwh": 1000,
                "numClientes": 50,
                "avaliacaoMedia": 4.5
            }
        }),
        "map": json.dumps({"0": ["variables.file"]}),
        "0": logo_file
    }

    response = client.post("/graphql", data=data, content_type="multipart/form-data")
    
    data = json.loads(response.data)

    fornecedor = data["data"]["createFornecedor"]["fornecedor"]

    yield fornecedor

    # Cleanup: Deletar fornecedor após o teste
    delete_query = """
    mutation ($id: Int!) {
        deleteFornecedor(id: $id)
    }
    """
    client.post("/graphql", json={"query": delete_query, "variables": {"id": fornecedor["id"]}})


def test_create_fornecedor(client):
    """
    Testa a criação de um fornecedor via GraphQL.
    """
    query = """
    mutation ($file: Upload!, $nome: String!, $estado: String!, $custoPorKwh: Float!, $limiteMinimoKwh: Int!, $numClientes: Int!, $avaliacaoMedia: Float!) {
        createFornecedor(
            nome: $nome,
            estado: $estado,
            custoPorKwh: $custoPorKwh,
            limiteMinimoKwh: $limiteMinimoKwh,
            numClientes: $numClientes,
            avaliacaoMedia: $avaliacaoMedia,
            logo: $file
        ) {
            fornecedor {
                id
                nome
                logo
            }
        }
    }
    """

    logo_file = (io.BytesIO(b"fake image data"), "logo.png")

    data = {
        "operations": json.dumps({
            "query": query,
            "variables": {
                "file": None,
                "nome": "Fornecedor Teste",
                "estado": "SP",
                "custoPorKwh": 0.5,
                "limiteMinimoKwh": 1000,
                "numClientes": 50,
                "avaliacaoMedia": 4.5
            }
        }),
        "map": json.dumps({"0": ["variables.file"]}),
        "0": logo_file
    }

    response = client.post("/graphql", data=data, content_type="multipart/form-data")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert "data" in data
    assert "createFornecedor" in data["data"]
    fornecedor = data["data"]["createFornecedor"]["fornecedor"]
    assert fornecedor["nome"] == "Fornecedor Teste"
    assert fornecedor["logo"] is not None


def test_get_fornecedores(client, fornecedor_teste):
    """
    Testa a consulta de fornecedores via GraphQL.
    """
    query = """
    {
        fornecedores {
            id nome estado custoPorKwh limiteMinimoKwh numClientes avaliacaoMedia logo
        }
    }
    """
    response = client.post("/graphql", json={"query": query})    
    data = json.loads(response.data)

    assert response.status_code == 200    
    fornecedores = data["data"]["fornecedores"]
    assert isinstance(fornecedores, list)
    assert any(f["id"] == fornecedor_teste["id"] for f in fornecedores)


def test_update_fornecedor(client, fornecedor_teste):
    """
    Testa a atualização de um fornecedor via GraphQL.
    """
    query = """
    mutation ($id: Int!, $nome: String!) {
        updateFornecedor(id: $id, nome: $nome) {
            fornecedor {
                id
                nome
            }
        }
    }
    """
    variables = {"id": fornecedor_teste["id"], "nome": "Fornecedor Atualizado"}

    response = client.post("/graphql", json={"query": query, "variables": variables})     
    data = json.loads(response.data)   

    assert response.status_code == 200
    assert "data" in data
    assert "updateFornecedor" in data["data"]
    fornecedor = data["data"]["updateFornecedor"]["fornecedor"]
    assert fornecedor["id"] == fornecedor_teste["id"]
    assert fornecedor["nome"] == "Fornecedor Atualizado"


def test_delete_fornecedor(client, fornecedor_teste):
    """
    Testa a exclusão de um fornecedor via GraphQL.
    """
    query = """
        mutation ($id: Int!) {
        deleteFornecedor(id: $id) {
            success
        }
        }
    """
    variables = {"id": fornecedor_teste["id"]}

    response = client.post("/graphql", json={"query": query, "variables": variables})
    print(response)
    data = json.loads(response.data)
    print(response.data)

    assert response.status_code == 200
    assert "data" in data
    assert data["data"]["deleteFornecedor"]['success'] is True

    # Testar se o fornecedor foi removido
    query = """
    {
        fornecedores {
            id
            nome
        }
    }
    """
    response = client.post("/graphql", json={"query": query})
    data = json.loads(response.data)
    fornecedores = data["data"]["fornecedores"]

    assert not any(f["id"] == fornecedor_teste["id"] for f in fornecedores)

