import React from 'react';
import { render, screen } from '@testing-library/react';
import Fornecedores from '../components/Fornecedores';

const mockFornecedores = [
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
];

test('renderiza lista de fornecedores corretamente', () => {
    render(<Fornecedores fornecedores={mockFornecedores} />);

    expect(screen.getByText('Fornecedores Disponíveis:')).toBeInTheDocument();
    expect(screen.getByText('Fornecedor 1')).toBeInTheDocument();

    expect(screen.getByText('Estado:')).toBeInTheDocument();
    expect(screen.getByText('SP')).toBeInTheDocument();

    expect(screen.getByText('Custo por kWh:')).toBeInTheDocument();
    expect(screen.getByText('0.5')).toBeInTheDocument();
});
