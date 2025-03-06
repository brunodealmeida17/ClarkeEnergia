import { gql } from '@apollo/client';

export const GET_FORNECEDORES = gql`
  query GetFornecedores($consumo: Int!) {
    fornecedores(limiteMinimoKwh: $consumo) {
      id
      nome
      estado
      custoPorKwh
      limiteMinimoKwh
      numClientes
      avaliacaoMedia
      logo
    }
  }
`;
