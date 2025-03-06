import React from 'react';
import { render, screen } from '@testing-library/react';
import { MockedProvider } from '@apollo/client/testing';
import App from '../App';
import { GET_FORNECEDORES } from '../graphql/queries';

const mocks = [
    {
        request: {
            query: GET_FORNECEDORES,
            variables: { consumo: null },
        },
        result: {
            data: {
                fornecedores: [
                    {
                        id: 1,
                        nome: 'Fornecedor 1',
                        estado: 'SP',
                        custoPorKwh: 0.5,
                        limiteMinimoKwh: 100,
                        numClientes: 200,
                        avaliacaoMedia: 4.5,
                        logo: '/logo1.png',
                    },
                ],
            },
        },
    },
];

test('renderiza botão de alternância de modo escuro/claro', async () => {
    render(
        <MockedProvider mocks={mocks} addTypename={false}>
            <App />
        </MockedProvider>
    );

    expect(screen.getByText(/modo escuro/i)).toBeInTheDocument(); 
});
